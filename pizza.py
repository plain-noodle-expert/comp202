#Cleo Tang 261070795
import math

PIZZA_CAKE_COST_PER_CENTIMETER_CUBED = 4.0
PIZZA_POUTINE_COST_PER_CENTIMETER_CUBED = 3.0
SPECIAL_INGREDIENT_COST = 19.99
FAIR = True

def get_pizza_area(diameter):
    '''(float)->float
    Take a float number as diameter,print the area of pizza
    >>>get_pizza_area(6)
    28.27433388
    >>>get_pizza_area(15)
    176.7145868
    >>>get_pizza_area(9.8)
    75.42963961
    '''
    return math.pi * (diameter/2)**2
    
def get_fair_quantity(diameter1, diameter2):
    '''(float,float)-> float
    Take two float numbers as diameters, return the
    amount of smaller pizza required to have at least
    same amount of larger pizza when FAIR is True,
    and 1.5 amount of true when FAIR is False.
    >>>get_fair_quantity(4.0,16.0)
    16.0
    >>>get_fair_quantity(13.4,10.0)
    2
    >>>get_fair_quantity(23.0,11)
    5
    '''
    diameter1 = float(diameter1)
    diameter2 = float(diameter2)
    
    ratio = (diameter1/diameter2)**2
    if ratio < 1:
        ratio = (diameter2/diameter1)**2
    if ratio // 1 != ratio:
        ratio = int(ratio + 1)
    amount_of_smaller_pizza = ratio
   
    if FAIR :
        return amount_of_smaller_pizza
    
    return amount_of_smaller_pizza * 1.5

def pizza_formula(d_large, d_small, c_large, c_small, n_small):
    '''(num,num,num,num,num)->float
    Take three float numbers and one -1,representing the missing
    input value,calculates and returns the missing input value
    as a float, rounded to two decimal places.
    >>>pizza_formula(12.0, 6.0, 10.0, -1, 2)
    5.0
    >>>pizza_formula(-1,4.5,12,11.0,2)
    6.65
    >>>pizza_formula(16.0,-1,9.9,6,3)
    7.19
    '''
    if d_large == -1 :
        d_large = sqrt((c_large * n_small * math.pow(d_small,2))/ c_small)
        return round(d_large,2)
    
    elif d_small == -1 :
        d_small = sqrt((c_small * math.pow(d_large,2)) / (c_large * n_small))
        return round(d_small,2)
    
    elif c_large == -1 :
        c_large = math.pow(d_large,2) * c_small / (math.pow(d_small,2) * n_small)
        return round(c_large,2)
    
    elif c_small == -1 :
        c_small = (math.pow(d_small,2) * n_small * c_large) / math.pow(d_large,2)
        return round(c_small,2)
    
    n_small = (c_small * math.pow(d_large,2) / (math.pow(d_small,2) * c_large))
    return round(n_small,2)
        
    
def get_pizza_cake_cost(base_diameter, height_per_level):
    '''(int,float)->float
    Returns the cost of the pizza cake as a float rounded to two decimal places.
    >>>get_pizza_cake_cost(10,2.0)
    2419.03
    >>>get_pizza_cake_cost(4,1.5)
    141.37
    >>>get_pizza_cake_cost(7,2.5)
    439.82
    '''
    total_pizza_area = 0
    for i in range(base_diameter):
        total_pizza_area += get_pizza_area(base_diameter - 1 * i)
        
    pizza_cake_cost = total_pizza_area * height_per_level * PIZZA_CAKE_COST_PER_CENTIMETER_CUBED

    if FAIR :
        return round(pizza_cake_cost,2)
    
    return round(pizza_cake_cost * 1.5,2)
        
def get_pizza_poutine_cost(diameter, height):
    '''(int,float)->float
    Returns the cost of the pizza poutine as a float rounded to
    two decimal places.
    >>>get_pizza_poutine_cost(10,2.0)
    471.24
    >>>get_pizza_poutine_cost(11,1.7)
    484.67
    >>>get_pizza_poutine_cost(6,1.0)
    84.82
    '''
    volume_of_poutine = get_pizza_area(diameter) * height
    cost_of_poutine = volume_of_poutine * PIZZA_POUTINE_COST_PER_CENTIMETER_CUBED
    if FAIR:
        return round(cost_of_poutine,2)
    return round(cost_of_poutine * 1.5,2)


    
def display_welcome_menu() :
    '''()->NoneType
    Displays to the screen a menu with a welcome message and
    the three options available to the user.
    >>>Welcome To BZY Pizza Hub. Our Pizzas Made With 100% Magic Pizza. Please choose an option:
    '''
    print("Welcome To BZY Pizza Hub. Our Pizzas Made With 100% Magic Pizza. Please choose an option:")
    print("A. Special Orders")
    print("B. Formula Mode")
    print("C. Quantity Mode")
    
    
