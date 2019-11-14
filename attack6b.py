from Crypto.Util import number
from myrsa import keygen, encrypt, decrypt
import math
import numpy

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
    psize = 1024
    sk, pk, mod, t, p, q = keygen(psize)
    G = number.getRandomRange(1, pk)
    tmp = number.GCD(G, pk)
    while tmp != 1:
        G = number.getRandomRange(1, pk)
        tmp = number.GCD(G, pk)
    print "Totient", t
    sq = isqrt(mod)
    sq2 = isqrt(pk)
    k = 0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
    size = psize * k
    print size
    #k = 0.0011893
    #sq = long(math.sqrt(mod)) + 1 
    first = long((sq * 0.100999999))
    third = long((sq * 0.000999999))
    fourth = long((sq * 0.009999999))
    print "N mod T", mod % t
    tries = 0
    ctxt = pow(msg, pk, mod)
    diff = mod - pk
    perc = long(sq * size)
    print third, perc, mod % t, t
    second = long(sq * 2) + third + (sq*perc) * (perc) + (perc*2)
    print "second", second
    mmin = second - perc
    mmax = second + perc
    third = third * perc
    guess = ((mod - ((first-fourth)*1))) - sq
    #guess = ((mod - ((first-fourth)*psize))) - sq
    #guess = ((second % mod) -(sq*psize)) - (t1*psize)
    tmp = guess
    #tmp = ((second / psize) + (second)) - ((sq*psize)*2)  - ((fourth*first)*psize) - (second%fourth) - ((sq2**2)*2)
    #tmp = (((tmp % second ) + sq) % mod) + (sq*psize*first)
    #tmp = (tmp % second) - (sq2*psize) - (sq*fourth) - (second/sq) - (fourth/sq) - (((first/sq)*psize)-fourth)
    #tmp = (tmp - 126719910000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
    #tmp = (tmp - (99999999999999999999999999999999999999999999999999999999926719910000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)*psize) 
    #tmp = ((((((tmp % mod) + tmp) % mod)) - (second%tmp)) + second) - (guess%tmp) - ((tmp%psize)*2) - ((third*psize)*psize) - ((fourth%second)*psize)
    #tmp = ((((((tmp % mod) + tmp) % mod)) - (second%tmp)) + second) - (guess%tmp) - ((tmp%psize)*2) - ((third*psize)*psize) - ((fourth%second)*psize)

    #tmp = ((((tmp % mod) + tmp) % mod)) - ((second%sq)*third) - (third%second) - (long(size)*2) - (second/sq) - (third/sq) - (tmp/second)
    #tmp = ((((tmp % mod) + tmp) % mod)) - ((sq*perc)*2) - (perc*2) - long(size) - ((perc%sq)*2) - (third**2)
    #tmp = long(((tmp % mod) + (sq*size)) ) * long(size)
    print "Guess", tmp
    totarget = (tmp - t)
    tbytes = number.long_to_bytes(totarget)
    print len(tbytes), len(str(totarget))
    print "To target", totarget
    tmp2 = pk
    while True:
        #tmp2 = tmp2 % sq
        tmp = tmp - 1
        #if tmp % mod >= mmin:
        #    tmp = tmp - sq
       
        #tmp = ((((((tmp % pk)) + mod) - (pk)) + tmp2) % pk) + (tmp2%pk) - (pk%tmp2) + (tmp2) + (tmp % mod) - G + (sq2+sq)
        #tmp2 = (((tmp2 % mod) + 1) % pk) + (tmp%pk) + (G%sq) + (sq%sq2) + (G%sq2) + sq
        #tmp = ((tmp % sq) + (mod) - (pk%sq) - (pk%sq2) - (mod %sq) - sq2) + 1
        #tmp2 = (((tmp2 % mod) * pk) % mod) + 1
        #tmp = ((tmp % sq) + (mod) - (pk%sq) - (pk%sq2) - ((mod %sq)) - sq) + (sq%sq2) + 1
        #tmp2 = (((tmp2 % mod) * pk) % mod) + 1
        #tmp = tmp - 1
        #if tmp > t:
        #    print "Above"
        #elif tmp < t:
        #    print "Below"
        #print tmp, t
        try:
            if (mod % tmp) >= mmin or (mod % tmp) <= mmax:
            #if numpy.testing.assert_approx_equal(tmp, third):
            # this is formatted for me
            #if 1 > 0:
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
