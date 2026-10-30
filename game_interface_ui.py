"""This module contains the functions for the game interface UI."""

""" References which were used while creating the code:
This was used to help understand how to used textwrap for a more effecient
way to display text in the terminal rather than using print statements and
having to manually add new lines and spaces to make it look good in the
terminal. Due to being discoved late only the games use it.
https://docs.python.org/3/library/textwrap.html
"""


# 16/10/26: Making the python terminals with a UI to make it more appealing and easy to read to increase the engadgment time of the end user.
# Creating functins to shorten the code in other python files.


def main_screen_information(global_delay, legacy):
    """Display main screen information."""
    # Imports time for delays
    import time

    # Main header
    menu_a = ("===========================================\n"
              "===                                     ===\n"
              "===       Welcome to the Game Hub!      ===\n"
              "===                                     ===\n"
              "===========================================")

    # Sub header with game selection
    menu_a1 = ("---       Game selection optinons.      ---\n"
               "-------------------------------------------\n"
               "---                                     ---\n"
               "---         [1]Higher or Lower          ---\n"
               "---Select if you think your current item---\n"
               "---          is worth more or less.     ---\n"
               "---                                     ---\n"
               "-------------------------------------------")

    # Using different strings so they can be printed seperately to allow waits
    menu_a2 = ("---                                     ---\n"
               "---              [2]Quizza              ---\n"
               "--- General knowledge from a large range---\n"
               "---            of questions.            ---\n"
               "---                                     ---\n"
               "-------------------------------------------")

    menu_a3 = ("---                                     ---\n"
               "---               [3]WordL              ---\n"
               "---  Wordle but with special abilities! ---\n"
               "---                                     ---\n"
               "-------------------------------------------")

    menu_a4 = ("---             [4]Settings             ---\n"
               "-------------------------------------------\n"
               "---               [5]Exit               ---\n"
               "-------------------------------------------")

    # Select the border style based on the user's terminal setting.
    # The delay between sections gives the user time to read each screen.
    if legacy is True:
        print(menu_a.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_a1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_a2.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_a3.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_a4.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_a)

        time.sleep(global_delay)

        print(menu_a1)

        time.sleep(global_delay)

        print(menu_a2)

        time.sleep(global_delay)

        print(menu_a3)

        time.sleep(global_delay)

        print(menu_a4)

        time.sleep(global_delay)


def game_selection_choice_input_ui(legacy):
    """Shortens the code in the main doccument to make it to read and edit."""
    menu_b = ("---                                     ---\n"
              "---       Please select an option.      ---\n"
              "---                                     ---\n"
              "-------------------------------------------")

    # Use the legacy border characters when legacy mode is enabled.
    if legacy is True:
        print(menu_b.replace("=", "#").replace("-", "#"))

    else:
        print(menu_b)


def invalid_input(global_delay, legacy):
    """UI to be used when a invalid input is recieved."""
    # Imports time for delays
    import time

    menu_c = ("---            INVALID INPUT!           ---\n"
              "-------------------------------------------")

    if legacy is True:
        print(menu_c.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_c)

        time.sleep(global_delay)


def game_selection_higher_lower_ui(global_delay, legacy):
    """Information about game and abilities for higher or lower."""
    import time

    menu_d = ("\n===========================================\n"
              "===                                     ===\n"
              "===     Welcome to Higher or Lower!     ===\n"
              "===                                     ===\n"
              "===========================================")

    menu_d1 = ("---                                     ---\n"
               "---In this game you will recieve an item---\n"
               "---  and its price, based on that price ---\n"
               "---   you will guess, 'more' or 'less'  ---\n"
               "-------------------------------------------")

    menu_d2 = ("---              ABILITIES              ---\n"
               "-------------------------------------------\n"
               "---  Type [1] to heal, lets the player  ---\n"
               "---     gain a life up to 3 charges.    ---\n"
               "-------------------------------------------\n"
               "--- Type [2] to get a percentage which  ---\n"
               "---gives a percentage based on how much ---\n"
               "--- higher or lower the seccond item is ---\n"
               "-------------------------------------------\n"
               "--- Type [3] to use double time, where  ---\n"
               "--- you gain twice the points but take  ---\n"
               "--- twice the damage for that question. ---\n"
               "-------------------------------------------")

    menu_d3 = ("---  There will be a shop that appears  ---\n"
               "---  on every 5th round where you can   ---\n"
               "---   spend your points on purchasing   ---\n"
               "---  new abilility charges to be used.  ---\n"
               "-------------------------------------------")

    if legacy is True:
        print(menu_d.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_d1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_d2.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_d3.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_d)

        time.sleep(global_delay)

        print(menu_d1)

        time.sleep(global_delay)

        print(menu_d2)

        time.sleep(global_delay)

        print(menu_d3)

        time.sleep(global_delay)


