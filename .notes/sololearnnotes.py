""" Basic concepts """

## Simple Operations ##

print(2 + 2)
print(5 + 4 - 3)

print(2*(3+4)) # Use asterisk (*) to indicate multiplication.
print(10 / 2)  # Use forward slash (/) to indicate division.

print(11 / 0) # Dividing by zero in Python produces an error.

## Floats (/) (integers) (1.0)

print(3 / 4) # Floats are used in Python to represent numbers that aren't integers (whole numbers). ex. 0.5 and -7.8237591.
# A float is also produced by running an operation on two floats, or on a float and an integer.
print(6 * 7.0)
print(4 + 1.65)

## Exponentiation (**)

print(2 ** 5) # Exponentiation is performed using 2 asterisks.
print(9 ** (1/5))

## Quotient (//)

print(20 // 6) # Floor division is done using two forward slashes (//) and is used to determine the quotient of a division (the quantity produced by the division of two numbers).
print(6 // 20.0)# You can also use Floor division on Floats.

## Remainder (%)

print(20 % 6) # The "modulo operator" is carried out with a percent symbol (%) and is used to get the remainder of a division.
print(1.25 % 0.5)

## Strings ##

print("Python is fun!") # A String is created by entering text between two single ('') or double ("") quotation marks.
print('Always look on the bright side of life')

## Backlash (\)

print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!') # Some characters can't be directly included in a string, For instance, double quotes ("") can't be directly included in a double quote string. (""); this would cause it to end prematurely. Characters like these must be escaped by placing a backlash (\) before them. Double quotes ("") only need to be escaped in double quote ("") strings, and the same is true for single quote ('') strings.
# Backlashes (\) can be also used to escape tabs, arbitrary Unicode characters, and various other things that can't be reliably printed.

## Newlines(\n)

print('One \nTwo \nThree') # \n represents a new line. It can be used in strings to create multi'ine output.                       
# Newlines will be automatically added for strings that are created using three quotes ("""string""")
print("""this
is a
multiline
text""")

## String operations ##

## Concatenation (str + str) (str * n)

print("Spam" + 'eggs') # As with integers and floats, strings in Python can be added, using a process called concatenation, which can be done on any two (2) strings.
print("2" + "2") # Even if your string contaions numbers, they are still added as strings rather than integers.
# Strings can also be multiplied by integers. This produces a repeated version of the original string. The order of the string and the intger doesn't matter, but the string usually comes first.
print("Spam" * 3)
print(4 * '2') 
# Strings can't be multiplied by other strings.
# Strings also can't be multiplied by floats, even if the floats are whole numbers.

## Variables ##

# A variable allows you to store a value by assigning it to a name, which can be used to refer to the value later in the program.
user = "Joey" # To assign a variable use one (1) equal sign (=)

# You can use variables to perform corresponding operations, just as you did with numbers and strings.
x = 7
print(x)

print(x + 3)
print(x)

# Variables can be assigned as many times as you want, in order to change their value in Python, variables don't have specific types;
# So you can assign a string to a variable, and later assign an integer to the same variable.
x = 123.456
print(x)

x = "This is a string"
print(x + "!")

# However, it is not good practice. To avoid mistakes, try to avoid overwriting the same variable with different data types.

## Variable names

# Certain restrictions apply in regard to the characters that may be used in Python variable names.
# The only characters that are allowed are letters, numbers, and underscores. Also, they can't start with numbers.

this_is_a_normal_name = 7

123abc = 7
SyntaxError: invalid syntax # Not following these rules result in errors.

## del statements (del)

# You can use the del statement to remove a variable, which means the reference from the next value is deleted, and trying to use the variable causes an error.

foo = 3
del foo
print(foo)
NameError: the name 'foo' is not defined

# Deleted variables can be reassigned to later as normal.

foo = 2
bar = 3
del bar
bar = 8
print(foo * bar)
# Outputs: 16

## Input ##



