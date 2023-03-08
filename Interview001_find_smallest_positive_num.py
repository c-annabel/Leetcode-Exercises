# Find the smallest positive number missing from an unsorted array
# Test run of the coding question

import math

def solution(A):  # Our original array

    # m = max(A)  # Storing maximum value
    # if m < 1:
    #     # In case all values in our array are negative
    #     return 1
    # if len(A) == 1:
    #     # If it contains only one element
    #     return 2 if A[0] == 1 else 1
    # l = [0] * m
    # print(l)
    # for i in range(len(A)):
    #     if A[i] > 0:
    #         if l[A[i] - 1] != 1:
    #             # Changing the value status at the index of our list
    #             l[A[i] - 1] = 1
    # for i in range(len(l)):
    #
    #     # Encountering first 0, i.e, the element with least value
    #     if l[i] == 0:
    #         return i + 1
    #         # In case all values are filled between 1 and m
    # return i + 2

    if max(A) < 1:
        return 1

    if len(A) == 1:
        return 2 if A[0] == 1 else 1

    A.sort()
    sorted_a = A.copy()

    avg = math.ceil(len(sorted_a)/2)

    mini_number = 0
    for i in range(1, sorted_a[avg]):
        if i not in sorted_a:
            mini_number = i
            return mini_number

    if mini_number == 0:
        for i in range(sorted_a[avg], max(A)+1):
            if i not in sorted_a:
                mini_number = i
                return mini_number

    return max(A)+1


# Driver Code
if __name__ == '__main__':
    # arr = [3, 7, 2, -10, -20]
    arr = [1, 3, 6, 4, 12, 2]
    # arr = [30, 15, 10, 44, 55, 6]
    print(solution(arr))