def game_selection_quizza_ui(global_delay, legacy):
    """Information about game and abilities for quizza."""
    import time

    menu_e = ("\n===========================================\n"
              "===                                     ===\n"
              "===         Welcome to Quizza!          ===\n"
              "===                                     ===\n"
              "===========================================")

    menu_e1 = ("---                                     ---\n"
               "---  In this game you will be asked a   ---\n"
               "--- question, given 4 options. You will ---\n"
               "--- have 3 lives and you lose when you  ---\n"
               "--- hit 0. You will be given a score at ---\n"
               "---        the end of the game.         ---\n"
               "-------------------------------------------")

    menu_e2 = ("---              ABILITIES              ---\n"
               "-------------------------------------------\n"
               "--- Type '50/50' to remove 2 incorrect  ---\n"
               "--- options with 3 charges or type '1'. ---\n"
               "-------------------------------------------\n"
               "--- 'skip' will skip the current        ---\n"
               "--- question with 3 charges or '2'.     ---\n"
               "-------------------------------------------\n"
               "--- 'double' will give the player       ---\n"
               "--- double points for the next correct  ---\n"
               "--- answer with 3 charges or '3'.       ---\n"
               "-------------------------------------------")

    menu_e3 = ("---  There will be a shop that appears  ---\n"
               "---  on every 5th round where you can   ---\n"
               "---   spend your points on purchasing   ---\n"
               "---  new abilility charges to be used.  ---\n"
               "-------------------------------------------")

    if legacy is True:
        print(menu_e.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_e1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_e2.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_e3.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_e)

        time.sleep(global_delay)

        print(menu_e1)

        time.sleep(global_delay)

        print(menu_e2)

        time.sleep(global_delay)

        print(menu_e3)

        time.sleep(global_delay)


def game_selection_wordl_ui(global_delay, legacy):
    """Information about game and abilities for wordl."""
    import time

    menu_f = ("\n===========================================\n"
              "===                                     ===\n"
              "===         Welcome to WordL!           ===\n"
              "===                                     ===\n"
              "===========================================")

    menu_f1 = ("---                                     ---\n"
               "---  In this game you will be asked to  ---\n"
               "--- guess a 5 letter word. You will     ---\n"
               "--- have 3 lives and you lose when you  ---\n"
               "--- hit 0. You will be given a score at ---\n"
               "---        the end of the game.         ---\n"
               "-------------------------------------------")

    menu_f2 = ("---              ABILITIES              ---\n"
               "-------------------------------------------\n"
               "--- Type 'letter_reveal' to reveal the  ---\n"
               "--- first letter in the word with 3     ---\n"
               "--- charges or type '1'.                ---\n"
               "-------------------------------------------\n"
               "--- 'extra_attempt' will give the player---\n"
               "--- a guess, with 3 charges or '2'.     ---\n"
               "-------------------------------------------\n"
               "--- 'skip_word' will skip the current   ---\n"
               "--- word with 3 charges or '3'.         ---\n"
               "-------------------------------------------")

    menu_f3 = ("---  There will be a shop that appears  ---\n"
               "---  on every 5th round where you can   ---\n"
               "---   spend your points on purchasing   ---\n"
               "---  new abilility charges to be used.  ---\n"
               "-------------------------------------------")

    if legacy is True:
        print(menu_f.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_f1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_f2.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_f3.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_f)

        time.sleep(global_delay)

        print(menu_f1)

        time.sleep(global_delay)

        print(menu_f2)

        time.sleep(global_delay)

        print(menu_f3)

        time.sleep(global_delay)


def game_selection_game_prompt_ui(global_delay, legacy):
    """Prompt user to select a game."""
    import time

    menu_g = ("---     What would you like to do?      ---\n"
              "-------------------------------------------\n"
              "---       [1]Play Game                  ---\n"
              "---       [2]View Past Scores           ---\n"
              "---       [3]Exit Game                  ---\n"
              "-------------------------------------------")

    if legacy is True:
        print(menu_g.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_g)

        time.sleep(global_delay)


def game_selection_exit(global_delay, legacy):
    """Exit message."""
    import time

    menu_h = ("===========================================\n"
              "===                                     ===\n"
              "===    Returning to Start / Exiting     ===\n"
              "===                                     ===\n"
              "===========================================")

    if legacy is True:
        print(menu_h.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_h)

        time.sleep(global_delay)


# FINISH THIS WITH THE LEGACY TERMINAL
def game_settings_ui(global_delay, legacy):
    """Display Settings UI."""
    import time

    menu_i = ("===========================================\n"
              "===                                     ===\n"
              "===             Settings                ===\n"
              "===                                     ===\n"
              "===========================================")

    menu_i1 = ("---                                     ---\n"
               "---  [1] Change Global Delay            ---\n"
               "---  [2] Old Python Terminal UI         ---\n"
               "---  [3] Return to Main Menu            ---\n"
               "-------------------------------------------")

    if legacy is True:
        print(menu_i.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_i1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_i)

        time.sleep(global_delay)

        print(menu_i1)

        time.sleep(global_delay)


