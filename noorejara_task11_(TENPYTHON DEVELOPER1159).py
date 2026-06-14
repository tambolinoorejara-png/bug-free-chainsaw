# DAY 1 (Variables, Data Types, I/O, Operators)
print("\n")
# Sum of Two Numbers
print("Sum of Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("\n")

# Area of Rectangle
print("Area of Rectangle")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print("Area =", area)
print("\n")

#Simple Interest
print("simple interst")
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
si = (p * r * t) / 100
print("Simple Interest =", si)
print("\n")

#Celsius to Fahrenheit
print("Celsius to Fahrenheit")
c = float(input("Enter Celsius: "))
f = (c * 9/5) + 32
print("Fahrenheit =", f)
print("\n")

#Salary with HRA and DA
print("Salary with HRA and DA")
salary = float(input("Enter Basic Salary: "))
hra = salary * 0.20
da = salary * 0.10
total = salary + hra + da
print("HRA =", hra)
print("DA =", da)
print("Total Salary =", total)
