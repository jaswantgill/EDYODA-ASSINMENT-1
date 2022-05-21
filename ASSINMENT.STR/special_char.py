s=input("Enter string")
special_characters = "!@#$%^&*()-+?_=,<>/"
if any(c in special_characters for c in s):
    print("String is not accepted")
else:
    print("String is accepted")
