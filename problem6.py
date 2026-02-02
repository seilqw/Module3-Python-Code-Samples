# Author: Seil Tekinaeva
# Date: 02/02/2026
# Problem 7
# The program calculates the return day of the week after a vacation

start_day = int(input("Enter the starting day number (0 = Sunday, 6 = Saturday): "))
nights = int(input("Enter the number of nights you will stay: "))

# %keeps the result between 0 and 6
return_day = (start_day + nights) % 7

print("You will return on day number:", return_day)

