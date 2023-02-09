# Functions Exercises

# 1. Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise
is_two = lambda x: x == 2
is_two(3)
is_two(2)

# 2. Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
is_vowel = lambda x: x.lower() in 'aeiou'
is_vowel('A')

# 3. Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
is_consonant = lambda x: x.lower() not in 'aeiou'
is_consonant('X')
x = 'eat'
is_consonant(x[0])

# 4. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
is_consonant = lambda x: x.lower() not in 'aeiou'
capital_consonant = lambda x: x.capitalize() if is_consonant(x[0]) else f"{x} starts with a vowel"
capital_consonant('ead')

# 5. Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(perc, bill):
    '''
    This function requires 2 positional arguments.
    The first argument should be a percent in decimal form.
    The second argument should be any integer or float value.
    '''
    if perc >= 0 and perc <= 1:
        return perc * bill
calculate_tip(.25, 10) 

# 6. Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original_price, discount_percent):
    '''
    This function takes 2 arguments,
    Argument 1: <float or integer> the original price of an item
    Argument 2: <float> the decimal form a discount
    '''
    if discount_percent >= 0 and discount_percent <= 1:
        return original_price * (1 - discount_percent)
apply_discount(10, .25)

# 7. Define a function named handle_commas. 
    # It should accept a string that is a number that contains commas in it as input, 
    # and return a number as output.
def handle_commas(x = None):
    '''
    This takes a string of numbers and commas as an argument and returns the number without commas as an integer
    '''
    if x == None:
        x = input('please enter a number \n')
    x = x.split(',')
    x = ''.join(x)
    return int(x)
handle_commas('123,0')
handle_commas()

# 8. Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

def get_letter_grade(x):
    '''
    This function takes a number grade (float or integer) as an argument and returns a letter grade
    '''
    if type(x) == str:
        x = int(float(x))
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
    else:
        return 'Not a valid score'    
get_letter_grade('25.5')

# 9. Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(x):
    '''
    This function takes a string as an argument and returns the string without vowels
    '''
    for char in x:
        if char in 'aeiouAEIOU':
            x = x.replace(char, '')
    return x

remove_vowels('chicken')

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
    x = x.strip()
    x = x.replace(' ', '_')
    x = x.lower()
    return x
normalize_name('Ricky Martion.  ')

# 11. Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(ls):
    '''
    This function takes in a lsit as an srgument and returns the cumulative sum as a list
    '''
    ls = [sum(ls[:i+1]) for i, v in enumerate(ls)]
    return ls

cumulative_sum([1, 2, 3])