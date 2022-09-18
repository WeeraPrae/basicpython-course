import turtle
tao = turtle.Pen()  
tao.shape('turtle')

def Circle():
    for i in range(10):
    	tao.circle(50)
    	tao.left(36)

def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()

def Triangle():
    for i in range(3):
        tao.left(120)
        tao.forward(50)
        

def Line1():
    tao.right(90)
    tao.forward(200)

def Line2():
    tao.forward(100)

Go(0,100)
Circle()
Line1()
Triangle()
Line2()

