import re
number =input("enter  the mobile number")
number_pattern = r'^\+1\d{10}$'

if re.match(number_pattern,number):
    print("number is valid")
else:
    print("number is not valid")
