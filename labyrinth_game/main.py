#!/usr/bin/env python3
from .constants import COMMANDS, ROOMS
from .player_actions import move_player, show_inventory, take_item, use_item
from .utils import (
    attempt_open_treasure,
    describe_current_room,
    get_input,
    show_help,
    solve_puzzle,
)


def process_command(game_state, command):
    """Process a user command and update game state."""
    parts = command.strip().lower().split(maxsplit=1)
    cmd = parts[0] if parts else ""
    arg = parts[1] if len(parts) > 1 else ""

    # Handle one-word direction commands (north, south, east, west)
    directions = ["north", "south", "east", "west"]
    if cmd in directions:
        move_player(game_state, cmd)
        return

    match cmd:
        case "look":
            describe_current_room(game_state)
        case "go":
            if arg:
                move_player(game_state, arg)
            else:
                print("Укажите направление (например, go north).")
        case "take":
            if arg == "treasure_chest":
                print("Вы не можете поднять сундук, он слишком тяжелый.")
            elif arg:
                take_item(game_state, arg)
            else:
                print("Укажите предмет (например, take torch).")
        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Укажите предмет (например, use torch).")
        case "inventory":
            show_inventory(game_state)
        case "solve":
            if game_state['current_room'] == "treasure_room":
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        case "quit" | "exit":
            print("Игра завершена.")
            game_state['game_over'] = True
        case "help":
            show_help(COMMANDS)
        case _:
            print("Неизвестная команда. Введите help для списка команд.")


def initialize_state() -> dict:
    """Initializes game state using constant configurations."""
    game_state = {'player_inventory': {}, 'current_room': 'entrance',
                  'game_over': False, 'steps_taken': 0,
                  'lab_items': populate_state(ROOMS, 'items'),
                  'lab_puzzles': populate_state(ROOMS, 'puzzle')
                  }
    return game_state


def populate_state(rooms: dict, parameter: str) -> dict:
    """Populates game state with labyrinth rooms' parameters."""
    i_dict = {}
    for room in rooms.keys():
        i_dict[room] = ROOMS[room][parameter][:] if ROOMS[room][parameter] is not None \
            else None
    return i_dict


def main():
    """Main game loop for Labyrinth of Treasures."""
    game_state = initialize_state()
    print("Добро пожаловать в Лабиринт сокровищ!")
    describe_current_room(game_state)

    while not game_state['game_over']:
        command = get_input()
        process_command(game_state, command)


if __name__ == "__main__":
    main()
