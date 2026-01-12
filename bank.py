import sys

if len(sys.argv) == 6:
    script_name = sys.argv[0]
    acc_holder = sys.argv[1]
    acc_number = sys.argv[2]
    acc_type = sys.argv[3]
    balance = float(sys.argv[4])
    transaction = float(sys.argv[5])
else:
    script_name = sys.argv[0]
    acc_holder = "Nilesh Pawar"
    acc_number = "35155838037"
    acc_type = "Savings"
    balance = 15000
    transaction = -3000

print("Script Name:", script_name)
print("Account Holder Name:", acc_holder)
print("Account Number:", acc_number)
print("Account Type:", acc_type)
print("Initial Balance:", balance)
print("Transaction Amount:", transaction)

if transaction > 0:
    balance = balance + transaction
    status = "Deposit Successful"
elif transaction <= balance:
    balance = balance + transaction
    status = "Withdrawal Successful"
else:
    status = "Transaction Failed - Insufficient Balance"
print("Transaction Status:", status)
print("Updated Balance:", balance)
