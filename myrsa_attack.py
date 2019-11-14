from Crypto.Util import number
from myrsa import keygen, encrypt, decrypt
import math

def isqrt(x):
    _1_50 = 1 << 50
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

def theNothing():
    msg = 123
    psize = 32
    sk, pk, mod, t, p, q = keygen(psize)
    print "Totient", t
    sq = isqrt(mod)
    k = 0.001189
    #sq = long(math.sqrt(mod)) + 1 
    third = long((sq * 2))
    tries = 0
    ctxt = pow(msg, pk, mod)
    diff = mod - pk
    perc = long(sq * k)
    print third, perc, mod % t, t
    mmin = third - perc
    mmax = third + perc
    guess = ((mod - third) % mod) - perc
    tmp = guess
    print "Guess", guess
    print "To target", guess - t
    while True:
        tmp = (tmp - 1)
        try:
            #if (mod % tmp) >= mmin or (mod % tmp) <= mmax:
            #if numpy.testing.assert_approx_equal(tmp, third):
            # this is formatted for me
            if 1 > 0:
                key = number.inverse(pk, tmp)
                ptxt = pow(ctxt, key, mod)
                if ptxt == msg:
                    print ptxt
                    print "Found it"
                    print "Tries", tries
                    break
                tries += 1
        except (ZeroDivisionError,AssertionError) as zer:
            pass

theNothing()
