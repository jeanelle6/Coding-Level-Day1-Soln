                          # Calc


# Goal: Create a program that imitates the behavior of a calculator below. 

"""
Example Output: 
    $ python calc.py
    First number: 5
    Operation: x
    Second number: 2.5
    12.5

Background: 
    Ultimately, computers are machines that preform math operations 
    (though, these operations can make magnificent things happen!). 
    Thus, one simple program we can make is a calculator!

Your Mission: 
    Your goal is to create a calculator in Python! Be sure to support addition (using +), 
    subtraction (using -), multiplication (using x), division (using /), and exponents (using ^)!
    This program should ask the user for a float, followed by an operation, f
    ollowed by another float, then print the result.

More Examples:
    $ python calc.py
    First number: 34.5
    Operation: +
    Second number: 7.5
    42.0

    $ python calc.py
    First number: 3
    Operation: ^
    Second number: 3
    27
    
"""

# Code goes below 

# Get user input for numbers and operation 
fst_num = float(input("First number: "))
operation = input("Operation: ")
snd_num = float(input("Second number: "))

# Calculate final result and print 
if operation == "+": 
    print(fst_num + snd_num)
elif operation == "x": 
    print(fst_num * snd_num)
elif operation == "-":
    print(fst_num - snd_num)
elif operation == "/":
    print(fst_num / snd_num)
else:
    print(fst_num ** snd_num)

