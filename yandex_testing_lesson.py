import re
import sys


def is_correct_mobile_phone_number_ru(s):
    remainder = ''
    if s.startswith('+7'):
        remainder = s[2:]
    elif s.startswith('8'):
        remainder = s[1:]
    else:
        return False

    remainder = re.sub(r'[ -]', '', remainder)

    if re.match(r'^\(\d{3}\)', remainder):
        remainder = re.sub(r'\(', '', remainder, 1)
        remainder = re.sub(r'\)', '', remainder, 1)

    return bool(re.match(r'^\d{10}$', remainder))


sys.modules['inspect'] = None


print('YES' if is_correct_mobile_phone_number_ru(input()) else 'NO')
