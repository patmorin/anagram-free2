#!/usr/bin/python3
import sys
from fractions import Fraction

def nonrep_suffix(s):
    for t in range(1, len(s)//2 + 1):
        if s[-2*t:-t] == s[-t:]:
            return False
    return True

def gen_nonrep(a, s, t):
    if t == 0:
        yield s
        return
    for c in a:
        sc = s + c
        if nonrep_suffix(sc):
            for z in gen_nonrep(a, sc, t-1):
                yield z

def count_nonrep(a, s, t):
    m = 0
    for z in gen_nonrep(a, s, t):
        m += 1
    return m

if __name__ == "__main__":
    try:
        k = int(sys.argv[1])
        c = int(sys.argv[2])
    except:
        sys.stderr.write("Usage: {} <k> <|sigma|>\n".format(sys.argv[0]))
        sys.exit(-1)
    print("k = {}, |sigma| = {}".format(k, c))
    sigma = "abcdefghijklmnopqrstuvwxyz"[:c]
    worst = Fraction(-1, 1)
    for s in gen_nonrep(sigma, "ab", k-2):
        c = 0
        b = 0
        for z in gen_nonrep(sigma, s, k-1):
            print("\r{}".format(z), end='')
            sys.stdout.flush()
            c += 1
            if z[-k+1:] == s[:-1]:
                b += 1
            # print("{}+{}={} ({})".format(s, z[-k+1:], z, z[-k+1:] == s[:-1]))
        ratio = Fraction(b,c)
        # print(b, c, ratio)
        if ratio > worst:
            worst = ratio
            worst_example = s
    print()
    print(worst_example, worst, worst/len(sigma))
