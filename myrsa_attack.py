from Crypto.Util import number
from myrsa import keygen, encrypt, decrypt
import math

def theNothing():
    msg = 123
    sk, pk, mod, t, p, q = keygen(24)
    sq = long(math.sqrt(mod)) + 1 
    third = (sq * 2) 
    tries = 0
    g = 0
    ctxt = pow(msg, pk, mod)
    mmin = 200000
    perc = long(sq * 0.014)
    print third, perc, mod % t, t
    mmin = third - perc
    mmax = third + perc
    guess = (mod - third) % mod
    print guess, t
    tmp = guess
    while True:
        tmp = tmp - 1
        try:
            if (mod % tmp) >= mmin or (mod % tmp) <= mmax:
                key = number.inverse(pk, tmp)
                ptxt = pow(ctxt, key, mod)
                if ptxt == msg:
                    print ptxt
                    print "Found it"
                    print g % mod
                    print "Tries", tries
                    break
                tries += 1
        except ZeroDivisionError as zer:
            pass

theNothing()
