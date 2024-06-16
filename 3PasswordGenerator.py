#  Creating A Random Password Generator

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
