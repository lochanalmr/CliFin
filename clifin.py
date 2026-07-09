from shared import VERSION
from greeting import ensure_and_greet_user
from transactions import data_entry, data_read
from assets import add_asset_entry, update_asset_value
from financial_status import view_current_financial_status
from help_module import help


if __name__ == '__main__':
    ensure_and_greet_user()
    print(f"You are currently running CliFin v{VERSION}")
    while True:
        print("\nMain Menu")
        print("1. Create New Transaction Record 💵")
        print("2. Create New Asset Record 💰")
        print("3. Update Value of Existing Asset 💹")
        print("4. View Historical Data 🕒")
        print("5. View Financial Status 🗽")
        print("6. Get Me Out of Here! 🚪")
        print("7. Explain Me! 😣")

        choice = input("Choose an option (1, 2, 3, 4, 5, 6, or 7): ").strip()

        if choice == '1':
            data_entry()
        elif choice == '2':
            add_asset_entry()
        elif choice == '3':
            update_asset_value()
        elif choice == '4':
            data_read()
        elif choice == '5':
            view_current_financial_status()
        elif choice == '7':
            help()
        elif choice == '6':
            print("Thank you for using CliFin!😎")
            input("Press [Enter] to exit.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

