from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and singletonBucketSort functions, and for the BC helper function.
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def singletonBucketSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    """TODO: Implement Radix Sort using BC and singletonBucketSort"""
    # Determine the maximum number in the array to find the max number of digits needed (k)
    max_num = max([elt[0] for elt in arr])
    k = math.ceil(math.log(max_num + 1, base))  # Calculate the number of digits needed

    # Perform sorting for each digit from least significant to most significant
    for digit_idx in range(k):
        # Generate digit-based keys using BC and sort using singletonBucketSort
        # Add (digit, element) pairs based on current digit and pass them to singletonBucketSort
        arr_with_digits = [(BC(elt[0], base, k)[digit_idx], elt) for elt in arr]
        arr = singletonBucketSort(base, arr_with_digits)
        
        # Extract back the sorted elements (removing the temporary digit key)
        arr = [elt[1] for elt in arr]
    return arr
