# ## Conditional Basics

# ##### a. Prompt the user for a day of the week, print out whether the day is Monday or not

monday = input('What day of the week is it? ')

if monday.lower() == 'monday':
    print('Today is Monday!')
else:
    print('Today is not Monday :/')

monday


# #### b. Prompt the user for a day of the week, print out whether the day is a weekday or a weekend

week_end_day = input('What day of the week is it?')
weekend = ['saturday', 'sunday']

if week_end_day.lower() in weekend:
    print('It\'s the freakin weekend')
else:
    print(f'It\'s {week_end_day}, get to work lackey')

week_end_day


# #### c. Create variables and make up values for:
#     The number of hours worked in one week
#     The hourly rate
#     How much the week's paycheck will be
# Write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours.

weekly_hours_worked = 999
hourly_rate = .10
paycheck = 0
if weekly_hours_worked > 40:
    paycheck = ((weekly_hours_worked - 40) * hourly_rate * 1.5) + (40 * hourly_rate)
else:
    paycheck = weekly_hours_worked * hourly_rate
    
paycheck


# Create an integer variable i with a value of 5. Create a while loop that runs so long as i is less than or equal to 15. Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1


# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

twos = 0

while twos <= 100:
    print(twos)
    twos += 2


# Alter your loop to count backwards by 5's from 100 to -10

take_five = 100
while take_five >= -10:
    print(take_five)
    take_five += -5


# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. 

squared = 2

while squared <= 1000000:
    print(squared)
    squared = squared ** 2


# Write a loop that uses print to create the output shown below.

take_five_again = 100

while take_five_again >= 5:
    print(take_five_again)
    take_five_again += -5


# ### For Loops

# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that numbe

number = int(input('I\'m begging for a number '))
times_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in times_ten:
    print(f'{number} x {n} = {number * n}')


# Create a for loop that uses print to create the output shown below.

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for n in int_list:
    print(n *str(n))


# ### break and continue

# Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

pos_int = int(input('Please enter a whole number greater than 0'))

while pos_int > -1:
    print(pos_int)
    pos_int += -1
    if pos_int == 0:
        break


# #### The input function can be used to prompt for input and use that input in your python code. Prompt the user to enter a positive number and write a loop that counts from 0 to that number. (Hints: note that the input function returns a string, so you'll need to convert this to a numeric type.)

counter = 0 
pos_number = int(input('Please enter a positive number'))
while pos_number: 
    print(counter)
    counter += 1
    if pos_number < 1:
        print('Please try again with a positive number')
    if counter > pos_number:
        break


# #### Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

numbers = list(range(51))
odd_numbers = [number for number in numbers if number % 2 == 1]
print(valid_answers)
while True:
    q = input('Please enter an odd number from 1 to 50: ')
    if q.isdigit():
        q = int(q)
        if q < 51 and q > 0:
            break

for i in odd_numbers:
    if i != q:
        print(f'Here is an odd number: {i}')
    else:
        print(f'Yikes! Skipping Number: {i}')


# ### Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.
# Write a program that prints the numbers from 1 to 100

numbers = list(range(101))
numbers.pop(0)

for number in numbers:
    print(number)

# For multiples of three print "Fizz" instead of the number

for number in numbers:
    if number % 3 == 0:
        print('Fizz')
    else:
        print(number)

# For the multiples of five print "Buzz".

for number in numbers:
    if number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
        
# For the multiuples of five and three print "FizzBuzz".

for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


# ### Display a table of powers.
#  Prompt the user to enter an integer
#  Display a table of squares and cubes from 1 to the value entered
#  Ask if the user wants to continue
#  Assume that the user will enter valid data
#  Only continue if the user agrees to

from prettytable import PrettyTable
enter = int(input('What number would you like to go up to? '))
# from prettytable import PrettyTable
# t = PrettyTable(['Name', 'Age'])
# t.add_row(['Alice', 24])
# t.add_row(['Bob', 19])
# print(t)

t = PrettyTable(['number', 'squared', 'cubed'])
for i in range(enter + 1):
    if i == 0:
        continue
    t.add_row([i, i ** 2, i**3])
print(t)


# ### Convert given number grades into letter grades.
# Prompt the user for a numerical grade from 0 to 100
# Display the corresponding letter grade
# Prompt the user to continue
# Assume that the user will enter valid integers for the grades
# The application should only continue if the user agrees to
# Grade Ranges:
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

a = list(range(88, 101))
b = list(range(80, 88))
c = list(range(67, 80))
d = list(range(60, 67))
f = list(range(0, 60))
grades_dict = [{'A': a}, {'B': b}, {'C': c}, {'D': d}, {'F': f}]

while True:
    user_score = int(input('Please enter your score: '))
    for grades in grades_dict:
        for grade in grades:
            for scores in grades[grade]:
                if user_score == scores:
                    print(grade)
    if user_score < 0 or user_score > 100:
        print('The score entered is invalid')
    cont = input('Would you like to continue? Type \'y\' or \'n\' and press enter')
    if cont.lower() == 'n':
        break


# Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

books = [
    {'title': 'interesting book1', 'author': 'great author1', 'genre': 'fascinating'},
    {'title': 'interesting book2', 'author': 'great author2', 'genre': 'fascinating'},
    {'title': 'interesting book3', 'author': 'great author3', 'genre': 'fascinating'},
    {'title': 'interesting book4', 'author': 'great author4', 'genre': 'fascinating'}]
q = input('What\'s your favorite genre? (Hint: type \'fascinating\') ')
for i in books:
    for k in i:
        if q == i[k]:
            print(i['title'])

