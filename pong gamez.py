import turtle as t


Player_A_Score= 0
Player_B_Score = 0



r = t.Screen()
r.title('Pong Game')
r.bgcolor("black")
r.setup(800,600)

Leftpaddle_A = t.Turtle()
Leftpaddle_A.speed(0)
Leftpaddle_A.color('white')
Leftpaddle_A.shape("square")
Leftpaddle_A.shapesize(5,1)
Leftpaddle_A.penup()
Leftpaddle_A.goto(-350,0)


Rightpaddle_B = t.Turtle()
Rightpaddle_B.speed(0)
Rightpaddle_B.color('white')
Rightpaddle_B.shape("square")
Rightpaddle_B.shapesize(5,1)
Rightpaddle_B.penup()
Rightpaddle_B.goto(350,0)


Ball = t.Turtle()
Ball.speed(0)
Ball.color('red')
Ball.shape('circle')
Ball.penup()
Ball.goto(0,0)
BallxDirection = 3.5
BallyDirection = 3.5

pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.ht()
pen.goto(0,260)
pen.write('Player A: 0                 Player B: 0', align = 'center', font = ('courier',24,'normal'))

def Leftpaddle_A_UP():
    y = Leftpaddle_A.ycor()
    y = y + 15
    Leftpaddle_A.sety(y)

def Leftpaddle_A_DOWN():
    y = Leftpaddle_A.ycor()
    y = y - 15
    Leftpaddle_A.sety(y)

def Rightpaddle_B_UP():
    y = Rightpaddle_B.ycor()
    y = y + 15
    Rightpaddle_B.sety(y)

def Rightpaddle_B_DOWN():
    y = Rightpaddle_B.ycor()
    y = y - 15
    Rightpaddle_B.sety(y)

r.listen()
r.onkeypress(Leftpaddle_A_UP,'w')
r.onkeypress(Leftpaddle_A_DOWN,'s')
r.onkeypress(Rightpaddle_B_UP,'Up')
r.onkeypress(Rightpaddle_B_DOWN,'Down')


while True:
    r.update()
   

    Ball.setx(Ball.xcor() + BallxDirection)
    Ball.sety(Ball.ycor() + BallyDirection)

    if Ball.ycor() > 290:
        Ball.sety(290)
        BallyDirection = BallyDirection * -1
    if Ball.ycor() < -290:
        Ball.sety(-290)
        BallyDirection = BallyDirection * -1
    if Ball.xcor() > 390:
        Ball.goto(0,0)
        BallxDirection = BallxDirection * -1
        Player_A_Score += 1
        pen.clear()
        pen.write("Score A:{}              Score B:{}".format(Player_A_Score, Player_B_Score), align = 'center' , font = ('arial', 24, 'normal'))

    if (Ball.xcor()) < -390:
        Ball.goto(0,0)
        BallxDirection = BallxDirection * -1
        Player_B_Score += 1
        pen.clear()
        pen.write("Score A:{}             Score B:{}".format(Player_A_Score, Player_B_Score), align = 'center' , font = ('arial', 24, 'normal'))

    


    if (Ball.xcor()> 340) and (Ball.xcor()< 350) and (Ball.ycor()< Rightpaddle_B.ycor() + 40 and Ball.ycor()> Rightpaddle_B.ycor() - 40):
        Ball.setx(340)
        BallxDirection = BallxDirection * -1

    if (Ball.xcor()< -340) and (Ball.xcor()> -350) and (Ball.ycor()< Leftpaddle_A.ycor() + 40 and Ball.ycor()> Leftpaddle_A.ycor() - 40):
        Ball.setx(-340)
        BallxDirection = BallxDirection * -1