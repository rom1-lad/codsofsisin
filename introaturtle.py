import turtle
class TurlrForNoobs:
#Cuadrado 
    def test(self):
        skk = turtle.Turtle()
        for i in range(4):
            skk.forward(50)
            skk.right(90)
        turtle.done()

#Estrella 
    def estrella(self):  
        est=turtle.Turtle()
        est.right(75)
        est.forward(100)
        for i in range(16):
            est.right(144)
            est.forward(100)
        turtle.done()    

#Circulo 
    def circulo(self):
        est=turtle.Turtle()
        est.right(100)
        est.forward(10)
        for i in range(25):
            est.right(14.4)
            est.forward(30)
        turtle.done()

t=TurlrForNoobs()
t.estrella()       
















