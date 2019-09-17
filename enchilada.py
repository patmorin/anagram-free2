import sys
from math import ceil, factorial
from fractions import Fraction

ir_tab = {0:0, 1:1, 2:1}
def irreducible(n):
    if n in ir_tab: return ir_tab[n]
    if n-1 not in ir_tab:
        for j in range(2, n-1): irreducible(j)  # avoid stack overflow
    ir_tab[n] = factorial(n) - sum( [factorial(i)*irreducible(n-i) for i in range(1, n)] )
    return ir_tab[n]


def choices(t, c):
    tmc = t % c
    tdc = t // c
    numer = factorial(t)
    denom = ((tdc+1)**tmc)*(factorial(tdc)**c)
    return  Fraction(numer, denom)

if __name__ == "__main__":
    c = int(sys.argv[1])
    s = 0
    e = Fraction(27182819, 10**7)
    # print(e)
    # print(float(e))
    for t in range(1, 10*c):
        a = irreducible(t)
        b = choices(t, c)
        best = min(a, b)
        d = Fraction(e*best, c**t)
        s += t**3 * d
        print(t, a, b, factorial(t), best, d)
    print(s, s-1, float(s-1))
