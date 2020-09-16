# CIS 2348 Homework 1 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 3.18

# Enter measurement
print("Enter wall height (feet):")
w_height = int(input())
print("Enter wall width (feet):")
w_width = int(input())

# Calculate measurements
area = w_height * w_width
print("Wall area: " + str(area) + " square feet")
paint1 = area / 350

# Print output
print("Paint needed: " + '{:.2f}'.format(paint1) + " gallons")
can1 = round(paint1)
print("Cans needed: " + str(can1) + " can(s)")
color = {
    "red": 35,
    "blue": 25,
    "green": 23
}
print("")
print("Choose a color to paint the wall:")
user_color = input()
price = color[user_color] * can1
print("Cost of purchasing " + str(user_color) + " paint: $" + str(price))
