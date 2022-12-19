import keyboard

h = 8
w = 20
prise = [6, 18]
position = [h - 2, 1]
barriers = [(1, 1), (2, 1), (2, 2), (1, 4), (1, 5), (1, 6), (1, 9),  (1, 11), (1, 15), (1, 16), (2, 5), (2, 8), (2, 9), (2, 10), (2, 13), (2, 18), (3, 7),  (3, 9), (3, 12), (3, 14), (3, 16), (3, 18), (4, 1),  (4, 2), (4, 4),  (4, 6),  (4, 7),  (4, 9), (4, 11), (4, 12), (4, 14), (4, 16), (4, 17), (4, 18), (5, 4), (5, 6), (5, 7), (5, 14), (5, 18), (6, 2), (6, 3), (6, 4), (6, 9), (6, 10), (6, 11), (6, 15), (6, 16)]
setPosition = []
gameOn = True

def render():
    for i in range(h):
        str = ''
        for e in range(w):
            if e == 0 or e == w - 1 or i == 0 or i == h - 1:
                str += '/'
            elif i == position[0] and e == position[1]:
                str += 'T'
            elif i == prise[0] and e == prise[1]:
                str += '$'
            elif (i, e) in barriers:
                str += '0'
            else:
                str += ' '
        print(str)

print('Игра "Лабиринт"')
print('Разработчик: Денега Владислав')
print('Персонаж игрока: T, цель лабиринта: $')
print('Чтобы двигаться, используйте стрелки клавиатуры')
print('Чтобы подтвердить ход, нажмите ctrl')
while gameOn:
    if not setPosition == position:
        setPosition = [position[0], position[1]] #избавились от ссылочной зависимости
        render()
    if position == prise:
        print('Вы прошли игру!')
        print('Нажмите ctrl для завершения')
        gameOn = False
    events = keyboard.record('ctrl')
    if events[1].name == 'up':
        if position[0] - 1 > 0:
            if not (position[0] - 1, position[1]) in barriers:
                position[0] -= 1
    if events[1].name == 'down':
        if position[0] + 1 < h - 1:
            if not (position[0] + 1, position[1]) in barriers:
                position[0] += 1
    if events[1].name == 'right':
        if position[1] + 1 < w - 1:
            if not (position[0], position[1] + 1) in barriers:
                position[1] += 1
    if events[1].name == 'left':
        if position[1] - 1 > 0:
            if not (position[0], position[1] - 1) in barriers:
                position[1] -= 1




