#Cleo Tang
#261070795

MOVEMENT_SYMBOLS = '><v^'
EMPTY_SYMBOL = '.'
TREASURE_SYMBOL = '+'
BREADCRUMB_SYMBOL = 'X'
MOVEMENT_SYMBOLS_3D = '*|'


def get_nth_row_from_map(treasure_map_2D,n,width,height):
    '''(str,int,int,int) -> str
    Takes a string of treasure map, integers of nth row,
    width and height, and returns the nth row of the map.
    >>>get_nth_row_from_map(">...∧v<...>.....∧..<",1,5,4)
    'v<...'
    >>>get_nth_row_from_map(">...∧v<...>.....∧..<",4,5,4)
    ''
    >>>get_nth_row_from_map(">..v<...∧..<",2,3,4)
    '..∧'
    '''
    
    start = n * width   #index of the first symbol of nth row
    end = start + width  #index of the first symbol of (n+1)th row
    
    if -1 < n < height :

        return treasure_map_2D[start:end]
    
    return ''






def print_treasure_map(treasure_map,width,height):
    '''(str,int,int) -> NoneType
    Takes a string of treasure map and the number of width and height.
    Prints out the treasure map with each row on its own line.
    >>>print_treasure_map("v<..>...∧.>>>.v",3,5)
    v<.
    .>.
    ..∧
    .>>
    >.v
    >>>print_treasure_map(".>.v.∧.>.v",5,2)
    .>.v.
    ∧.>.v
    >>>print_treasure_map(">..v∧....<<<",4,3)
    >..v
    ∧...
    .<<<
    '''
    for n in range(height):
        nth_row = get_nth_row_from_map(treasure_map,n,width,height)
        print(nth_row)






def change_char_in_map(treasure_map,row_index,colm_index,char,width,height):
    '''(str,int,int,str,int,int) -> str
    takes a string of treasure map, integers of row and column indices, character c,
    and integer width and height as inputs. Returns a copy of the given treasure map
    string but with the character at the given row and column index replaced by c.
    If either or both of the indices are invalid, return the input string unchanged.
    >>>change_char_in_map("<..vvv..^^vv",1,1,"X",4,3)
    '<..vvX..^^vv'
    >>>change_char_in_map("..^^.<>.",1,4,"c",4,2)
    '..^^.<>.'
    >>>change_char_in_map("<>...^..>",3,3,"A",3,3)
    '<>...^..>'
    '''
    changed_map = ''
    index = row_index * width + colm_index #index of the symbol we want to alter
    
    if -1 < row_index < height and -1 < colm_index < width:
        
        # yes I can use string slice instead of for loop
        
        for i in range(len(treasure_map)):
            
            symbol = treasure_map[i]  
            
            #if the symbol is the target, alter the symbol
            if i == index:
                
                symbol = char
            
            changed_map += symbol
        
        return changed_map
    
    #if the index is invalid, the original string will be returned
    return treasure_map
        
    
    
    


def get_proportion_travelled(treasure_map):
    '''(str) -> float
    Takes a string of treasure map as input and returns
    the percentage rounded to two decimal place of the map
    that was travelled.
    >>>get_proportion_travelled("..XXX..")
    0.43
    >>>get_proportion_travelled("XX...X.X")
    0.5
    >>>get_proportion_travelled(".......")
    0.0
    '''
    num_breadcrumb_symbol = 0
    
    #I can use a count method here
    for symbol in treasure_map:
        
        if symbol == BREADCRUMB_SYMBOL:
            
            num_breadcrumb_symbol += 1
    
    
    proportion = num_breadcrumb_symbol / len(treasure_map)
    return round(proportion,2)





def get_nth_map_from_3D_map(treasure_map_3D,n,width,height,depth):
    '''(str,int,int,int,int) -> str
    Takes a string of 3D map, integers of nth map wanted, width,
    height and depth of the map, and returns the nth row of the map.
    Returns empty string if n is invalid.
    >>>get_nth_map_from_3D_map("..XX.>>.<...^..v<X",0,3,3,2)
    '..XX.>>.<'
    >>>get_nth_map_from_3D_map("..XX..<..XX.",3,2,2,3)
    ''
    >>>get_nth_map_from_3D_map("...^.>.<...X..<<<.",2,3,2,3)
    '..<<<.'
    '''
    start = width * height * n  #index of the first symbol of nth map
    end = start + width * height  #index of the first symbol of (n+1)th map
    
    
    if -1 < n < depth:  #check validity of n
        
        return treasure_map_3D[start:end]
    
    return ''






def print_3D_treasure_map(treasure_map_3D,width,height,depth):
    '''(str,int,int,int) -> NoneType
    Takes a string of 3D treasure map, integers of width, height
    and depth as inputs, prints out the 3D maps with a blank line
    between each map.
    >>>print_3D_treasure_map("..XX.>>..<.v",2,3,2)
    ..
    XX
    .>
    
    >.
    .<
    .v
    >>>print_3D_treasure_map("..XX...X.<.v",3,2,2)
    ..X
    X..
    
    .X.
    <.v
    >>>print_3D_treasure_map("XX...X<.vv...^^X..XXX...",4,2,3)
    XX..
    .X<.
    
    vv..
    .^^X
    
    ..XX
    X...
    '''
    for n in range(depth):
        
        nth_3D_map = get_nth_map_from_3D_map(treasure_map_3D,n,width,height,depth)
        print_treasure_map(nth_3D_map,width,height)
        
        if n < depth-1 :
            print()
        





def change_char_in_3D_map(treasure_map_3D,row_index,colm_index,depth_index,char,width,height,depth):
    '''(str,int,int,int,str,int,int,int) -> str
    Takes inputs a string of 3D map, integers of row, column, and depth index, a string character
    and integers of width, height and depth, returns a string with symbol at given row, column
    and depth replaced by character.If the indices are out of bound, original string will be returned.
    >>>change_char_in_3D_map("X..>>..^^",2,1,0,"ç",3,3,1)
    X..>>..ç^
    >>>change_char_in_3D_map("...XXX...><..vvX",1,1,2,"∆",4,2,2)
    '...XXX...><..vvX'
    >>>change_char_in_3D_map("^..vvv.X<..X",1,1,0,"π",3,2,2)
    ^..vπv.X<..X
    '''
    #ROW_index indicates the overall index of the row of the whole map
    ROW_index = depth_index * height + row_index
    
    #check the validity of the indices
    if -1 < row_index < height and -1 < colm_index < width and -1 < depth_index < depth:
        treasure_map_3D = change_char_in_map(treasure_map_3D,ROW_index,colm_index,char,width,height * depth)
        
    return treasure_map_3D







