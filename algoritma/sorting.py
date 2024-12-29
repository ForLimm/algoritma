#Muhammad Haliim
#F55123012

# PSEUDOCODE
# BUBBLE_SORT(arr):
#     n = length(arr)
#     FOR i FROM 0 TO n-1:
#         FOR j FROM 0 TO n-i-2:
#             IF arr[j] > arr[j+1]:
#                 SWAP arr[j] AND arr[j+1]
#     RETURN arr

# MERGE_SORT(arr):
#     IF length(arr) > 1:
#         mid = length(arr) // 2
#         L = arr[0:mid]       
#         R = arr[mid:length(arr)]  

#         MERGE_SORT(L)
#         MERGE_SORT(R)
#     
#         i = j = k = 0
#         WHILE i < length(L) AND j < length(R):
#             IF L[i] < R[j]:
#                 arr[k] = L[i]
#                 i = i + 1
#             ELSE:
#                 arr[k] = R[j]
#                 j = j + 1
#             k = k + 1

#         WHILE i < length(L):
#             arr[k] = L[i]
#             i = i + 1
#             k = k + 1

#         WHILE j < length(R):
#             arr[k] = R[j]
#             j = j + 1
#             k = k + 1

#     RETURN arr

import random
import time

# Function to generate random array
def generate_random_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

# Main program
if __name__ == "__main__":
    # Generate 100 random integers between 1 and 1000
    X = generate_random_array(100, 1, 1000)

    # Measure execution time for Bubble Sort
    start_bubble = time.time()
    sorted_bubble = bubble_sort(X.copy())
    end_bubble = time.time()
    print("Bubble Sort Result:")
    print(sorted_bubble)
    print(f"Bubble Sort Time: {end_bubble - start_bubble:.6f} seconds")

    # Measure execution time for Merge Sort
    start_merge = time.time()
    sorted_merge = merge_sort(X.copy())
    end_merge = time.time()
    print("\nMerge Sort Result:")
    print(sorted_merge)
    print(f"Merge Sort Time: {end_merge - start_merge:.6f} seconds")
