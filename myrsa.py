import random
from Crypto.Util import number
from Crypto.Random import random

# requires pycrypto for prime number generation

def genPrimes(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    while q == p:
        q = number.getPrime(psize)
    return p, q


def keygen(psize):
    p, q = genPrimes(psize)
    n = p * q
    t = ((p - 1) * (q - 1))
    e = number.getRandomRange(1, t)
    g = number.GCD(e, t)
    while g != 1:
        e = number.getRandomRange(1, t)
        g = number.GCD(e, t)
        if g == 1:
            break
    sk = number.inverse(e, t)
    return sk, e, n, t, p, q

def encrypt(ptxt, pk, mod):
    return pow(ptxt, pk, mod)


def decrypt(ctxt, sk, mod):
    return pow(ctxt, sk, mod)
