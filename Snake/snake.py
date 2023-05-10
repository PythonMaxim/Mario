#подключаю модули

from turtle import *
from time import sleep
from random import randint

#границы осей положительные и отрицательные экрана

border_x = 400
border_y = 400

#скорость обновления кадров (используется через sleep)

delay = 0.05

#границы игры

game_border = Turtle()
game_border.speed(0)
game_border.hideturtle()
game_border.penup()
game_border.goto(-350, -350)
game_border.pendown()
game_border.color('light gray')
game_border.begin_fill()
for i in range(2):
    game_border.forward(700)
    game_border.left(90)
    game_border.forward(600)
    game_border.left(90)
game_border.end_fill()

#создаю объект экран

scr = Screen()
scr.title('змейка для папы')
scr.bgcolor('white smoke')
scr.setup(border_x * 2, border_y * 2)
scr.tracer(0)

#подпись-приветствие

pen = Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.color('black')
pen.goto(-350, 360)
pen.write('Привет! Эта змейка специально для тебя!', font=('Arial', 20, 'bold'))
pen.goto(-350, 330)
pen.write('Управлять нужно стрелочками', font=('Arial', 20, 'bold'))
pen.goto(-350, 300)
pen.write('Лучший счет в игре обновляется после каждого запуска', font=('Arial', 20, 'bold'))
pen.goto(-350, 270)
pen.write('Не забудь сфоткать, если наберешь много очков!', font=('Arial', 20, 'bold'))

#счет в игре

score = 0
best_score = 0

points = Turtle()
points.hideturtle()
points.penup()
points.speed()
points.color('black')
points.goto(0, 315)

#создаю счет в игре

score, best_score = 0, 0

#создаю саму змею

snake = Turtle()
snake.shape('square')
snake.color('dark green')
snake.penup()
snake.goto(0, -50)
snake.direction = 'Stop'

#создаю еду

food = Turtle()
food.penup()
food.speed(0)
food.shape('square')
food.color('dark orange')
food.goto(randint(-350 + 20, 350 - 20), randint(-350 + 20, 250 - 20))

#создаю список-туловище

body = []

#функции, отправляющие еду в рандомное место на экране:

def generate_food():
    food.goto(randint(-350 + 20, 350 - 20), randint(-350 + 20, 250 - 20))

#функции, которые задают направление движения

def go_up():
    if snake.direction != 'Down':
        snake.direction = 'Up'

def go_down():
    if snake.direction != 'Up':
        snake.direction = 'Down'

def go_right():
    if snake.direction != 'Left':
        snake.direction = 'Right'

def go_left():
    if snake.direction != 'Right':
        snake.direction = 'Left'

#функция движения змеи в зависимости от того, в каком она направлении

def move():
    if snake.direction == 'Up':
        snake.sety(snake.ycor() + 20)
    elif snake.direction == 'Down':
        snake.sety(snake.ycor() - 20)
    elif snake.direction == 'Left':
        snake.setx(snake.xcor() - 20)
    elif snake.direction == 'Right':
        snake.setx(snake.xcor() + 20)

#функции, меняющие направление змейки, если нажаты определенные клавиши

scr.listen()
scr.onkeypress(go_up, 'Up')
scr.onkeypress(go_down, 'Down')
scr.onkeypress(go_left, 'Left')
scr.onkeypress(go_right, 'Right')

while True:

    scr.update()

    if score >= best_score:
        best_score = score

    if snake.direction != 'Stop':
        pen.clear()
        points.clear()
        points.write("счёт: {},  лучший счёт : {}".format(score, best_score), align="center", font=("Arial", 20, "bold"))

    if snake.xcor() < -340 or snake.xcor() > 340 or snake.ycor() < -340 or snake.ycor() > 240:
        sleep(1)
        snake.goto(0, -50)
        snake.direction = 'Stop'
        for i in body:
            i.goto(1000, 1000)
        body.clear()
        delay = 0.05
        score = 0

        pen.goto(0, 0)
        pen.write('Эхх...', align='center', font=('Arial', 20, 'bold'))

    if snake.distance(food) < 20:
        generate_food()
        score += 10

        #новые детальки тела

        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.color('dark green')
        new_segment.shape('square')
        new_segment.penup()
        delay -= 0.001
        body.append(new_segment)

    #двигаю детальки к телу

    for i in range(len(body)-1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)

    #движение первой детальки на место головы

    if len(body) > 0:
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x, y)

    move()

    # чекаю столкновения

    for i in body:
        if i.distance(snake) < 20:
            sleep(1)
            snake.goto(0, -50)
            snake.direction = 'Stop'
            for i in body:
                i.goto(1000, 1000)
            body.clear()
            delay = 0.05
            score = 0
            pen.goto(0, 0)
            pen.write('Эхх...', align='center', font=('Arial', 20, 'bold'))

    sleep(delay)