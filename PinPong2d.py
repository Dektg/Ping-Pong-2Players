import turtle
from random import choice, randint

window = turtle.Screen()
window.title("2d Ping-Pong")
# Размеры окна на весь монитор
window.setup(width=1.0, height=1.0)
# Задний фон
window.bgcolor("black")

# Отрисовка поля
border_rectangle = turtle.Turtle()
border_rectangle.color("white")
border_rectangle.speed(5)
# Спрятал отрисовку курсора
border_rectangle.hideturtle()
border_rectangle.up()
border_rectangle.goto(-500, 300)
border_rectangle.down()
border_rectangle.begin_fill()
border_rectangle.goto(500, 300)
border_rectangle.goto(500, -300)
border_rectangle.goto(-500, -300)
border_rectangle.goto(-500, 300)
border_rectangle.end_fill()

border_rectangle.goto(0, 300)
border_rectangle.color("black")
# Повернуться вниз
border_rectangle.setheading(270)

# Цикл для пунктира
for i in range(0, 25, 1):
    if i % 2 == 0:
        border_rectangle.forward(24)
    else:
        border_rectangle.up()
        border_rectangle.forward(24)
        border_rectangle.down()

rocket_a = turtle.Turtle()
rocket_a.color("black")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_a.penup()
rocket_a.goto(-450, 0)

rocket_b = turtle.Turtle()
rocket_b.color("black")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
# Не оставляет следов
rocket_b.penup()
rocket_b.goto(450, 0)
space_rocket = 80

def move_up():
    y = rocket_a.ycor() + space_rocket
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down():
    y = rocket_a.ycor() - space_rocket
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_b():
    y = rocket_b.ycor() + space_rocket
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_b():
    y = rocket_b.ycor() - space_rocket
    if y < -250:
        y = -250
    rocket_b.sety(y)


ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)

ball_dx = 0.1
ball_dx = float(ball_dx)

ball_dy = 1.0
ball_dy = float(ball_dy)


ball.penup()

window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_up_b, "Up")
window.onkeypress(move_down_b, "Down")

while True:
    def ball_setx():
        ball.xcor() + ball_dx
    ball_setx()
    def ball_sety():
        ball.ycor() + ball_dy
    ball_sety()

    if ball.ycor() >= 290:
        ball_dy = -ball_dy

    if ball.ycor() <= -290:
        ball_dy = -ball_dy

    if ball.xcor() >= 490:
        ball.goto(0, randint(-150, 150))
        ball_dx = choice([-5, 5])
        ball_dy = choice([-5, 5])

    if ball.xcor() <= -490:
        ball.goto(0, randint(-150, 150))
        ball_dx = choice([-5, 5])
        ball_dy = choice([-5, 5])
window.mainloop()
