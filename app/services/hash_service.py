import string
from app.config import settings

BASE69 = settings.BASE69

def encode(num):
    base = len(BASE69)
    print(num, base)
    arr = []

    while num:
        num, rem = divmod(num, base)
        arr.append(BASE69[rem])

    arr.reverse()
    return ''.join(arr)
