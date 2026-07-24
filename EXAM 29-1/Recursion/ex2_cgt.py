
"""Ex3: 6 marks

Define the function ex3(dirin, letters)
recursive or using recursive functions or methods, which receives as arguments
- dirin: the path of a directory
- letters: a list of single characters (strings of length 1).

The function returns a dictionary that has the characters in letters as keys 
and the number of `.txt` files in the directory (and all its subdirectories) 
that **start with that character** (the first character of the first line of the file) as values.

Example:

If the directory "texts" has the following structure:

texts/
 ├─ alpha.txt  (first line: "apple pie")
 ├─ beta.txt   (first line: "banana split")
 ├─ gamma.txt  (first line: "grape juice")
 └─ sub/
     ├─ ant.txt    (first line: "avocado")
     └─ blueberry.txt (first line: "blueberry muffin")

Calling the function:

ex3("texts", ["a", "b", "g"])

must return:

{"a": 2, "b": 2, "g": 1}

Explanation:
- "a" → alpha.txt + sub/ant.txt ✅  
- "b" → beta.txt + sub/blueberry.txt ✅  
- "g" → gamma.txt ✅  

WARNING 0: Define the recursive function at the outermost level.  

WARNING 1: Use os.listdir, os.path.isfile, and os.path.isdir. Do NOT use os.walk.  

WARNING 2: Use string concatenation with '/' for paths, not os.join (for Windows compatibility).  

"""


import os

def ex2(dirin, letters):
    res={}

    for letter in letters:
        res[letter]=0

    for item in os.listdir(dirin):
        path= dirin+'/'+item

        if os.path.isfile(path) and path.endswith('.txt'):
            for letter in letters:
                if first_letter(path,letter):
                    res[letter]+=1
        elif os.path.isdir(path):
            sub_dic = ex2(path,letters)
            for k,v in sub_dic.items():
                res[k]+=v

    return res

def first_letter(path,letter):
    with open(path,'r') as f:
        first_line = f.readline()
        if first_line!= "":
            first_char = first_line[0]
            if first_char == letter :
                return True
    return False

