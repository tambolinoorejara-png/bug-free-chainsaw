# DAY 2(Conditions)
print("\n")

# Positive, Negative or Zero
print("Positive, Negative or Zero")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
print("\n")

# Largest Among Two Numbers
print("Largest Among Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)
print("\n")

#Largest Among Three Numbers
print("Largest Among Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest =", max(a, b, c))
print("\n")

#Even or Odd
print("Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print("\n")

#Leap Year
print("Leap Year")
year = int(input("Enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")
