# Given an integer, return as a string the binary representation of the integer.

def bin_repr(i):
    power, remainder = 0, i
    while 2 ** power < i:
        power += 1

    out = ['0'] * (power + 1)

    while remainder > 0:
        if 2 ** power <= remainder:
            remainder -= 2 ** power
            out[power] = '1'
        power -= 1

    return ''.join(reversed(out)).lstrip('0')
