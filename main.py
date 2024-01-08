import random
import streamlit as st


def main():
    st.sidebar.title("Password Toolkit")
   

    choice = st.sidebar.selectbox("MENU", ["Password Generator", "Password Validator"])
    if choice == "Password Generator":
        st.title("Password Generator")
        length = int(get_length())
        if st.button("submit"):
            password = generate_password(length)
            st.info(f"your password is {password}")
    elif choice == "Password Validator":
        st.title("Password Validator")
        validator()


def get_length():
    return st.number_input("Enter the length", 0)


def generate_password(len):
    password = ""

    for i in range(len):
        ascii_value = random.randint(32, 126)
        password += chr(ascii_value)
    return password


def validator():
    st.text(
        """This password validation is based on certain conditions
             1. uppercase letters >2
             2. lowercase letters >2
             3. special characters >2
             4. digits >2
             5. length >12
             Based on these parameters you will get the strength of the password in percent
             
          """
    )
    password = st.text_input("Enter your password ", "password....")
    if st.button("Submit"):
        count = check(password)
        percent = (count / 5) * 100

        if percent <= 30:
            st.error(f"your password is too weak (STRENGTH= {percent}%)")
        elif percent <= 70:
            st.warning(f"your password is weak (STRENGTH= {percent}%)")
        elif percent > 70:
            st.success(f"your password is strong (STRENGTH= {percent}%)")


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
