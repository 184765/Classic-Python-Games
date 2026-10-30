"""Contains the game logic for wordL game."""
# Used reference for color: https://pypi.org/project/colorama/
from colorama import init, Fore, Style  # Color for output in the terminal

init(autoreset=True)  # Automatically resets color statement

GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
GREY = Fore.LIGHTBLACK_EX
RESET = Style.RESET_ALL

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["letter_reveal", "extra_attempt", "skip_word",
                "1", "2", "3", "help", "shop"]


def wordl_shop(points, letter_reveal, extra_attempt, skip_word,
               legacy, global_delay):
    """Allow the player to purchase additional ability uses."""
    from game_interface_ui import game_ui

    # Sets the prices for the shop
    prices = {"1": 3, "2": 3, "3": 10}

    while True:
        game_ui(
            [
                "WORDL ABILITY SHOP",
                f"Available points: {points}",
                "",
                f"1. Letter Reveal - {prices['1']} points",
                f"2. Extra Attempt - {prices['2']} points",
                f"3. Skip Word - {prices['3']} points",
                "",
                "0. Leave shop",
            ],
            legacy, global_delay, True,
        )

        # Gets user shop input
        choice = input("Choose an option: ").strip()

        if choice == "0":
            break

        if choice not in prices:
            game_ui("Invalid choice. Enter 0, 1, 2 or 3.",
                    legacy, global_delay)
            continue

        if points < prices[choice]:
            game_ui("Not enough points!", legacy, global_delay)
            continue

        points -= prices[choice]

        if choice == "1":
            letter_reveal += 1
            message = "Purchased one Letter Reveal use!"
        elif choice == "2":
            extra_attempt += 1
            message = "Purchased one Extra Attempt use!"
        else:
            skip_word += 1
            message = "Purchased one Skip Word use!"

        game_ui(
            [message, f"Points remaining: {points}"],
            legacy, global_delay,
        )

    return points, letter_reveal, extra_attempt, skip_word


# Store feedback for each letter and count unmatched answer letters
# so repeated letters are handled correctly.
def colour_feedback(guess, answer):
    """Colour each letter based on WordL feedback."""
    feedback = [""] * 5
    remaining = {}

    # Correct positions first.
    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = GREEN + guess[i].upper() + RESET
        else:
            remaining[answer[i]] = remaining.get(answer[i], 0) + 1

    # Then letters in the wrong positions.
    for i in range(5):
        if guess[i] == answer[i]:
            continue

        if remaining.get(guess[i], 0) > 0:
            feedback[i] = YELLOW + guess[i].upper() + RESET
            remaining[guess[i]] -= 1
        else:
            feedback[i] = GREY + guess[i].upper() + RESET

    return " ".join(feedback)


# Arrange the letters into three rows to resemble a QWERTY keyboard.
def display_keyboard(keyboard, legacy, global_delay):
    """Display a coloured QWERTY keyboard without UI wrapping."""
    rows = [
        "Q W E R T Y U I O P",
        " A S D F G H J K L",
        "  Z X C V B N M",
    ]

    print("\n========== KEYBOARD ==========")

    # Apply the latest colour feedback to each letter before printing it.
    for row in rows:
        coloured_letters = []

        for letter in row:
            if letter.isalpha():
                colour = keyboard.get(letter, "")
                coloured_letters.append(
                    f"{colour}{letter}{RESET}"
                )

        print(" ".join(coloured_letters))

    print("==============================\n")

# Rank feedback colours so a weaker result cannot overwrite
# a stronger result from an earlier guess.
def update_keyboard(keyboard, guess, answer):
    """Keep the strongest feedback received for each letter."""
    priority = {"": 0, GREY: 1, YELLOW: 2, GREEN: 3}
    feedback = [""] * 5
    remaining = {}

    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = GREEN
        else:
            remaining[answer[i]] = remaining.get(answer[i], 0) + 1

    for i in range(5):
        if guess[i] == answer[i]:
            continue

        if remaining.get(guess[i], 0) > 0:
            feedback[i] = YELLOW
            remaining[guess[i]] -= 1
        else:
            feedback[i] = GREY

    # Update each keyboard letter only when its new feedback is stronger.
    for letter, new_colour in zip(guess.upper(), feedback):
        old_colour = keyboard.get(letter, "")
        if priority[new_colour] > priority[old_colour]:
            keyboard[letter] = new_colour


def wordl_view_scores(legacy, global_delay):
    """Display score history during this program run."""
    from game_interface_ui import game_ui

    if not score_list:
        game_ui("No past scores yet.", legacy, global_delay)
        return []

    messages = ["WORDL - PAST SCORES"]

    for index, (score, rounds, username_rc) in enumerate(
        zip(score_list, total_rounds_list, username_list),
        start=1,
    ):
        messages.append(
            f"{index}. {username_rc}: {score}/{rounds}"
        )

    game_ui(messages, legacy, global_delay, True)
    return list(zip(score_list, total_rounds_list, username_list))


