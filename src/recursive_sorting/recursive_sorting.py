# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # merged_arr = sorted(elements)
    merged_arr = sorted(arrA + arrB)

    return merged_arr


# test_array_one = [1, 2, 3]
# test_array_two = [4, 5, 6]
# print(merge(test_array_one, test_array_two))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # we need to split it into two arrays

    if len(arr) > 1:
        lhs = merge_sort(arr[:len(arr)//2])
        rhs = merge_sort(arr[len(arr)//2:])

        arr = merge(lhs, rhs)

    return arr


test_array = [0, 2, 1, 3, 4, 5, 6]
merge_sort(test_array)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
