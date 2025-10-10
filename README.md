# Labyrinth of Treasures

"Labyrinth of Treasures" is a text-based adventure game written in Python.
Navigate through a mysterious labyrinth, solve puzzles, avoid traps,
and collect items to unlock the treasure chest in the `treasure_room`.
The game features random events, inventory management, and a command-driven interface,
providing an engaging experience for players.

## Installation

The game is available as a `.whl` package on PyPI.
Follow these steps to install and run it:

1. Install Poetry (if not already installed):

   `sudo apt install python3-poetry`

2. Ensure Poetry version is 1.8.4 or higher:

   `poetry --version`

3. Create a New Project Directory:

   `mkdir labyrinth_game`

   `cd labyrinth_game`

4. Initialize a Poetry Environment:

   `poetry init -n`

5. Install the Game from PyPI:

   `poetry add labyrinth_game`

6. Verify Installation:Check that the package is installed:

   `poetry show`

## Requirements

* Python: 3.11 or higher
* Poetry: 1.8.2 or higher
* Make: Required for running the make project command
* Operating System: Linux (tested on Ubuntu)
* Dependencies: None (game uses only the standard math module)

## Usage

* **Run the Game**: Ensure you’re in the project directory 
with the Poetry environment activated.
* **Use the Makefile to start the game**:

`make project`

Alternatively, if the Makefile is not available, run:

`poetry run project`

## Gameplay:

The game starts in the entrance room.
Use commands to navigate, interact with items, and solve puzzles.
Objective: Reach the treasure_room and open the treasure_chest to win.

## Available Commands:

* go <direction> or <direction> (e.g., north, go north): Move in the specified direction (
* north, south, east, west).
* look: Display the current room’s description, items, exits, and puzzle status.
* take <item>: Pick up an item from the room (e.g., take torch).
* use <item>: Use an item from your inventory (e.g., use torch).
* inventory: Show your current inventory.
* solve: Attempt to solve a puzzle in the current room or open the treasure chest in
* treasure_room.
* help: Display the list of available commands.
* quit or exit: Exit the game.

## Example Gameplay

Here's a complete playthrough from launch to winning the treasure:

<details>
<summary>Click to play the recording</summary>

<a title="Labyrinth of Treasures Demo" href="https://asciinema.org/a/HgbZC2EoLYQ5hsRzRmPadGyEZ?autoplay=1" target="_blank">
<img src="https://asciinema.org/a/HgbZC2EoLYQ5hsRzRmPadGyEZ.svg" style="max-width:100%;" alt="asciicast" />
</a>
</details>

## Notes

* **Random Events**: Moving may trigger random events like finding a coin, hearing a
scare, or activating a trap in trap_room (if you lack a torch).
* **Puzzles**: Some rooms (e.g., hall, library, trap_room) have puzzles. Correct answers
yield rewards like treasure_key or coin.
* **Treasure Room**: Requires rusty_key to open bronze_box
and magic treasure_key to enter treasure_room and open treasure_chest (or a correct code).

**Author**: patonik

**License**: This project is licensed under the GNU GENERAL PUBLIC LICENSE.