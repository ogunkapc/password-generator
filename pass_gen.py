# generate password from random letters and symbols with minimum length

import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '@#$%&*/\?'

use_for = lower_case + upper_case + number + symbols
length_of_password = 8

password = "".join(random.sample(use_for, length_of_password))

print('Generated password:', password)