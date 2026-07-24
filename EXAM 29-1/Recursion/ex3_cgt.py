"""

Ex4: 8 marks

Define the function ex4(dirin, words)
recursive or using recursive functions or methods, which receives as arguments:
- dirin: the path of a directory
- words: a list of strings.

The function returns a dictionary that has the strings in words as keys
and the **maximum number of times** that word appears in a **single `.txt` file**
found in the directory or any of its subdirectories.

In other words:
- You must scan all `.txt` files recursively
- For each word, count how many times it appears in EACH file
- Keep the **maximum count per word**, not the total

Example:

Directory structure:

docs/
 ├─ a.txt        → "cat dog cat dog cat"
 ├─ b.txt        → "dog dog dog"
 └─ sub/
     ├─ c.txt    → "cat cat"
     └─ d.txt    → "dog cat dog cat"

Calling:

ex4("docs", ["cat", "dog"])

must return:

{"cat": 3, "dog": 3}

Explanation:
- "cat":
    - a.txt → 3
    - c.txt → 2
    - d.txt → 2
    → max = 3
- "dog":
    - a.txt → 2
    - b.txt → 3
    - d.txt → 2
    → max = 3

WARNING 0: The recursive function must be defined at the outermost level.

WARNING 1: Use os.listdir, os.path.isfile, and os.path.isdir only.
Do NOT use os.walk or import additional libraries.

WARNING 2: Paths must be built using string concatenation with '/'.

WARNING 3: Reading the same file multiple times unnecessarily may lead to inefficient solutions.
"""
import os

def ex3(dirin, words):
    res ={}
    for word in words:
        res[word]=0

    for item in os.listdir(dirin):
        path= dirin+'/'+item

        if os.path.isfile(path) and path.endswith('.txt'):
            for word in words:
                current= amount(path,word)
                if current>res[word]:
                    res[word]=current
        elif os.path.isdir(path):
            sub_res=ex3(path, words)
            for k,v in sub_res.items():
                if sub_res[k]>res[k]:
                    res[k]=sub_res[k]
    return res

punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~" 

def amount(path,word):
    with open(path,'r') as f:
        total=0
        for line in f:
            for char in line.strip().split():
                cleaned=char.strip(punctuation)
                if cleaned==word :
                    total+=1
    return total

                    
