import os

# Replace 'MY_VARIABLE_NAME' with the name of your environment variable
my_variable_value = os.environ.get('EMAIL_PASS')

if my_variable_value:
    print("The value of EMAIL_USER is:", my_variable_value)
else:
    print("EMAIL_USER is not set.")
