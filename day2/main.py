# Data Types

# String
print("Hello"[4])

print("123" + "345")

# integer
print(123 + 345)

# float
print(type(3.14159))

#Boolean
True
False

print(round(8/3))

score = 0
height = 1.8
isWinning = True

# f-string
print(f"your score is {score}, your height is {height},you are winning is {isWinning}")

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# format the result to 2decimal places = 33.60
# Tip:There are 2 ways to round a number.You might have to do some googling to solve this.
# write your code below this line


# Tip calculator
print("Welcome to the tip calculator.")
bill_amount = float(input("What was the total bill?"+" "+"$"))
tip_percent = int(input("What percentage tip would you like to give? 10,12, or 15? "))
how_many_way_split = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round( (bill_amount + bill_amount  * (tip_percent/100))/how_many_way_split,2)}")


