from turtle import Screen,Turtle
from create_paddles import Create_paddle
from  ball import  Ball
import time
from scoreboard import  Score


#create a screen
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

#create paddles
r_paddle=Create_paddle((350,0))
l_paddle=Create_paddle((-350,0))
ball=Ball()
scoreboard=Score()



#paddles controllers
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on=True
while game_is_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()

    #ball bounce against the wall
    if ball.ycor() > 280 or ball.ycor()  <-280:
        ball.bounce_y()
    #ball bounce against the paddles
    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor()< -320:
        ball.bounce_x()
        #increase the speed



    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.update_left_score()


    #detect L paddle misses
    if ball.xcor() <-380:
        ball.reset()
        scoreboard.update_right_score()







screen.exitonclick()