from Crypto.Util import number
from myrsa import keygen
import gmpy2

# Breaks RSA with false keys

def ZanderTheorem(n):
    x = gmpy2.isqrt(n)
    third = (x * 2)
    tmp = long(pow(x, 2) - third)
    y = gmpy2.isqrt(tmp)
    while True:
        w = x**2 - n - y**2
        if n % w <= third:
            break
        if w > 0:
            y += 1
        else:
            x += 1
    return x+y

psize = 2048
message = "tH3N0tHinG"
msg = number.bytes_to_long(message)
sk, pk, n, t, p, q = keygen(psize)
print p, q, t
myp = ZanderTheorem(n)
myq = n / myp
print myp, myq
tt = ((myp - 1) * (myq - 1))
mysk = number.inverse(pk, tt)
ptxt = pow(ctxt, sk, n)
if ptxt == msg:
    print "Message:", number.long_to_bytes(ptxt)
