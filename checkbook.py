# importing required modules
import csv
import os


fields = ['type', 'amount', 'balance']
dict_base = {
    'type': None,
    'amount': 0,
    'balance':0
}

# A Function for amount validity
def valid_amnt(amnt):
    '''
    This function checks input to ensure it is a number based on the US dollar system. 
    It will return true if all conditions are met. These conditions include:
        Only accepts digits which may include a decimal
        All entries must include at least 1 digit
        No more than 2 digits after the decimal
    '''
    # with the split on the '.' valid input will have 2 elements in the list 
    input_check = amnt.split('.')
    # more than 2 elements in the input_check list means there are too many decimals (US standards)
    if len(input_check) > 2:
        print(f'{amnt} is not a valid input \n')
        return False
    # a one element list is a single string and can be checked later for digits
    elif len(input_check) != 1:
        # The last element will only having 2 characters ~ 3 characters for cents is 1 dollar
        if len(input_check[-1]) > 2:
            print(f'{amnt} is not a valid input \n')
            return False
    if amnt == '.':
        print(f'{amnt} is not a valid input \n')
        return False
    if amnt == '':
        print(f'{amnt} is not a valid input \n')
        return False
    # each character is checked to see if it is either a digit or a decimal place
    for char in amnt:
        # if the character is a digit or a '.' then it is a valid character for input (possibilities of more than 1 '.' have been ruled out previously)
        if char.isdigit() or char == '.':
            continue
        # a blank else statement would be suitable, but in case of oversight I specify that non-digits and non-'.' are not valid
        elif char.isdigit() == False and char != '.':
                print(f'{amnt} is not a valid input \n')
                return False
    return True

def view_balance():
    '''
    This function returnd the last recorded balance from the checkbook.csv file
    '''
    # open the cheeckbook.csv file for reading and alias it as f
    with open('checkbook.csv', 'r') as f:
        # the information read from f as dictionaries is stored in the variable contents 
        contents = csv.DictReader(f, fieldnames=fields)
        # a list comprehension places the dictionaries held in the contents variable into a the variable lines
        lines = [line for line in contents][1:]
    # the value for the key 'balance' in the last dictionary of the list lines is assigned to the variable current_balance
    current_balance = lines[-1]['balance']
    # a message with the current balance is returned to the user
    return print(f"Your current balance is: ${current_balance} \n")

def debit():
    '''
    This function:
        1. Asks for user input (a US dollar amount)
        2. Checks the input for validity
            2.1 Exits the function when certain conditions are not met (see valid_amnt())
        3. Updates a csv file with a new debit record entry
            3.1 The debit record subtracts the user input from the last balance recorded to create an updated balance
        4. Displays a new balance
    '''
    # a variable that prompts the user for input to be recorded
    amnt = input('How much would you like to withdraw?\nPlease only enter numbers and a decimal when necessary. \n')
    # the user input is run in the valid_amnt function to check for vthe validity needed for credit to operate    
    if valid_amnt(amnt):
        # amnt is converted to float to be used in mathematical operations later 
        amnt = float(amnt)
        # the information read from f as dictionaries is stored in the variable contents
        with open('checkbook.csv', 'r') as f:
            # the information read from f as dictionaries is stored in the variable contents 
            contents = csv.DictReader(f, fieldnames=fields)
            # a list comprehension places the dictionaries held in the contents variable into a the variable lines
            lines = [line for line in contents][1:]
        # opens the csv file for appending and aliases it as f
        with open('checkbook.csv', 'a') as f:
            # the ability to append a dictionary to the csv file is added to the writer variable
            writer = csv.DictWriter(f, fieldnames=fields)
            # the method .writerow is called to append a dictionary as a row to f
            writer.writerow(
                {
                    'type': 'debit',
                    # the user input will be used as the value attached to the 'amount' key
                    'amount': amnt,
                    # the key 'balance' value is the difference of the last balance and the user input 
                    'balance': float(lines[-1]['balance']) - amnt
                })
        # opens the newly appended checkbook.csv for reading
        with open('checkbook.csv', 'r') as f:
            contents = csv.DictReader(f, fieldnames=fields)
            lines = [line for line in contents][1:]
        # the last balance entered is called (the newly updated one) and assigned to the variable new_balance
        new_balance = lines[-1]['balance']
        # the function is exited and the updated balance is displayed for user info
        return print(f"Your new balance is: ${new_balance} \n")
    # when a user inputs an invalid amount, the function will exit
    else:
        return

