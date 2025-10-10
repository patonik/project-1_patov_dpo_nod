import datetime
import math
import time

from .constants import ROOMS, EVENT_MODULO, EVENT_TYPE_MODULO


def get_input(prompt="> "):
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def pseudo_random(seed, modulo):
    """Generate a pseudo-random integer in [0, modulo) using a mathematical formula."""
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = x - math.floor(x)
    return math.floor(fractional_part * modulo)


def trigger_trap(game_state):
    """Simulate a trap activation with consequences for the player."""
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state['player_inventory']

    if inventory:
        modulo = len(inventory)
        item_index = pseudo_random(game_state['steps_taken'], modulo)
        item_key = list(inventory.keys())[item_index]
        inventory.pop(item_key)
        print(f"Вы потеряли предмет: {item_key}")
    else:
        damage = pseudo_random(game_state['steps_taken'], EVENT_MODULO)
        if damage < 3:
            print("Ловушка оказалась смертельной! Вы проиграли.")
            game_state['game_over'] = True
        else:
            print("Вы чудом уцелели!")


def random_event(game_state):
    """Trigger a random event during player movement."""
    event_trigger = pseudo_random(game_state['steps_taken'], EVENT_MODULO)
    if event_trigger != 0:
        return  # No event occurs

    event_type = pseudo_random(round(time.time()*1000), EVENT_TYPE_MODULO)
    current_room = game_state['current_room']

    match event_type:
        case 0:  # Find Coin
            print("Вы нашли монетку на полу!")
            game_state['lab_items'][current_room].append("coin")
        case 1:  # Scare
            print("Вы слышите шорох в темноте...")
            if "sword" in game_state['player_inventory'].keys():
                print("Вы размахиваете мечом и отпугиваете существо!")
        case 2:  # Trap
            if (current_room == "trap_room"
                    and "torch" not in game_state['player_inventory'].keys()):
                print("Опасность! Пол под вами задрожал...")
                trigger_trap(game_state)


def describe_current_room(game_state):
    """Display the description of the current room, items, exits, and puzzle status."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    print(f"\n== {current_room.upper()} ==")

    print(room_data['description'])

    items = game_state['lab_items'][current_room]
    if items:
        print("Заметные предметы:", ", ".join(items))

    exits = room_data['exits']
    print("Выходы:", ", ".join(exits.keys()))

    if game_state['lab_puzzles'][current_room] is not None:
        if current_room == 'trap_room_2':
            if 'torch' in game_state['player_inventory'].keys() and \
                    game_state['player_inventory']['torch'] == 'on':
                print('You light the surroundings with your torch '
                      'and can see levers on the pillars of green, red, '
                      'and blue colors.')
                print('Solve the puzzle with "solve" command...')
            else:
                print("If only you had a light source...")
        else:
            print("Кажется, здесь есть загадка (используйте команду solve).")


def solve_puzzle(game_state):
    """Attempt to solve the puzzle in the current room."""
    current_room = game_state['current_room']
    puzzle = game_state['lab_puzzles'][current_room]

    if puzzle is None:
        print("Загадок здесь нет.")
        return

    if current_room == "dining_room":
        print('You start solving the puzzle but it takes eternity to solve it.'
              'You die out of old age serving philosophers')
        game_state['game_over'] = True
        return
    question, correct_answer = puzzle
    print(question)
    user_answer = get_input("Ваш ответ: ").lower()

    # Define alternative answers
    valid_answers = [correct_answer.lower()]
    if correct_answer == "10":
        valid_answers.append("десять")
    elif correct_answer == "шаг шаг шаг":
        valid_answers.append("шагшагшаг")  # Allow no spaces

    if user_answer in valid_answers:
        print("Правильно!")
        game_state['lab_puzzles'][current_room] = None  # Remove puzzle
        # Room-specific rewards
        if current_room == "library":
            game_state['player_inventory']["treasure_key"] = 'off'
            print("Вы получили ключ от сокровищницы!")
        elif current_room == "hall":
            game_state['player_inventory']["coin"] = 'off'
            print("Вы нашли монетку за правильный ответ!")
    else:
        print("Неверно. Попробуйте снова.")
        if current_room.startswith("trap_room"):
            trigger_trap(game_state)


def solve_riddle(game_state, riddle, item):
    """Attempt to solve the riddle related to the item in the inventory."""

    if riddle is None:
        print("No riddle.")
        return

    question, correct_answer, success, failure = riddle
    print(question)
    user_answer = get_input("Ваш ответ: ")

    if user_answer and user_answer.strip().lower() == correct_answer.lower():
        print("Правильно!")
        print(success)
    else:
        print("Failure!")
        print(failure)
    game_state['player_inventory'].pop(item)


def attempt_open_treasure(game_state):
    """Attempt to open the treasure chest in the treasure room."""
    if game_state['current_room'] != "treasure_room":
        print("Здесь нет сундука с сокровищами.")
        return

    if "treasure_key" in game_state['player_inventory'].keys():
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        game_state['lab_items']["treasure_room"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
    else:
        choice = get_input("Сундук заперт. ... Ввести код? (да/нет): ").lower()
        if choice == "да":
            puzzle = game_state['lab_puzzles']["treasure_room"]
            if puzzle is None:
                print("Код не требуется.")
                return
            question, correct_answer = puzzle
            print(question)
            code = get_input("Ваш ответ: ")
            if code.lower() == correct_answer.lower():
                print("Код верный! Сундук открыт!")
                game_state['lab_items']["treasure_room"].remove("treasure_chest")
                game_state['lab_puzzles']["treasure_room"] = None
                print("В сундуке сокровище! Вы победили!")
                game_state['game_over'] = True
            else:
                print("Неверный код.")
        else:
            print("Вы отступаете от сундука.")


def show_help(commands):
    """Display available commands with descriptions."""
    print("\nДоступные команды:")
    for cmd, desc in commands.items():
        print(f"{cmd:<16} - {desc}")
