import random
import sys
import streamlit as st

#https://passwordgeneratorandvalidatorfirstprogram.streamlit.app/
def main():
    st.title("Password Generator and Validator")
    st.text(
        """\t\t\t menu
              1. password generator 
              2. password validator 
              3. exit from the program
          """
    )

    while True:
        choice = input("Enter the choice ")
        print()
        if int(choice) == 1:
            len = int(get_length())
            password = generate_password(len)

            print(f"\nyour password is {password}\n")

        elif int(choice) == 2:
            validator()

        elif int(choice) == 3:
            print("Exiting from the program... ")
            sys.exit()
        else:
            print("Enter a valid choice ... ")


def get_length():
    while True:
        length = input("Enter the length ")
        if length.isdigit():
            return length
        else:
            print("invalid length .... ")


def generate_password(len):
    password = ""

    for i in range(len):
        ascii_value = random.randint(32, 126)
        password += chr(ascii_value)
    return password


def validator():
    print(
        """This password validation is based on certain conditions 
             1. uppercase letters >2
             2. lowercase letters >2
             3. special characters >2
             4. digits >2
             5. length >12
             Based on these parameters you will get the strength of the password in percent
             
          """
    )
    password = input("Enter your password ")

    count = check(password)
    percent = (count / 5) * 100

    print()
    print(f"your password is {percent}% strong ")

    if percent < 50:
        print("use our password generator to make your password even stronger ")


def check(password):
    upper = 0
    lower = 0
    special = 0
    digit = 0

    for i in password:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isdigit():
            digit += 1
        if i.isalnum() == False:
            special += 1

    count = 0
    if upper > 2:
        count += 1
    if lower > 2:
        count += 1
    if special > 2:
        count += 1
    if digit > 2:
        count += 1
    if len(password) > 12:
        count += 1

    return count


if __name__ == "__main__":
    main()
