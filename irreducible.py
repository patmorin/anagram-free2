import sys
from math import log2, sqrt, gamma, factorial


fac_tab = {0:1, 1:1}
def factorial(n):
    f = 1
    for k in range(n, 0, -1):
        if k in fac_tab:
            break
    for i in range(k+1, n+1):
        fac_tab[i] = i * fac_tab[i-1]
    return fac_tab[n]

ir_tab = {0:0, 1:1, 2:1}
def irreducible(n):
    if n in ir_tab: return ir_tab[n]
    if n-1 not in ir_tab:
        for j in range(2, n-1): irreducible(j)  # avoid stack overflow
    ir_tab[n] = factorial(n) - sum( [factorial(i)*irreducible(n-i) for i in range(1, n)] )
    return ir_tab[n]


def gfactorial(x):
    return gamma(x+1)

def anagram_upper_bound(c, n):
    """ An upper bound on the number of anagrams of length n over an alphabet
    of size c"""
    return c**(n/c)*factorial(n)/gfactorial(n/c)**c

if __name__ == "__main__":
    a = dict()
    with open('irreducible.txt') as fp:
        for line in fp:
            (n, an) = line.split()
            a[int(n)] = int(an)
    # print(a)

    for n in range(1, 400):
        assert(a[n] == irreducible(n))
        # print(n, log2(a[n])/n)

    c = int(sys.argv[1])
    weights = [log2(c)*n-log2(irreducible(n)) for n in range(1, 2*c+1)]
    krafts = [1/2**w for w in weights]
    print(weights)
    print(krafts)
    print("kraft sum = ", sum(krafts))
    print("free kraft = ", 1-sum(krafts))
    print("code 0 size >", log2(1/(1-sum(krafts))))
    for n in range(1, 2*c+1):
        print(n, log2(c)-log2(irreducible(n))/n,
                 log2(c)-log2(anagram_upper_bound(c, 2*n))/(2*n))

    # print("free kraft - 1/2**(4/5) = ", 1-sum(krafts)-1/2**(4/5))
