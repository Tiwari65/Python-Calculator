# Display the calculator menu
print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Take the user's operation choice
choice = int(input("Enter your choice (1-4): "))

# Get two numbers from the user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# Perform the selected operation
if choice == 1:
    print("Addition:", num1 + num2)

elif choice == 2:
    print("Subtraction:", num1 - num2)

elif choice == 3:
    print("Multiplication:", num1 * num2)

elif choice == 4:
    # Check to avoid division by zero
    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Can't divide by 0.")

# Handle invalid menu choices
else:
    print("Invalid choice.")