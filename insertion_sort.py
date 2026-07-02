def insertion_sort_descending(arr):
    """
    Sorts a list in monotonically decreasing order using Insertion Sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift elements smaller than key one position to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test_cases = [
        [5, 2, 9, 1, 5, 6, 7, 3],
        [1, 2, 3, 4, 5],          # already ascending
        [5, 4, 3, 2, 1],          # already descending
        [10],                     # single element
        [],                       # empty list
        [3, 3, 3, 3],             # all duplicates
    ]

    for case in test_cases:
        original = case.copy()
        result = insertion_sort_descending(case)
        print(f"Original: {original} -> Sorted (descending): {result}")