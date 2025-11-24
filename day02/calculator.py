def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divide one number by another.

    Args:
        a (float or int): The dividend.
        b (float or int): The divisor (must not be zero).

    Returns:
        float: The result of dividing a by b.

    Raises:
        TypeError: If either a or b is not a number (int or float).
        ValueError: If b is zero.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be numbers (int or float).")
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(divide(5, 3))
