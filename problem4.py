# Author: Seil Tekinaeva
# Date: 02/02/2026
# Problem 5
# The program calculates MPG for a car

miles= float(input("Enter the number of miles driven:"))
gallons= float(input("Enter the number of gallons used:"))

if gallons== 0:
    print("Error. Try again!")

else:
    mpg= miles/gallons
    print("Your car's fuel efficiency is:", round(mpg, 2), "MPG")
    
