def help():
    print(f"\nOption 1: Create New Transaction Record 💵")
    print("This option lets you add a new income or expense transaction.")
    print("You will choose the transaction type, category, and amount before it is saved.")

    print(f"\nOption 2: Create New Asset Record 💰")
    print("This option lets you record non-spendable assets such as fixed deposits or investments.")
    print("You will enter the asset name, type, and amount for storage.")

    print(f"\nOption 3: Update Value of Existing Asset 💹")
    print("This option lets you update an existing asset's value without editing the database manually.")
    print("You can select the asset by ID and enter a new amount for it.")
    print("This is especially useful for assets whose values change over time.")

    print(f"\nOption 4: Manage Existing Transactions 📝")
    print("This option lets you view, edit, or delete transactions that already exist.")
    print("You can choose to view all transactions or filter them by year, month, or day.")
    print("After selecting a transaction by ID, you can review its details, delete it, or edit its amount, type, or category.")

    print(f"\nOption 5: View Historical Data 🕒")
    print("This option shows historical transaction data for a selected month.")
    print("You can choose between a summary view, raw data view, or both.")
    print("When raw data is shown, you can also export the results as a CSV file.")

    print(f"\nOption 6: View Financial Status 🗽")
    print("This option presents a concise summary of your current financial standing.")
    print("It includes your net asset value, spendable balance, and a breakdown of your assets.")

    print(f"\nOption 7: Explain Me! 😣")
    print("You are here right now😂")

    print(f"\nOption 8: Get Me Out of Here! 🚪")
    print("This option exits the program.")

    print(f"\nImportant❗: Do not delete storage.db or assets.db files created by the program, as they contain all transaction and asset records.")
