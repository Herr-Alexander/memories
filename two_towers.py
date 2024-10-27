# Чтение ввода
n = int(input())

# Разделяем трёхзначное число на отдельные цифры
d1 = n // 100            # первая цифра
d2 = (n // 10) % 10       # вторая цифра
d3 = n % 10               # третья цифра

# Составляем все возможные двухзначные числа
two_digit_numbers = [
    d1 * 10 + d2,
    d1 * 10 + d3,
    d2 * 10 + d1,
    d2 * 10 + d3,
    d3 * 10 + d1,
    d3 * 10 + d2
]

# Исключаем результаты, которые не являются двухзначными числами
two_digit_numbers = [num for num in two_digit_numbers if num >= 10]

# Находим минимальное и максимальное двухзначное число
min_number = min(two_digit_numbers)
max_number = max(two_digit_numbers)

# Выводим результат
print(min_number, max_number)
