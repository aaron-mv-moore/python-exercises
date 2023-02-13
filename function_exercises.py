# Functions Exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise
# This function will determine if the input is the number 2. The input must be an integer
is_two = lambda x: x == 2 or x == '2' # edit: forgot to accept strings

# The following two lines are to test the function
is_two(3)
is_two(2)

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
# this function will allow us to see if the string passed is a vowel. The string should be a single character and is not case sensitive 
# added more conditions to ensure user input does not break code
is_vowel = lambda x: x.lower() in 'aeiou' if type(x) == str and len(x) == 1 else False
is_vowel('A')

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
# this function is being created to detect consonants. .lower() allows the input to not be case sensitive. 
# edited to include more conditions to make the function more robust
is_consonant = lambda x: x.lower() not in 'aeiou' if type(x) == str and len(x) == 1 and x.isalpha() == True else False
# Testing the funtion
is_consonant('X')
x = 'eat'
is_consonant(x[0])

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

capital_consonant = lambda x: x.capitalize() if is_consonant(x[0]) else f"{x} starts with a vowel"
capital_consonant('ead')

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(perc, bill):
    '''
    This function requires 2 positional arguments.
    The first argument should be a percent in decimal form.
    The second argument should be any integer or float value.
    '''
    # This conditional ststement is used to ensure the first argument is a percent in decimal form
    if perc >= 0 and perc <= 1:
        # if the condition  is met, the function excutes and returns the tip amount
        return perc * bill
calculate_tip(.25, 10) 

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percent):
    '''
    This function takes 2 arguments,
    Argument 1: <float or integer> the original price of an item
    Argument 2: <float> the decimal form a discount
    '''
    # this condition is to ensure the argument entered is a percentage in decimal form
    if discount_percent >= 0 and discount_percent <= 1:
        # The function will return the new price after the discoutn is applied
        return original_price * (1 - discount_percent)
apply_discount(10, .25)

# 7. Define a function named handle_commas. 
    # It should accept a string that is a number that contains commas in it as input, 
    # and return a number as output.
def handle_commas(x = None):
    '''
    This takes a string of numbers and commas as an argument and returns the number without commas as an integer
    '''
    # this condition is in case someone doesn't enter anything. this input will define x
    if x == None:
        x = input('please enter a number \n')
    # split the string at each comma and place the remaining numbers in a list
    x = x.split(',')
    # rejoin all the strings in the list with no commas
    x = ''.join(x)
    # return the string as an integer
    return int(x)
# testing the function
handle_commas('123,0')

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    '''
    This function takes a number grade (float or integer) as an argument and returns a letter grade
    '''
    # this converts a string argument to an integer
    if type(x) == str:
        x = int(float(x))
    # for each condtion, a specific letter will be returned that corresponds with the condition
    if x >= 0 and x < 60:
        return 'F'
    elif x < 70:
        return 'D'
    elif x < 80:
        return 'C'
    elif x < 90:
        return 'B'
    elif x < 101:
        return 'A'
    # if none of the conditions are met, the user will be notified that the argument entered is not valid for its use
    else:
        return 'Not a valid score'    
get_letter_grade('25.5')

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    '''
    This function takes a string as an argument and returns the string without vowels
    '''
    # create a loop to individually check each character in the string
    for char in x:
        # a condition to check each character or element is a vowel
        if char in 'aeiouAEIOU':
            # if the condition is met, the character will be replaced with nothing
            x = x.replace(char, '')
    # after each character replaced or ignored, the edited string is returned
    return x
remove_vowels('chicken')

# another solution
def remove_vowels2(x):
    new_x = ''
    for char in x:
        if is_vowel(char):
            continue
        else:
            new_x += char
    return new_x
remove_vowels2('chicken')

# another solution
def remove_vowels3(x):
    new_x = [char for char in x if is_vowel(char) == False]
    return ''.join(new_x)
remove_vowels3('chicken')

# 10. Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
    # anything that is not a valid python identifier should be removed
    # leading and trailing whitespace should be removed
    # everything should be lowercase
    # spaces should be replaced with underscores
    # for example:
        # Name will become name
        # First Name will become first_name
        # % Completed will become completed

def normalize_name(x):
    '''
    This function takes a string as an argument and returns the string with only valid python identifiers
    '''
    # reassign the string stripped of trailing spaces
    x = x.strip()
    # reassign the string with the spaces replaced with underscores
    x = x.replace(' ', '_')
    # reassign the string with all characters in lower case
    x = x.lower()
    return x
normalize_name('Ricky Martion.  ')

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

list1 = [1, 2, 3, 4, 5]

def cumulative_sum(ls):
    # create a blank list for the values to be placed in
    ls1 = []
    # enumerate the entered list to get indices
    for i, v in enumerate(ls):
        # add the first index alone because you cannot becasue you cannot call a value 
        # from a ls1 becasue it has no values
        if i == 0:
            ls1.append(ls[i])
        # for all other values
        else:
            # we will add the value associated with the currently looping index
            # to the previous value placed in the new list
            ls1.append(ls[i] + ls1[i-1])
    # finally, the list will be pushed to the user
    return ls1

    
def cumulative_sum1(ls):
    '''
    This function takes in a lsit as an argument and returns the cumulative sum as a list
    '''
    # a list comrpehension that enumerates the list(provides the index and element value)
    # the index number is assigned to variable i
    # the sum function is adding the first element value up to the the element value the loop is currently on 
    # this is achieve using the the index number + 1 becasue when calling for a range of indexes it is up to 
    # but not including the number
    ls = [sum(ls[:i+1]) for i, v in enumerate(ls)]
    return ls

cumulative_sum1(list1)