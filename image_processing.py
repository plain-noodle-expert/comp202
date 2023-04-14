#Cleo Tang
#261070795
import doctest

def is_valid_image(image_list):
    '''(list<list<int>>) -> bool
    Takes as input a nested list of PGM image matrix,
    returns True if the matrix is valid, False otherwise.
    >>> is_valid_image([[2,3,2,3],[0,3,10,23],[220,200,200,200]])
    True
    >>> is_valid_image([['1','1'],[12,'abc']])
    False
    >>> is_valid_image([[1,1,1],[35,35,35],[155,155,155]])
    True
    '''
    for nth_row in image_list:
        
        #each row of the matrix has the same length
        if type(nth_row) != list or len(image_list[0]) != len(nth_row):
            return False
        
        #each row contains only integers between 0 and 255
        for elmt in nth_row:
            
            if type(elmt) != int or elmt < 0 or elmt > 255 :
                return False
        
    return True


def is_valid_compressed_image(comp_image):
    '''(list<list<str>>) -> bool
    Takes as input a nested list of compressed image matrix,
    with each sublist contains only string of form AxB.Returns
    True if the matrix list is valid, False otherwise.
    >>> is_valid_compressed_image([['0x3','34x3'],['34x6','10x0']])
    False
    >>> is_valid_compressed_image([['0x4','25x4'],['8x3','5x5']])
    True
    >>> is_valid_compressed_image([['123x321','345x1'],['255x322']])
    False
    '''
    
    for row in comp_image:
        sum_B = 0
        if type(row) != list:
            return False
        for elmt in row:            
            if type(elmt) != str:
                return False           
            x_index = elmt.find('x') 
            A = elmt[:x_index]
            B = elmt[x_index+1:]            
            is_in_correct_form = x_index != -1 and A.isdecimal() and B.isdecimal()
            
            if not is_in_correct_form or int(A) < 0 or int(A) > 255 or int(B) <= 0:
                return False
            
            sum_B += int(B)
            
        if row == comp_image[0]:  # the sum of B of the first row 
            prev_sum_B = sum_B
        
        if prev_sum_B != sum_B:
            return False
        
        prev_sum_B = sum_B
    
    return True
            
            
    
def load_regular_image(filename):
    '''(str) -> list<list<int>>
    Takes as input a filename of a PGM image file,
    and loads in the image contained in the file and
    returns it as an image matrix.
    >>> PGM_file = open('test.pgm','w')
    >>> PGM_file.write('P2\\n4 4\\n255\\n0 0 0 0\\n0 255 255 0\\n255 0 0 255\\n0 255 255 0\\n')
    55
    >>> PGM_file.close()
    >>> load_regular_image('test.pgm')
    [[0, 0, 0, 0], [0, 255, 255, 0], [255, 0, 0, 255], [0, 255, 255, 0]]
    >>> PGM_file = open('test.pgm','w')
    >>> PGM_file.write('P2\\n3 4\\n255\\n255 255 255\\n0 255 0\\n0 255 0\\n255 255 255\\n')
    51
    >>> PGM_file.close()
    >>> load_regular_image('test.pgm')
    [[255, 255, 255], [0, 255, 0], [0, 255, 0], [255, 255, 255]]
    >>> PGM_file = open('test.pgm','w')
    >>> PGM_file.write('P2\\n3 4\\n255\\n255 255 255\\n0 255 0\\n0 \\'255\\'\\n255 255 255\\n')
    51
    >>> PGM_file.close()
    >>> load_regular_image('test.pgm')
    Traceback (most recent call last):
    AssertionError: the image matrix is not in correct PGM format
    '''
    
    image_matrix = [] 
    PGM_image = open(filename,'r')
    content = PGM_image.read()
    PGM_image.close()
    
    if len(content) == 0:
        raise AssertionError('the image matrix is not in correct PGM format')
    
    content = content.strip().split('\n')
    
    while '' in content:
        content.remove('')
        
    #check validity of first and third lines of PGM file
    if content[0] != 'P2' or content[2] != '255':
        raise AssertionError('the image matrix is not in correct PGM format')
    
    #check validity of second line of PGM file
    row_col = content[1].split()
    if len(row_col) != 2:
        raise AssertionError('the image matrix is not in correct PGM format')    
    for elmt in row_col:
        if not elmt.isdecimal():
            raise AssertionError('the image matrix is not in correct PGM format')
        if len(content[3:]) != int(row_col[1]) or len(content[3].split()) != int(row_col[0]):
            raise AssertionError('the image matrix is not in correct PGM format')
                
    for line in content[3:]:        
        row = line.split()
        row_list = []
        #convert numbers in row_matrix from str to int
        for num in row:            
            if not num.isdecimal():
                raise AssertionError('the image matrix is not in correct PGM format')
            row_list.append(int(num))
        image_matrix.append(row_list)
    
    if not is_valid_image(image_matrix):
        raise AssertionError('the image matrix is not in correct PGM format')

    return image_matrix


