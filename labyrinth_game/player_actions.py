from .constants import ROOMS, RIDDLES
from .utils import describe_current_room, random_event, solve_riddle, trigger_trap


def show_inventory(game_state):
    inventory = game_state['player_inventory']
    if inventory:
        print("Ваш инвентарь:", ", ".join(inventory))
    else:
        print("Ваш инвентарь пуст.")


def move_player(game_state, direction):
    """Move the player to a new room in the specified direction."""
    current_room = game_state['current_room']
    exits = ROOMS[current_room]['exits']

    if direction in exits:
        next_room = exits[direction]
        if (next_room == "treasure_room"
                and "treasure_key" not in game_state['player_inventory'].keys()):
            print("Дверь заперта. Нужен ключ, чтобы пройти дальше.")
            return
        if current_room == "dining_room" and game_state['lab_puzzles'][current_room] is not None:
            print("The door seems to be blocked. Probably you need to solve the puzzle to unlock it...")
            return
        if current_room.startswith("trap_room") and game_state['lab_puzzles'][current_room] is not None:
            trigger_trap(game_state)
            if game_state['game_over']:
                return
        game_state['current_room'] = next_room
        game_state['steps_taken'] += 1
        if next_room == "treasure_room":
            print(
                "Вы используете найденный ключ, чтобы открыть путь в комнату сокровищ.")
            game_state
        describe_current_room(game_state)
        random_event(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """Take an item from the current room and add it to the player's inventory."""
    current_room = game_state['current_room']
    room_items = game_state['lab_items'][current_room]

    if item_name in room_items:
        if item_name == 'treasure_chest':
            print('Too heavy...')
            return
        game_state['player_inventory'][item_name] = 'off'
        room_items.remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    """Use an item from the player's inventory."""
    if item_name not in game_state['player_inventory'].keys():
        print("У вас нет такого предмета.")
        return

    match item_name:
        case "torch":
            print("Стало светлее.")
            game_state['player_inventory']['torch'] = 'on'
        case "sword":
            print("Вы чувствуете себя увереннее.")
        case "bronze_box":
            print("Вы открыли шкатулку!")
            if "rusty_key" in game_state['player_inventory'].keys():
                print('Prey! There is an inscription on the box\'s lid: ')
                solve_riddle(game_state, RIDDLES['riddle_1'], 'bronze_box')
                game_state['player_inventory'].pop('rusty_key')
            else:
                print('You need a key to open it...')
        case _:
            print("Вы не знаете, как это использовать.")
