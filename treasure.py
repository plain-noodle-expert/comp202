#Cleo Tang
#261070795

#I know all the function inside treasure_utils, therefore I would like to import all
from treasure_utils import *
import random


def generate_treasure_map_row(width,map_3D):
    '''(int,bool) -> str
    Takes an integer of width and a boolean indicating the chance
    of a 3D map being generated as inputs.Creates and returns a
    single row of the given width of a treasure map.
    >>>random.seed(211)
    >>>generate_treasure_map_row(10,False)
    'v.>v<^<<..'
    >>>generate_treasure_map_row(20,False)
    '<.<<<^.>.v>^^v><<^.>'
    >>>generate_treasure_map_row(16,True)
    '^^v|^><.<>>^v.vv'
    '''
    treasure_map = ''
    
    if width == 0:
        return treasure_map
    
    for k in range(width):
        number = random.randint(1,6)
        
        if 0 < number < 6:    #total chance of getting number 1-5 is 5/6
            i = random.randint(0,3)  #randomly choose a movement symbol, if it is a movement symbol
            treasure_map += MOVEMENT_SYMBOLS[i]
            
        else:   #chance of getting numebr 6 is 1/6
            treasure_map += EMPTY_SYMBOL
    
    
    if not map_3D:
        return treasure_map
    
    
    treasure_map_3D = ''
    p = random.randint(0,1)   
    
    if p == 1:   #1 indicates that one char will be a 3D symbol, 0 indicates no 3D symbol
        
        index = random.randint(0,width-1)   #randomly select a symbol in map to change to a 3D symbol

        symbol_3D_index = random.randint(0,1)  #randomly choose a 3D symbol
        
        #only one symbol would be 3D symbol
        for i in range(len(treasure_map)):
            symbol = treasure_map[i]
            if i == index:
                symbol = MOVEMENT_SYMBOLS_3D[symbol_3D_index]
            treasure_map_3D += symbol
        
        
        return treasure_map_3D
        
    #if p == 0,no symbol changed to 3D symbol
    return treasure_map






def generate_treasure_map(width,height,map_3D):
    '''(int,int,bool) -> str
    Takes inputs integers of width and height of the map and a boolean indicating
    if a 3D map would be generated.Returns a string of map of given width and height.
    >>>random.seed(211)
    >>>generate_treasure_map(3,3,True)
    '>v.v.v∧<<'
    >>>generate_treasure_map(4,3,True)
    '>.<<∧.*.<*>.'
    >>>generate_treasure_map(3,5,True)
    '><<>∧∧vv....|.<'
    '''
    #first character must be a right-pointing symbol
    #first row of the map:
    treasure_map_2D = MOVEMENT_SYMBOLS[0] + generate_treasure_map_row(width-1,map_3D)
    
    for i in range(height-1):   #rest (height-1) rows of the map
        
        treasure_map_2D += generate_treasure_map_row(width,map_3D)
    
    return treasure_map_2D






def generate_3D_treasure_map(width,height,depth):
    '''(int,int,int) -> str
    Takes inputs integers of width,height and depth of
    the map and returns a 3D map of given width, height
    and depth.
    >>>random.seed(211)
    >>>generate_3D_treasure_map(3,2,2)
    '>.>v<∧><.∧<∧'
    >>>generate_3D_treasure_map(3,4,3)
    '><|v|<.>∧|<∧>.<>>∧v.vvv∧><∧<v><<.∧∧v'
    >>>generate_3D_treasure_map(4,3,2)
    '>vvv.>|.v<∧|>>.v<<v>.><<'
    '''
    treasure_map_3D = ''
    
    for i in range(depth):
        map_3D_p = random.randint(0,1)   #creates a possibility of map_3D being True or False
        
        map_3D = False    #default as false
        
        if map_3D_p == 1:   # 1/2 chance to be True
            map_3D = True
        
        treasure_map_3D += generate_treasure_map(width,height,map_3D)
    
    return treasure_map_3D





