expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = int(input("Enter amount: "))

        expense = {"item": item, "amount": amount}
        expenses.append(expense)

        print("Expense added successfully!")

    
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")

        else:
            print("\n===== YOUR EXPENSES =====")

            for expense in expenses:
                print(expense["item"], "-", expense["amount"])


    
    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total spending:", total)


    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
