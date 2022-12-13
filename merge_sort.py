
# A recursive implementation of merge sort. It is nondestructive.
def merge_sort(lst):
    # Base case: A list with one or fewer
    # elements is already sorted
    if len(lst) <= 1:
        return lst

    # Find the start, end, and midpoint of the list
    midpoint = len(lst) // 2
    start = 0
    end = len(lst)

    # Recursively sort the left and right sides of the list
    left = merge_sort(lst[start:midpoint])
    right = merge_sort(lst[midpoint:end])

    # Now that we are guaranteed that the left and right sides are sorted,
    # we can merge them together.
    output = []
    while len(left) > 0 and len(right) > 0:
        # If the smallest left value is smaller than the smallest right value,
        # add it to our output list
        if left[0] < right[0]:
            output.append(left.pop(0))
        # Otherwise, add the smallest right value
        else:
            output.append(right.pop(0))

    # At the end of this process, either left or right may still contain
    # values. Since they are in sorted order, we can just add them to
    # the output list as-is.
    output.extend(left)
    output.extend(right)

    return output

lst = [13, 2, 13, 3, 5, 7, -100, 243, 3]
print(merge_sort(lst))


# def search(lst, x):
#     print(lst)
#     if len(lst) == 0:
#         return False

#     midpoint = len(lst) // 2

#     if lst[midpoint] == x:
#         return True

#     if x > lst[midpoint]:
#         return search(lst[midpoint+1:], x)
#     else:
#         return search(lst[:midpoint], x)

# print(search(lst, 5))
