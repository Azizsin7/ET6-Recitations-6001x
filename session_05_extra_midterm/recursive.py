"""Write a recursive Python function, given a non-negative integer N,
to calculate the no. of occurrences of digit 7 in N.
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.
"""
def count7(N):
    """
    Recursively counts the number of times digit 7 appears in the integer N.
    
    Parameters:
    N (int): A non-negative integer
    
    Returns:
    int: The count of digit 7 in N
    """
    if N == 0:  # Base case: if the number is 0, stop recursion
        return 0
    elif N % 10 == 7:  # If the last digit is 7, add 1 and recurse on the rest
        return 1 + count7(N // 10)
    else:  # Otherwise, just recurse on the rest
        return count7(N // 10)

# Example test cases
print(count7(1237123))  # Output: 1
print(count7(717))      # Output: 2
print(count7(77777))    # Output: 5
print(count7(0))        # Output: 0
print(count7(7897897))  # Output: 3
