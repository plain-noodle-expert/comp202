import turtle
from math import sqrt

leo = turtle.Turtle()
leo.penup()
leo.goto(-300,260)
leo.pendown()
leo.left(30)

leo.speed(10)

def top_line_of_hexagons():
    '''() -> NoneType
    draw top line of hexagons
    '''
    for i in range(30):
        leo.color("blue")
        leo.forward(10)
        leo.right(60)
    
        leo.color("pink")
        leo.forward(10)
        leo.left(60)

def bottom_line_of_hexagons():
    '''() -> NoneType
    draw bottom line of hexagons
    '''
    for i in range(30):
        leo.color("purple")
        leo.forward(10)
        leo.left(60)
        
        leo.color("lime")
        leo.forward(10)
        leo.right(60)
    
def a_row_of_sticks(d1,d2,h):
    '''(int,int,int) -> NoneType
    draw vertical sides of hexagons
    '''
    for i in range(15):
        
        leo.penup()
        leo.goto(-300 + 10 * sqrt(3) * d1, 260 - h * 10)
        leo.pendown()
        
        leo.color("gray")
        leo.forward(10)
    
        leo.penup()
        leo.goto(-300 + 10 * sqrt(3) * d2, 260 - h * 10)
        leo.pendown()
    
        leo.color("red")
        leo.forward(10) 
        
        d1 += 2
        d2 += 2
                
    
def grid_of_hexagons():
    '''() -> NoneType
    draw a grid hexagons
    '''
    n = 1
    m = 3
    for i in range (15):
        
        top_line_of_hexagons()
        
        leo.penup()
        leo.goto(-300,260 - 10 * n)
        leo.pendown()
        leo.right(60)
    
        bottom_line_of_hexagons()
        
        leo.left(60)
        
        leo.penup()
        leo.goto(-300,260 - 10 * m)
        leo.pendown()
        
        n += 3
        m += 3
    
    leo.right(120)
    h = 0
    for i in range(15):
        d1 = 0
        d2 = 1
        a_row_of_sticks(d1,d2,h)
        
        leo.penup()
        leo.goto(-300+300*sqrt(3),260 - 10 * h)
        leo.pendown()
        leo.color("gray")
        leo.forward(10)
        
        h += 3
    
    h = 1.5
    for i in range(15):
        d1 = 0.5
        d2 = 1.5
        
        a_row_of_sticks(d1,d2,h)
        
        h += 3
    
    leo.left(120)
    leo.penup()
    leo.goto(-300,260 - (h-1.5) * 10)
    leo.pendown()
    top_line_of_hexagons()
    

grid_of_hexagons()    
    
    
    
    
