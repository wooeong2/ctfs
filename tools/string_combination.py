#-*- coding: utf-8 -*-
# Some CTF need to bruteforce.
import hashlib
from itertools import product

def flag(a, b, c):
    tmp_a = hashlib.sha1(a+" "+b).hexdigest()
    tmp_b = hashlib.sha1(c).hexdigest()
    return 'FLAG{' + hashlib.sha256(tmp_a+tmp_b).hexdigest() + '}'

a = ["abc", ]
b = ["2019-08-03 01:52:30", ]
c = ["2019-08-03 01:54:53"]

# Remove Duplicates
a = list(dict.fromkeys(a))
b = list(dict.fromkeys(b))
c = list(dict.fromkeys(c))

items = [a, b, c]
for i in list(product(*items)):
    print flag(i[0], i[1], i[2])
