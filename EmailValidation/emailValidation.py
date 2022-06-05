# email = input("Enter your Email : ")
# k = 0
# j = 0
# d = 0
# if len(email) >= 6:
#     if email[0].isalpha():
#         if ("@" in email) and (email.count("@") == 1):
#             if (email[-4] == ".") ^ (email[-3] == "."):
#                 for i in email:
#                     if i == i.isspace():
#                         k = 1
#                     elif i.isalpha():
#                         if i == i.upper():
#                             j = 1
#                     elif i.isdigit():
#                         continue
#                     elif i == "_" or i == "." or i == "@":
#                         continue
#                     else:
#                         d = 1
#                 if k == 1 or j == 1 or d == 1:
#                     print("wrong Email 5 :", email)
#                 else:
#                     print("Right Email :", email)
#             else:
#                 print("wrong Email 4 :", email)
#         else:
#             print("Wrong Email 3 :", email)
#     else:
#         print("Wrong Email 2 :", email)
# else:
#     print("Wrong Email 1 :", email)


# Email Validation using RegEx module..............

import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Email : ")
if re.search(email_condition, user_email):
    print("Right Email :", user_email)
else:
    print("Wrong Email :", user_email)