def credit():
    '''
    This function:
        1. Asks for user input (based on US dollar system)
        2. Checks the input for validity
            2.1 Exits the function when certain conditions are not met (see valid_amnt())
        3. Updates a csv file with a new credit record entry
            3.1 The credit record adds the user input to the last balance recorded to create an updated balance
        4. Displays the updated balance from the new record entry
    '''
    amnt = input('How much would you like to deposit? \nPlease only enter numbers and a decimal when necessary. \n')
    # the user input is run in the valid_amnt function to check for vthe validity needed for credit to operate
    if valid_amnt(amnt):
        # amnt is converted to float to be used in mathematical operations later 
        amnt = float(amnt)
        # opens the csv file for reading and aliases as f
        with open('checkbook.csv', 'r') as f:
            # the information read from f as dictionaries is stored in the variable contents 
            contents = csv.DictReader(f, fieldnames=fields)
            # a list comprehension places the dictionaries held in the contents variable into a the variable lines
            lines = [line for line in contents][1:]
        # opens the csv file for appending and aliases it as f
        with open('checkbook.csv', 'a') as f:
            # the ability to append a dictionary to the csv file is added to the writer variable
            writer = csv.DictWriter(f, fieldnames=fields) 
            # the method .writerow is called to append a dictionary as a row to f
            writer.writerow(
                {
                    'type': 'credit',
                    # the user input will be used as the value attached to the 'amount' key
                    'amount': amnt,
                    # the last balance recorded is called and converted to a float then added to the amount for a new balance
                    'balance': float(lines[-1]['balance']) + amnt 
                })
        # opens the newly appended checkbook.csv for reading
        with open('checkbook.csv', 'r') as f:
            contents = csv.DictReader(f)
            lines = [line for line in contents]
        # the last balance entered is called (the newly updated one) and assigned to the variable new_balance
        new_balance = lines[-1]['balance']
        # the function is exited and the updated balance is displayed for user info
        return print(f'Your new balance is ${new_balance} \n')
    # when a user inputs an invalid amount, the function will exit
    else:
        return

def transaction_history():
    ''' '''
    with open('checkbook.csv', 'r') as f:
        contents = csv.DictReader(f, fieldnames=fields)
        lines = [line for line in contents][1:]
    print('Below is your transaction history\n')
    for line in lines:
        print(line)
    return     

def goodbye():
    ''' 
    This function prints a statement to the user
    '''
    return print('~~~ Thank you for using the terminal checkbook! ~~~') 

def terminal_checkbook():
    '''
    This function creates an interactive checkbook ledger with options for the user to select from 
    '''
    # a while loop is used to continuously prompt the user until they chose to exit
    while True:
        # the introductory screen that asks the user what they would like to do and returns a user to this initial screen when other options are completed
        print('What would you like to do?\n\n 1) view current balance\n 2) record a debit (withdraw)\n 3) record a credit (deposit)\n 4) view transaction history\n 5) exit \n')
        choice = input('Your choice? ')
        # adding controls in case someone enters an invalid 
        if choice.isdigit() == False:
            print('Please enter a number')
            continue
        elif choice.isdigit():
            choice = int(choice)
        if choice > 4 or choice < 1:
            print('Invalid choice: ', choice, '\n')
        elif choice == 1:
            # allows a user to view their last balance
            view_balance()
            cont = input('Would you like to continue? Enter \'y\' or \'n\' \n')
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                goodbye()
                break 
            else:
                print('Invalid entry. You are being redirected to the home screen. \n') 
        elif choice == 2:
            # allows a user to record a debit or withdrawal
            debit()
            cont = input('Would you like to continue? Enter \'y\' or \'n\' \n')
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                goodbye()
                break 
            else:
                print('Invalid entry. You are being redirected to the home screen. \n')
        elif choice == 3:
            # allows a user to record a credit or deposit
            credit()
            cont = input('Would you like to continue? Enter \'y\' or \'n\' \n')
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                goodbye()
                break 
            else:
                print('Invalid entry. You are being redirected to the home screen. \n')
        elif choice == 4:
            transaction_history()
            cont = input('Would you like to continue? Enter \'y\' or \'n\' \n')
            if cont.lower() == 'y':
                continue
            elif cont.lower() == 'n':
                goodbye()
                break 
            else:
                print('Invalid entry. You are being redirected to the home screen. \n')              
        elif choice == 5:
            # returns a user a goodby message and exits the loop and the function
            goodbye()
            break
    return

# initializing needed variables
fields = ['type', 'amount', 'balance']
dict_base = {
    'type': None,
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
