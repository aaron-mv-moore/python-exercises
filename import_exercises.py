from function_exercises import calculate_tip

# calling the function to calculate the tip
calculate_tip(.25,10)

# printing the results
print(calculate_tip(.25,10))

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