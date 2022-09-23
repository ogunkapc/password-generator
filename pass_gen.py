# generate password from random letters and symbols with minimum length

import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '@#$%&*/\?'

use_for = lower_case + upper_case + number + symbols
length_of_password = 