import turtle

"""Квадрати"""

# def square(lenth):
#     for i in range(4):
#         abc.color(colors[i % 4])
#         abc.forward(lenth)
#         abc.left(90)
#
# colors = ["red", "blue", "brown", "green"]
# abc = turtle.Turtle()
# abc.speed(5)
#
# dovgyna = 40
# for i in range(36):
#     abc.circle(dovgyna)
#     abc.right(10)
#     dovgyna += 5

"""Трикутники та квадрати"""

# pen = turtle.Turtle()
#
# pen.speed(1)

# Квадрат
# n = 5
# sum_angle = (n - 2) * 180
# if sum_angle % n == 0:
#     angle = sum_angle // n
#     for i in range(n):
#         pen.forward(100)
#         pen.left(180 - angle)

# Трикутник
# angle = 60
# n = 3
# for i in range(n):
#     pen.forward(100)
#     pen.left(180 - angle)

"""3-10 кутники"""

bob = turtle.Turtle()
bob.speed(1)

def abc(n, dovgyna):
    sum_angle = (n - 2) * 180
    if sum_angle % n == 0:
        angle = sum_angle // n
        for i in range(n):
            bob.forward(100)
            bob.left(180 - angle)

for i in range(3, 11):
    abc(i, 50)