"""
Implement the recursive function operations(nums, ops), or another function that uses recursion,

which takes as input a list of positive integers nums and a list of strings ops indicating operations on
the numbers.
 Both lists could contain duplicates. The function must recursively generate all possible
arithmetic expressions, where each expression is a string. The expressions are derived by joining two
or more numbers taken from nums with operations from the ops. The function must return all the
constructed expressions.
The following rules apply when constructing the expression:
(a) Once a number is used in the expression, it can no longer be used (unless there are other duplicates).
For example, if nums=[5,5,0] and ops=['+','*'] 5+5+0 is a valid expression, while 0+5+0 is not
valid. (too many 0s).
(b) Operations cannot be reused (unless there are other duplicates).
For example, 5+5+0 is not valid because + was used twice.
The function returns a set with all the generated expressions with maximum lenght. (i.e. that contains
all numbers or all operators)
Example: if nums = [5, 0, 5] and ops = ['+', '*', '+'], the function will return the set:
{'0+5+5', '5*5+0',' 0*5+5',' 5+5*0', '5+0*5', '5*0+5', '5+0+5', '5+5+0', '0+5*5'}

"""


def operations(nums,ops):
    expression=str(nums[0])
    sub=build(expression,nums,ops)

    return set(sub)




def build(expression,nums,ops):
    recursive=[]
    for i in range(len(nums[1:])):
        for j in range(len(ops)):
            new_expression= expression+str(ops[j])+str(nums[i])
            new_nums=nums[:i]+nums[i+1:]
            new_ops=ops[:j]+ops[j+1:]
            recursive.append(new_expression)
            build(new_expression,new_nums,new_ops)

    return recursive