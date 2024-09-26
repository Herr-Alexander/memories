import turtle, time

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

# bob = turtle.Turtle()
# bob.speed(1)
# bob.up()
# bob.setposition(-50, -50)
# bob.down()
#
# def abc(n, dovgyna):
#     sum_angle = (n - 2) * 180
#     if sum_angle % n == 0:
#         angle = sum_angle // n
#         for i in range(n):
#             bob.forward(100)
#             bob.left(180 - angle)
#
# for i in range(3, 11):
#     abc(i, 50)

"""Зiрка"""

# bob = turtle.Turtle()
# bob.speed(5)
#
# def star_fill(n, dovgyna):
#     bob.begin_fill()
#     star(n, dovgyna)
#     bob.end_fill()
#
# def star(n, dovgyna):
#     if n % 2 != 0:
#         for i in range(n):
#             bob.forward(dovgyna)
#             angle = n // 2 * 360 / n
#             bob.left(angle)
#
# for i in range(5, 16, 2):
#     star_fill(i, 150)
#     time.sleep(1)
#     bob.reset()

"""Зоряне небо"""

bob = turtle.Turtle()
bob.color("yellow")
bob.speed(1)

def star_fill(n, dovgyna):
    bob.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            bob.forward(dovgyna)
            angle = n // 2 * 360 / n
            bob.left(angle)
    bob.end_fill()

star_fill(5, 150)

window = turtle.Screen()
window.bgcolor("black")
time.sleep(5)