def load_compressed_image(filename):
    '''(str) -> list<list<str>>
    Takes as input a filename of a compressed PGM image file,
    and loads in the image contained in the file and returns
    it as a compressed image matrix.Raises a AssertionError if
    the matrix is invalid.
    >>> PGM_compressed_file = open('test.pgm','w')
    >>> PGM_compressed_file.write('P2C\\n24 4\\n255\\n0x24\\n0x13 50x9 0x2\\n23x12 255x10 1x2\\n0x24\\n')
    54
    >>> PGM_compressed_file.close()
    >>> load_compressed_image('test.pgm')
    [['0x24'], ['0x13', '50x9', '0x2'], ['23x12', '255x10', '1x2'], ['0x24']]
    >>> PGM_compressed_file = open('test.pgm','w')
    >>> PGM_compressed_file.write('P2C\\n24 3\\n255\\n0x13 200x9 0x2\\n23x12 5x10 1x2\\n0x1 2x2 55x20 66x1\\n')
    62
    >>> PGM_compressed_file.close()
    >>> load_compressed_image('test.pgm')
    [['0x13', '200x9', '0x2'], ['23x12', '5x10', '1x2'], ['0x1', '2x2', '55x20', '66x1']]
    >>> PGM_compressed_file = open('test.pgm','w')
    >>> PGM_compressed_file.write('P2C\\nabc \\n255\\n0x24\\n0x12 50x9 0x2\\n23x13 255x10 1x2\\n0x24\\n')
    54
    >>> PGM_compressed_file.close()
    >>> load_compressed_image('test.pgm')
    Traceback (most recent call last):
    AssertionError: the compressed image matrix is not in correct format
    '''

    comp_image_matrix = [] 
    comp_PGM_image = open(filename,'r')
    content = comp_PGM_image.read()
    comp_PGM_image.close()
    
    content = content.strip().split('\n')
    while '' in content:
        content.remove('')
    # check if the file is empty 
    if len(content) == 0:
        raise AssertionError('the compressed image matrix is not in correct format')
    
    #check the validity of first line and third line
    if content[0] != 'P2C' or content[2] != '255':
        raise AssertionError('the compressed image matrix is not in correct format')
    row_col = content[1].split()
    if len(row_col) != 2 or len(content[3:]) != int(row_col[1]):
        raise AssertionError('the compressed image matrix is not in correct format')
    
    # check row length validity
    B_sum = 0
    for elmt in content[3].split():
        if elmt.count('x') != 1:
            raise AssertionError('the compressed image matrix is not in correct format')
        x_index = elmt.find('x')
        if type(int(elmt[x_index+1:])) != int or type(int(elmt[:x_index])) != int:            
            raise AssertionError('the compressed image matrix is not in correct format')        
        B_sum += int(elmt[x_index+1:])
    if B_sum != int(row_col[0]):
        raise AssertionError('the compressed image matrix is not in correct format')
    
    # load
    for line in content[3:]:
        
        line = line.strip()
        row_matrix = line.split()
        comp_image_matrix.append(row_matrix)    
    
    if not is_valid_compressed_image(comp_image_matrix):        
        raise AssertionError('the compressed image matrix is not in correct format')
    
    return comp_image_matrix



