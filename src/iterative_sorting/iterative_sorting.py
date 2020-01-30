# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        for x in range(i + 1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x

        # TO-DO: swap

        temp = arr[i]
        arr[i] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_was_performed = True
    while swap_was_performed == True:
        swap_was_performed = False

        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swap_was_performed = True
            # else:
            #     swap_was_performed = False

    return arr


# test_list = [1, 2, 4, 3]
# print(bubble_sort(test_list))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
