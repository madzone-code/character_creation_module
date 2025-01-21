from random import randint

# Импорт библиотеки для графики.
from graphic_arts.start_game_banner import run_screensaver

# Определяем глобальные константы
DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    '''Описание родительского класса героя на базе которого
    будут создаваться остальные классы.
    '''

    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'
    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    # Конструктор класса.
    def __init__(self, name):
        self.name = name

    # 3 метода класса: атака, защита, особое.
    # Зависят от констант и свойств объекта.
    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return (f'{self.name} нанёс противнику урон, равный {value_attack}')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} ед. урона')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}"')

    # Метод строкового представления объекта(выводится при печати объекта).
    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'


# 3 Дочерних класса с описанием и частью переопределенных констант.
class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def choice_char_class(char_name: str) -> Character:
    '''Функция выбора класса. На вход принимает имя (str).'''

    # Добавляем словарь, где ключи - имена классов,
    # а значения - соответствующие классы.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    approve_choice: str = ''

    # Пока не жмякнем 'y', выбираем класс.
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                               'за которого хочешь играть: Воитель — warrior, '
                               'Маг — mage, Лекарь — healer: '
                               )
        if selected_class in game_classes:
            char_class: Character = game_classes[selected_class](char_name)
        # Если ввод не из перечисленных классов,
        # то создаем персонажа из дефолтного класса.
        else:
            char_class = Character(char_name)
        # Вывели в терминал описание персонажа (метод __str__).
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class


def start_training(character: Character) -> str:
    """Функция тренировки."""

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = input('Введи команду: ')
    while cmd != 'skip':
        # Судя по теории урока, словарь 'commands' нужно вынести за цикл.
        # Однако, если это сделать, значения словаря в цикле не меняется.
        # То есть, при первом проходе, определяются значения и каждый раз
        # выводятся именно они. Одни и те же. А так работает, так как при
        # каждой итерации, значения переопределяются.
        commands = {
            'attack': character.attack(),
            'defence': character.defence(),
            'special': character.special(),
        }
        if cmd in commands:
            print(commands[cmd])
        else:
            print('Глаза разуй и напечатай одну из перечисленных комманд!')
        cmd = input('Введи команду: ')
    return 'Тренировка окончена.'


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    start_training(choice_char_class(char_name))
