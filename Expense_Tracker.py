print("--- Smart Student Expense Tracker ---")

expense_report = {
    "Food": 0.0,
    "Transport": 0.0,
    "Entertainment": 0.0,
    "Studies": 0.0,
    "Other": 0.0
}

print("Categories: 1. Food | 2. Transport | 3. Entertainment | 4. Studies | 5. Other")
print("(Type 'done' at any time to print the final report)\n")

while True:
    choice = input("Choose category number (1-5) or 'done': ").strip()
    
    if choice.lower() == 'done':
        break
        
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice! Please choose a number from 1 to 5.")
        continue
        
    try:
        amount = float(input("Enter amount (SAR): "))
        if amount < 0:
            print("Amount cannot be negative!")
            continue
            
        if choice == '1':
            expense_report["Food"] += amount
        elif choice == '2':
            expense_report["Transport"] += amount
        elif choice == '3':
            expense_report["Entertainment"] += amount
        elif choice == '4':
            expense_report["Studies"] += amount
        elif choice == '5':
            expense_report["Other"] += amount
            
        print("Expense added successfully!\n")
        
    except ValueError:
        print("Please enter a valid number for the amount!\n")
        
        
print("\n===============================")
print("     FINAL EXPENSE REPORT      ")
print("===============================")
total_all = 0
for category, total_amount in expense_report.items():
    print(f"- {category}: {total_amount} SAR")
    total_all += total_amount
print("-------------------------------")
print(f"TOTAL SPENT: {total_all} SAR")
print("===============================")
