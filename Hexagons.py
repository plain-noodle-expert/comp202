from math import sqrt
import turtle

leo = turtle.Turtle()
leo.penup()
leo.backward(300)
leo.left(90)
leo.forward(250)
leo.pendown()
leo.speed(10)
leo.pensize(3)

n = 1
t = 2
m = 0
h = 0

#here leo will starts from coordinate(-300,250),and point upwards
def single_hexagon1():

    leo.color("green")
    leo.forward(10)
    leo.right(60)
    
    leo.color("blue")
    leo.forward(10)
    leo.right(60)
    
    leo.color("pink")
    leo.forward(10)
    leo.right(60)
    
    leo.color("red")
    leo.forward(10)
    leo.right(60)
    
    leo.color("lime")
    leo.forward(10)
    leo.right(60)
    
    leo.color("purple")
    leo.forward(10)
    leo.backward(10)
    leo.right(60)
    

#now leo is at the bottom of a hexagon and face upward in purple.

#the coordinate of leo is now (-300+5√3,245)
def single_hexagon2():

    leo.color("red")
    leo.forward(10)
    leo.right(60)
    
    leo.color("blue")
    leo.forward(10)
    leo.right(60)
    
    leo.color("pink")
    leo.forward(10)
    leo.right(60)
    
    leo.color("green")
    leo.forward(10)
    leo.right(60)
    
    leo.color("lime")
    leo.forward(10)
    leo.right(60)
    
    leo.color("purple")
    leo.forward(10)
    leo.backward(10)
    leo.right(60)
    
def two_hexagons():
    
    single_hexagon1()
#ready to draw a stick    
    leo.color("gray")
    leo.backward(10)
#leo now at (-300+5√3,235),the bottom of the gray "stick line"
    leo.penup()
    leo.goto(-300+10*sqrt(3)*n,250-m*30)
    leo.pendown()
#ready to draw a second hexagon in same direction    
    single_hexagon2()
#ready to draw a yellow stick line
    leo.color("yellow")
    leo.backward(10)
#leo is now at the bottom of the yellow stick line,facing upward
    leo.penup()
    leo.goto(-300+10*sqrt(3)*t,250-30*m)
    leo.pendown()
#now at (-300+20*sqrt(2),250)
    
def a_row_of_hexagons():

    for i in range(15):
        two_hexagons()
        global n
        n += 2
        global t
        t += 2
        
#finish


def two_hexagons_without_sticks():

    single_hexagon1()
    
    leo.penup()
    leo.goto(-300+10*sqrt(3)*n,250-m*30)
    leo.pendown()
    
    single_hexagon2()
#leo has to go back to (-300+10*sqrt(3)*t) to draw another hexagon in a row   
    leo.penup()
    leo.goto(-300+10*sqrt(3)*t,250-30*m)
    leo.pendown()
    
def a_row_of_hexagons_without_sticks():
    global n
    n = 1
    for i in range(15):
        two_hexagons_without_sticks()
        n += 2
        global t
        t += 2

def many_rows_of_hexagons():
    for i in range(16):
        global n
        n = 1
        global t
        t = 2
        a_row_of_hexagons()
        global m
        m += 1
#we reset n and m so other functions we call here can use n, t and m
        leo.penup()
        leo.goto(-300,250-30*m)
        leo.pendown()
#move to the last row

    a_row_of_hexagons_without_sticks()
    
many_rows_of_hexagons()