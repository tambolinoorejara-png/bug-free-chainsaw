# DAY 3 (Loops)
print("\n")
# Print 1 to 100
print("Print 1 to 100")
for i in range(1, 101):
    print(i)
print("\n")

# Even Numbers 1 to 100
print("Even Numbers 1 to 100")
for i in range(2, 101, 2):
    print(i)
print("\n")

#Sum of First N Natural Number
print("Sum of First N Natural Number")
n = int(input("Enter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum =", total)
print("\n")

#Multiplication Table
print("Multiplication Table")
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)
print("\n")

#Factorial
print("Factorial")
n = int(input("Enter number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)
