"""EX04 - 'list' Utility Functions."""
__author__ = "730523434"

def all(xs: list[int], a: int) -> bool:
    """Returns True if all numbers in the list match the given number, False otherwise or if the list is empty."""
    if len(xs) == 0:
        return False
    
    for x in xs:
        if x != a:
            return False
    
    return True

def max(input: list[int]) -> int:
    """Returns the largest number in the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest = input[0]  # Initialize largest with the first element
    for num in input:
        if num > largest:
            largest = num

    return largest

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if each number at each index is equal in both lists and if not, returns False."""
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True