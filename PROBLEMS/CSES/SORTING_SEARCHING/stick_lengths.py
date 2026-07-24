# There are n sticks with some lengths. Your task is to modify the sticks so that each stick has the same length.
# You can either lengthen and shorten each stick. Both operations cost x where x is the difference between the new and original length.
# What is the minimum total cost?
# Input
# The first input line contains an integer n: the number of sticks.
# Then there are n integers: p_1,p_2,\ldots,p_n: the lengths of the sticks.
# Output
# Print one integer: the minimum total cost.



# average 

def stick():
    res=0
    n = int(input()) # nbr of sticks
    lengths = list(map(int,input().split()))    
    sum = 0
    for element in lengths:
        sum+=element
    # ideal = (sum-(sum%n))//n
    ideal = sum//n
    for element in lengths:
        if element >= ideal :
            res += element - ideal 
        else :
            res+= ideal - element  
    return ideal
print(stick())



# median

def stick1():
    res=0
    n = int(input()) # nbr of sticks
    lengths = list(map(int,input().split()))
    new_len = sorted(lengths)
    medi= n//2
    for element in new_len : 
        if element>= new_len[medi]:
            res+= element-new_len[medi]
        else:
            res+= new_len[medi]- element 

    return res 

    


print( stick1())
