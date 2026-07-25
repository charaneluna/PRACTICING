# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k
# and nums[i] + nums[j] + nums[k] == 0.


# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.



# this one takes O(n**3) bc there is 3 seperate searches 
def threeSum(l):
    visited=[]
    n = len(l)
    ans = list()
    for i in range(n):
        first = l[i]
        new_l = l[:i]+l[i+1:]
        for k in range(len(new_l)):
            second = new_l[k]
            new_l2 = new_l[:k]+new_l[k+1:]
            for third in new_l2:
                if first+second+third ==0:
                    if sorted([first,second,third]) not in visited:
                        visited.append(sorted([first,second,third]))
                        ans.append([first,second,third])
    return ans


# the better approach is to set the first number and then make two pointers go through the
# sorted list and check the total


def threeSum2(l):
    ans = []
    new_l = sorted(l)
    n = len(l)
    for i in range(n-2):
        left =  i+1
        right = n-1
        total = new_l[i]+new_l[left]+new_l[right]
        while left<= right :
            if total ==0:
                ans.append(sorted([new_l[i],new_l[left],new_l[right]])) if sorted([new_l[i],new_l[left],new_l[right]]) not in ans else None
                left +=1
                right-=1
            elif total <0 :
                left +=1
            else :
                right -=1
        
    return ans


    



print(threeSum2([-1,0,1,2,-1,-4]))