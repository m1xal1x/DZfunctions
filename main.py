import math
def proverka1():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число:  "))
        return a, b
    except ValueError:
        print("Введено неверное значение")
        return 0, 0
def proverka2():
    try:
        c = int(input("Введите число: "))
        return c
    except ValueError:
        print("Введено неверное значение")
        return 0
def summa(a, b):
    return a+b
def vych(sum1,sum2):
    return a - b
def umnozh(a,b):
    return a*b
def delen(a,b):
    if b != 0:
        return a/b
    else:
        print("На ноль делить нельзя")
def stepen(a,b):
    return a**b
def koren(c):
    return math.sqrt(c)
def factorial(c):
    return math.factorial(c)
def sinus(c):
    return math.sin(c)
def cosinus(c):
    return math.cos(c)
def tg(c):
    return math.tan(c)
menu = 0
while menu != 11:
    print("1.Сложение")
    print("2.Вычитание")
    print("3.Умножение")
    print("4.Деление")
    print("5.Возведение в степень")
    print("6.Квадратный корень")
    print("7.Факториал")
    print("8.Синус")
    print("9.Косинус")
    print("10.Тангенс")
    print("11.Выход из программы")
    try:
        menu = int(input())
    except ValueError:
        print("Введите число от 1 до 11")
    match menu:
        case 1:
            a, b = proverka1()
            print('Ответ: ', summa(a, b))
        case 2:
            a, b = proverka1()
            print('Ответ: ', vych(a, b))
        case 3:
             a, b = proverka1()
             print('Ответ: ', umnozh(a, b))
        case 4:
             a, b = proverka1()
             print('Ответ: ', delen(a, b))
        case 5:
             a, b = proverka1()
             print('Ответ: ', stepen(a, b))
        case 6:
             c = proverka2()
             print('Ответ: ', koren(c))
        case 7:
            c = proverka2()
            print('Ответ: ', factorial(c))
        case 8:
            c = proverka2()
            print('Ответ: ', sinus(c))
        case 9:
            c = proverka2()
            print('Ответ: ', cosinus(c))
        case 10:
            c = proverka2()
            print('Ответ: ', tg(c))




def rectangle_area(width, height):
    if width <= 0 or height <= 0:
       print("Ширина или длина меньше 0 или равна ему")
    else:
        P = width * height
        return P
try:
    print(rectangle_area(width=float(input("Введите ширину: ")), height=int(input("Введите высоту: "))))
except ValueError:
    print("Введено неверное значение")





def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
try:
    print(is_even(number=float(input("Введите число: "))))
except ValueError:
    print("Введено неверное значение")





def sum_digits(number):
    s = 0
    if number < 0:
        print("Введено отрицательное число ")
    else:
        while number > 0:
            s += number % 10
            number //= 10
        return s
try:
    print(sum_digits(number=int(input("Введите число "))))
except ValueError:
    print("Введено неправильное значение")

