# In Python, variables store a value; conditionals decide whether that value is correct or not. This is called Boolean logic, and it is handled by True or False.

# Example:
v = 1
n = 2
if n == 2:
    print(n + v)
# Here the two values will be added if the condition is true, so the output will be 3.
# We have three conditionals that will help us: if, elif, and else.

# if: if the condition is True, execute the lines inside the if statement.
# elif: If the first 'if' condition is not True, evaluate this other option.
# else: If the previous `if` (and other `elif`s) evaluates to false, execute this.

# Example:
v = 1
n = 2
if n == 4:
    print("n is 4")
elif n == 1:
    print("n is 1")
elif n == 12:
    print("n is 12")
else:
    print("n is", n)
