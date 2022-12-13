# A recursive implementation of binary search. Binary search
# requires that the input list is already in sorted order.
def binary_search(lst, x):
    # If the list has no elements, there is nothing to search for
    if len(lst) == 0:
        return False

    # Find the midpoint of the list and check whether the element
    # we're looking for is there
    midpoint = len(lst) // 2

    # If we found it, great - go ahead and return
    if lst[midpoint] == x:
        return True

    # Otherwise, determine where we need to search next
    if x > lst[midpoint]:
        # If x is greater than the value at the midpoint, we
        # continue searching in the sublist to the right of
        # the midpoint
        return binary_search(lst[midpoint + 1 :], x)
    else:
        # If x is less than the value at the midpoint, we
        # continue searching in the sublist to the left of
        # the midpoint
        return binary_search(lst[:midpoint], x)


lst = [-100, -24, -4, 2, 8, 34, 49, 99, 194]
print(2, binary_search(lst, 2))
print(3, binary_search(lst, 3))
