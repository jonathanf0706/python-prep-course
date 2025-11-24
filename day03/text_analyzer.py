def count_words(text: str) -> int:
    """
    Return the number of words in the text.
    
    Words are separated by any whitespace. Empty strings and strings
    containing only whitespace return 0.
    
    Args:
        text: The input text to analyze.
        
    Returns:
        The number of words in the text.
        
    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("")
        0
        >>> count_words("   ")
        0
    """
    if not text:
        return 0
    return len(text.split())


def count_characters(text: str, include_spaces: bool = False) -> int:
    """
    Return the number of characters in the text.
    
    Args:
        text: The input text to analyze.
        include_spaces: If False, exclude space characters only.
                       Note: Only removes ' ' (space), not other whitespace.
                       Default is False.
        
    Returns:
        The number of characters, optionally excluding spaces.
        
    Examples:
        >>> count_characters("hello world")
        10
        >>> count_characters("hello world", include_spaces=True)
        11
        >>> count_characters("")
        0
    """
    if not text:
        return 0
    
    if not include_spaces:
        # Preserve original behavior: only remove space characters
        text = text.replace(" ", "")
    
    return len(text)


def find_longest_word(text: str) -> str:
    """
    Return the longest word in the text.
    
    If multiple words have the same maximum length, returns the first
    occurrence. Empty strings return an empty string.
    
    Args:
        text: The input text to analyze.
        
    Returns:
        The longest word, or empty string if input is empty/whitespace.
        
    Examples:
        >>> find_longest_word("hello world")
        'hello'
        >>> find_longest_word("")
        ''
        >>> find_longest_word("a bb ccc")
        'ccc'
    """
    if not text:
        return ""
    
    words = text.split()

    return max(words, key=len)

