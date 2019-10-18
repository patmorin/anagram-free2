#!/usr/bin/python3
import sys
import random
from collections import defaultdict

def repetitive_suffix(s):
    """Return (half) the length of the shortest repetitive suffix in s"""
    for t in range(1, len(s)//2 + 1):
        if s[-2*t:-t] == s[-t:]:
            return t
    return 0

def normalize(s):
    sigma="abcdefghijklmnopqrstuvwxyz"
    map = dict()
    i = 0
    for x in s:
        if x not in map:
            map[x] = sigma[i]
            i += 1
    return "".join([map[x] for x in s])

if __name__ == "__main__":
    try:
        c = int(sys.argv[1])
        r = int(sys.argv[2])
    except:
        sys.stderr.write("Usage: {} <|sigma|> <r>\n".format(sys.argv[0]))
        sys.exit(-1)
    sigma = "abcdefghijklmnopqrstuvwxyz"[:c]
    s = [sigma[0]]

    hist = defaultdict(int)
    hist2 = defaultdict(int)
    i = 0
    while 1 < 2:
        i += 1
        s += random.choice(sigma)
        t = repetitive_suffix(s)
        hist2[t] += 1
        while t > 0:
            s.pop()
            t -= 1

        if len(s) >= r:
            hist["".join(normalize(s[-r:]))] += 1

        if i % 1000 == 0:
            print("="*70)
            print(i, len(s))
            d = sum(hist.values())
            for k in sorted(hist.keys()):
                print(k, hist[k]/d, d/hist[k])
            print("-"*70)
            hist3 = defaultdict(int)
            for j in range(len(s)-r):
                hist3[normalize("".join(s[j:j+r]))] += 1
            d = sum(hist3.values())
            for k in sorted(hist3.keys()):
                print(k, hist3[k]/d, d/hist3[k])

            print("-"*70)
            d = sum(hist2.values())
            for t in range(10):
                print(t, hist2[t]/d)
