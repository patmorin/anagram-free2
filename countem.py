import sys
import collections
import math
from math import log2

def histogram_distance(hist0, hist1):
    """Return the L1 distance between two histograms"""
    dist = 0
    for c in hist0.keys():
        dist += abs(hist0[c] - hist1[c])
    for c in hist1:
        if c not in hist0: dist += abs(hist0[c] - hist1[c])
    return dist

def equal_histograms(hist0, hist1):
    """Return true iff two histograms are equal"""
    return histogram_distance(hist0, hist1) == 0

def histogram(s):
    h = collections.defaultdict(int)
    for c in s:
        h[c] += 1
    return h

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

def count_anagram_free(c, n):
    count = 0
    s = [c-1]
    while s:
        if anagram_suffix(s) == 0:
            if len(s) == n:
                count += 1
            else:
                s.append(-1)
        while len(s) > 0 and s[-1] == c-1:
            s.pop(-1)
        if len(s) > 0:
            s[-1] = s[-1] + 1
    return c*count

def string(s):
    return "".join(["abcdefghijklmnopqrstuvwxz"[i] for i in s])

def count_triggers(c, n):
    count = 0
    s = [c-1]
    while s:
        if anagram_suffix(s) == 0:
            if len(s) == n-1:
                if histogram_distance(histogram(s[:n//2]),
                                      histogram(s[n//2:])) == 1:
                    count += 1
            else:
                s.append(-1)
        while len(s) > 0 and s[-1] == c-1:
            s.pop(-1)
        if len(s) > 0:
            s[-1] = s[-1] + 1
    return c*count


if __name__ == "__main__":
    c = int(sys.argv[1])
    for n in range(2, 30, 2):
        a = count_anagram_free(c, n)
        print('A', n//2, a, log2(a)/n, log2(c)-log2(a)/n)
        t = count_triggers(c, n)
        print('T', n//2, t, log2(t)/n, log2(c)-log2(t)/n)
        # print(n, count, count**(1/n), log2(count)/n, n*log2(c)-log2(count), (n+1)*log2(c)-log2(count*c))
