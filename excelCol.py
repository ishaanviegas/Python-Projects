def col2num(col):
    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num

def num2col(num):
    letters = ''
    while num:
        num, mod = divmod(num-1, 26)
        letters += chr(mod + 65)      # 65 == ord('A')
    return ''.join(reversed(letters))