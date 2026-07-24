'''
Ex3: 6 marks
Implement the function ex3(dirin, K, extensions) which, given a directory path 'dirin',
an integer K, and a list of target 'extensions' (e.g., ['txt', 'pdf']), must find all
directories that contain a sufficient number of files with one of the specified extensions.

Return a dictionary that has:
  - As keys: the full path (string) of each directory (using '/' as a separator).
  - As values: the total number of files (counted recursively in all sub-levels)
    whose extension is in the 'extensions' list.
The dictionary should only include directories where the total count of such files is strictly greater than K.

The function must be recursive, or call a top-level recursive function,
i.e., one defined externally at the same level in the current file.
'''

import os

def ex3(dirin, K, extensions):
    dic=cleaner(dirin,extensions)
    res={}
    for k,v in dic.items():
        if v>K:
            res[k]=v
    return res


def diver(dirin,extensions):
    dict_return={}
    count=0
    for item in os.listdir(dirin):
        path= dirin+'/'+item
        if os.path.isfile(path):
            for element in extensions:
                if path.endswith(element):
                    count+=1

        if os.path.isdir(path):
            new_dic=diver(path,extensions)
            for k, v in new_dic.items():
                dict_return[k] = v
            count+=new_dic[path]

    dict_return[dirin]=count
    return dict_return

def cleaner(dirin,extensions):
    old = diver(dirin,extensions)
    clean={}

    for k,v in old.items():
        if os.path.isdir(k):
            clean[k]=v
    return clean