def game_username_ui(legacy):
    """Game Username Prompt."""
    menu_j = ("===========================================\n"
              "===     Please enter your username:     ===\n"
              "===========================================")

    if legacy is True:
        print(menu_j.replace("=", "#").replace("-", "#"))

    else:
        print(menu_j)


def user_help(global_delay, legacy):
    """User help UI."""
    import time

    menu_k = ("===========================================\n"
              "===                                     ===\n"
              "===              User Help              ===\n"
              "===                                     ===\n"
              "===========================================")

    menu_k1 = ("---                                     ---\n"
               "---  [1] How to play the games          ---\n"
               "---  [2] How to use abilities           ---\n"
               "---  [3] Return to Game                 ---\n"
               "-------------------------------------------")

    menu_k2 = ("---  Which game picked for explanation? ---\n"
               "---  [1] Higher or Lower                ---\n"
               "---  [2] Quizza                         ---\n"
               "---  [3] WordL                 ---\n"
               "-------------------------------------------")

    if legacy is True:
        print(menu_k.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

        print(menu_k1.replace("=", "#").replace("-", "#"))

        time.sleep(global_delay)

    else:
        print(menu_k)

        time.sleep(global_delay)

        print(menu_k1)

        time.sleep(global_delay)

    # Ask which help category the user wants, then select a game
    # if they request game-specific instructions.
    try:
        user_help_choice = int(input())

        if user_help_choice == 1:
            if legacy is True:
                print(menu_k2.replace("=", "#").replace("-", "#"))

                time.sleep(global_delay)

            else:
                print(menu_k2)

                time.sleep(global_delay)

            # Ask which game's instructions should be displayed.
            user_help_game_choice = int(input())

            if user_help_game_choice == 1:
                game_selection_higher_lower_ui(global_delay, legacy)
            elif user_help_game_choice == 2:
                game_selection_quizza_ui(global_delay, legacy)
            elif user_help_game_choice == 3:
                game_selection_wordl_ui(global_delay, legacy)
            else:
                print(invalid_input(global_delay, legacy))
                return

        elif user_help_choice == 2:
            if legacy is True:
                print(menu_k2.replace("=", "#").replace("-", "#"))

                time.sleep(global_delay)

            else:
                print(menu_k2)

                time.sleep(global_delay)

            user_help_game_choice = int(input())

            if user_help_game_choice == 1:
                game_selection_higher_lower_ui(global_delay, legacy)
            elif user_help_game_choice == 2:
                game_selection_quizza_ui(global_delay, legacy)
            elif user_help_game_choice == 3:
                game_selection_wordl_ui(global_delay, legacy)
            else:
                print(invalid_input(global_delay, legacy))
                return

        elif user_help_choice == 3:
            return

    # Handle non-numeric menu input instead of allowing the program to crash.
    except ValueError:
        print(invalid_input(global_delay, legacy))
        return


# Reworked function to make UI creation easier for game sections
def game_ui(message, legacy, global_delay, title=False):
    """User Interface for Game."""
    # Imports needed
    import time
    import textwrap  # Used to split text into paragraphs for a consistent UI

    # Sets the width of the textwrap
    width = 43  # Includes the UI border
    content_width = 37  # Sets the allowed amount of text discluding UI

    # Adjusts border based on user settings
    if legacy is True:
        edge = "#"  # Sets up border used for UI
        separator = "#" * width

    # Title used for key headings inside of the game
    elif title is True:
        edge = "="
        separator = "=" * width

    else:
        edge = "-"
        separator = "-" * width

    # Convert a single message into separate lines, or use the supplied
    # list of messages, before wrapping and displaying the text.
    if isinstance(message, str):  # Checks if it is a string
        # Split the message every new line for several messages and compact UI
        messages = message.split("\n")

    else:
        messages = message  # If not a string, assume it is a list of messages

    # Print the UI
    print(separator)  # Print the top border

    # Processes each line seperately to allow for textwrap to be used
    for lines in messages:
        # Converts the line into multiple shorter lines if its too large
        wrapped_lines = textwrap.wrap(str(lines), width=content_width)

        # Prints an empty line if recieved
        if not wrapped_lines:
            wrapped_lines = [""]  # Ensure at least one empty line is printed

        # Displays each line produced by textwrap
        for line in wrapped_lines:
            if title is True:
                line = line.center(content_width)  # Center the title text

            print(f"{edge * 3}{line.ljust(content_width)}{edge * 3}")

    print(separator)  # Prints the bottem line

    time.sleep(global_delay)
