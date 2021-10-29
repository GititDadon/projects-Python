import turtle
wn=turtle.Screen()
wn.title('Ping-Pong_Game')
wn.setup(width=800,height=600)
wn.bgcolor("pink")
wn.tracer(0)

#paddle_A:
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color('black')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) #starts at (350,0) in the left side of the screen
#paddle_B:
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color('black')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) #starts at (350,0) in the right side of the screen
#Ball:
ball=turtle.Turtle()
ball.shape('circle')
ball.color('black')
ball.speed(0)
ball.goto(0,0)
ball.penup()
ball.dx=0.2
ball.dy=0.2
#Pen:
pen=turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score:0',font=('Courier',24,'normal'),align='center')
#score
score=0

#movements:
def paddle_a_UP():
    y=paddle_a.ycor() #returns y cordinate
    y+=20
    paddle_a.sety(y) #set y cor to the new y cor
def paddle_a_Down():
    y=paddle_a.ycor() #returns y cordinate
    y-=20
    paddle_a.sety(y) #set y cor to the new y cor
def paddle_b_UP():
    y=paddle_b.ycor() #returns y cordinate
    y+=20
    paddle_b.sety(y) #set y cor to the new y cor
def paddle_b_Down():
    y=paddle_b.ycor() #returns y cordinate
    y-=20
    paddle_b.sety(y) #set y cor to the new y cor
#Keyboard Binding:
wn.listen()
wn.onkeypress(paddle_a_UP,'w') #when keyboard pressed on letter w,move paddle a upwards
wn.onkeypress(paddle_a_Down,'s')#when keyboredis pressed on letter s, move down
wn.onkeypress(paddle_b_UP,'Up')
wn.onkeypress(paddle_b_Down,'Down')



while True:
    wn.update()
    #Ball Movements:
    ball.setx(ball.xcor()+ball.dx) #settin x cor to be current location + dx
    ball.sety(ball.ycor()+ball.dy)

    #Border Check:
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*=-1 #reverses Direction
        score+=1
        pen.clear()
        pen.write('Score:', score, font=('Courier', 24, 'normal'), align='center')
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx*=-1
        score += 1
        pen.clear()
        pen.write('Score:',score, font = ('Courier', 24, 'normal'), align = 'center')
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*=-1
    #Paddle&Ball Collision:
    if (ball.xcor() >340 and ball.xcor()<350) and (ball.ycor()< paddle_b.ycor()+60) and ball.ycor()>paddle_b.ycor():
        ball.setx(340)
        ball.dx*=-1
        score+=1
    if (ball.xcor() <-340 and ball.xcor()>-350) and (ball.ycor()< paddle_a.ycor()+40) and ball.ycor()>paddle_a.ycor():
        ball.setx(-340)
        ball.dx*=-1



