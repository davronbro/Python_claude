# ----- VARIABLES -----
name = "Alex"       # String
age = 25            # Integer
height = 1.75       # Float
is_student = True   # Boolean

print(name, age, height, is_student)

# ----- NUMBERS -----
# Integers
x = 42
negative = -10
big_num = 1_000_000  # Underscores for readability: 1,000,000


# Floats
pi = 3.14159
scientific = 2.5e6   # 2,500,000


# Complex
complex_num = 3 + 4j


# Operations
sum_result = 5 + 3       # Addition: 8
diff_result = 5 - 3      # Subtraction: 2
product = 5 * 3          # Multiplication: 15
division = 5 / 3         # Division: 1.6666...
floor_div = 5 // 3       # Floor Division: 1
remainder = 5 % 3        # Modulus: 2
power = 5 ** 3           # Exponentiation: 125


# ----- STRINGS -----
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a multi-line string"""


# String operations
concatenation = "Hello" + " " + "World"    # "Hello World"
repetition = "Python " * 3                # "Python Python Python "


# String methods
text = "  Python is amazing  "
length = len(text)                  # 21
upper_case = text.upper()           # "  PYTHON IS AMAZING  "
lower_case = text.lower()           # "  python is amazing  "
stripped = text.strip()             # "Python is amazing"
replaced = text.replace("is", "was")# "  Python was amazing  "
split_text = text.split()           # ["Python", "is", "amazing"]
contains = "Python" in text         # True


# String formatting
name = "Alex"
age = 25
# f-strings (Python 3.6+)
profile = f"Name: {name}, Age: {age}"
# format() method
profile2 = "Name: {}, Age: {}".format(name, age)


# Slicing
word = "Python"
first_char = word[0]      # "P"
substring = word[1:4]     # "yth"
from_third = word[2:]     # "thon"
till_fourth = word[:4]    # "Pyth"
last_char = word[-1]      # "n"
reversed_word = word[::-1]# "nohtyP"


# ----- BOOLEAN -----
is_valid = True
is_invalid = False

# Boolean operations
and_result = True and False  # False
or_result = True or False    # True
not_result = not True        # False


# Comparison operators
equal = (5 == 5)        # True
not_equal = (5 != 10)   # True
greater = (10 > 5)      # True
less = (5 < 10)         # True
greater_equal = (5 >= 5)# True
less_equal = (5 <= 10)  # True


# ----- TYPE CONVERSION -----
int_from_str = int("42")        # 42
float_from_str = float("3.14")  # 3.14
str_from_num = str(42)          # "42"
bool_from_int = bool(1)         # True (0 is False, any other number is True)
int_from_float = int(3.99)      # 3 (truncates, doesn't round)