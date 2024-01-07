# Password ToolKit

https://passwordgeneratorandvalidatorfirstprogram.streamlit.app/

This Python application leverages the Streamlit library to provide a user-friendly web interface for password generation and validation. Whether you need a strong, randomly generated password or want to assess the strength of an existing one, this toolkit has you covered.

## Features:
  ### 1.Password Generator
  Generate secure passwords with ease by specifying the desired length. The generator ensures a mix of uppercase letters, lowercase letters, digits, and special characters.

  ### 2.Password Validator
  Evaluate the strength of your password based on specific criteria, including the number of uppercase letters, lowercase letters, special characters, digits, and overall length. The application provides a strength 
  percentage and categorizes passwords as too weak, weak, or strong.
## How to Use:
1.Run the program using streamlit:
```bash
$ streamlit run password_toolkit.py
```
2.Select "Password Generator" or "Password Validator" from the menu.

3.Follow the prompts to generate or validate a password.
## How to Use Command-Line Version:
1.Clone the Repository:
```bash
git clone https://github.com/An-AvG-Geek/Password_Toolkit.git
```
2.Navigate into the Directory:
```bash
cd Password_Toolkit
```
3.Install Necessary Requirements:
```bash
pip install -r requirements.txt
```
4.Run the Script:
```bash
python terminal_version.py
```




## Dependencies:
- Python 3.x
- Streamlit
- Random
