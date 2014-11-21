#!/usr/bin/env python

table = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
    90: 'ninety'
}

def english(n):
    if n == 1000: return 'one thousand'
    elif n >= 100:
        ret = english(n // 100) + ' hundred'
        if n % 100 != 0:
            ret += ' and ' + english(n % 100)
        return ret
    elif n >= 20: return table[(n // 10) * 10] + english(n % 10)
    elif n > 0: return table[n]
    return ''

print(sum(map(lambda x: len(english(x).replace(' ', '')), range(1, 1001))))
