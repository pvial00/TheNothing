import gmpy2

def ZanderTheoremZ(n):
    '''The following algorithm breaks RSA modulae in a generally timely manner.'''
    assert n % 2 != 0
    sq = gmpy2.isqrt(n)
    l = long(gmpy2.log10(n)) 
    m = (sq / l) 
    a = 0
    b = (a * a) - n
    while not gmpy2.is_square(b):
        a = ((a + n + sq) % m) + sq
        b = ((a * a) - n)
    p = int(a + gmpy2.isqrt(b))
    q = int(a - gmpy2.isqrt(b))
    return p, q

def main():
    Nstring = raw_input("Enter a modulus N to factor:")
    P, Q = ZanderTheoremZ(long(Nstring))
    phi = ((P - 1) * (Q - 1))
    print "P", P
    print "Q", Q
    print "Phi", phi

main()
