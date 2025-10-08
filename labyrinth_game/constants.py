ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. '
                       'На полу лежит старый факел.',
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. '
                       'По центру стоит пьедестал с запечатанным сундуком.',
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room',
                  'east': 'trap_room_2'},
        'items': [],
        'puzzle': (
            'На пьедестале надпись: "Назовите число, которое идет после девяти". '
            'Введите ответ цифрой или словом.',
            '10')
    },
    'trap_room': {
        'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: '
                       '"Осторожно — ловушка".',
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': (
            'Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд '
            '(введите "шаг шаг шаг")',
            'шаг шаг шаг')
    },
    'library': {
        'description': 'Пыльная библиотека. На полках старые свитки. '
                       'Где-то здесь может быть ключ от сокровищницы.',
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': (
            'В одном свитке загадка: "Что растет, когда его съедают?" '
            '(ответ одно слово)',
            'резонанс')
    },
    'armory': {
        'description': 'Старая оружейная комната. На стене висит меч, '
                       'рядом — небольшая бронзовая шкатулка.',
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None
    },
    'treasure_room': {
        'description': 'Комната, на столе большой сундук. '
                       'Дверь заперта — нужен особый ключ.',
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': (
            'Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага,'
            ' 2*5= ? )',
            '10')
    },
    'trap_room_2': {
        'description': 'In the middle of the room rotten human remains cause'
                       ' repugnant stench. '
                       'You are terrified but try to explore the environment.',
        'exits': {'north': 'dining_room', 'east': 'hall'},
        'items': ['skull', 'cobweb'],
        'puzzle': ('The levers should be activated in particular order. What is it?',
                   'red green blue')
    },
    'dining_room': {
        'description': 'There is a dining table at which 5 asian people are sitting '
                       'and seem to be pondering. '
                       'They have only 5 chopsticks, and once in a while '
                       'some of them start eating',
        'exits': {'south': 'trap_room_2'},
        'items': ['chainsaw'],
        'puzzle': ('There is an inscription on the wall: '
                   '\'Prevent wise men from starvation and they will share'
                   ' their wisdom\'',
                   '')
    }
}

COMMANDS = {
    "go <direction>": "перейти в направлении (north/south/east/west)",
    "look": "осмотреть текущую комнату",
    "take <item>": "поднять предмет",
    "use <item>": "использовать предмет из инвентаря",
    "inventory": "показать инвентарь",
    "solve": "попытаться решить загадку в комнате",
    "quit": "выйти из игры",
    "help": "показать это сообщение"
}

RIDDLES = {
    "riddle_1":
        (
            '\'I can fall off a building and live, but put me in water I will die. '
            'What am I?\'',
            'paper',
            'When you pronounce the answer a piece of paper appears in your hands. '
            'You look at the picture on it. '
            'It is dim but you can make out a wounded knight holding '
            'a tricolor flag. '
            'The colors are red, green, and blue',
            'The bronze box disappears. Probably, this was important...'
        )

}