def wordl_game(global_delay, legacy):
    """Wordle Game Logic."""
    from wonderwords import RandomWord  # Can be used to generate random
    from spellchecker import SpellChecker  # Check if word valid
    from game_interface_ui import user_help, game_ui, game_username_ui

    # Variables for games
    spell = SpellChecker()
    rw = RandomWord()
    lives = 3
    score = 0
    shop_points = 0
    total_rounds = 0
    current_round_attempts = 0
    max_attempts = 6
    skip_word = 1
    extra_attempt = 3
    letter_reveal = 3
    game_running = True
    generate = True
    words_used = []

    game_username_ui(legacy)

    username = input()

    while game_running is True:
        if lives <= 0:
            game_ui(
                [
                    "GAME OVER",
                    f"Player: {username}",
                    f"Final score: {score}/{total_rounds}",
                    f"Shop points earned: {shop_points}",
                ],
                legacy, global_delay, True,
            )
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        if generate is True:
            rnd_word = rw.word(word_min_length=5, word_max_length=5).lower()
            # Generate another word if selected word has already been used.
            while rnd_word in words_used:
                rnd_word = rw.word(
                    word_min_length=5,
                    word_max_length=5,
                ).lower()

            # Record the word so it cannot be selected again during this game.
            words_used.append(rnd_word)
            generate = False
            wordl = True
            current_round_attempts = 0
            max_attempts = 6  # Reset max attempts for each round
            # Reset keyboard feedback and guessed letters for the new word.
            keyboard = {}
            guessed_letters = set()

        game_ui(
            [
                f"Round: {total_rounds + 1}",
                f"Score: {score}/{total_rounds}",
                f"Lives remaining: {lives}",
                f"Attempts: {current_round_attempts}/{max_attempts}",
                f"Shop points: {shop_points}",
                "",
                "Guess the 5-letter word.",
                "Type 'help' for instructions.",
                "Type 'shop' to buy abilities.",
            ],
            legacy, global_delay, True,
        )

        while wordl is True:
            # End the current round when all available attempts exhausted.
            if current_round_attempts >= max_attempts:
                game_ui(
                    [
                        f"You've used all {max_attempts} attempts.",
                        f" The word was: {rnd_word}"
                    ],
                    legacy, global_delay, True
                )
                lives -= 1
                total_rounds += 1
                wordl = False
                generate = True
                current_round_attempts = 0
                break

            guess = input(
                f"\nAttempt {current_round_attempts + 1}/{max_attempts}: "
            )

            # Removes unwanted whitespace and capitalization
            cor_guess = guess.strip().lower()

            # Handle ability commands.
            if cor_guess in ability_list:
                if cor_guess in ("letter_reveal", "1"):
                    # First position: letter has not appeared a prior guess.
                    if letter_reveal > 0:
                        letter_reveal -= 1
                        reveal_index = next(
                            (
                                i for i, c in enumerate(rnd_word)
                                if c not in guessed_letters
                            ),
                            None,
                        )
                        if reveal_index is not None:
                            game_ui(
                                [
                                    "Letter Reveal: Position ",
                                    f"{reveal_index + 1} is ",
                                    f"'{rnd_word[reveal_index]}'"
                                ],
                                legacy, global_delay
                            )
                        else:
                            game_ui(
                                "All letters have been guessed.",
                                legacy, global_delay
                            )
                    else:
                        game_ui(
                            "No more letter reveals left.",
                            legacy, global_delay
                        )
                    continue

                elif cor_guess in ("extra_attempt", "2"):
                    if extra_attempt > 0:
                        extra_attempt -= 1
                        # Increase the attempt limit.
                        max_attempts += 1
                        game_ui(
                            [
                                "Extra attempt added. Total attempts: ",
                                f"{max_attempts}"
                            ],
                            legacy, global_delay
                        )
                    else:
                        game_ui(
                            "No more extra attempts left.",
                            legacy, global_delay
                        )
                    continue

                elif cor_guess in ("skip_word", "3"):
                    # End this word's round without deducting a life.
                    if skip_word > 0:
                        skip_word -= 1
                        game_ui(
                            f"Skipped word: {rnd_word}",
                            legacy, global_delay
                        )
                        total_rounds += 1
                        wordl = False
                        generate = True
                        current_round_attempts = 0
                        break
                    else:
                        game_ui(
                            "No more skips left.",
                            legacy, global_delay
                        )
                    continue

                elif cor_guess == "help":
                    user_help(global_delay, legacy)
                    continue

                elif cor_guess == "shop":
                    (
                        shop_points,
                        letter_reveal,
                        extra_attempt,
                        skip_word,
                    ) = wordl_shop(
                        shop_points,
                        letter_reveal,
                        extra_attempt,
                        skip_word,
                        legacy,
                        global_delay,
                    )
                    continue

            # Checks if guess is 5 letters
            if len(cor_guess) != 5:
                game_ui(
                    "Enter a 5-letter word.",
                    legacy, global_delay
                )
                continue

            # Checks if guess is a valid word
            if cor_guess not in spell:
                game_ui(
                    "Not a valid word. Please try again.",
                    legacy, global_delay, True
                )
                continue

            if cor_guess == rnd_word:
                game_ui(
                    [
                        "Correct! You solved the word!",
                        f"The word was: {rnd_word.upper()}",
                        "+1 score point",
                        "+1 shop point",
                    ],
                    legacy, global_delay, True,
                )

                print("Feedback: " + colour_feedback(cor_guess, rnd_word))
                update_keyboard(keyboard, cor_guess, rnd_word)
                display_keyboard(keyboard, legacy, global_delay)

                score += 1
                shop_points += 1
                total_rounds += 1
                wordl = False
                generate = True
                current_round_attempts = 0
                break

            print("Feedback: " + colour_feedback(cor_guess, rnd_word))

            update_keyboard(keyboard, cor_guess, rnd_word)
            display_keyboard(keyboard, legacy, global_delay)

            guessed_letters.update(cor_guess)
            current_round_attempts += 1
