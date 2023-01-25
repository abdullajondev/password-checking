password = input("please enter your password: ")

digits = {}

if len(password) >= 8:
    digits["length"] = True
else:
    digits["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
digits["digit"] = digit


uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

digits["uppercase"] = uppercase


print((digits))
if all(digits.values()) == True:
    print("strong password")
else:
    print("weak password")