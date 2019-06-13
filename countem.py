import sys
import collections
import math
from math import log2

def equal_histograms(hist0, hist1):
    for c in hist0:
        if hist0[c] != hist1[c]: return False
    for c in hist1:
        if hist0[c] != hist1[c]: return False
    return True


def anagram_suffix(s, amax=0):
    """Return half the length of the shortest non-empty suffix of s that is an anagram, or 0 if no such suffix exists"""
    hist0 = collections.defaultdict(int)
    hist1 = collections.defaultdict(int)
    for t in range(1, len(s)//2+1):
        hist0[s[len(s)-2*t]] += 1
        hist0[s[len(s)-2*t+1]] += 1
        hist0[s[len(s)-t]] -= 1
        hist1[s[len(s)-t]] += 1
        if amax < t and equal_histograms(hist0, hist1): return t
    return 0

def countem(c, n):
    count = 0
    s = [c-1]
    while s:
        if anagram_suffix(s) == 0:
            if len(s) == n:
                count += 1
                # print(''.join([ 'abcdefghijlm'[i] for i in s]))
            else:
                s.append(-1)
        while len(s) > 0 and s[-1] == c-1:
            s.pop(-1)
        if len(s) > 0:
            s[-1] = s[-1] + 1
    return c*count


if __name__ == "__main__":
    c = int(sys.argv[1])
    for n in range(1, 30):
        count = countem(c, n)
        print(n, count, count**(1/n), log2(count)/n, n*log2(c)-log2(count), (n+1)*log2(c)-log2(count*c))
