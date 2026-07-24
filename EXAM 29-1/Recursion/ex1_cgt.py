"""
Ex2: 6 marks

Define the function ex2(dirin, extensions)
recursive or using recursive functions or methods, which receives as arguments
- dirin: the path of a directory
- extensions: a list of strings representing file extensions.

The function returns a dictionary that has the strings in extensions as keys
and the number of files having that extension as values, considering all files
contained in the directory dirin and all its subdirectories.

WARNING 0: Define the recursive function at the outermost level, otherwise
it will not pass the recursion test.

WARNING 1: We recommend using the os.listdir,
os.path.isfile, and os.path.isdir functions and NOT the os.join function in
Windows. Use string concatenation with the ‘/’ character.

WARNING 2: It is forbidden to use the os.walk function or import other libraries.

"""



import os
def ex2(dirin, extensions):
    dic={}
    for word in extensions:
        dic[word]=0

    for item in os.listdir(dirin):
        path= dirin+'/'+ item

        if os.path.isfile(path) and path.endswith('.txt'):
            for word in extensions:
                if contain_word(path,word):
                    dic[word]+=1
        elif os.path.isdir(path):
            sub_dic= ex2(path,extensions)
            for w,v in sub_dic.items():
                if w in dic:
                    dic[w]+=v
                elif w not in dic:
                    dic[w]=v                   
    return dic

def contain_word(path, word):
    with open(path,'r') as f:
        for line in f:
            if word in line:
                return True
    return False

