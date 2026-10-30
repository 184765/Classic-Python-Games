"""The main python file for containing game logic and code to be played."""

# Importing the necessary libraries
import time

from higher_lower_game import higher_or_lower, view_scores
from quizza import quizza_game, quizza_view_scores
from wordL import wordl_game, wordl_view_scores

# Variables for score and game state
main_game_loop = True
wait_time = 2
legacy = False
settings_adjust = 0
global_delay = 1.5  # Global delay variable

# Keep returning to the main menu until the user chooses to exit.
while main_game_loop is True:

    # UI imports
    from game_interface_ui import (main_screen_information, invalid_input,
                                   game_selection_choice_input_ui,
                                   game_selection_higher_lower_ui,
                                   game_selection_quizza_ui,
                                   game_selection_wordl_ui,
                                   game_selection_game_prompt_ui,
                                   game_settings_ui,
                                   game_selection_exit)

    # An introduction greeting message
    main_screen_information(global_delay, legacy)

    time.sleep(global_delay)  # Stops the program for 2s so the user can read

    # Makes sure game_selection_choice has a value
    game_selection_choice = -1

    game_selection_choice_input_ui(legacy)

    # Checks if the user input is valid and if not, ask for a new input
    try:
        game_selection_choice = int(input())

    # If the user input is not a number, it will print an invalid input
    except ValueError:
        invalid_input(global_delay, legacy)
        continue

    # Handle input that cannot be converted into an integer.
    if game_selection_choice not in [1, 2, 3, 4, 5]:
        invalid_input(global_delay, legacy)
        continue

    # Apply the setting selected by the user.
    if game_selection_choice == 4:
        game_settings_ui(global_delay, legacy)

        settings_choice = int(input())  # User select which setting to change

        if settings_choice == 1:
            print("---          Pick Delay Time.           ---\n"
                  "-------------------------------------------")

            try:
                settings_adjust = float(input())

            except ValueError:
                invalid_input(global_delay, legacy)
                continue

            global_delay = settings_adjust

            print(f"---    Delay Time Now: {global_delay}   ---\n"
                  f"-------------------------------------------")

        # Enable legacy mode or restore the modern terminal style.
        elif settings_choice == 2:
            print("---          Pick Terminal Type.        ---\n"
                  "---            [1] for Legacy           ---\n"
                  "---            [2] for Modern           ---\n"
                  "-------------------------------------------")

            try:
                settings_adjust = int(input())

            except ValueError:
                invalid_input(global_delay, legacy)
                continue

            if settings_adjust == 1:
                legacy = True
                print("###     Terminal Type Now: Legacy       ###\n"
                      "###########################################")

            elif settings_adjust == 2:
                legacy = False
                print("---    Terminal Type Now: Modern       ---\n"
                      "-------------------------------------------")

            else:
                invalid_input(global_delay, legacy)
                continue

        elif settings_choice == 3:
            game_selection_exit(global_delay, legacy)
            game_selection_choice = 0

        time.sleep(global_delay)

        continue

    if game_selection_choice == 5:
        game_selection_exit(global_delay, legacy)
        main_game_loop = False
        break

    # Keep showing this game's menu until the user returns to the main menu.
    while game_selection_choice == 1:
        # Displays ability and game information
        game_selection_higher_lower_ui(global_delay, legacy)

        game_selection_game_prompt_ui(global_delay, legacy)

        try:
            game_choice = int(input())

        except ValueError:
            invalid_input(global_delay, legacy)
            continue

        if game_choice == 1:
            higher_or_lower(legacy, global_delay)

        elif game_choice == 2:
            view_scores(legacy, global_delay)  # Displays scores from all runs
            time.sleep(global_delay)

        elif game_choice == 3:
            game_selection_exit(global_delay, legacy)
            game_selection_choice = 0

        else:
            invalid_input(global_delay, legacy)

    while game_selection_choice == 2:
        game_selection_quizza_ui(global_delay, legacy)

        game_selection_game_prompt_ui(global_delay, legacy)

        try:
            game_choice = int(input())

        except ValueError:
            invalid_input(global_delay, legacy)
            continue

        if game_choice == 1:
            quizza_game(global_delay, legacy)  # Starts the Quizza game

        elif game_choice == 2:
            # Displays scores from all runs
            quizza_view_scores(legacy, global_delay)
            time.sleep(global_delay)

        elif game_choice == 3:
            game_selection_exit(global_delay, legacy)
            game_selection_choice = 0

        else:
            invalid_input(global_delay, legacy)

    while game_selection_choice == 3:
        game_selection_wordl_ui(global_delay, legacy)

        game_selection_game_prompt_ui(global_delay, legacy)

        try:
            game_choice = int(input())

        except ValueError:
            invalid_input(global_delay, legacy)
            continue

        if game_choice == 1:
            wordl_game(global_delay, legacy)

        elif game_choice == 2:
            wordl_view_scores(legacy, global_delay)  # Displays scores
            time.sleep(global_delay)

        elif game_choice == 3:
            game_selection_exit(global_delay, legacy)
            game_selection_choice = 0

        else:
            invalid_input(global_delay, legacy)
