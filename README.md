<img width="878" height="575" alt="Screenshot 2026-09-18 at 09 54 00" src="https://github.com/user-attachments/assets/565c38e1-cc4c-48fa-b36f-086b373ed479" />

# Games Compendium

A Python command-line game collection containing three different games: **Higher or Lower, Quizza, and WordL**.

The project was created as a collection of simple games that can be played from one main menu. Each game has its own gameplay, scoring system and features, while the main program handles navigation between them.

## Games

### Higher or Lower

Higher or Lower is a price guessing game. The player is shown an item and its price, then has to guess whether the next item will cost more or less.

The game includes:

* 3 lives
* Score tracking
* Randomised items and prices
* Abilities
* Ability charges
* Ability regeneration
* Percentage hints
* A double-time scoring ability

### Quizza

Quizza is a general knowledge quiz game. The player is given a question and multiple possible answers and gains points for answering correctly.

The game includes:

* Multiple-choice questions
* Lives
* Score tracking
* Randomised questions
* 50/50 ability
* Skip ability
* Double-score ability

### WordL

WordL is a five-letter word guessing game based around the main idea of Wordle. The player attempts to find the correct word while receiving feedback about their guesses.

The game includes:

* Five-letter words
* Multiple attempts
* Word validation
* Letter feedback
* Score tracking
* Lives

## How It Was Made

The project was made using **Python** and was developed gradually rather than creating every feature at once.

I first created the main menu and basic game structure. I then developed the games individually, starting with the core gameplay before adding additional features such as abilities, scoring, feedback and validation.

The games are separated into different Python files, while `main.py` is used to run the overall program and navigate between the games.

During development I regularly tested the games and fixed problems as they appeared. Some examples include preventing repeated random items, fixing percentage calculations, adding input validation, improving ability logic, adding better player feedback and making sure WordL only accepts valid words.

## Development Process

The project went through multiple stages of development:

1. Created the main game menu.
2. Built the basic Higher or Lower gameplay.
3. Added abilities and scoring systems.
4. Created Quizza and its question system.
5. Created WordL and its word-generation system.
6. Added instructions and gameplay feedback.
7. Tested the games and fixed bugs.
8. Improved the code structure and game logic.

Testing was an important part of the project because it helped identify problems that were not obvious while writing the code. For example, testing found issues with repeated items, questions not displaying correctly, ability feedback and invalid WordL guesses.

## What I Learned

Through developing this project, I learned more about using Python functions, lists, dictionaries, loops, conditional statements and randomisation. I also learned that testing is important because code can appear to work while still having problems when different inputs or situations are used.

A major part of the project was learning how to build features gradually. Instead of trying to make the complete game immediately, I created a basic working version first and then added features and fixes over time.

## Project Structure

The main files are separated by their purpose:

* `main.py` — Runs the main program and game selection menu.
* `higher_lower_game.py` — Contains the Higher or Lower game.
* `quizza.py` — Contains the Quizza game.
* `wordL.py` — Contains the WordL game.
* Game data/storage files — Contain information used by the games.

## Technologies and Resources

The main programming language used was **Python**.

The project also used external Python resources/libraries where needed, including **Wonderwords** for generating words for WordL.

## Future Development

There are still areas that could be improved. These include further improving the menu and interface, expanding the ability systems, improving score saving, adding more game content and continuing to test the games with different users.

The project is intended to be developed further through testing and iteration rather than being considered finished after the first working version.
