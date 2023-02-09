import turtle
import random
import time

score = 0
game = True

screen = turtle.Screen()
screen.title("Snake | Score " + str(score))
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

# Snake body
body = []

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(random.randrange(-280,280,20), random.randrange(-280,280,20))

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"


screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

def check_fordeath():
    if(snake.xcor() >= 300 or snake.ycor() <= -300 or snake.xcor() <= -300 or snake.ycor() >= 300):
        return False
    else:
        return True

while True:
    if game:
        screen.update()   
        screen.title("Snake | Score " + str(score))
        game = check_fordeath()

        # Check for collision with the food
        if snake.distance(food) == 0:
            # Move food to a random location
            x = random.randrange(-280,280,20)
            y = random.randrange(-280,280,20)
            food.goto(x,y)
            score = score + 1

            # Add a new segment to the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("lightgreen")
            new_segment.penup()
            body.append(new_segment)    

        # Check for collision with the body
        for segment in body:
            if segment.distance(snake) == 0:
                snake.color("red")
                food.color("red")
                for segment in body:
                    segment.color("red")
                game = False

        # Move the body segments to the right place
        for i in range(len(body) - 1, 0, -1):
            x, y = body[i-1].pos()
            body[i].goto(x, y)

        # Move the 0th segment to where the snake is
        if len(body) > 0:
            x, y = snake.pos()
            body[0].goto(x, y)  
        
        move()

        time.sleep(0.1)
    else:
        food.color("black")
        snake.color("black")
        for i in range(0,len(body),1):
            body[i].color("black")
        screen.update()
        text = turtle.Turtle()
        text.color("white")
        text.write("ENDE! Dein Score war : " + str(score),font=("Arial",10,"normal"))  
        screen.update()

    