def load_image(filename):
    '''(str) -> list<list<int/str>>
    Takes as input a filename of a PGM image file, loads in the content
    and returns the image matrix according to the type of the file. Raises
    a AssertionError otherwise.
    >>> PGM_file1 = open('test.pgm','w')
    >>> PGM_file1.write('P2\\n3 4\\n255\\n255 255 255\\n0 255 0\\n0 255 0\\n255 255 255\\n')
    51
    >>> PGM_file1.close()
    >>> load_image('test.pgm')
    [[255, 255, 255], [0, 255, 0], [0, 255, 0], [255, 255, 255]]
    >>> PGM_compressed_file = open('test.pgm','w')
    >>> PGM_compressed_file.write('P2C\\n24 3\\n255\\n0x13 200x9 0x2\\n23x12 5x10 1x2\\n0x1 2x2 55x20 66x1\\n')
    62
    >>> PGM_compressed_file.close()
    >>> load_image('test.pgm')
    [['0x13', '200x9', '0x2'], ['23x12', '5x10', '1x2'], ['0x1', '2x2', '55x20', '66x1']]
    >>> PGM_compressed_file = open('test.pgm','w')
    >>> PGM_compressed_file.write('P2C\\n24 3\\n256\\n0x13 200x9 0x2\\n23x12 5x10 1x2\\n0x1 2x2 55x20 66x1\\n')
    62
    >>> PGM_compressed_file.close()
    >>> load_image('test.pgm')
    Traceback (most recent call last):
    AssertionError: the compressed image matrix is not in correct format
    '''
    
    PGM_file = open(filename,'r')
    content = PGM_file.read()
    PGM_file.close()
    # check if the file is empty
    if len(content) == 0:
        raise AssertionError('the image file is not in correct format')
    line = content.split('\n')
    if line[0] == 'P2':
        return load_regular_image(filename)   
    elif line[0] == 'P2C':
        return load_compressed_image(filename)
        
    raise AssertionError('the image file is not in correct format')




def save_regular_image(image_matrix, filename):
    '''(list<list<int>>) -> NoneType
    Takes as input a nested list of image matrix and saves it in a file
    with the given filename.Raises a AssertionError if the image matrix
    is invalid.
    >>> save_regular_image([[0, 0, 0, 0, 0], [211]*2+[98]*3], 'test.pgm')
    >>> pgm_file = open('test.pgm', 'r')
    >>> pgm_file.read()
    'P2\\n5 2\\n255\\n0 0 0 0 0\\n211 211 98 98 98\\n'
    >>> pgm_file.close()
    >>> image1 = [[23]*3+[34]*2, [0]*5, [0]*2+[255]*1+[0]*2]
    >>> save_regular_image(image1, 'test.pgm')
    >>> image2 = load_image('test.pgm')
    >>> image1 == image2
    True
    >>> save_regular_image([[0]*5, [255]*5+['a']*3], 'test.pgm')
    Traceback (most recent call last):
    AssertionError: the given image matrix is not in valid PGM format.
    '''
    pgm_file = open(filename, 'w')
    
    if not is_valid_image(image_matrix):
        pgm_file.close()
        raise AssertionError('the given image matrix is not in valid PGM format.')
    
    row_num = str(len(image_matrix))
    digit_num = str(len(image_matrix[0]))
    
    pgm_file.write('P2\n' + digit_num + ' ' + row_num + '\n255\n')
    
    for row in image_matrix:
        
        pgm_file.write(str(row[0]))
        
        for i in range(1,len(row)):
            
            pgm_file.write(' '+str(row[i]))
                
        pgm_file.write('\n')
            
    pgm_file.close()




def save_compressed_image(image_matrix, filename):
    '''(list<list<str>>,str) -> NoneType
    Takes a nested list and a filename (string) as input,
    and saves it in the compressed PGM format to a file
    with the given filename. Raises an AssertionError if
    the compressed matrix is not valid.
    >>> save_compressed_image([['0x8', '1x2'], ['0x10']], 'test.pgm')
    >>> fobj = open('test.pgm','r')
    >>> fobj.read()
    'P2C\\n10 2\\n255\\n0x8 1x2\\n0x10\\n'
    >>> fobj.close()
    >>> image1 = ([['8x4', '25x3'], ['255x7'], ['99x6', '0x1']])
    >>> save_compressed_image(image1, 'test.pgm')
    >>> image2 = load_image('test.pgm')
    >>> image1 == image2
    True
    >>> save_compressed_image([['abcx234', '23x10'], ['3x3', '7x7']],'test.pgm')
    Traceback (most recent call last):
    AssertionError: the compressed image matrix is not in a valid PGM format.
    '''

    comp_pgm_file = open(filename, 'w')
    
    if not is_valid_compressed_image(image_matrix):
        comp_pgm_file.close()
        raise AssertionError('the compressed image matrix is not in a valid PGM format.')
    
    row_num = str(len(image_matrix))
    digit_num = 0
    for elmt in image_matrix[0]:
        x_index = elmt.find('x') 
        B = elmt[x_index+1:]
        digit_num += int(B)
    
    comp_pgm_file.write('P2C\n'+str(digit_num)+' '+row_num+'\n255\n')
    
    for row in image_matrix:
        row_digits = ' '.join(row)
        comp_pgm_file.write(row_digits+'\n')
    
    comp_pgm_file.close()
    
    



