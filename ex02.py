# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

st1 = 'привет, привет, Мир'
st2 = 'привет'


def finder(stOne, stTwo):
    t = 0
    for i in range(len(stOne)-len(stTwo)):
        if (stOne[i:i+len(stTwo)] == stTwo):
            # тут выбираем элементы в квадратных скобках
            t += 1
    return t


print(finder(st1, st2))
