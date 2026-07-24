'''
Ex: 7 marks
Implement the function ex(dirin, extensions) which, given a directory path
'dirin' and a list of file extensions 'extensions' (e.g., ['txt', 'pdf']),
must analyze the directory tree recursively.

Return a dictionary that has:
  - As keys: the full path (string) of each directory (using '/' as a separator).
  - As values: a tuple (direct, recursive) where:
      * direct is the number of files in that directory ONLY whose extension
        is in the 'extensions' list (files in subdirectories are NOT counted).
      * recursive is the total number of such files found in the directory
        and all its subdirectories.

Include all directories in the dictionary, even if both values are 0.

The function must be recursive, or call a top-level recursive function,
i.e., one defined externally at the same level in the current file.
'''

import os

def ex(dirin,extensions):
    dic_ret= diver(dirin,extensions)

    return dic_ret



def diver(dirin,extensions):
    dic={}
    recursive=0
    direct=0
    for item in os.listdir(dirin):
        path = dirin + '/' + item
        if os.path.isfile(path):
            for ext in extensions:
                if path.endswith(ext):
                    direct+=1
        if os.path.isdir(path):
            sub_dict= diver(path,extensions)
            recursive+=sum(v[1] for v in sub_dict.values())
            dic.update(sub_dict)
    recursive+=direct
    dic[dirin]=(direct,recursive)

    return dic


