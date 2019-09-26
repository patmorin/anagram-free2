import sys
from math import ceil, factorial, e, log2
from math import log as ln
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
    e = Fraction(27182819, 10**7)
    w = [2**(-0.95*log2(c)/c)]
    # w = [2**(-1.5/c)]
    # w = [c**(-1/c)]
    # c2 = Fraction(9*c, 10)
    for t in range(1, 10**6):
        # print(w)
        a = irreducible(t)
        b = choices(t, c)
        x = (c-1)**t
        if a <= b and a <= x:
            best = a
            txt = 'a'
        elif b <= a and b <= x:
            best = b
            txt = 'b'
        else:
            best = x
            txt = 'x'
        best = min(a, b)
        best = min(best, x)
        w.append(Fraction(best, c**t))
        # print(t, a, b, best, sum(w), float(sum(w)))
        f = float(sum(w[1:]))
        print(t, txt, w[0], f, w[0]+f)
