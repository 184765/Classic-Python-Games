"""Contains the game logic for wordL game."""

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["letter_reveal", "extra_attempt", "skip_word"]


def wordL_view_scores():
    """Display score history during this current run of the program."""
    if not score_list:
        print("No past scores yet.")
        return []

    print("Past scores:")

    for index, (score, total_rounds, username_rc) in enumerate(
        zip(score_list, total_rounds_list, username_list),
        start=1,
    ):
        print(f"{index}. {username_rc}: Score: {score}/{total_rounds}")
    return list(zip(score_list, total_rounds_list, username_list))


def wordL_game():
    """WordL game logic."""
    from wonderwords import RandomWord  # Can be used to generate random
    from spellchecker import SpellChecker  # Check if word valid

    # Variables for games
    spell = SpellChecker()
    rw = RandomWord()
    lives = 3
    score = 0
    total_rounds = 0
    current_round_attempts = 0
    max_attempts = 6
    skip_word = 1
    extra_attempt = 3
    letter_reveal = 3
    game_running = True
    generate = True
    words_used = []

    username = input("Please enter your username: ")

    while game_running is True:
        if lives <= 0:
            print(
                f"Game Over! Your final score is: {score}/{total_rounds}"
            )
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        if generate is True:
            rnd_word = rw.word(word_min_length=5, word_max_length=5).lower()
            while rnd_word in words_used:
                rnd_word = rw.word(
                    word_min_length=5,
                    word_max_length=5,
                ).lower()

            words_used.append(rnd_word)
            generate = False
            wordL = True
            current_round_attempts = 0
            max_attempts = 6  # Reset max attempts for new round

        print(f"Current Round: {total_rounds + 1}")
        print(
            f"Guess the 5-letter word\n"
            f"Current Score: {score}/{total_rounds}\n"
            f"Lives Remaining: {lives}\n"
        )

        while wordL is True:
            if current_round_attempts >= max_attempts:
                print(
                    f"You've used all {max_attempts} attempts."
                    f" The word was: {rnd_word}"
                )
                lives -= 1
                total_rounds += 1
                wordL = False
                generate = True
                current_round_attempts = 0
                break

            guess = input(
                f"\nAttempt {current_round_attempts + 1}/{max_attempts}: "
            )

            # Removes unwanted whitespace and capitalization
            cor_guess = guess.strip().lower()

            if cor_guess in ability_list:
                if cor_guess == "letter_reveal":
                    if letter_reveal > 0:
                        letter_reveal -= 1
                        reveal_index = next(
                            (i for i, c in enumerate(rnd_word)
                             if c not in guess),
                            None,
                        )
                        if reveal_index is not None:
                            print(
                                f"Letter Reveal: The letter at position"
                                f" {reveal_index + 1} is "
                                f"'{rnd_word[reveal_index]}'"
                            )
                        else:
                            print("All letters have already been guessed.")
                    else:
                        print("No more letter reveals left.")

                elif cor_guess == "extra_attempt":
                    if extra_attempt > 0:
                        extra_attempt -= 1
                        max_attempts += 1
                        print(
                            f"Extra Attempt: You now have {max_attempts}"
                            f" attempts for this round."
                        )
                    else:
                        print("No more extra attempts left.")

                elif cor_guess == "skip_word":
                    if skip_word > 0:
                        skip_word -= 1
                        print(
                            f"Skip Word: The word '{rnd_word}'"
                            f" has been skipped."
                        )
                        total_rounds += 1
                        wordL = False
                        generate = True
                        current_round_attempts = 0
                        break
                    else:
                        print("No more skips left.")

            # Checks if guess is 5 letters
            if len(cor_guess) != 5:
                print("Enter a 5-letter word.")
                continue

            # Checks if guess is a valid word
            if cor_guess not in spell:
                print("Not a valid word. Please try again.")
                continue

            if cor_guess == rnd_word:
                score += 1
                total_rounds += 1
                wordL = False
                generate = True
                current_round_attempts = 0
                break

            feedback = []
            remaining_letters = {}

            for i in range(5):
                if cor_guess[i] == rnd_word[i]:
                    feedback.append(f"[{cor_guess[i].upper()}]")
                else:
                    remaining_letters[rnd_word[i]] = (
                        remaining_letters.get(rnd_word[i], 0) + 1
                    )
                    feedback.append("_")

            for i in range(5):
                if cor_guess[i] == rnd_word[i]:
                    continue
                if (
                    cor_guess[i] in remaining_letters
                    and remaining_letters[cor_guess[i]] > 0
                ):
                    feedback[i] = cor_guess[i].lower()
                    remaining_letters[cor_guess[i]] -= 1

            print("Feedback: " + " ".join(feedback))
            current_round_attempts += 1