def special_orders() :
    '''()->NoneType
    Prints out the total cost of the order according to the
    user's choice.
    >>>special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 2
    Enter height: 1.0
    Do you want the guacamole: no
    The cost is $9.42
    >>>special_orders()
    Would you like the cake or poutine? poutine
    Enter diameter: 5
    Enter height: 2.0
    Do you want the guacamole: no
    The cost is $117.81
    >>>special_orders()
    Would you like the cake or poutine? cake
    Enter diameter: 10
    Enter height: 1.5
    Do you want the guacamole: yes
    The cost is $1834.26
    '''
    
    cake_poutine = input("Would you like the cake or poutine: ")
    base_diameter = int(input("Enter diameter: "))
    height_per_level = float(input("Enter height: "))
    guacamole = input("Do you want the guacamole: ")
    
    diameter = base_diameter
    height = height_per_level
    
    cost = 0
    if guacamole == "y" or guacamole == "yes":
        cost += SPECIAL_INGREDIENT_COST
    
    if cake_poutine == "poutine":
        cost += get_pizza_poutine_cost(diameter, height)
        print("The cost is $",cost)
    
    elif cake_poutine == "cake":
        cost += get_pizza_cake_cost(base_diameter, height_per_level)
        print("The cost is $",cost)
    
def quantity_mode():
    '''() -> NoneType
    Takes as the diameters of two pizzas the user inputs,
    prints out the minimum number of smaller pizzas needed
    to get at least same amount of one large pizzas by area.
    >>>quantity_mode()
    Enter diameter1: 14.0
    Enter diameter2: 8.0
    You should buy 4 pizzas.
    >>>quantity_mode()
    Enter diameter1: 12.8
    Enter diameter2: 6.6
    You should buy 4 pizzas.
    >>>quantity_mode()
    Enter diameter1: 7.0
    Enter diameter2: 11.0
    You should buy 3 pizzas.
    '''
    diameter1 = float(input("Enter diameter1: "))
    diameter2 = float(input("Enter diameter2: "))
    
    print("You should buy",get_fair_quantity(diameter1, diameter2),"pizzas")
    
def formula_mode():
    '''() -> NoneType
    Takes as input the user's diameter of a large pizza and small pizza,
    cost of a large and small pizza, and number of small pizzas in order,
    with one of the value being -1, and prints out the actual value that
    was given as -1.
    >>>formula_mode()
    Enter large diameter: 12.0
    Enter small diameter: 6.0
    Enter large price:10
    Enter small price:-1
    Enter small number:2
    The missing value is: 5.0
    >>>formula_mode()
    Enter large diameter: 8.8
    Enter small diameter: 5.3
    Enter large price:-1
    Enter small price:4.9
    Enter small number:2
    The missing value is: 6.75
    >>>formula_mode()
    Enter large diameter: -1
    Enter small diameter: 9.0
    Enter large price:6.89
    Enter small price:5.5
    Enter small number:1.5
    The missing value is: 12.34
    '''
    d_large = float(input("Enter large diameter: "))
    d_small = float(input("Enter small diameter: "))
    c_large = float(input("Enter large price: "))
    c_small = float(input("Enter small price: "))
    n_small = float(input("Enter samll number: "))
    
    missing_value = pizza_formula(d_large, d_small, c_large, c_small, n_small)
    print("The missing value is:",missing_value)
    

def run_pizza_calculator():
    '''() -> NoneType
    Displays a welcome message to the user and
    a list of program options, and then calls
    the appropriate function.If the user inputs
    an invalid option, prints out "Invalid mode.".
    >>>run_pizza_calculator()
    Welcome To BZY Pizza Hub. Our Pizzas Made With 100% Magic Pizza. Please choose an option: A
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: A
    Would you like the cake or poutine? cake
    Enter diameter: 2
    Enter height: 1.5
    Do you want the guacamole? yes
    The cost is 23.56
    >>>run_pizza_calculator()
    Welcome To BZY Pizza Hub. Our Pizzas Made With 100% Magic Pizza. Please choose an option: A
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: B
    Enter large diameter:13.0
    Enter small diameter: -1
    Enter large price: 11.3
    Enter small price: 6.6
    Enter samll number: 3
    The missing value is: 5.74
    >>>run_pizza_calculator()
    Welcome To BZY Pizza Hub. Our Pizzas Made With 100% Magic Pizza. Please choose an option: A
    A. Special Orders
    B. Formula Mode
    C. Quantity Mode
    Your choice: D
    '''
    display_welcome_menu()
    choice = input("Your choice:")
    if choice == "A":
        special_orders()
    elif choice == "B":
        formula_mode()
    elif choice == "C":
        quantity_mode()
    else:
        print("Invalid mode")













    