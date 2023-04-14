#Cleo Tang 261070795
import turtle
import math

def an_icecream(radius_of_iceball,width_of_cone,height_of_cone):
    '''(float,float,float) -> NoneType
    Uses turtle module to draw an icecream with
    customized sizes of iceball and cone.
    '''
    radius_of_iceball = float(radius_of_iceball)
    width_of_cone = float(width_of_cone)
    height_of_cone = float(height_of_cone)
    
    if 0 < width_of_cone/(2 * radius_of_iceball) <= 1 :

        side_length_of_cone = math.sqrt((width_of_cone/2) ** 2 + height_of_cone**2)
        angle_of_cone = 2 * math.atan(width_of_cone/2/height_of_cone)
        cos_angle_1 = math.sqrt(1-((width_of_cone/2)/radius_of_iceball) ** 2)
        angle_1 = math.acos(cos_angle_1)
        angle_of_iceball = math.degrees(2 * math.pi - angle_1 * 2) 
        angle_2 = math.atan(height_of_cone/(width_of_cone/2))
    
        leo.penup()
        leo.goto(-250,200)
        leo.pendown()
    
        leo.fillcolor("brown")
        leo.begin_fill()
        leo.backward(width_of_cone)
        leo.right(math.degrees(angle_2))
        leo.forward(side_length_of_cone)
        leo.left(math.degrees(math.pi-angle_of_cone))
        leo.forward(side_length_of_cone)
        leo.end_fill()
    
        leo.fillcolor("blue")
        leo.begin_fill()
        leo.right(math.degrees(angle_2 - angle_1))
        leo.circle(radius_of_iceball,angle_of_iceball)
        leo.end_fill()
        leo.left(math.degrees(angle_1))
    else:
        print("leo can't make an icecream for you!")
    
def a_dragon():
    '''() -> NoneType
    Uses turtle module to draw a creature
    that is dragon
    '''

    leo.penup()
    leo.goto(0,0)
    leo.pendown()
    
#body of dragon 
    leo.forward(100)
    leo.left(90)
    leo.forward(80)
    leo.left(90)
    leo.forward(50)
    leo.left(90)
    leo.forward(30)
    leo.right(90)
    leo.forward(150)
    leo.left(90)
    leo.forward(50)
    leo.left(90)
    leo.forward(100)
    leo.left(180)

#tail of the dragon
    n = -1
    for i in range (2):
        n += 1
        leo.penup()
        leo.goto(-100,20 + 10 * n)
        leo.pendown()
        leo.forward(50 - 10 * n)
    
    leo.right(60)
    
    for i in range (2):
        leo.penup()
        leo.goto(-150 + 10 * (n-1),20 + 10 * (n-1))
        leo.pendown()
        n += 1
        leo.forward(20)
    leo.right(30)
    leo.circle(10,270)
    
    leo.left(90)
    m = 0
    for i in range(2):
        leo.penup()
        leo.goto(80 - m * 20,80)
        leo.pendown()
        leo.color("wheat")
        leo.begin_fill()
        leo.forward(10)
        leo.circle(5,180)
        leo.forward(10)
        leo.right(180)
        leo.end_fill()
        m += 1
    
    for i in range(2):
        leo.penup()
        leo.goto(65 + (m-2) * 20,65)
        leo.pendown()
        leo.color("black")
        leo.begin_fill()
        leo.circle(5,360)
        leo.end_fill()
        m += 1

    leo.penup()
    leo.goto(60,50)
    leo.pendown()
    leo.right(90)
    leo.forward(20)
    
    h = 0
    for i in range(3):
        leo.penup()
        leo.goto(90,55 - h * 5)
        leo.pendown()
        leo.forward(40)
        h += 1
    
    h = 0    
    for i in range(3):
        leo.penup()
        leo.goto(55,58 - h * 5)
        leo.pendown()
        leo.backward(40)
        h += 1
        
        
    leo.right(90)
    a = 0
    for i in range(4):
        leo.penup()
        leo.goto(80 - a * 40,10)
        leo.pendown()
        
        leo.forward(50)
        leo.backward(15)
        leo.left(30)
        leo.forward(15)
    
        leo.penup()
        leo.goto(80 - a * 40,-25)
        leo.pendown()
        leo.right(60)
        leo.forward(15)
        
        leo.left(30)
        a += 1
    
    
def a_pearly_nautilus():
    '''() -> NoneType
    Uese turtle module to draw a pearly nautilus.
    '''
    leo.penup()
    leo.goto(100,-200)
    leo.pendown()
    
    m = 0
    for i in range(5):
        leo.circle(50 / (2 ** m),180)
        m += 1
    
  
def my_artwork(radius_of_iceball,width_of_cone,height_of_cone):
    '''(float,float,float) -> NoneType
    The function takes three inputs and make a drawing
    that consists an incream, a dragon and a pearly
    nautilus.
    '''
    global leo
    leo = turtle.Turtle()
    
    an_icecream(radius_of_iceball,width_of_cone,height_of_cone)
    a_dragon()
    a_pearly_nautilus()
    
    leo.penup()
    leo.goto(-250,-250)
    leo.pendown()
    
    leo.right(-60)
    leo.circle(30,270)




        