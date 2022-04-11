# Implementation of binary search algorithm 

# Prove that binary search is faster than naive search 

# Naive search: scan entire list and ask if its equal to the target
# if yes, return the index 
# if no, then return -1

def naive_search(l, target):
    # example l = [2, 4, 6, 4, 6, 8, 3, 5]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer
# leverage the fact that the list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
        
    # example l = [3, 5, 7, 9, 10, 34, 45, 67, 78, 89, 90] # should return 5
    midpoint = (low + high) // 2 # 2
    
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
