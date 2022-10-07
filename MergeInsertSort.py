import time
import numpy as np


N = 8


def merge(A, p, q, r):
    """Merge two sorted sublists/subarrays to a larger sorted sublist/subarray.
    Arguments:
    A -- a list/array containing the sublists/subarrays to be merged
    p -- index of the beginning of the first sublist/subarray
    q -- index of the end of the first sublist/subarray;
    the second sublist/subarray starts at index q+1
    r -- index of the end of the second sublist/subarray
    """
    # start_time_merge = time.time()
    # Copy the left and right sublists/subarrays.
    # If A is a list, slicing creates a copy.
    if type(A) is list:
        left = A[p: q + 1]
        right = A[q + 1: r + 1]
    # Otherwise a is a np.array, so create a copy with list().
    else:
        left = list(A[p: q + 1])
        right = list(A[q + 1: r + 1])

    i = 0  # index into left sublist/subarray
    j = 0  # index into right sublist/subarray
    k = p  # index into a[p: r+1]

    # Combine the two sorted sublists/subarrays by inserting into A
    # the lesser exposed element of the two sublists/subarrays.

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    # After going through the left or right sublist/subarray, copy the
    # remainder of the other to the end of the list/array.
    if i < len(left):  # copy remainder of left
        A[k: r + 1] = left[i:]
    if j < len(right):  # copy remainder of right
        A[k: r + 1] = right[j:]

    # end_time_merge = time.time()
    # print("Execution Merge Time: --- %s seconds ---" % (end_time_merge - start_time_merge))


def merge_sort(A, use_insertion_sort=False, p=0, r=None):
    """Sort the elements in the sublist/subarray a[p:r+1].
    Arguments:
    A -- a list/array containing the sublist/subarray to be merged
    p -- index of the beginning of the sublist/subarray (default = 0)
    r -- index of the end of the sublist/subarray (default = None)
    """

    # If r is not given, set to the index of the last element of the list/array.
    if r is None:
        r = len(A) - 1
    if p >= r:  # 0 or 1 element?
        return

    portion = (r - p) + 1

    if use_insertion_sort and portion < N:
        # print('Smaller : ' + str(r - p))
        insertion_sort(A, p, portion)
        return

    q = (p + r) // 2  # midpoint of A[p: r]
    merge_sort(A, use_insertion_sort, p, q)  # recursively sort A[p: q]
    merge_sort(A, use_insertion_sort, q + 1, r)  # recursively sort A[q+1: r]
    merge(A, p, q, r)  # merge A[p: q] and A[q+1: r] into A[p: r]


def merge_sort_helper(A, use_insertion_sort=False, p=0, r=None):
    start_time_sort = time.time()
    merge_sort(A, use_insertion_sort)
    end_time_sort = time.time()
    print("Execution Sort Time: --- %s seconds ---" % (
        end_time_sort - start_time_sort))  # input should be bigger to avoid error of time mesurement


def insertion_sort(A, start, n):
    """Sort a list or numpy array.
    Argument:
    A -- a list or numpy array
    start -- start index in A
    n -- portion size in A
    """
    # Traverse the list or array from index 1 to n-1.
    # print("Insert : start : " + str(start) + " portion : "+ str(n))
    for i in range(1, n):
        key = A[start + i]

        # Insert A[i] into the sorted subarray a[0:i].
        # Compare stored key with the already sorted values to its left.
        # Move each item one position to the right until we find the
        # position for the key or fall off the left end of the list or array.
        j = i - 1
        while j >= 0 and A[start + j] > key:
            A[start + j + 1] = A[start + j]
            j -= 1

        # Insert key at the correct position in the list or array.
        A[start + j + 1] = key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Pythan')
    # list1 = [11, 1, 51, 1, 5, 3]
    input = np.random.randint(-5000, 5000, size=10000)
    print("Input Size : " + str(input.size))

    list1 = np.copy(input)
    list1test = list(list1)
    print("vanilla MergeSort")
    merge_sort_helper(list1)
    # print(list1)
    # print(list1 == sorted(list1test))

    list2 = np.copy(input)
    list2test = list(list2)
    print("MergeSort + InsertionSort for N : " + str(N))
    merge_sort_helper(list2, use_insertion_sort=True)
    # print(list2)
    # print(list2 == sorted(list2test))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
