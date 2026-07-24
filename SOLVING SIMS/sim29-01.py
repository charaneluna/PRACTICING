#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operations to carry out FIRST:
 1) Save this file as program.py 
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER
 3) When your functions are ready, save the file in the window for the
    collection.

IMPORTANT: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""
from sympy.printing.tree import tree

name = "Maurizio"
surname = "Mancini"
student_id = "12345678"



# %% ----------------------------------- FUNC1 ------------------------- #

'''func1: 2 marks
Define the function func1(n) that gets an integer n and returns the number
of bits set to one for the binary representation of the integer n. 
You can use the builtin function bin.

    Example:
        n = 31 (binary 11111) -> expected: 5
        n = 16 (binary 10000) -> expected: 1
'''

def func1(n):
    nbr = bin(n)
    count=0
    for num in nbr:
        if num==str(1):
            count+=1
    return count



# %% ----------------------------------- FUNC2 ------------------------- #
'''func2: 4 marks
Define the function func2(message, colors) that gets a string and a dictionary
as input.
The string message contains tags such as [color].
The dictionary colors has keys as strings and values as strings, linking
a color with its hexadecimal codes. The function must return a new string
where each tag [color] is modified in the corresponding hexadecimal code
<hex>, found in the "colors" dictionary.

    Example:
        message: "Welcome to [red]Hell!"
        colors: {'red': '0xFF0000'}
        Result: "Welcome to <#FF0000>Hell!"
'''

def func2(message,colors):
    for k,v in colors.items():
        color=k
        co_code=v
    
    message = message.replace('['+color+']', '<'+co_code+'>')
    return message


# %% ----------------------------------- FUNC3 ------------------------- #
''' func3: 4 marks

Define func3(inventory, recipe_file) that receives a dictionary made of strings
with integer values and a string 'recipe_file'.
The function must read a recipe from the input file and check whether a player
can craft an item from the materials in their inventory.
The inventory is in the format {material_name: quantity}.
The recipe in file is made of rows in the form of 'material_name:quantity'.
The function must return the number of items that can be crafted from the
inventory's material, based on the recipe.
If the required material is not in inventory, the function returns 0.


    Examples:
        inventory: {"iron": 5, "wood": 10}
        recipe01: {"iron": 2, "wood": 4}
        Result: 2 
        
        inventory: {"iron": 5, "wood": 10}
        recipe02: {"iron": 3, "leather": 1, "wood": 1}
        Result: 0 (leather is missing from the inventory)

    '''

def func3(inventory,recipe_file):
    recipe = {}
    with open(recipe_file,'r') as fin:
        for i in range(len(fin)):
            line= fin.readline().strip()



    



    pass

# %% ----------------------------------- FUNC4 ------------------------- #
""" Func 4: 4 marks
Implement the function func4(base_stats, equipment) which takes as input:
    -base_stats, a dictionary of statistics as string:int,
    -equipment, a list of dictionaries in the form of 
       -'stat': statistic, where statistic is a string
       -'type': operation, where operation can be 'add' or 'mul'
       -'val': value, where value is a numeric value.
The function must calculate the final statistics by applying equipment
bonuses to base_stats.
Each object specifies which statistic it influences via the 'stat' key.

    ORDER OF APPLICATION FOR EACH STATISTIC:
    1. First apply all 'add' bonuses to the specific base statistic.
    2. On the result, apply all 'mul' bonuses of the same statistic.
    
    All statistics must be rounded to the second decimal digit.

    Example:
        base_stats= {'att': 100, 'def': 50}
        equipment= [
            {'stat': 'att', 'type': 'add', 'val': 10},
            {'stat': 'att', 'type': 'mul', 'val': 1.1},
            {'stat': 'def', 'type': 'add', 'val': 5}
        ]
        Result: {'att': 121.0, 'def': 55.0}
"""



# %% ----------------------------------- FUNC5 ------------------------- #
""" Func 5: 8 marks
Define the function func5(inputfile_png, outputfile_png) that gets as input
two strings representing filenames of png files. The function must read
the image stored in the file inputfile_png, that is a black image in which
for each line there is a segment of a single color.
The function must write in a new file outputfile_png the image obtained
by sorting the rows of the read image according to the following criteria:
    - by the length of the segments, in decreasing order 
    - by the sum of all the components of the color of the segment, in decreasing order
    - by the color components, in increasing order (namely (0,0,0) < (0,0,1)).

Finally, the function must return the length of the longest segment found.
Remember to use the functions images.load and images.save for loading and
saving images from/to files.
"""
import images



# %% ----------------------------------- EX1 ------------------------- #
""" Ex1: 6 marks

Implement the function ex1(root), recursive or
using recursive functions or methods, which checks whether a binary tree
taken as input is balanced in height.
root is a node instance of the class BinaryTree as defined in tree.

A tree is balanced if, for each node, the difference in height
between the left and right subtrees is no greater than 1.
"""

    
# %% ----------------------------------- EX2 ------------------------- #
""" Ex2: 6 marks
    
Define ex2(data) a recursive function or one that uses recursive functions
or methods that receives a list that may contain integers or other
nested lists at any level.
The function must calculate the sum of all EVEN numbers encountered.

    RULES:
    - If an element is a list, it must be explored recursively.
    - If it is an integer and is even, it must be added to the total.
    - If it is an odd integer or an empty list, it does not contribute to the sum.

    Example:
        data = [1, [2, [3, 4]], 6]
        Even numbers: 2, 4, 6
        Output: 12    
"""

    
###########################################################################
if __name__ == '__main__':
    # your tests go here
    print('*'*50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*'*50)