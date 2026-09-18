"""A game that asks a series of general knowledge questions, multi-answer."""

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["50/50", "skip", "double"]
options_list = ["A", "B", "C", "D"]

# Predefined Variables
username = ""
ability_wait = 2
fifty_fifty_uses = 0
skip_uses = 0
double_uses = 0


def quizza_view_scores():
    """Display score history during this current run of the program."""
    if not score_list:
        print("No past scores yet.")
        return []

    print("Past scores:")

    for index, (score, total_rounds, username_rc) in enumerate(
        zip(score_list, total_rounds_list, username_list), start=1
    ):
        print(f"{index}. {username_rc}: Score: {score}/{total_rounds}")
    return list(zip(score_list, total_rounds_list, username_list))


def quizza_game():
    """Quizza game logic."""
    import random
    import time

    from game_storage_quizza import quizza

    # Variables for games
    lives = 3
    score = 0
    double = 1
    total_rounds = 0
    game_running = True
    generate = True

    fifty_fifty_uses = 3
    skip_uses = 3
    double_uses = 3

    username = input("Please enter your username: ")

    while game_running is True:
        print(f"Current Round: {total_rounds + 1}")

        if lives <= 0:
            print(f"Game Over! Your final score is: {score}/{total_rounds}")
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        if generate is True:
            random_question = random.choice(list(quizza.keys()))
            question = quizza[random_question]["question"]
            multichoice = quizza[random_question]["multi choice"]
            answer = quizza[random_question]["answer"]

        print(
            question
        )
        guess = input(
            f"Select your option:\n"
            f"{multichoice}\n"
            f"or use an ability: "
        ).strip()
        guess_upper = guess.upper()

        valid_abilities = {ability.upper() for ability in ability_list}
        if (
            guess_upper not in options_list
            and guess_upper not in valid_abilities
        ):
            print(
                f"Invalid input. Please enter {multichoice} "
                "or an ability."
            )
            generate = False
            continue

        if guess_upper in valid_abilities:
            if guess_upper == "50/50" and fifty_fifty_uses > 0:
                print("50/50 ability used. Two incorrect options removed.")
                multichoice = [
                    option for option in multichoice
                    if option[0] == answer or random.choice([True, False])
                ]
                print(f"New options: {multichoice}")
                generate = False
                fifty_fifty_uses -= 1
                time.sleep(ability_wait)
                continue

            elif guess_upper == "SKIP" and skip_uses > 0:
                print("Skip ability used. Question skipped.")
                generate = True
                skip_uses -= 1
                time.sleep(ability_wait)
                continue

            elif guess_upper == "DOUBLE" and double_uses > 0:
                print(
                    "Double points ability used. "
                    "Next correct answer will give double points."
                )
                double = 2
                double_uses -= 1
                generate = False
                time.sleep(ability_wait)
                continue

            else:
                print("No uses left for that ability.")
                generate = False
                time.sleep(ability_wait)
                continue

        guess = guess_upper

        if guess == answer:
            print("Correct!")
            score += 1 * double
            double = 1
            total_rounds += 1
            generate = True
            time.sleep(1)
            if score % 3 == 0 and score != 0: # Ability regeneration system
                if fifty_fifty_uses < 3:
                    fifty_fifty_uses += 1
                if double_uses < 3:
                    double_uses += 1
        else:
            print("Incorrect!")
            lives -= 1 * double
            total_rounds += 1 * double
            double = 1
            print(f"Lives remaining: {lives}")
            generate = True
            time.sleep(1)

    return list(zip(score_list, total_rounds_list, username_list))

