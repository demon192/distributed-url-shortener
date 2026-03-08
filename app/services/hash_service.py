import string

BASE69 = string.digits + string.ascii_letters + "#" + "$" + "^" + "&" + "!" +"@" + "%"

def encode(num):
    base = len(BASE69)
    arr = []

    while num:
        num, rem = divmod(num, base)
        arr.append(BASE69[rem])

    arr.reverse()
    return ''.join(arr)
