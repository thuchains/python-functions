def calculate_budget(income, rent, food, entertainment):
    
    income = float(input("Enter your monthly income: $"))
    rent = float(input("Enter rent expense: $"))
    food = float(input("Enter food expense: $"))
    entertainment = float(input("Enter entertainment expense: $"))
    total_expenses = rent + food + entertainment
    remaining_money = income - total_expenses

    print("=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Money: ${remaining_money}")

    if remaining_money < 0:
        print("Budget Advice: You're overspending! Cut back on expenses")
    elif remaining_money < 100: 
        print("Budget Advice: Your budget is tight. Be careful with spending.")
    else:
        print("Budget Advice: Great job! You have money left over.")

        