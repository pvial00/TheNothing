from Crypto.Util import number
from myrsa import keygen
#import gmpy2
import math

# Breaks RSA with false keys

def ZanderTheorem1(n):
    k = 2
    x = long(math.sqrt(n)) 
    #x = gmpy2.isqrt(n)
    third = (long(math.sqrt(n)) * 2)
    #tmp = long(pow(x, 2) - third)
    y = (long(math.sqrt(third)) - 1) * k
    #y = gmpy2.isqrt(tmp)
    steps = 0
    while True:
        w = (((x**k - n - y**k) * k) * k)
        try:
            if w == 0:
                break
        except ZeroDivisionError as zer:
            pass
        if w > 0:
            y += 1
        else:
            x += 1
        steps += 1
    print "steps", steps
    return x+y

def ZanderTheorem2(n):
    k = 2
    x = long(math.sqrt(n)) 
    #x = gmpy2.isqrt(n)
    third = (long(math.sqrt(n)) * 2)
    #tmp = long(pow(x, 2) - third)
    y = (long(math.sqrt(third)) - 1) * k
    #y = gmpy2.isqrt(tmp)
    steps = 0
    while True:
        w = ((x**k - n - y**k) * k) * k
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        if n % w <= third and w % n > third:
            y += 1
        steps += 1
    print "steps", steps
    return x+y

def fermat(n):
    from math import sqrt
    x = long(sqrt(n)) + 1
    y = long(sqrt(x**2 - n))
    steps = 0
    while True:
        w = x**2 - n - y**2
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        steps += 1
    print "steps", steps
    return x+y

psize = 24
message = "A"
msg = number.bytes_to_long(message)
sk, pk, n, t, p, q = keygen(psize)
#ap = fermat(n)
#myp = ZanderTheorem1(n)
myp = ZanderTheorem2(n)
myq = n / myp
ctxt = pow(msg, pk, n)
tt = ((myp - 1) * (myq - 1))
print myp, myq, tt
mysk = number.inverse(pk, tt)
ptxt = pow(ctxt, mysk, n)
if ptxt == msg:
    print "Message:", number.long_to_bytes(ptxt)
