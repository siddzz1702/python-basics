# Day 3 Project: Simple ATM Simulator
# starting balance

print("=== Welcome to Python Bank ATM ===")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Deposited:", amount)
    print("New balance:", balance)

elif choice == 3:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawn:", amount)
        print("New balance:", balance)
    else:
        print("Insufficient funds!")

elif choice == 4:
    print("Thank you for using Python Bank. Goodbye!")

else:
    print("Invalid choice. Please enter a number between 1 and 4.")
