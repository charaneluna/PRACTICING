# You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
# Input
# The first input line has an integer n: the number of values.
# The second line has n integers x_1,x_2,\dots,x_n.
# Output
# Print one integers: the number of distinct values



def distinct():
    res=0
    n = int(input())
    integers = list(map(int,input().split()))

    lis= [0]*n
    for i in range(n) :
        lis[integers[i]]+=1
    
    for element in lis:
        if element!=0:
            res+=1

    return res
    

print(distinct())


# using sets

def distinct1():
    n = int(input())
    lis = set(list(map(int,input().split())))
    print(len(lis))
distinct1()

# no set used 

def distinct2():
    n= int(input())
    lis = list(map(int,input().split()))

    visited= []
    for i in range(n):
        if lis[i] not in visited:
            visited.append(lis[i])
        else: 
            pass

    return len(visited)

print(distinct2())