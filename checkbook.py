# import modules
import csv
import os

# establish function for turning strings into floats
def money_machine(x):
    '''
    This function takes a us currency string as an argument and returns the string with only valid python identifiers
    '''
    # reassign the string stripped of trailing spaces
    x = x.strip()
    # reassign the string with the spaces replaced with nothing
    x = x.replace(' ', '')
    # reassign the string with the $ replaced with nothing
    x = x.replace('$', '')
    # reassign the string with commas removed
    x = x.replace(',', '')
    # reassigns the string as a float
    x = float(x)
    return x

# create a function to view balance
def view_balance():
    with open('checkbook.csv', 'r') as f:
            contents = csv.DictReader(f, fieldnames=fields)
            lines = [line for line in contents][1:]
    current_balance = lines[-1]['balance']
    return print(f"Your current balance is: ${current_balance} \n")

# create a function to record withdrawals from an account or debit transactions
def debit():
    with open('checkbook.csv', 'r') as f:
            contents = csv.DictReader(f, fieldnames=fields)
            lines = [line for line in contents][1:]
    debit_amnt = input('How much would you like to withdraw? ')
    if debit_amnt.isdigit() == False:
        print(f'{debit_amnt} is not a valid input \n')
        return
    debit_amnt = money_machine(debit_amnt)
    if float(lines[-1]['balance']) - debit_amnt  < 0:
        overdraft = input('Your account will go into the negative.\nWould you like to continue? (y/n) ')
        if overdraft.lower() == 'y':
            with open('checkbook.csv', 'a') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writerow(
                {
                    'type': 'debit',
                    'amount': debit_amnt,
                    'balance': round(float(lines[-1]['balance']) - float(debit_amnt), 2)
                })
            with open('checkbook.csv', 'r') as f:
                contents = csv.DictReader(f, fieldnames=fields)
                lines = [line for line in contents][1:]
            new_balance = lines[-1]['balance']
            return print(f"Your new balance is: ${new_balance} \n")
        elif overdraft.lower() == 'n':
            return
    else:
        with open('checkbook.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writerow(
                {
                    'type': 'debit',
                    'amount': debit_amnt,
                    'balance': round(float(lines[-1]['balance']) - float(debit_amnt), 2)
                })
        with open('checkbook.csv', 'r') as f:
            contents = csv.DictReader(f, fieldnames=fields)
            lines = [line for line in contents][1:]
        new_balance = lines[-1]['balance']
        return print(f"Your new balance is: ${new_balance} \n")
    
# a function to record deposits to an account ledger or credit added
def credit():
    with open('checkbook.csv', 'r') as f:
        contents = csv.DictReader(f, fieldnames=fields)
        lines = [line for line in contents][1:]
    credit_amnt = input('How much would you like to deposit? ')
    if credit_amnt.isdigit() == False:
            print(f'{credit_amnt} is not a valid input \n')
            return
    elif credit_amnt.isdigit():
            credit_amnt = money_machine(credit_amnt)
    with open('checkbook.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow(
            {
                'type': 'credit',
                'amount': credit_amnt,
                'balance': float(lines[-1]['balance']) + credit_amnt 
            })
    with open('checkbook.csv', 'r') as f:
        contents = csv.DictReader(f, fieldnames=fields)
        lines = [line for line in contents][1:]
    new_balance = lines[-1]['balance']
    return print(f'Your new balance is ${new_balance} \n')

# Transaction history function
def transaction_history():
    with open('checkbook.csv', 'r') as f:
        contents = csv.DictReader(f, fieldnames=fields)
        lines = [line for line in contents][1:]
    print('Below is your transaction history\n')
    for line in lines:
        print(line)
    return 

# exiting function
def goodbye():
    return print('~~~ Thank you for using the terminal checkbook! ~~~') 

# function for the checkbook
def terminal_checkbook():
    while True:
        # the introductory screen that asks the user what they would like to do
        print('What would you like to do?\n\n 1) view current balance\n 2) record a debit (withdraw)\n 3) record a credit (deposit)\n 4) transaction history\n 5) exit \n')
        choice = input('Your choice? ')
        # adding controls in case someone enters an invalid 
        if choice.isdigit() == False:
            print('Please enter a number')
            continue
        elif choice.isdigit():
            choice = int(choice)
        if choice > 5 or choice < 1:
            print('Invalid choice: ', choice, '\n')
        elif choice == 1:
            view_balance()
        elif choice == 2:
            debit()
        elif choice == 3:
            credit()
        elif choice == 4:
            transaction_history()
        elif choice == 5:
            goodbye()
            break
    return

# initializing needed variables
fields = ['type', 'amount', 'balance']
dict_base = {
    'type': 'new checkbook',
    'amount': 0,
    'balance':0
}
if os.path.exists('checkbook.csv'):
    print('~~~ Welcome to your terminal checkbook ~~~')
    terminal_checkbook()
else: 
    # initial setup
    with open('checkbook.csv', 'w') as f:
        # the variable writer holds the csv
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        # this inserts the base information into csv file needed for the future functions to operate
        writer.writerow(dict_base)
    terminal_checkbook()
