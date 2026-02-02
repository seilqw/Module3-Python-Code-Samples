# Author: Seil Tekinaeva
# Date: 02/02/2026
# Problem 3
# The program greets only predifined names

name= input("What is your name? ")
instructor_name= "Zoe"
name_clean= name.strip() .lower()
instructor_clean= instructor_name.strip() .lower()
if name_clean== "seil" or name_clean== instructor_clean:
    print("Hello,", name.strip() + "!")
else:
    print("You are not on a greeting list.")
