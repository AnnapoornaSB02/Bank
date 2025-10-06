initial_balance = float(input("Enter initial balance: ₹"))
deposit = float(input("Enter deposit amount: ₹"))

new_balance = initial_balance + deposit

print(f"\nInitial Balance: ₹{initial_balance}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{new_balance}")

withdraw = float(input("Enter amount to withdraw: ₹"))

final_balance = balance_after_deposit - withdraw


print(f"Withdraw: ₹{withdraw}")
print(f"Final Balance: ₹{final_balance}")
