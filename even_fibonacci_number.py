"""
Написать функцию возвращающую четные элементы последовательности Фибоначчи.
Например, f(4) вернет 0,2,8,34
"""

def even_fibonacci_number(n:int):
    """
    Функция возвращает четные элементы последовательности Фибоначчи.
    """
    even_list = []
    if type(n) != int:
        return 'The variable is not a number'
    elif n == 0:
        return 'None'
    f0, f1 = 0, 1
    even_list.append(f0)
    for i in range((n-1)*3-1):
        f0, f1 = f1, f0+f1
        if f1%2 == False:
            even_list.append(f1)
    even_str = ','.join(str(x) for x in even_list)
    return even_str


def main():
    print('main:')

    #number_of_even_numbers = int(input())
    number_of_even_numbers = 4 #временный ввод постоянный
    print(even_fibonacci_number(number_of_even_numbers))
    print('__________________', '\n')



def test():
    """
    Функция тестирует - функция четные элементы последовательности Фибоначчи.
    """

    print('test:')
    print("Test sort even_fibonacci_number function:", even_fibonacci_number.__doc__)

    print('testcase #1: ', end='')
    print('Ok' if even_fibonacci_number('a') == 'The variable is not a number' else 'Fail')
    print()

    print('testcase #2: ', end='')
    print('Ok' if even_fibonacci_number(0) == 'None' else 'Fail')
    print()

    print('testcase #3: ', end='')
    print('Ok' if even_fibonacci_number(3) == '0,2,8' else 'Fail')
    print()

    print('testcase #4: ', end='')
    print('Ok' if even_fibonacci_number(4) == '0,2,8,34' else 'Fail')

    print('__________________')



if __name__ == "__main__":
    main()
    test()