def save_image(image_matrix, filename):
    '''(list<list<str/int>>, str) -> NoneType
    Takes as input a nested list of PGM image and a filename,
    saves the nested list into the file given the filename, as
    different format accoding to the type of elements in the list.
    Raises a AssertionError if the image matrix is invalid.
    >>> save_image([['25x4', '1x2'], ['0x6']], 'test.pgm')
    >>> fobj = open('test.pgm','r')
    >>> fobj.read()
    'P2C\\n6 2\\n255\\n25x4 1x2\\n0x6\\n'
    >>> image1 = [[0, 0, 0, 0, 0], [211]*2+[98]*3]
    >>> save_image(image1, 'test.pgm')
    >>> image2 = load_image('test.pgm')
    >>> image1 == image2
    True
    >>> save_image([['43x4', '23x10'], ['3x3', '7x7']],'test.pgm')
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    if is_valid_image(image_matrix):
        save_regular_image(image_matrix, filename)
    elif is_valid_compressed_image(image_matrix):
        save_compressed_image(image_matrix, filename)
    else:
        raise AssertionError('the image matrix is not in a valid PGM format.')





def invert(image_matrix):
    '''(list<list<int>>) -> list<list<int>>
    Takes as input a non_compressed PGM image matrix, and
    returns the inverted image.
    >>> image = [[0, 100, 0], [55, 25, 155], [255, 255, 255]]
    >>> invert(image)
    [[255, 155, 255], [200, 230, 100], [0, 0, 0]]
    >>> image
    [[0, 100, 0], [55, 25, 155], [255, 255, 255]]
    >>> invert([['a', 'b', 'c'], ['12', '13', '14']])
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    >>> invert([[100, 200, 450], [35, 0, 0]])
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    inverted_matrix = []
    if is_valid_image(image_matrix):
        
        for row in image_matrix:
            inverted_row = []
            for num in row :
                inverted_num = 255 - num
                inverted_row.append(inverted_num)
            inverted_matrix.append(inverted_row)
    else:
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    return inverted_matrix





