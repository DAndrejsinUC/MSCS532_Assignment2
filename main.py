import random
from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort the input array using the merge sort algorithm.
    
    Args:
        arr (List[int]): The input array to be sorted
        
    Returns:
        List[int]: The sorted array
    """
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays into a single sorted array.
    
    Args:
        left (List[int]): First sorted array
        right (List[int]): Second sorted array
        
    Returns:
        List[int]: Merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr: List[int]) -> List[int]:
    """
    Sort the input array using the quick sort algorithm.
    
    Args:
        arr (List[int]): The input array to be sorted
        
    Returns:
        List[int]: The sorted array
    """
    if len(arr) <= 1:
        return arr
        
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def generate_number_list(n: int, list_type: str) -> list:
    """
    Generate a list of n numbers based on the specified type.
    
    Args:
        n (int): The number of elements to generate
        list_type (str): Type of list to generate ('ascending', 'descending', or 'random')
        
    Returns:
        list: Generated list of numbers
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
        
    if list_type.lower() not in ['ascending', 'descending', 'random']:
        raise ValueError("list_type must be 'ascending', 'descending', or 'random'")
    
    if list_type.lower() == 'ascending':
        return list(range(1, n + 1))
    elif list_type.lower() == 'descending':
        return list(range(n, 0, -1))
    else:  # random
        return random.sample(range(1, n * 2), n)  # Using n*2 to have a wider range of numbers

# Test the function
def test_number_list():
    print("Testing with n=5:")
    print("\nAscending order:")
    print(generate_number_list(5, 'ascending'))
    
    print("\nDescending order:")
    print(generate_number_list(5, 'descending'))
    
    print("\nRandom order:")
    print(generate_number_list(5, 'random'))

if __name__ == "__main__":
    test_number_list()
