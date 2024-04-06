'''
Created on Apr 2, 2024

@author: Administrator
'''
import turtle
#create the window screen 
wscreen = turtle.Screen()
#create an instance of the turtle 
sturtle=turtle.Turtle()
#sturtle.shape("turtle")
sturtle.penup()
sturtle.home()
for x in range(12):
    sturtle.forward(wscreen.canvwidth/4)
    sturtle.stamp()
    sturtle.right(360/30)
    sturtle.backward(wscreen.canvwidth/16)
    sturtle.stamp()
    sturtle.right(360/30)
    sturtle.forward(wscreen.canvwidth/16)
    sturtle.stamp()
print(wscreen.canvheight, wscreen.canvwidth)
print(wscreen.window_height())
print(wscreen.window_width()
      )
wscreen.exitonclick()

