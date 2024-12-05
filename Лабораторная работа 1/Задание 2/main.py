# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания

# TODO: инстанцировать все описанные классы, создав три объекта.C()
# TODO: вызвать метод с некорректными аргументами(b)
# TODO: вызвать метод с некорректными аргументами(a)
from task_1 import Hogwarts, Dragon, MagicWand

if __name__ == "__main__":

    hogwarts = Hogwarts('Gryffindor', 50)
    dragon = Dragon('Fire', 'China', 5, True)
    wand = MagicWand(10.5, 'phoenix feather')

    try:
        hogwarts.add_students("10")
    except TypeError as e:
        print('Ошибка: неправильные данные')

    try:
        dragon.grow("three")
    except TypeError as e:
        print('Ошибка: неправильные данные')

    try:
        wand_with_invalid_length = MagicWand("10", 10)
    except TypeError as e:
        print('Ошибка: неправильные данные')