def follow_trail(treasure_map,row,colm,depth_index,width,height,depth,tiles):
    '''(str,int,int,int,int,int,int,int) -> NoneType,NoneType,str
    Takes inputs a string of a map, starting row, column and depth indices, width,
    height and depth of the map as well as the number of tiles to travel, in integer.
    Returns a travelled map in string and the number of treasure collected and symbol
    visited.
    >>>follow_trail('>>v..v|.<...', 0, 0, 0, 3, 2, 2, 100)
    Treasures collected: 0
    Symbols visited: 7
    'XXX..XX.X...'
    >>>follow_trail('>.v|.*..v<+<', 0, 2, 0, 3, 2, 2, 5)
    Treasures collected: 1
    Symbols visited: 5
    '>.X|.X..vX+X'
    >>>follow_trail('>.+<..',0,0,0,6,1,1,-1)
    Treasures collected: 2
    Symbols visited: 6
    'X.+X..'
    '''
    treasures_collected = 0
    symbols_visited = 0
    
    
    if not -1 < row < height or not -1 < colm < width or not -1 < depth_index < depth:
        
        return treasure_map
    
    
    char = BREADCRUMB_SYMBOL
    
    if tiles == -1:
        tiles = len(treasure_map)
    
    for trail in range(tiles):
        #index of the starting symbol in the map
        index = depth_index * height * width + row * width + colm
        
        if treasure_map[index] == MOVEMENT_SYMBOLS[0]:
            colm_movement = 1
            row_movement = 0
            depth_movement = 0
        
        elif treasure_map[index] == MOVEMENT_SYMBOLS[1]:
            colm_movement = -1
            row_movement = 0
            depth_movement = 0
        
        elif treasure_map[index] == MOVEMENT_SYMBOLS[2]:
            colm_movement = 0
            row_movement = 1
            depth_movement = 0
        
        elif treasure_map[index] == MOVEMENT_SYMBOLS[3]:
            colm_movement = 0
            row_movement = -1
            depth_movement = 0
            
        elif treasure_map[index] == TREASURE_SYMBOL:
            treasures_collected += 1

        elif treasure_map[index] == MOVEMENT_SYMBOLS_3D[0]:
            colm_movement = 0
            row_movement = 0
            depth_movement = 1
        
        elif treasure_map[index] == MOVEMENT_SYMBOLS_3D[1]:
            colm_movement = 0
            row_movement = 0
            depth_movement = -1
        
        elif treasure_map[index] == BREADCRUMB_SYMBOL:
            print("Treasures collected:",treasures_collected)
            print("Symbols visited:",symbols_visited)
            return treasure_map
        
        
        if not treasure_map[index] == EMPTY_SYMBOL and not treasure_map[index] == TREASURE_SYMBOL:            
            treasure_map = change_char_in_3D_map(treasure_map,row,colm,depth_index,char,width,height,depth)

        #if it is an empty symbol, movement will be the same as last loop
        #manipulate row, colm, depth indices
        
        #column
        if colm == 0 and colm_movement == -1:            
            colm = width-1       
        elif colm == width-1 and colm_movement == 1:
            colm = 0        
        else:
            colm = colm + colm_movement
        
        
        
        #row
        #row is above depth manipulation for if row after manipulation
            #is out of bound of depth, it can be adjusted.
        if row == 0 and row_movement == -1:
            depth_index -= 1
            row = height-1
        elif row == height-1 and row_movement == 1:
            depth_index += 1
            row = 0
        else:
            row = row + row_movement
        
        
        
        #depth
        if depth_index < 0 or depth_index == 0 and depth_movement == -1:
            depth_index = depth-1
        elif depth_index > depth-1 or depth_index == depth-1 and depth_movement == 1:
            depth_index = 0
        else:
            depth_index = depth_index + depth_movement


        symbols_visited += 1
    
    print("Treasures collected:",treasures_collected)
    print("Symbols visited:",symbols_visited)
    return treasure_map


