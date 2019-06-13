import sys
import collections
import math

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

def countem_r(s, a):
    if len(a) == 0:
        # print(''.join([ 'abcdefghijlm'[i] for i in s]))
        return 1

    if anagram_suffix(s) > 0:
        return 0

    count = 0
    for i in range(len(a)):
        a[i], a[-1] = a[-1], a[i]
        x = a.pop(-1)
        s.append(x)
        count += countem_r(s, a)
        s.pop(-1)
        a.append(x)
        a[i], a[-1] = a[-1], a[i]
    return count

def countem(c, n):
    return countem_r(list(range(n)), list(range(n)))

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def irreducible(n):
    factorial(n) - sum([factorial(k)*])


if __name__ == "__main__":
    c = int(sys.argv[1])
    counts = list()
    weights = list()
    krafts = list()
    for n in range(1, c+1):
        count = countem(c, n)
        counts.append(count)
        weights.append(math.log(c/2,2)*n-math.log(count, 2))
        krafts.append(1/2**weights[-1])
        print(n, counts[-1], weights[-1], sum(krafts))
    print(weights)
    print(krafts)
    print(sum(krafts))
