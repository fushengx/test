import string



def column2row(col):

    num = 0
    for c in col:
        if c in string.ascii_letters:
            num = num * 26 + (ord(c.upper()) - ord('A')) + 1
    return num


def row2column(row):

    str = ""
    while row > 0:
        row, remainder = divmod(row - 1, 26)
        str = chr(65 + remainder) + str
    return str



print(column2row("AA"))
print(row2column(27))
