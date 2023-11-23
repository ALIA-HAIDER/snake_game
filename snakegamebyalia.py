#snake game by Alia Haider
import turtle
import time
import random
delay=0.1
score=0
high_score=0
#screen
do=turtle.Screen()
do.title("snake by Alia Haider")
do.bgcolor("skyblue")
do.setup(width=700,height=700)
do.tracer(0)
#snake head
snake=turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("skyblue","black")
snake.up()
snake.goto(0,0)
snake.down()
snake.direction="stop"
#food
food=turtle.Turtle()
food.shape("circle")
food.color("red","red")
food.up()
food.goto(0,250)

segments=[]
#written
word=turtle.Turtle()
word.speed(0)
word.color("black","white")
word.up()
word.goto(-250,200)
word.down()
word.write("Score: 0 High score:0  <A/H>", font=("Courier", 20, "normal"))
 

#word.write("score=0 High score;0",align="Centre",font=("arial",20,"normal"))
#movements
def go_up():
    if snake.direction!="down":
        snake.direction="up"
def go_down():
    if snake.direction!="up":
        snake.direction="down"
def go_left():
    if snake.direction!="right":
        snake.direction="left"
def go_right():
    if snake.direction!="left":
        snake.direction="right"
def move():
    if snake.direction =="up":
        y=snake.ycor()
        snake.sety(y+20)
    if snake.direction =="down":
        y=snake.ycor()
        snake.sety(y-20)
    if snake.direction =="left":
        x=snake.xcor()
        snake.setx(x-20)
    if snake.direction =="right":
        x=snake.xcor()
        snake.setx(x+20)
#keyboard control
do.listen()
do.onkeypress(go_up,"Up")
do.onkeypress(go_down,"Down")
do.onkeypress(go_left,"Left")
do.onkeypress(go_right,"Right")
#mainloop game
while True :
    do.update()
    #for collision with borders
    if snake.xcor()>349 or snake.ycor()>349 or snake.ycor()<-349 or snake.xcor()<-349:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction="stop"
        #reset the score
        score=0
        #rest the delay
        delay=0.1
        #hide the segments
        for segment in segments:
            segment.goto(10000,10000)

        word.clear()
        score=0
        word.write("Score:{}" ,font=("courier",24,"normal"))
        #collisiion with food
    if snake.distance(food)<20:
         x=random.randint(-339,339)
         y=random.randint(-339,339)
         food.goto(x,y)
          #add a segment
         new_seg=turtle.Turtle()
         new_seg.speed(0)
         new_seg.shape("square")
         new_seg.color("grey")
         new_seg.up()
         segments.append(new_seg)
        #increase the score
         score=+10
         if score>high_score:
 
          high_score=score
          word.clear()
          word.write("score:{}",font=("courier",24,"normal"))
        # move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=snake.xcor()
        y=snake.ycor()
        segments[0].goto(x,y)
    move()
    #head collision with body
    for segment in segments:
        if segment.distance(snake)<20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction="stop"
            #hide the segment
            for segment in segments:
                segment.goto(1000,1000)
            #clear the segment lists
            segments.clear()
            #reset the score
            score=0
            #reset the delay
            delay=0.1
            word.clear()
            word.write("score:{}  high score:{}")


    time.sleep(delay)

        






do.mainloop()
turtle.exitonclick()