def flip_horizontal(image_matrix):
    '''(list<list<int>>) -> list<list<int>>
    Takes as input a non-compressed PGM image matrix, returns
    the image matrix flipped horizontally.Should not modify the
    input matrix. An AssertionError raised if the image matrix
    is invalid.
    >>> image = [[1, 2, 3, 4, 5], [0, 8, 5, 8, 8], [5, 4, 3, 2, 1]]
    >>> flip_horizontal(image)
    [[5, 4, 3, 2, 1], [8, 8, 5, 8, 0], [1, 2, 3, 4, 5]]
    >>> image
    [[1, 2, 3, 4, 5], [0, 8, 5, 8, 8], [5, 4, 3, 2, 1]]
    >>> image = [[1, 2, 3, 4, 5], [8, 8, 8, 8], [5, 4, 3, 2, 1]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    >>> image = [[211, 200, 345], [0, 0, 0], [255, 255, 255]]
    >>> flip_horizontal(image)
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    flipped_matrix = []
    
    if is_valid_image(image_matrix):
        
        for row in image_matrix:
            
            #flipped_row = []
            
            #for num in row[::-1]:
                #flipped_row.append(num)
            
            flipped_matrix.append(row[::-1])
        
    else:
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    return flipped_matrix

    




def flip_vertical(image_matrix):
    '''(list<list<int>>) -> list<list<int>>
    Takes as input a non-compressed PGM image matrix, returns
    the image matrix flipped vertically.Should not modify the
    input matrix. An AssertionError raised if the image matrix
    is invalid.
    >>> image = [[1, 0, 0, 5], [3, 3, 3, 3], [5, 10, 34, 25]]
    >>> flip_vertical(image)
    [[5, 10, 34, 25], [3, 3, 3, 3], [1, 0, 0, 5]]
    >>> image
    [[1, 0, 0, 5], [3, 3, 3, 3], [5, 10, 34, 25]]
    >>> image = [['axb'], ['35x7'], [0, 0, 0, 0], [1, 2, 3, 4]]
    >>> flip_vertical(image)
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    >>> image = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    >>> flip_vertical(image)
    [[10, 11, 12], [7, 8, 9], [4, 5, 6], [1, 2, 3]]
    >>> image
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    '''
    flipped_matrix = []
    
    if is_valid_image(image_matrix):
        
        for row in image_matrix[::-1]:
            flipped_matrix.append(row)
    else:
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    return flipped_matrix







def crop(image_matrix,row_index,colm_index,row_num,colm_num):
    '''(list<list<int>>, int, int, int, int) -> list<list<int>>
    Takes as inputs a non_compressed PGM image matrix, two non-negative
    integers as row and column indices, two positive integers as
    row and column numbers. Returns a matrix corresponding to the pixels
    contained in the target rectangle, raises an AssertionError if the
    image matrix is invalid.
    >>> image = [[1, 0, 0, 5], [3, 12, 12, 3], [5, 13, 34, 27]]
    >>> crop(image, 1, 1, 2, 3)
    [[12, 12, 3], [13, 34, 27]]
    >>> image
    [[1, 0, 0, 5], [3, 12, 12, 3], [5, 13, 34, 27]]
    >>> image = [[10, 5], [12, 12], [13, 27], [33, 96]]
    >>> crop(image, 0, 0, 4, 1)
    [[10], [12], [13], [33]]
    >>> image
    [[10, 5], [12, 12], [13, 27], [33, 96]]
    >>> image = [[23, 23, 23], [245, 100]]
    >>> crop(image, 3, 2, 2, 3)
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    target_matrix = []
    
    if not is_valid_image(image_matrix):
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    else:
        valid_index = row_index < len(image_matrix) and colm_index < len(image_matrix[0])
        max_row_num = len(image_matrix) - row_index
        max_colm_num = len(image_matrix[0]) - colm_index
        valid_num = row_num <= max_row_num and colm_num <= max_colm_num
        
        if valid_index and valid_num:
            
            for row in image_matrix[row_index : row_index + row_num]:
                target_row = []
                
                for num in row[colm_index : colm_index + colm_num]:
                    target_row.append(num)
                
                target_matrix.append(target_row)
        else:
            raise AssertionError('the image matrix is not in a valid PGM format.')
    
    return target_matrix






def find_end_of_repetition(a_list, index,target):
    '''(list<int>, int, int) -> int
    Takes as input a list of integers and one index, one target number.
    Returns the index of the last consecutive occurrence of the target
    number.
    >>> find_end_of_repetition([2, 2, 2, 2, 5, 3], 1, 2)
    3
    >>> find_end_of_repetition([0, 0, 2, 2, 2, 2, 2], 2, 2)
    6
    >>> find_end_of_repetition([-1, 12, 12, 34, 2, 3], 0, -1)
    0
    '''

    for i in range(index+1, len(a_list)+1):
        
        if i == len(a_list) or a_list[i] != target:
            return i-1
        




def compress(image_matrix):
    '''(list<list<int>>) -> list<list<str>>
    Takes as input a non-compressed PGM matrix and returns a
    compressed image matrix. Raises an AssertionError if the
    matrix is invalid.
    >>> compress([[11, 11, 245, 245, 245], [0, 0, 0, 0 ,0]])
    [['11x2', '245x3'], ['0x5']]
    >>> compress([[25, 25, 25, 10], [300, 133, 133, 133], [0]*5])
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    >>> compress([[100]*6, [150]*3+[3, 4, 5], [13]*6])
    [['100x6'], ['150x3', '3x1', '4x1', '5x1'], ['13x6']]
    '''
    if not is_valid_image(image_matrix):
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    comp_image_matrix = []
    for row in image_matrix:
        comp_row = []
        target = row[0]
        target_index = 0
        
        while True:            
            next_target_index = find_end_of_repetition(row, target_index, target) + 1
            num_target = next_target_index - target_index
            
            comp_row.append(str(target)+'x'+str(num_target))
            
            if next_target_index == len(row):
                break
            
            target = row[next_target_index]
            target_index = next_target_index
         
        comp_image_matrix.append(comp_row)

    return comp_image_matrix







