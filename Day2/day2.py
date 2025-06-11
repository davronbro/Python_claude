# Day 2: Variables and Data Types

# Core Concepts: Variables and Data Types
# Variables in Python

# Think of variables as labeled containers for storing data. In Python, creating variables is straightforward:

name = "Alex"
age = 25

# Key points about Python variables:

  # No declaration needed before assignment
  # Dynamic typing (type can change during execution)
  # Case-sensitive (age and Age are different variables)
  # Names can contain letters, numbers, and underscores (cannot start with a number)
  # Some names are reserved (like if, for, while) and can't be used as variable names

#---------------------------

# Python's Basic Data Types

# Numbers:
  # Integers (int): Whole numbers without decimals
  # Floating-point (float): Numbers with decimal points
  # Complex (complex): Numbers with real and imaginary parts


# Strings (str):
  # Text enclosed in quotes (single, double, or triple quotes)
  # Immutable (cannot be changed after creation)
  # Can be indexed and sliced like name[0] (first character) or name[1:3] (characters from index 1 to 2)

#--------------------------

# Type Conversion (Casting)
# Python allows converting between data types:

int() # - Convert to integer
float() # - Convert to floating-point
str() # - Convert to string
bool() # - Convert to boolean

x = int("42")   # String to integer: 42
y = float(42)   # Integer to float: 42.0
z = str(42)     # Integer to string: "42"

# -------------------------

# String Operations and Methods
  # Strings in Python have many built-in methods  

    # upper(), lower() -  Change case
    # strip() - Remove whitespace
    # replace(old, new) - Replace substrings
    # split(separator) - Split string into list
    # len(string) - Get length of string (not a method but a function)

# -------------------------

# Practical Examples

# Number operations
num1 = 10
num2 = 3.5
result = num1 + num2  # 13.5 (float)

print(result)

# String manipulation
first_name = "Python"
last_name = "Developer"
full_name = first_name + " " + last_name  # "Python Developer"
greeting = f"Hello, {full_name}!"  # f-strings for formatting

print(greeting)

# String methods
text = "  python is amazing  "
cleaned_text = text.strip()  # "python is amazing"
uppercase_text = text.upper()  # "  PYTHON IS AMAZING  "
replaced_text = text.replace("amazing", "awesome")  # "  python is awesome  "

print(cleaned_text, uppercase_text, replaced_text)

#--------------------------

# F-strings (Formatted String Literals)
# F-strings provide an elegant way to embed expressions inside string literals:

name = "Alex"
age = 25
profile = f"Name: {name}, Age: {age}, Birth Year: {2025 - age}"

print(profile)








