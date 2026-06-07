def process_expense(expense, current_total):
    try:
        new_expense = int(expense)
        if new_expense < 0:
            print("--> Warning: Negative expense entered. Adjusting ledger...")
        
        # Accumulator Pattern
        updated_total = current_total + new_expense
        return updated_total, True
    except ValueError:
        print("Invalid Input String. Type-Safety enforced.")
        return current_total, False


def run_financial_engine():
    total = 0 
    print("  FINANCIAL LOGIC ENGINE v2.1 ")
    print("Enter your expense amounts below.")
    print("Type 'quit' at any time to halt and review.")
    
    while True:
        expense = input("Enter expense amount: ").strip()
        
        # Sentinel Kill Switch Check
        if expense.lower() == 'quit':
            print("\n[Execution Halted Via Sentinel]")
            break
            
        total, success = process_expense(expense, total)
        if success:
            print(f"Current Running Total: ${total}")
            
    print(f"FINAL TOTAL SPENT: ${total}.00")


if __name__ == "__main__":
    run_financial_engine()