def decompress(image_matrix):
    '''(list<list<str>>) -> list<list<int>>
    Takes as input a compressed PGM image matrix, returns
    a decompressed matrix if the compressed image matrix is
    valid, otherwise, raises an AssertionError.
    >>> decompress([['25x5'], ['7x5'], ['4x1', '1x4']])
    [[25, 25, 25, 25, 25], [7, 7, 7, 7, 7], [4, 1, 1, 1, 1]]
    >>> decompress([['200x6'], ['7x6'], ['4x2', '2x4']])
    [[200, 200, 200, 200, 200, 200], [7, 7, 7, 7, 7, 7], [4, 4, 2, 2, 2, 2]]
    >>> decompress([['100x2', '50x3'], ['7x4'], ['4x2', '2x2']])
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    
    if not is_valid_compressed_image(image_matrix):
        raise AssertionError('the image matrix is not in a valid PGM format.')
    
    decomp_matrix = []
    for row in image_matrix:
        
        row_matrix = []
        
        for elmt in row:
            x_index = elmt.find('x')
            A = int(elmt[:x_index])
            B = int(elmt[x_index+1:])
            row_matrix += [A]*B
        
        decomp_matrix.append(row_matrix)

    return decomp_matrix




def process_command(commands):
    '''(str) -> NoneType
    Takes as input a string of a sequence of commands separated
    by white space, and executes the commands in turn without
    returning anything.
    >>> fobj = open('test.pgm', 'w')
    >>> fobj.close()
    >>> save_image([['25x4', '1x3'], ['10x7']], 'test.pgm')
    >>> process_command("LOAD<test.pgm> DC INV INV SAVE<test.pgm>")
    >>> image = load_image("test.pgm")
    >>> image2 = load_image("test.pgm")
    >>> image == image2
    True
    >>> fobj = open('test.pgm', 'w')
    >>> fobj.close()
    >>> save_image([['25x4', '1x2'], ['0x6']], 'test.pgm')
    >>> process_command('LOAD<test.pgm> DC CR<0,1,2,3> SAVE<test.pgm>')
    >>> load_image('test.pgm')
    [[25, 25, 25], [0, 0, 0]]
    >>> image = open('test.pgm', 'w')
    >>> image.close()
    >>> save_image([[25, 25, 25, 10], [30, 133, 133, 133], [0]*4],'test.pgm')
    >>> process_command('LOAD<test.pgm> CP FH FH FV CP SAVE<test.pgm>')
    Traceback (most recent call last):
    AssertionError: the image matrix is not in a valid PGM format.
    '''
    
    commands_list = commands.split()
    
    for command in commands_list:
        
        if 'LOAD' in command:
            
            filename = command[5:-1]
            
            image_matrix = load_image(filename)                  
        
        elif command == 'INV':
            
            image_matrix = invert(image_matrix)
        
        elif command == 'FH':
            
            image_matrix = flip_horizontal(image_matrix)
        
        elif command == 'FV':
            
            image_matrix = flip_vertical(image_matrix)
            
        elif 'CR' in command:
            if command[-1] != '>' or command[3:-1].count(',') != 3:
                raise AssertionError("Invalid command.")
            parameters = command[3:-1].split(',')
            for elmt in parameters:
                if not elmt.isdecimal():
                    raise AssertionError("Invalid command")
            row_index, colm_index, row_num, colm_num = parameters
            image_matrix = crop(image_matrix, int(row_index), int(colm_index), int(row_num), int(colm_num))
        
        elif command == 'CP':
            
            image_matrix = compress(image_matrix)
                
        elif command == 'DC':
            
            image_matrix = decompress(image_matrix)

        elif 'SAVE' in command:
            
            filename = command[5:-1]
            
            save_image(image_matrix, filename)
            
        else:
            raise AssertionError('invalid commands included.')





if __name__ == '__main__':
    doctest.testmod()