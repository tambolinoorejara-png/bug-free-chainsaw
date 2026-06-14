# DAY 4 (Functions)
print("\n")
# Square of a Number
print("Square of a Number")
def square(n):
    return n * n
num = int(input("Enter number: "))
print("Square =", square(num))
print("\n")

# Maximum of Two Numbers
print("Maximum of Two Numbers")
def maximum(a, b):
    return max(a, b)
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Maximum =", maximum(x, y))
print("\n")

#Simple Interest Function
print("Simple Interest Function")
def simple_interest(p, r, t):
    return (p * r * t) / 100
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
print("Simple Interest =", simple_interest(p, r, t))
print("\n")

#Even or Odd Function
print("Even or Odd Function")
def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print(check(n))
print("\n")

#Area of Circle
print("Area of Circle")
def area_circle(r):
    return 3.14 * r * r

radius = float(input("Enter radius: "))
print("Area =", area_circle(radius))
