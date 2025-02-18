"""
Created on Fri Feb  7 08:32:12 2025

@author: somai
Problem 2: Calculate the Sum of the First N Natural Numbers (Using a Loop)
Explanation:
We want to calculate the sum of the first n natural numbers (1 + 2 + 3 + ... + n). This can be done by iterating from 1 to n and keeping track of the cumulative sum.

Concepts Covered:

For loops
Accumulator variables (total)
Instructions:
Write a function sum_n_iterative(n) that takes a positive integer n as input and returns the sum of the first n natural numbers.
Inside the function:
Initialize a variable total to 0.
Use a for loop to iterate from 1 to n.
In each iteration, add the current number to total.
Return the final value of total.
Test the function with several values of n (e.g., 5, 10, 100).
"""
def sum_n_iterative(n):
    """Returns the sum of the first n natural numbers using a loop."""
    total = 0  # Initialize the accumulator variable to store the sum

    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        total += i  # Add the current number i to total

    return total  # Return the final sum
# Test cases
print(sum_n_iterative(5))   # Output: 15
print(sum_n_iterative(10))  # Output: 55
print(sum_n_iterative(100)) # Output: 5050

