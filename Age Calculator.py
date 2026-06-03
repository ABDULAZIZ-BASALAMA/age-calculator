from datetime import date
from hijri_converter import Hijri, Gregorian

def calculate_hijri_age():
    print("\n--- 🗓️ Hijri Age Calculator ---")
    try:
        birth_year = int(input("Enter your Hijri birth year (e.g., 1426): "))
        birth_month = int(input("Enter your Hijri birth month (1-12): "))
        birth_day = int(input("Enter your Hijri birth day (1-30): "))
        
        birth_date_hijri = Hijri(birth_year, birth_month, birth_day)
    except ValueError:
        print("❌ Error: Please enter valid numbers and correct Hijri dates.")
        return

    today_gregorian = date.today()
    today_hijri = Gregorian(today_gregorian.year, today_gregorian.month, today_gregorian.day).to_hijri()

    age_years = today_hijri.year - birth_date_hijri.year
    age_months = today_hijri.month - birth_date_hijri.month
    age_days = today_hijri.day - birth_date_hijri.day

    if age_days < 0:
        age_months -= 1
        age_days += 30 

    if age_months < 0:
        age_years -= 1
        age_months += 12

    birth_date_gregorian = birth_date_hijri.to_gregorian()

    print("\n" + "="*40)
    print("🎉 Your current age in Hijri calendar is:")
    print(f" {age_years} years, {age_months} months, and {age_days} days.")
    print("-"*40)
    print("💡 Additional Information:")
    print(f" Your Gregorian birth date is: {birth_date_gregorian.strftime('%Y-%m-%d')} AC")
    print("="*40)


def calculate_gregorian_age():
    print("\n--- 📅 Gregorian Age Calculator ---")
    try:
        birth_year = int(input("Enter your birth year (e.g., 2005): "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_day = int(input("Enter your birth day (1-31): "))
        
        birth_date = date(birth_year, birth_month, birth_day)
    except ValueError:
        print("❌ Error: Please enter valid numbers and correct dates.")
        return

    today = date.today()
    
    age_years = today.year - birth_date.year
    age_months = today.month - birth_date.month
    age_days = today.day - birth_date.day

    if age_days < 0:
        age_months -= 1
        age_days += 30

    if age_months < 0:
        age_years -= 1
        age_months += 12

    birth_date_hijri = Gregorian(birth_year, birth_month, birth_day).to_hijri()

    print("\n" + "="*40)
    print("🎉 Your current age in Gregorian calendar is:")
    print(f" {age_years} years, {age_months} months, and {age_days} days.")
    print("-"*40)
    print("💡 Additional Information:")
    print(f" Your Hijri birth date is: {birth_date_hijri.year}-{birth_date_hijri.month}-{birth_date_hijri.day} AH")
    print("="*40)


def main():
    while True:
        print("\n========================================")
        print("   Welcome to Ultimate Age Calculator   ")
        print("========================================")
        print("1. Calculate Age using Hijri Calendar 🗓️")
        print("2. Calculate Age using Gregorian Calendar 📅")
        print("3. Exit ❌")
        print("----------------------------------------")
        
        choice = input("Select an option (1, 2, or 3): ").strip()
        
        if choice == '1':
            calculate_hijri_age()
        elif choice == '2':
            calculate_gregorian_age()
        elif choice == '3':
            print("\nThank you for using the Age Calculator! Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
