from typing import List, Set


def find_duplicates(lst: List) -> List:
    """
    Finds and returns a list of elements that appear more than once in the list.
    
    The function preserves the original order in which each element first appeared.
    
    Args:
        lst: A list of elements (any type)
    
    Returns:
        A list of elements that appear at least twice, in the order of their first appearance
    
    Example:
        >>> find_duplicates([1, 2, 3, 2, 4, 3, 5, 3, 2])
        [2, 3]
        >>> find_duplicates(['a', 'b', 'a', 'c', 'b', 'a'])
        ['a', 'b']
        >>> find_duplicates([1, 2, 3])
        []
    """
    seen: Set = set()
    duplicates: List = []
    
    for item in lst:
        if item in seen:
            # If we've already seen the item and it's not yet in the duplicates list
            if item not in duplicates:
                duplicates.append(item)
        else:
            # Mark the item as seen
            seen.add(item)
    
    return duplicates


from typing import Dict
from collections import Counter

def count_characters(text: str) -> Dict[str, int]:
    """
    Counts the frequency of each character in the given text.

    Args:
        text: A string of text

    Returns:
        A dictionary with characters as keys and their frequencies as values.
        Returns an empty dictionary if the string is empty.
    """
    if not text:
        return {}
    return dict(Counter(text))
# Improvements:
# - Used proper type hints with 'Dict[str, int]' explicitly imported.
# - Handled edge case for empty string, returning empty dict immediately.
# - Used collections.Counter for a more concise and pythonic approach.
# - Converted Counter to dict for exact return type as in the original.


# The error happens because in Python, a single equals sign '=' is used for assignment,
# not for comparison. To compare values (like checking if b is zero), you need a double equals '=='.

def safe_divide(a, b):
    if b == 0:  # <-- This line caused the error; it should use '==' for comparison
        return "cannot divide"
    return a / b

safe_divide(5, 3)

