# An iterative implementation of linear search. The list can
# be in any order
def linear_search(lst, x):
    # This is a simple algorithm: Just iterate through the list
    # and return True if we find what we're looking for
    for i in lst:
        if i == x:
            return True
    
    # Otherwise, return False
    return False


lst = [32, 9, 103, -22, -59, 1, 300, 2]
print(2, linear_search(lst, 2))
print(3, linear_search(lst, 3))
