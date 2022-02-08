"""
Игра 'обратные крестики-нолики'.
"""
from tkinter import Tk, Button
from random import randint

root = Tk()
root.title('Обратные крестики-нолики')
game_run = True
field = []
cross_count = 0
SIZE = 10


def new_game():
    """
    Функция нажатия кнопки "new game"
    """
    for x in range(SIZE):
        for y in range(SIZE):
            field[x][y]['text'] = ' '
            field[x][y]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(x, y):
    """
    Функия нажатия кнопки на поле
    """
    if game_run and field[x][y]['text'] == ' ':
        field[x][y]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_defeat()
        if game_run and cross_count < SIZE ** 2 % 2 + SIZE ** 2 // 2:
            computer_move()
            check_defeat()


def check_defeat():
    """
    Функция проверяет появился ли проигравший.
    """
    for i in range(SIZE):
        for j in range(SIZE):
            try:
                check_line(field[i][j],
                           field[i][j + 1],
                           field[i][j + 2],
                           field[i][j + 3],
                           field[i][j + 4])

                check_line(field[j][i],
                           field[j + 1][i],
                           field[j + 2][i],
                           field[j + 3][i],
                           field[j + 4][i])

                check_line(field[i][j],
                           field[i - 1][j + 1],
                           field[i - 2][j + 2],
                           field[i - 3][j + 3],
                           field[i - 4][j + 4])

                check_line(field[i][j],
                           field[i + 1][j + 1],
                           field[i + 2][j + 2],
                           field[i + 3][j + 3],
                           field[i + 4][j + 4])
            except IndexError:
                continue


def check_line(a, b, c, d, e):
    """
    Проверяет есть ли линия из 5-ти одинаковых элементов
    """
    if a['text'] == b['text'] == c['text'] == d['text'] == e['text'] != " ":
        defeat(a, b, c, d, e)


def computer_move():
    """
    Функия игры компьютера
    """
    while True:
        x = randint(0, SIZE - 1)
        y = randint(0, SIZE - 1)
        if field[x][y]['text'] == ' ':
            field[x][y]['text'] = 'O'
            break


def defeat(a, b, c, d, e):
    """
    Функция поржения
    """
    a['background'] = b['background'] = c['background'] = d['background'] = e['background'] = 'red'
    global game_run
    game_run = False


def start():
    """
    Функция начала игры
    """
    for row in range(SIZE):
        line = []
        for col in range(SIZE):
            button = Button(root, text=' ', width=2, height=1,
                            font=('Verdana', 20, 'bold'),
                            background='lavender',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_button = Button(root, text='new game', command=new_game)
    new_button.grid(row=SIZE, column=0, columnspan=SIZE, sticky='nsew')
    root.mainloop()


start()
