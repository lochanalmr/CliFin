from shared import init_assets_db, init_db


def view_current_financial_status():
    print("\nView Financial Status")

    conn = init_db()
    c = conn.cursor()
    c.execute("SELECT amount, type FROM storage")
    rows = c.fetchall()
    conn.close()

    total_income = 0.0
    total_expenses = 0.0
    for amount, transaction_type in rows:
        normalized_type = transaction_type.lower()
        if normalized_type == 'income':
            total_income += abs(amount)
        elif normalized_type == 'expense':
            total_expenses += abs(amount)

    spendable_balance = total_income - total_expenses

    print(f"Spendable balance: LKR {spendable_balance:.2f}")

    asset_conn = init_assets_db()
    asset_cursor = asset_conn.cursor()
    asset_cursor.execute("SELECT name, asset_type, amount FROM assets ORDER BY created_at")
    asset_rows = asset_cursor.fetchall()
    asset_conn.close()

    asset_totals = {}
    for _, asset_type, amount in asset_rows:
        asset_totals[asset_type] = asset_totals.get(asset_type, 0.0) + abs(amount)

    print("Other assets:")
    if asset_rows:
        for asset_type, total in sorted(asset_totals.items()):
            print(f"- {asset_type}: LKR {total:.2f}")
    else:
        print("- None")

    other_assets_total = sum(asset_totals.values())
    net_asset_value = spendable_balance + other_assets_total
    print(f"Total other assets: LKR {other_assets_total:.2f}")
    print(f"Estimated net asset value: LKR {net_asset_value:.2f}")
    return
