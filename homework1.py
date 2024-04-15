# CIS 2348 Homework 1 Fall 2020.
# Dwayne Ellis
# Student ID: 
# Birthday Calculator
# Coding Problem 1 - Calculating the age of a person based on current date and the birthday of the user.


# Prompt user for name
name = input("Enter your name:")

# Prompt user for current date
print("Enter current date as (MM/DD/YYYY):")
current_month = int(input('Month:'))
current_day = int(input('Day:'))
current_year = int(input('Year:'))

# Prompt user for their birthday
print("Enter your birthday as (MM/DD/YYYY):")
birthday_month = int(input('Month:'))
birthday_day = int(input('Day:'))
birthday_year = int(input('Year:'))

# Calculate age

age = current_year - birthday_year

# Print entered information

print("Birthday Calculator")
print("Current Date:", current_month, current_day, current_year)
print("Birthday:", birthday_month, birthday_day, birthday_month)
print("Hello", name + "!", "You are", age, "years old."+'\n')


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
