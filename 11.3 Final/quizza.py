"""The main python file for containing game logic and code to be played."""

# Importing the necessary libraries
import time

from higher_lower_game import higher_or_lower, view_scores
from quizza import quizza_game, quizza_view_scores
from wordL import wordL_game, wordL_view_scores

# Variables for score and game state
main_game_loop = True
wait_time = 2

# Constants for compact design
int_error = "Invalid Input"

# An introduction greeting message.
print("Welcome to the Game Hub!")
time.sleep(wait_time)  # Stops the program for 2s so the user can read

# The main loop for the game.
while main_game_loop is True:
    print("\nYour game selection of avalible games is: \n"
          "1. Higher or Lower: \n"
          "Select if you think your current item is worth more or less. \n"
          "2. Quizza: \n"
          "General knowledge from a large range of questions. \n"
          "3. WordL: \n"
          "Wordle but with special abilities!\n"
          "0. Exit Game: \n")
    time.sleep(wait_time)  # Stops the program for 2s so the user can read

    game_selection_choice = 0

    try:
        game_selection_choice = int(input("Please select an option: "))

    except ValueError:
        print(int_error)
        continue

    if game_selection_choice not in [0, 1, 2, 3]:
        print("Not a valid selection option.")
        continue

    if game_selection_choice == 0:
        print("Exiting the program. Goodbye!")
        main_game_loop = False
        break

    while game_selection_choice == 1:
        print("Welcome to higher or lower.\n"
              "In this game you will recieve an item and its price,\n"
              "based on that price you will guess, 'more' or 'less'\n")
        time.sleep(wait_time)  # Stops the program for 2s so the user can read

        print("======Abilities======\n"
              "Type 'heal' lets the player to gain a life with 3 charges\n"
              "'percentage' will give the player a percentage of how much"
              " higher or lower the second item is with 3 charges\n"
              "'double time' will give the player twice the amount of "
              "score but take twice as much damage with 3 charges.\n")
        time.sleep(wait_time)

        print("'percentage' and 'double time' will "
              "regenerate every 3 points.\n"
              "You will have 3 lives and you lose when you hit 0.\n")

        time.sleep(wait_time)

        try:
            game_choice = int(input("What would you like to do?\n"
                                    "1. Play Game\n"
                                    "2. View Past Scores\n"
                                    "3. Exit Game\n\n"))

        except ValueError:
            print(int_error)
            continue

        if game_choice == 1:
            higher_or_lower()

        elif game_choice == 2:
            view_scores()  # Displays scores from all runs
            time.sleep(2)

        elif game_choice == 3:
            game_selection_choice = 0

        else:
            print("Not a valid selection option.")

    while game_selection_choice == 2:
        print("Welcome to Quizza!\n"
              "In this game you will be asked a question, given 4 options.\n"
              "You will have 3 lives and you lose when you hit 0.\n"
              "You will be given a score at the end of the game.\n")
        time.sleep(wait_time)

        print("======Abilities======\n"
              "Type '50/50' to remove 2 incorrect options with 3 charges\n"
              "'skip' will skip the current question with 3 charges\n"
              "'double' will give the player double points for the"
              "  next correct answer with 3 charges\n")
        time.sleep(wait_time)

        try:
            game_choice = int(input("What would you like to do?\n"
                                    "1. Play Game\n"
                                    "2. View Past Scores\n"
                                    "3. Exit Game\n\n"))

        except ValueError:
            print(int_error)
            continue

        if game_choice == 1:
            quizza_game()

        elif game_choice == 2:
            quizza_view_scores()  # Displays scores from all runs
            time.sleep(2)

        elif game_choice == 3:
            game_selection_choice = 0

        else:
            print("Not a valid selection option.")

    while game_selection_choice == 3:
        print("Welcome to WordL!\n"
              "In this game you will be asked to guess a 5 letter word.\n"
              "You will have 3 lives and you lose when you hit 0.\n"
              "You will be given a score at the end of the game.\n")

        time.sleep(wait_time)

        print("How the game works:\n"
              "When you guess a word, the game will give you feedback on your"
              " guess.\n"
              "If a letter is in the correct position, it will be shown in"
              " uppercase.\n"
              "If a letter is in the word but in the wrong position, "
              "it will be shown in lowercase.\n")

        time.sleep(wait_time)

        print("======Abilities======\n"
              "Type 'letter_reveal' to reveal the first "
              "letter in the word with 3 charges\n"
              "'extra_attempt' will give the player a guess, with 3 charges\n"
              "'skip_word' will skip the current word with 3 charges\n")

        time.sleep(wait_time)

        try:
            game_choice = int(input("What would you like to do?\n"
                                    "1. Play Game\n"
                                    "2. View Past Scores\n"
                                    "3. Exit Game\n\n"))

        except ValueError:
            print(int_error)
            continue

        if game_choice == 1:
            wordL_game()

        elif game_choice == 2:
            wordL_view_scores()  # Displays scores from all runs
            time.sleep(2)

        elif game_choice == 3:
            game_selection_choice = 0

        else:
            print("Not a valid selection option.")

