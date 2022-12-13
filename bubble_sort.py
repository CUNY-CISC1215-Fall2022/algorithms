# An iterative implementation of bubble sort. It is destructive.
def bubble_sort(lst):
    # Continue looping until we have not swapped any elements of the list
    swapped = True
    while swapped:
        # One iteration of bubble sort: Iterate through the list and see if
        # there are any pairs of elements we need to reorder
        swapped = False

        for i in range(len(lst) - 1):
            # If we encounter a sequential pair of elements in the wrong order,
            # swap them
            if lst[i + 1] < lst[i]:
                swapped = True
                tmp = lst[i + 1]
                lst[i + 1] = lst[i]
                lst[i] = tmp


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, -99]

bubble_sort(lst)
print(lst)


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
