# 5. You have rented some movies for your kids:
    # The Little Mermaid for 3 days
    # Brother Bear for 5 days
    # Hercules for 1 day
# If the daily fee to rent a movie is 3 dollars, how much will you have to pay?
mermaid_lngth = 3
bear_lngth = 5
herc_lngth = 1
daily_fee = 3
total_cost = daily_fee * (mermaid_lngth + bear_lngth + herc_lngth)
print(f"I will have to pay ${total_cost} for my rented movies.")

# 6. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.
# They pay you the following hourly rates:
    # Google: 400 dollars
    # Amazon: 380 dollars
    # Facebook: 350 dollars
# This week you worked: 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
# How much will you receive in payment for this week?
g_rate = 400        
a_rate = 380
f_rate = 350
g_hours = 6
a_hours = 4
f_hours = 10
g_pay = g_rate * g_hours
a_pay = a_rate * a_hours
f_pay = f_rate * f_hours
total_pay = g_pay + a_pay + f_pay

print(f'I will receive ${total_pay} this week in gross pay.')

# 7. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
students_enrolled = 12
max_enrollment = 15
class_enrollment_status = students_enrolled / max_enrollment
print(class_enrollment_status)
stud_schedule = {'Monday', 'Tuesday', 'Wednesday', 'Friday'}
class_schedule = {'Thursday'}
class_schedule.intersection(stud_schedule)

if class_enrollment_status < 1 and class_schedule.intersection(stud_schedule) != class_schedule:
    print('Congrats, you can enroll in the class')
else:
    print('Sorry, you can\'t enroll')

# 8. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
items_bought = int(input('How many items did you buy? Please enter a whole number.'))
offer_expired = input('Is the offer expired? Please enter T or F')
prem_member = input('Are you a premium member? Please enter T or F')

if prem_member.lower() == "f" and items_bought > 2 and offer_expired.lower() == "f":
    print('Offer approved')
elif prem_member.lower() == "t" and offer_expired.lower() == "f":
    print('Offer approved')
else:
    print('Sorry, we cannot approve this offer')


# 9. Create a variable that holds a boolean value for each of the following conditions:
    # The password must be at least 5 characters
    # The username must be no more than 20 characters
    # The password must not be the same as the username
    # Bonus Neither the username or password can start or end with whitespace
username = 'codeup'
password = 'notastrongpassword'

login_info_check = (len(password) >= 5) and (len(username) < 21) and (username != password) and ((username.startswith(' ') == False) and (username.endswith(' ') == False)) and ((password.startswith(' ') == False) and (password.endswith(' ') == False))
print(login_info_check)
