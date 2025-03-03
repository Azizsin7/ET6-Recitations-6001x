"""
Problem 3: Black-Box Testing for a Square Root Function
Objective: Identify failing cases using black-box testing and modify the function to handle negative numbers properly.

The function calculates the approximate square root using binary search.
However, it might fail for some edge cases.

Your task:
1. Use **black-box testing** to identify failing cases.
2. Modify the function to handle **negative numbers properly**.
"""

def sqrt(x, eps=0.0001):
    """Returns the approximate square root of x."""
    low, high = 0, x
    guess = (low + high) / 2
    while abs(guess**2 - x) > eps:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2
    return guess

# Test Cases
print(sqrt(25))  # Expected: ~5.0
print(sqrt(0))   # Expected: 0
print(sqrt(-9))  # Expected: ERROR!
