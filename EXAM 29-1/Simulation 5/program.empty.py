#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
""" Operations to carry out FIRST:
 1) Save this file as program.py
 2) Assign the variables below with your
    NAME, SURNAME and STUDENT ID NUMBER
"""

name = "NAME"
surname = "SURNAME"
student_id = "MATRICULATION NUMBER"

"""
To pass the exam you must get at least 18.
The final grade is the sum of the scores of the solved problems.

WARNING: You can not import any additional library.

NOTE: set DEBUG = True in `grade.py` to improve debugging; but
remember that recursion is tested (and graded) only if DEBUG = False
"""

# %% ----------------------------------- FUNC1 ------------------------- #
''' func1: 3 marks
Define the function 
    func1(D1, D2, D3)
which receives as arguments:
- D1: a dictionary with string keys  and integer values
- D2: a dictionary with integer keys and integer values
- D3: a dictionary with integer keys and string  values
and which returns a dictionary containing the keys of all the input dictionaries.
The corresponding values are:
- the maximum values among the corresponding keys, considering for the 
  strings the value obtained by summing the Unicode values of all characters.

Example:
D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
D2 = { 1 : 5     , 3 : 12   , 5 : 9 }
D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }

expected = {'uno': 1, 'due': 2, 'tre': 3, 1: 5, 3: 12, 5: 862, 12: 637, 90: 732}
'''

def func1(D1, D2, D3):
    # your code goes here
    pass


# D1 = { 'uno' : 1 , 'due' : 2, 'tre' : 3 }
# D2 = { 1 : 5     , 3 : 12   , 5 : 9 } 
# D3 = { 12 : 'papere', 90 : 'cavalli', 5 : 'sogliole' }
# print(func1(D1,D2,D3))


# %% ----------------------------------- FUNC2 ------------------------- #
''' func2: 3 marks
Define the function 
    func2(L1, L2, L3)
which receives as arguments 3 lists of integers L1, L2, and L3, and returns the set
of elements that appear in only two of the three lists.

Example:
L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
L2 = [ 5, 6, 1, 8, 3, 2 ]
L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]

expected: {9}
'''


def func2(L1, L2, L3):
    # your code goes here
    pass


# example
# L1 = [ 1, 2, 6, 2, 8, 4, 9, 1, 7 ]
# L2 = [ 5, 6, 1, 8, 3, 2 ]
# L3 = [ 10, 8, 9, 1, 2, 8, 9, 6, 10 ]
# print(func2(L1,L2,L3))


# %% ----------------------------------- FUNC3 ------------------------- #
""" func3: 6 marks

Define the function 
    func3(input_filename, output_filename)
which receives the following arguments:
- input_filename: the path to a text file containing a rectangular matrix 
    of integers with N rows and 2N columns
- output_filename: the path to a file in which you must write a square matrix
    NxN 
The function must read the N x 2N matrix of integers and transform it 
into an NxN square matrix in which the value in cell i,j is obtained by adding:
- the value of the cell in row i and column N+j
- all the elements in column j.
The function must also return the sum of all the elements in the input matrix.

Example: the file func3/in_5.txt contains the matrix
    1 2 1 2
    2 3 2 3
the function must transform it into the matrix
    4 7
    5 8

write the matrix in the output file and return 16.

"""

def func3(input_filename, output_filename):
    # your code goes here
    pass



# print(func3('func3/in_1.txt', 'func3/out_1.txt'))

# %% ----------------------------------- FUNC4 ------------------------- #
""" func4: 8 marks

Define the function func4(file_png_in) 
which receives a string as argument, representing the name of a PNG file.
The image contains snowflakes and Christmas trees on a black background.

The snowflake is made up of 5 identical pixels in the shape of a cross (C=color, .=black)
C.C
.C.
C.C
while the Christmas trees are made up of 10 identical pixels as follows (C=color, .=black)
..C..
.CCC.
CCCCC
..C..

The function returns a pair with the number of snowflakes and Christmas trees
found in the image of the input file, as a tuple SNOWFLAKES,TREES


"""
import images

def func4(file_png_in):
    # your code goes here
    pass

# print(func4("func4/func4_100_100_10.png"))


# %% ----------------------------------- EX.1 ------------------------- #
"""
Ex1: 6 marks

Define the function ex1(dirin, words)
recursive or using recursive functions or methods, which receives as arguments
- dirin: the path of a directory
- words: a list of strings.

The function returns a dictionary that has the strings in words as keys 
and the number of ‘.txt’ files containing that word as values.

WARNING 0: Define the recursive function at the outermost level, otherwise
it will not pass the recursion test.

WARNING 1: We recommend using the os.listdir,
os.path.isfile, and os.path.isdir functions and NOT the os.join function in
Windows. Use string concatenation with the ‘/’ character.

WARNING 2: It is forbidden to use the os.walk function or import other libraries.

"""
import os

def ex1(dirin, words):
    # your code goes here
    pass

# print(ex1('ex1/A', ["fish", "bird","monkey", "lizard","tuna"]))

# %% ----------------------------------- EX.2 ------------------------- #
"""
Ex2: 6 marks

Implement the function ex2(root: BinaryTree) -> int that takes as input
the root of a binary tree, as defined in the 'BinaryTree' class of the 'tree.py' module,
and returns an integer corresponding to the maximum value that can be obtained
by multiplying the value of a node by its level, assuming that the level of the root is 1.

Example:

        ______20_____       level 1          ______13______
       |             |                      |              |
      15__        ___1___   level 2      ___7___        ___10___
          |      |       |              |       |      |        |
          -2    11       4  level 3    _-5_    -1_    _9_      _3_
                                      |    |      |  |   |    |   |
                            level 4 -10    4      6  5  -2    -6  2

 If the tree is the one on the left, the function must return the value 33 = 11 * 3

 If the tree is the one on the right, the function must return the value 27 = 9 * 3
********************************************************************
Note: if you write an additional function, DO NOT define the additional recursive function 
as an internal function but place it at the same level as ex1, 
otherwise you will not pass the recursive test!
"""
from tree import BinaryTree

def ex2(root):
    # your code goes here
    pass

# root = BinaryTree.fromList([20, [15,None,[-2,None,None]],
# [1, [11,None,None], [4,None,None]]])
# print(ex2(root))
#
# root = BinaryTree.fromList([13,
# [7,[-5,[-10,None,None],[4,None,None]],[-1,None,[6,None,None]]],
# [10, [9,[5,None,None],[-2,None,None]],
#  [3,[-6,None,None],[2,None,None]]]])
# print(ex2(root))

# %%
###################################################################################
if __name__ == '__main__':
    # your tests go here
    print('*' * 50)
    print('You have to run grade.py if you want to debug with the automatic grader.')
    print('Otherwise you can insert here you code to test the functions but you have to write your own tests')
    print('*' * 50)
