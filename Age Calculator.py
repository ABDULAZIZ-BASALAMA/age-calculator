from datetime import datetime

today = datetime.now()
current_year = today.year
current_month = today.month
current_day = today.day

print("--- Age Calculator ---")

try:
    Y = int(input("Year of birth: "))
    M = int(input("Month of birth: "))
    D = int(input("Day of birth: "))

    birth_date = datetime(Y, M, D)
    
    if birth_date > today:
        print("Error: Date of birth cannot be in the future!")
    else:
        d = current_day
        m = current_month
        y = current_year

        if d < D:
            d += 30
            m -= 1

        if m < M:
            m += 12
            y -= 1

        years = y - Y
        months = m - M
        days = d - D

        print("\n--- Your Age ---")
        print(f"Years: {years}")
        print(f"Months: {months}")
        print(f"Days: {days}")

except ValueError:
    print("Error: Invalid date! Please check the numbers you entered (e.g., Month 1-12, Day 1-31).")
