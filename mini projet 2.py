import random
import string

pass_len =12

charValue=string.ascii_letters+string.punctuation+string.digits
password = ""

for i in range (pass_len):
    password+=random.choice(charValue)
    # print("your random password of 12 lenghth:",password)
print("Your password of 12 characters is :", password)
   