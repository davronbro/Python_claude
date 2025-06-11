# Task 1: Personal Information

name = "Davron"
age = 24
height_meters = 1.80
is_wroker = True

# Print personal information using f-strings

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height in meters: {height_meters}")
print(f"Is he worker: {is_wroker}")

# Calculate height conversions

height_cm = height_meters * 100
height_feet = height_meters * 3.28084

print(f"Height in meters: {height_meters} m")
print(f"Height in centimeters: {height_cm} cm")
print(f"Height in feet: {height_feet} ft")

feet = int(height_feet)
decimal_part = height_feet - feet
inches = round(decimal_part * 12)
print(f"Height: {feet} ft {inches} in")

# --------------------------------------

# Task 2: Type Conversion

num = 25 + int("125")
conv_float = float(42) / 7
conv_int = int(3.14159)
conv_boolean = bool(0)
convert_boolean = bool("") 

print(num)
print(conv_float)
print(conv_int)
print(conv_boolean)
print(convert_boolean)

# --------------------------------------

# Task 3: String Manipulation

text = "Python programming is fun and useful"

upper_case = text.upper()
lower_case = text.lower()
replaced = text.replace("fun", "amazing")
length = len(text)
split_text = text.split()
substring = text[2:4]   
reversed_word = text[::-1]

print(upper_case, lower_case, replaced, length, split_text, substring, reversed_word)



# --------------------------------------

# Task 4: Data Analysis

# Oylik daromad, xarajat va soliq stavkasi
monthly_income = 3000
monthly_expenses = 2100
tax_rate = 0.20

# Soliq miqdori (oylik)
monthly_tax = monthly_income * tax_rate
#              3000              0.20  = 600 soliq

# Soliqdan keyingi oylik sof daromad
post_tax_income = monthly_income - monthly_tax
#                    3000              600 = 2400 sof foyda

# Tejab qolingan pul (oylik)
monthly_savings = post_tax_income - monthly_expenses
#                    2400              2100 = 300 tejab qolingan pul

# Tejash foizi (oylik sof daromadga nisbatan)
savings_rate = (monthly_savings / post_tax_income) * 100
#                    300              2400 * 100 = 12,5


# Natijalarni chiqaramiz
print("Oylik soliq miqdori:", monthly_tax)
print("Oylik sof daromad:", post_tax_income)
print("Oylik xarajatlar:", monthly_expenses)
print("Oylik tejab qolingan pul:", monthly_savings)
print("Tejash foizi:", round(savings_rate, 2), "%")


# Task 5: Temperature Converter

temp = float(input("Enter temperature value: "))
unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

# Convert based on input unit
if unit == "C":
  # Convert Celsius to Fahrenheit
  converted_temp = (temp * 9/5) + 32
  print(f"{temp}°C is equal to {converted_temp:.1f}°F")
elif unit == "F":
    # Convert Fahrenheit to Celsius
    converted_temp = (temp - 32) * 5/9
    print(f"{temp}°F is equal to {converted_temp:.1f}°C")
else:
    print("Invalid unit. Please enter C or F.")


# Challange BMI calculator

# User's weight (in kilograms) and height (in meters)
weight = float(input("Enter your weight (in kilograms) -> "))
height = float(input("Enter your weight (in meters)-> "))

# BMI formula: weight divided by height squared
bmi = weight / (height ** 2)

# Check which category the BMI falls into
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# Print the result, rounded to 2 decimal places
print("Your BMI is:", round(bmi, 2))
print("Category:", category)







