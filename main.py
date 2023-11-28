from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(Number):
    """Вычисляет квадратный корень."""
    root1 = sqrt(Nubmer)
    return root1


def calc(your_number):
    """Проверка корня."""
    root = 0
    if your_number <= 0:
        return root
    print(f"Мы вычислили квадратный корень из введённого вами числа." 
          f"Это будет: {calculate_square_root(your_number)}")

    
print(message)
calc(25.5)