"""A game that asks a series of general knowledge questions, multi-answer."""

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["50/50", "skip", "double", "1", "2", "3", "help"]
options_list = ["A", "B", "C", "D"]

# Predefined Variables
username = ""
ability_wait = 2
fifty_fifty_uses = 0
skip_uses = 0
double_uses = 0


def quizza_view_scores(legacy, global_delay):
    """Display score history during this current run."""
    from game_interface_ui import game_ui

    if not score_list:
        game_ui("No past scores yet.", legacy, global_delay)
        return []

    messages = ["Past Scores:"]

    # Combine each player's name, score and number of rounds,
    # then number each result for display.
    for index, (score, total_rounds, username_rc) in enumerate(
        zip(score_list, total_rounds_list, username_list),
        start=1
    ):
        messages.append(
            f"{index}. {username_rc}: {score}/{total_rounds}"
        )

    game_ui(messages, legacy, global_delay)

    return list(zip(score_list, total_rounds_list, username_list))


def quizza_ability_shop(
    score, spent_points, fifty_fifty_uses,
    skip_uses, double_uses, legacy, global_delay
):
    """Allow players to purchase extra ability uses."""
    from game_interface_ui import game_ui

    fifty_price = 3
    skip_price = 10
    double_price = 1

    game_ui(
        [
            "Welcome to the Ability Shop!",
            f"Available points: {score - spent_points}",
            "",
            f"1. 50/50 use: {fifty_price} points",
            f"2. Skip use: {skip_price} points",
            f"3. Double use: {double_price} points",
            "0. Exit shop"
        ],
        legacy, global_delay, True
    )

    # Keep the shop open until the player chooses to leave.
    while True:
        points = score - spent_points
        game_ui(f"Points remaining: {points}", legacy, 0)

        choice = input("Choose an option: ").strip()

        # Stop accepting purchases when player selects the exit option.
        if choice == "0":
            break

        elif choice == "1":
            if points >= fifty_price:
                spent_points += fifty_price
                fifty_fifty_uses += 1
                game_ui("Purchased one 50/50 use!", legacy, global_delay)
            else:
                game_ui("Not enough points!", legacy, global_delay)

        elif choice == "2":
            if points >= skip_price:
                spent_points += skip_price
                skip_uses += 1
                game_ui("Purchased one Skip use!", legacy, global_delay)
            else:
                game_ui("Not enough points!", legacy, global_delay)

        elif choice == "3":
            if points >= double_price:
                spent_points += double_price
                double_uses += 1
                game_ui("Purchased one Double use!", legacy, global_delay)
            else:
                game_ui("Not enough points!", legacy, global_delay)

        else:
            game_ui(
                "Invalid choice. Enter 0, 1, 2 or 3.",
                legacy, global_delay
            )

    return (
        spent_points, fifty_fifty_uses,
        skip_uses, double_uses
    )


def quizza_game(global_delay, legacy):
    """Quizza game logic."""
    import random

    from game_storage_quizza import quizza
    from game_interface_ui import user_help, game_ui, game_username_ui

    # Variables for games
    lives = 3
    score = 0
    double = 1
    total_rounds = 0
    game_running = True
    generate = True
    spent_points = 0
    shop_interval = 5
    last_shop_round = 0

    fifty_fifty_uses = 3
    skip_uses = 3
    double_uses = 3

    game_username_ui(legacy)

    username = input()

    while game_running is True:
        game_ui(
            [
                f"Current Score: {score}/{total_rounds}",
                f"Lives remaining: {lives}",
                f"Current Round: {total_rounds + 1}"
            ],
            legacy, global_delay, True
        )

        game_ui(
            [
                "Abilities:",
                f"50/50 uses left: {fifty_fifty_uses}",
                f"Skip uses left: {skip_uses}",
                f"Double uses left: {double_uses}"
            ],
            legacy, global_delay
        )

        if lives <= 0:
            game_ui(
                f"Game Over! Your final score is: {score}/{total_rounds}",
                legacy, global_delay
            )
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        # Select a new random question and retrieve its question text,
        # answer options and correct answer from the question dictionary.
        if generate is True:
            random_question = random.choice(list(quizza.keys()))
            question = quizza[random_question]["question"]
            multichoice = quizza[random_question]["multi choice"]
            answer = quizza[random_question]["answer"]

        game_ui(
            [
                question,
                "",
                *multichoice,
                "",
                "Choose A, B, C or D,",
                "or enter an ability."
            ],
            legacy, global_delay
        )

        guess = input("Your choice: ").strip()
        guess_upper = guess.upper()

        valid_abilities = {ability.upper() for ability in ability_list}

        if len(multichoice) == 1:
            # Handles all options stored in one long string
            available_options = [
                option.strip()[0]
                for option in multichoice[0].split(",")
                if option.strip()
            ]
        else:
            # Handles options stored as separate strings
            available_options = [
                option.strip()[0]
                for option in multichoice
                if option.strip()
            ]

        if (
            guess_upper not in available_options
            and guess_upper not in valid_abilities
        ):
            game_ui(
                [
                    "Invalid input.",
                    "Choose A, B, C or D,",
                    "or enter an ability."
                ],
                legacy, global_delay
            )
            generate = False
            continue

        if guess_upper in valid_abilities:
            # Remove up to two incorrect options.
            if guess_upper in ("50/50", "1") and fifty_fifty_uses > 0:
                incorrect_options = [
                    option for option in multichoice
                    if option[0] != answer
                ]

                removed_options = random.sample(
                    incorrect_options,
                    min(2, len(incorrect_options))
                )

                multichoice = [
                    option for option in multichoice
                    if option not in removed_options
                ]

                game_ui(
                    [
                        "50/50 ability used!",
                        "Two incorrect options removed.",
                        *multichoice
                    ],
                    legacy, global_delay
                )

                generate = False
                fifty_fifty_uses -= 1
                continue

            elif guess_upper in ("SKIP", "2") and skip_uses > 0:
                game_ui(
                    "Skip ability used. Question skipped.",
                    legacy, global_delay
                )
                generate = True
                skip_uses -= 1
                continue

            elif guess_upper in ("DOUBLE", "3") and double_uses > 0:
                # Set the score or life-loss multiplier.
                game_ui(
                    [
                        "Double points ability used. ",
                        "Next correct answer will give double points."
                    ],
                    legacy, global_delay
                )
                double = 2
                double_uses -= 1
                generate = False
                continue

            elif guess_upper in ("HELP",):
                user_help(global_delay, legacy)
                generate = False
                continue

            else:
                game_ui(
                    "No uses left for that ability.",
                    legacy, global_delay
                )
                generate = False
                continue

        guess = guess_upper

        # Compare the player's answer with the correct answer and update
        # the score, lives and completed-round count.
        if guess == answer:
            game_ui(
                "Correct!",
                legacy, global_delay, True
            )
            score += 1 * double
            double = 1
            total_rounds += 1
            generate = True

        else:
            game_ui(
                "Incorrect!",
                legacy, global_delay, True
            )
            lives -= 1 * double
            total_rounds += 1
            double = 1
            generate = True

        # Open the shop every five completed questions.
        if (
            total_rounds > 0
            and total_rounds % shop_interval == 0
            and total_rounds != last_shop_round
            and lives > 0
        ):
            (
                spent_points,
                fifty_fifty_uses,
                skip_uses,
                double_uses
            ) = quizza_ability_shop(
                score,
                spent_points,
                fifty_fifty_uses,
                skip_uses,
                double_uses,
                legacy,
                global_delay
            )

            last_shop_round = total_rounds

    return list(zip(score_list, total_rounds_list, username_list))
