
#Random password generator 
import random
import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
charValue = string.ascii_letters+string.digits+string.punctuation
# print(random.choice(charValue))
pass_len=int(input("Enter the size of Required Random password"))
password =""
for i in range (pass_len):
    password =password+ random.choice(charValue)

    
print(f"Your",pass_len,"digit Random Password is :",password)
