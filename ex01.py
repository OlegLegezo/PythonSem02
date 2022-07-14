# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

#функции с мал букв! значения по умолчанию
def func1(a=1, b=-2):
#def func1(a: int, b: int) -> list(тайп хинтинг):
    my_list = [1]
    while len(my_list) < a:

        my_list.append(my_list[-1]*b)
        # .append позволяет добавлять элемент в конце списка, который уже существует
    print(my_list)
    return my_list


func1(5, -3)
