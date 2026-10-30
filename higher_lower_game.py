"""Game file for the higher or lower game."""

# Lists
score_list = []
total_rounds_list = []
username_list = []
ability_list = ["percentage", "heal", "double time", "%", "1", "2", "3",
                "help"]

# Predefined variables
heal_uses = 0
pecentage_uses = 0
double_time_uses = 0
username = ""


def view_scores(legacy, global_delay):
    """Display score history during this current run."""
    from game_interface_ui import game_ui

    if not score_list:
        game_ui(
            "No past scores yet.",
            legacy, global_delay
        )
        return []

    messages = ["Past Scores:"]

    # Pair each player's name with their score and total rounds,
    # then number the entries for display.
    for index, (score, total_rounds, username_rc) in enumerate(
        zip(score_list, total_rounds_list, username_list),
        start=1
    ):
        messages.append(
            f"{index}. {username_rc}: {score}/{total_rounds}"
        )

    game_ui(messages, legacy, global_delay)

    return list(zip(score_list, total_rounds_list, username_list))


def ability_shop(score, spent_points, heal_uses,
                 pecentage_uses, double_time_uses,
                 legacy, global_delay):
    """Allow players to buy additional ability uses."""
    from game_interface_ui import game_ui
    shop = True

    # Prices for purchasing extra ability uses
    heal_price = 10
    percentage_price = 3
    double_time_price = 1

    game_ui(
        [
            "Welcome to the Ability Shop!",
            f"Available points: {score - spent_points}",
            "",
            "0. Exit shop",
            f"1. Heal use: {heal_price} points",
            f"2. Percentage use: {percentage_price} points",
            f"3. Double Time use: {double_time_price} points"
        ],
        legacy, global_delay, True
    )

    # Keep the shop open until the player chooses to exit.
    while shop:
        # Calculate the player's remaining currency
        points = score - spent_points

        game_ui(
            f"Points remaining: {points}",
            legacy, global_delay
        )

        choice = input("Choose an option: ").strip()

        if choice == "0":
            shop = False

        elif choice == "1":
            # Only allow a purchase if the player has enough unspent points.
            if points >= heal_price:
                spent_points += heal_price
                heal_uses += 1
                game_ui("Purchased one Heal use!", legacy, global_delay)
            else:
                game_ui("Not enough points!", legacy, global_delay)

        elif choice == "2":
            if points >= percentage_price:
                spent_points += percentage_price
                pecentage_uses += 1
                game_ui(
                    "Purchased one Percentage use!",
                    legacy, global_delay
                )
            else:
                game_ui("Not enough points!", legacy, global_delay)

        elif choice == "3":
            if points >= double_time_price:
                spent_points += double_time_price
                double_time_uses += 1
                game_ui(
                    "Purchased one Double Time use!",
                    legacy, global_delay
                )
            else:
                game_ui("Not enough points!", legacy, global_delay)

        else:
            game_ui("Invalid choice. Enter 0, 1, 2 or 3.",
                    legacy, global_delay)

    # Return updated values to the main game
    return spent_points, heal_uses, pecentage_uses, double_time_uses


def higher_or_lower(legacy, global_delay):
    """Higher or lower game logic."""
    import random
    from game_storage_higher_lower import higher_or_lower
    from game_interface_ui import (game_username_ui, invalid_input, user_help,
                                   game_ui)

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
    spent_points = 0
    shop_interval = 5
    last_shop_round = 0

    # Select the starting item and retrieve its information from the
    # game's item dictionary.
    random_item = random.choice(list(higher_or_lower.keys()))

    # Get the item and price from the dictionary
    item1 = higher_or_lower[random_item]["item"]
    price1 = higher_or_lower[random_item]["price"]

    game_username_ui(legacy)

    username = input()

    while game_running is True:

        if lives <= 0:
            game_ui(
                f"Game Over! Your final score is: {score}/{total_rounds}",
                legacy, global_delay, True
            )
            score_list.append(score)
            total_rounds_list.append(total_rounds)
            username_list.append(username)
            game_running = False
            break

        # Generate a new comparison item when the previous round has finished
        # or when the current comparison needs to be replaced.
        if generate is True:
            random_item2 = random.choice(list(higher_or_lower.keys()))
            item2 = higher_or_lower[random_item2]["item"]
            price2 = higher_or_lower[random_item2]["price"]

        # Skip comparisons involving the same item or equal prices,
        # because they do not provide a clear higher-or-lower answer.
        if (
            item1 == item2
            or price1 == price2
        ):
            generate = True
            continue

        game_ui(
            # Creates a list so borders arn't printed for every line
            [
                f"Current Round: {total_rounds+1}",
                f"Lives: {lives}",
                f"Score: {score}",
                f"Item 1: {item1}",
                f"Price: {price1}"
            ],
            legacy, global_delay
        )

        game_ui(
            [
                "Abilities:",
                f"Heal uses left: {heal_uses}",
                f"Percentage uses left: {pecentage_uses}",
                f"Double Time uses left: {double_time_uses}"
            ],
            legacy, global_delay
        )

        game_ui(
            [
                f"Is {item2} worth more or less than {item1}?",
                "Enter 'more' or 'less':"
            ],
            legacy, global_delay
        )

        guess = input().lower()

        if guess not in ['more', 'less'] and guess not in ability_list:
            print(invalid_input(global_delay, legacy))
            continue

        # Process ability commands separately from normal guesses.
        if guess in ability_list:
            if guess in ('heal', '1') and heal_uses > 0:  # Heals
                lives += 1
                generate = False
                heal_uses -= 1
                game_ui(
                    [
                        f"Current Lives: {lives}",
                        f"Heal uses left: {heal_uses}"
                    ],
                    legacy, global_delay
                )

            elif guess in ('percentage', '%', '2') and pecentage_uses > 0:
                # Calculate the percentage difference between two item prices.
                percentage = (price1 - price2) / price1 * 100
                checked_percentage = abs(percentage)
                checked_percentage = round(checked_percentage, 2)
                generate = False
                pecentage_uses -= 1
                game_ui(
                    [
                        "Seccond item price is higher or lower",
                        f"{checked_percentage}%",
                        f"Percentage uses left: {pecentage_uses}"
                    ],
                    legacy, global_delay
                )

            elif guess in ('double time', '3') and double_time_uses > 0:
                double = 2
                generate = False
                double_time_uses -= 1
                game_ui(
                    [
                        "You now can gain twice the points",
                        "or lose double the lives on this question.",
                        f"Double time uses left: {double_time_uses}"
                    ],
                    legacy, global_delay
                )

            elif guess == 'help':
                user_help(global_delay, legacy)

        elif (
            (guess == "more" and price2 > price1)
            or (guess == "less" and price2 < price1)
        ):
            game_ui(
                "Correct!",
                legacy, global_delay, True
            )
            score += 1 * double
            total_rounds += 1
            item1 = item2
            price1 = price2
            double = 1
            generate = True

        else:
            game_ui(
                "Incorrect!",
                legacy, global_delay, True
            )
            lives -= 1 * double
            total_rounds += 1
            item1 = item2
            price1 = price2
            double = 1
            generate = True

        # Open the shop after every five completed rounds
        if (
            total_rounds > 0
            and total_rounds % shop_interval == 0
            and total_rounds != last_shop_round
        ):
            (
                spent_points,
                heal_uses,
                pecentage_uses,
                double_time_uses
            ) = ability_shop(
                score,
                spent_points,
                heal_uses,
                pecentage_uses,
                double_time_uses,
                legacy,
                global_delay
            )

            last_shop_round = total_rounds

    return score_list, total_rounds_list, username_list
