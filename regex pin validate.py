# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

import re
def validate_pin(pin):
    if re.match('\n*',pin):
        return False #handle newline
    elif re.match('^[0-9][0-9][0-9][0-9]$',pin) or re.match('^[0-9][0-9][0-9][0-9][0-9][0-9]$',pin):
        return True
    else:
        return False

print(validate_pin('1234\n'))

# actual solution
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()