import random
import streamlit as st
from streamlit_option_menu import option_menu


def main():
    st.set_page_config(page_title="Password Toolkit",page_icon="🔐")
    with st.sidebar:
        choice = option_menu(
            menu_title="Password Toolkit",
            options=["Password Generator", "Password Validator"],
            menu_icon="tools",
            icons=["key", "shield-lock"],
        )
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
    password = st.text_input("Enter your password ", "password....")
    if st.button("Submit"):
        parameters = check(password)
        count = 0

        if len(password) >= 6:
            st.success("Length is >6")
            count += 1
        else:
            st.error("The length is less than requirement")

        if parameters[0] >= 2:
            st.success("Uppercase present")
            count += 1
        else:
            st.error("Uppercase characters not satisfied  ")

        if parameters[1] >= 2:
            st.success("Lowercase present")
            count += 1
        else:
            st.error("Lowercase characters not satisfied")

        if parameters[2] >= 1:
            st.success("Digits present ")
            count += 1
        else:
            st.error("Numeric characters not satisfied ")

        if parameters[3] >= 1:
            st.success("Special characters present ")
            count += 1
        else:
            st.error("Special characters not satisfied")

        if parameters[4] > 0:
            st.error("Space is present")
        else:
            st.success("No space is found ")
            count += 1

        percent = (count / 6) * 100
        st.progress(int(percent), "STRENGTH")

        if percent == 100:
            st.balloons()


def check(password):
    upper = 0
    lower = 0
    special = 0
    digit = 0
    space = 0

    for i in password:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isdigit():
            digit += 1
        if i.isalnum() == False:
            special += 1
        if i.isspace():
            space += 1
            special -= 1

    return [upper, lower, digit, special, space]


if __name__ == "__main__":
    main()
