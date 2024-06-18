# TASK 3

# Creating A Random Password Generator 
# It is a useful tool that generates random passwords for users.
# In this project i have created a password generator usin Python, allowing users to 
# specify the length of password, and after it the randomly generated password will be displayed on screen


import random
import string

print("Hello We Wll create a random password for need")


def pswrd():
    len = int(input("Enter the length of PASSWORD you want : "))

    lowC = string.ascii_lowercase
    uppC = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    combine = lowC + uppC + digits + symbols

    x = random.sample(combine, len)

    password = "".join(x)
    print(password)
    pswrd()


pswrd()
