# add two number 
a =float(input("Enter first number: "))
b =float(input("Enter second number: "))
c = a + b
print("The sum is:", c)

# subtract two number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = a - b
print("The difference is:", c)

# multiply two number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = a * b
print("The product is:", c)

#divide two number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if b != 0:
    c = a / b
    print("The quotient is:", c)
else:
    print("Error: Division by zero is not allowed.")

#find the remainder of two number
a = float(input("Enter First number: "))
b = float(input("Enter Second number: "))
if b != 0:
    c = a % b
    print("The remainder is:", c)
else:
    print("Error: Division by zero is not allowed.")
#swap two number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Before swapping :")
print("First number:", a)
print("Second number:", b)
c = a
a = b
b = c

print("After swapping:")
print("First number:", a)
print("Second number:", b)
#Average of two number
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = (a + b) / 2
print("The average is:", c)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
