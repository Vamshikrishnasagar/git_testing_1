import logging
import os
import datetime
import sys

# Get parameters from Jenkins environment variables
user_file_name = os.environ.get('LOG_FILE_NAME', 'default_log')
user_name      = os.environ.get('USER_NAME', 'default_user')
user_email     = os.environ.get('USER_EMAIL', 'user@example.com')

today_datee = datetime.datetime.today().strftime('%Y-%m-%d')

location = r'D:\PythonProjects\git_works\RootFolder'
os.makedirs(location, exist_ok=True)

sub_folder = os.path.join(location, 'SubFolder')
os.makedirs(sub_folder, exist_ok=True)

FileName = os.path.join(
    sub_folder,
    f'{user_file_name}_{today_datee}.logs'
)

logging.basicConfig(
    level=logging.DEBUG,
    filemode='a',
    filename=FileName,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

def addition_two_numbers(a, b=20):
    logging.info(f'Addition two numbers : {a} + {b} = {a+b}')
    return a + b

# addition_two_numbers(110)
# addition_two_numbers(125, 125)

first_number   = os.environ.get('first_number', '1')
second_number  = os.environ.get('second_number', '1')
addition_two_numbers(a=int(first_number),
                     b = int(second_number))

print("script completed...")
print(f"Log file created: {FileName}")


"""
Use os.environ when running scripts in Jenkins — it’s cleaner, safer, and Jenkins-native.

Use sys.argv if:
You need to run the script from the terminal often.
You want to support both Jenkins and local runs with the same script.


IT IS FOR BOTH

import os
import sys

user_file_name = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get('LOG_FILE_NAME', 'default_log'))
user_name      = (sys.argv[2] if len(sys.argv) > 2 else os.environ.get('USER_NAME', 'default_user'))
user_email     = (sys.argv[3] if len(sys.argv) > 3 else os.environ.get('USER_EMAIL', 'user@example.com'))

"""