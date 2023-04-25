#!/usr/bin/python3
''' validate utf8 module '''


def bin8(n):
    ''' converts a number into an 8-bit zero padded binary '''
    b = bin(n)[2:].zfill(8)
    l = len(b)
    if l > 8:
        return b[l - 8:]
    return b


def validUTF8(data):
    ''' validates if `data` is utf8 encoded '''
    valid = True
    while data and valid:
        byte = data[0]
        b = bin8(byte)
        code_point = 0
        valid = False
        if b.startswith('0'):
            code_point = int(b[1:], 2)
            valid = code_point >= 0 and code_point <= 0x7f
            data = data[1:]
        elif (b.startswith('110') and
              len(data) >= 2 and
              bin8(data[1]).startswith('10')):
            code_point = int(b[3:] + bin8(data[1])[2:], 2)
            valid = code_point >= 0x80 and code_point <= 0x7ff
            data = data[2:]
        elif (b.startswith('1110') and
              len(data) >= 3 and
              bin8(data[1]).startswith('10') and
              bin8(data[2]).startswith('10')):
            code_point = int(b[4:] + bin8(data[1])[2:] + bin8(data[2])[2:], 2)
            valid = code_point >= 0x800 and code_point <= 0xffff
            data = data[3:]
        elif (b.startswith('11110') and
              len(data) >= 4 and
              bin8(data[1]).startswith('10') and
              bin8(data[2]).startswith('10') and
              bin8(data[3]).startswith('10')):
            code_point = int(b[5:] + bin8(data[1])[2:] +
                             bin8(data[2])[2:] + bin8(data[3])[2:], 2)
            valid = code_point >= 0x1000 and code_point <= 0x10ffff
            data = data[4:]
    return valid
