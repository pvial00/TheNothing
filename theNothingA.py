from Crypto.Util import number
from myrsa import keygen
from math import sqrt, log, e
import gmpy2

def ZanderTheoremX(n, psize):
    k = 2
    l = long(log(n)) 
    l2 = long(log(n, 2)) 
    l10 = long(log(n, 10)) 
    x = (gmpy2.isqrt(n) - (l * l))
    #x = (gmpy2.isqrt(n) - (l * 2)) - (l2 * psize) + (l10 * l10)
    third = (long((x * 2) * (psize * 0.2)))
    _third = long(x * 2)
    y = ((gmpy2.isqrt(third)) + ((l * l)*2))
    #y = ((gmpy2.isqrt(third)) + ((l * l)*2) + (l2 * l2)) + l10
    guess = n - third
    print "Z", x, y, l
    steps = 0
    while True:
        w = long(((x**k - (n) - y**k) * l) * 2)
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        if n % w <= third and w % n > third:
            y += 1
        if (n - w) <= guess:
            y += 1
        steps += 1
    print "steps", steps
    return (x+y)

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

def fermatX(n):
    from math import sqrt
    l = long(log(n))
    third = gmpy2.isqrt(n) * 2
    x = long(sqrt(n)) + 1
    guess = n - third
    y = long(gmpy2.isqrt(third)) - (l * l)
    #y = long(sqrt(x**2 - n))
    steps = 0
    while True:
        w = (pow(x, 2) - n - pow(y, 2)) * 2
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        steps += 1
        if n % w <= third and w % n > third:
            y += 1
    print "steps", steps
    return x+y

def ZanderTheorem(n, psize):
    l = long(log(n)) - 1
    x = gmpy2.isqrt(n) 
    third = long((x * 2) * (psize * 0.2))
    y = (gmpy2.isqrt(third) - l)
    print "Z", x, y, l
    steps = 0
    while True:
        w = ((x**2 - (n) - y**2) * 2) * 2
        if w == 0:
            break
        if w > 0:
            y += 1
        else:
            x += 1
        if n % w <= third and w % n > third:
            y += 1
        if w % n == 0:
            y += 1
        steps += 1
    print "steps", steps
    return (x+y)

psize = 16
message = "M"
msg = number.bytes_to_long(message)

sk, pk, n, t, p, q = keygen(psize)
myp = ZanderTheoremX(n, psize)
myq = n / myp
print myp, myq
ctxt = pow(msg, pk, n)
print ctxt
tt = ((myp - 1) * (myq - 1))
mysk = number.inverse(pk, tt)
ptxt = pow(ctxt, mysk, n)
if ptxt == msg:
    print "Got it", number.long_to_bytes(ptxt)
