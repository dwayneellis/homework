# CIS 2348 Homework 1 Fall 2020.
# Dwayne Ellis
# Student ID: 0833810
# Lab 5.19

# Output menu of automotive services with corresponding cost
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
    "-": 0
}
# Prompt user for two services from the menu
print("")
print("Select first service:")
first_service = input()
print("Select second service:")
second_service = input()

# Output an invoice for services selected
print("")
print("Davy's auto shop invoice")
print("")
if first_service == "-":
    print("First Service : No service")
else:
    print("First Service : " + str(first_service) + ", $" + str(services[first_service]))
if second_service == "-":
    print("Second Service : No service")
else:
    print("Second Service : " + str(second_service) + ", $" + str(services[second_service]))
print("")
total = services[first_service] + services[second_service]
print("Total: $" + str(total))
