def min_cost(l, current_idx, arr):
    n = len(l)
    cost = l[current_idx]
    if current_idx == n-1: # I am done
        arr[current_idx] = cost
        return cost
    ans = cost + min_cost(l, current_idx+1, arr)# I am sure I can make one step forward
    if current_idx + 3 < n:
        ans = min(ans, cost + min_cost(l, current_idx+3, arr))
    arr[current_idx] = ans
    return ans


# def path_cost(l, current_idx):
#     """returns the minimal cost of going from the current_index index to the last."""
#     if current_idx == len(l)-1:
#         return l[current_idx]
#     if current_idx + 3 < len(l):
#         return l[current_idx] + min(path_cost(l, current_idx+1), path_cost(l, current_idx+3))
#     return l[current_idx] + path_cost(l, current_idx+1)


def solve(l):
    """returns the minimal cost of going from the first index to the last."""
    arr = [-1]*len(l)
    ans = min_cost(l, 0, arr)
    print(arr)
    return ans


def dynamic(l):
    n = len(l)
    path = list(range(n))
    ans = [-1]*n
    pos = n-1
    answer = []
    
    for i in range(3):
        ans[i] = sum(l[:i+1])
        path[i] = i-1
    for i in range(3, n):
        ans[i] = l[i] + min(ans[i-1], ans[i-3])
        path[i] = i-1 if ans[i-1] < ans[i-3] else i-3
    while(pos >= 0):
        answer.append(pos)
        pos = path[pos]
        
    return list(reversed(answer))

  
    
if __name__ == "__main__":
    l1 = [5,2,8]
    l2 = [4,10,1,1,100]
    l3 = [7,100,100,1,7,7]
    print(dynamic(l3))
  