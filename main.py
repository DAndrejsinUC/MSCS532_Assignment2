import random

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
