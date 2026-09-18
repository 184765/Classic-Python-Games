"""Game file for the higher or lower game."""

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["percentage", "heal", "double time", "%"]

# Predefined variables
heal_uses = 0
pecentage_uses = 0
double_time_uses = 0
ability_pause = 1.5
username = ""


def view_scores():
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


def higher_or_lower():
    """Higher or lower game logic."""
    import random
    import time
    from game_storage_higher_lower import higher_or_lower

    # Variables for game
    lives = 3
    score = 0
    total_rounds = 0
    heal_uses = 3
    pecentage_uses = 3
    double_time_uses = 3
    double = 1
    game_running = True
    generate = True

    random_item = random.choice(list(higher_or_lower.keys()))

    # Get the item and price from the dictionary
    item1 = higher_or_lower[random_item]["item"]
    price1 = higher_or_lower[random_item]["price"]

    username = input("Please enter your username: ")

    while game_running is True:

        if lives <= 0:
            print(f"Game Over! Your final score is: {score}/{total_rounds}")
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        if generate is True:
            random_item2 = random.choice(list(higher_or_lower.keys()))
            item2 = higher_or_lower[random_item2]["item"]
            price2 = higher_or_lower[random_item2]["price"]

        if (
            item1 == item2
            or price1 == price2
        ):
            continue

        print(f"Current Round: {total_rounds+1}")

        print(f"Item 1: {item1}")
        print(f"Price: {price1}")

        time.sleep(ability_pause)

        guess = input(f"Is {item2} worth more or less than {item1}?\n"
                      "(Enter 'more' or 'less'): ").lower()

        if guess not in ['more', 'less'] and guess not in ability_list:
            print("Invalid input. Please enter 'more', 'less' or an ability.")
            continue

        if guess in ability_list:
            if guess == 'heal' and heal_uses > 0:  # Heals the player
                lives += 1
                generate = False
                heal_uses -= 1
                print(f"Current Lives: {lives}")
                print(f"Heal uses left: {heal_uses}")
                time.sleep(ability_pause)

            elif guess in ('percentage', '%') and pecentage_uses > 0:
                percentage = (price1 - price2) / price1 * 100
                checked_percentage = abs(percentage) 
                checked_percentage = round(checked_percentage, 2)
                generate = False
                pecentage_uses -= 1
                print(f"Seccond item price is higher or lower {percentage}%")
                print(f"Percentage uses left: {pecentage_uses}")
                time.sleep(ability_pause)

            elif guess == 'double time' and double_time_uses > 0:
                double = 2
                generate = False
                double_time_uses -= 1
                print("You now can gain twice the points\n"
                      "or lose double the lives on this question.")
                print(f"Double time uses left: {double_time_uses}")

        elif (
            (guess == "more" and price2 > price1)
            or (guess == "less" and price2 < price1)
        ):
            print("Correct!")
            score += 1 * double
            total_rounds += 1 * double
            item1 = item2
            price1 = price2
            double = 1
            generate = True
            if score % 3 == 0 and score != 0:
                if pecentage_uses < 3:
                    pecentage_uses += 1
                    print(f"Percentage regenerated: {pecentage_uses}")
                if double_time_uses < 3:
                    double_time_uses += 1
                    print(f"Double time regenerated: {double_time_uses}")

        else:
            print("Incorrect!")
            lives -= 1 * double
            total_rounds += 1 * double
            item1 = item2
            price1 = price2
            double = 1
            generate = True

    return score_list, total_rounds_list, username_list

