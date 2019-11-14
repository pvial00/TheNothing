import random
from Crypto.Util import number
from Crypto.Random import random

# requires pycrypto for prime number generation

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def mygcd(a, b):
    while True:
        while b != 0:
            a, b = b, a % b
        return a


def keygen(psize):
    p = number.getPrime(psize)
    q = number.getPrime(psize)
    n = p * q
    
    t = ((p - 1) * (q - 1))
    e = random.randint(1, t)
    g = mygcd(e, t)
    while g != 1:
        e = random.randint(1, t)
        g = mygcd(e, t)
        if g == 1:
            break
    sk = multiplicative_inverse(e, t)
    return sk, e, n, t, p, q

def encrypt(ptxt, pk, mod):
    return pow(ptxt, pk, mod)


def decrypt(ctxt, sk, mod):
    return pow(ctxt, sk, mod)
