import random
import sys
import streamlit as st

#https://passwordgeneratorandvalidatorfirstprogram.streamlit.app/
def main():
    st.title("Password Generator and Validator")
    

    while True:
        choice=st.selectbox("MENU",["Password Generator","Password Validator"])
        if choice=="Password Generator":
            length=int(get_length())
            password=generate_password(length)
            st.success(f"your password is {password}")
        elif choice=="Password Validator":
            validator()



def get_length():
    return st.slider("Select the level", 0, 50)
        


def generate_password(len):
    password = ""

    for i in range(len):
        ascii_value = random.randint(32, 126)
        password += chr(ascii_value)
    return password


def validator():
    st.write(
        """This password validation is based on certain conditions 
             1. uppercase letters >2
             2. lowercase letters >2
             3. special characters >2
             4. digits >2
             5. length >12
             Based on these parameters you will get the strength of the password in percent
             
          """
    )
    password = st.text_input("Enter your password ","password....")

    count = check(password)
    percent = (count / 5) * 100

    
    st.success(f"your password is {percent}% strong ")

    if percent < 50:
        st.error("use our password generator to make your password even stronger ")


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
