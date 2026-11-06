# personal_calculator.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("\nHello, {}!".format(name))
print(f"Your age is {age}.")

print(f"\nAddition: {first_number + second_number:g}")
print(f"Subtraction: {first_number - second_number:g}")
print(f"Multiplication: {first_number * second_number:g}")

if second_number != 0:
    print(f"Division: {first_number / second_number}")
else:
    print("Division: Cannot divide by zero.")
