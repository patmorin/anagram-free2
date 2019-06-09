# Very inefficient code for generating low-entropy anagram-free strings
import random
import collections
import math
import sys

def is_anagram(s):
    return len(s) % 2 == 0 and sorted(s[:len(s)//2]) == sorted(s[len(s)//2:])

def entropy(hist, n):
    h = 0
    for c in hist:
        pc = hist[c]/n
        h += pc*math.log(1/pc, 2)
    return h

def high_entropy_suffix(s, t):
    """Return the length of the shortest suffix of s whose entropy exceeds t or return -1 if no such suffix exists"""
    hist = collections.defaultdict(int)
    for i in range(len(s)-1, -1, -1):
        hist[s[i]] += 1
        if entropy(hist, len(s)-i) >= t: return len(s)-i
    return -1

def equal_histograms(hist0, hist1):
    for c in hist0:
        if hist0[c] != hist1[c]: return False
    for c in hist1:
        if hist0[c] != hist1[c]: return False
    return True

def anagram_suffix(s, amax):
    """Return half the length of the shortest suffix of s that is an anagram or -1 if no such suffix exists"""
    if len(s) < 2: return -1
    hist0 = collections.defaultdict(int)
    hist1 = collections.defaultdict(int)
    hist0[s[len(s)-2]] = 1
    hist1[s[len(s)-1]] = 1
    # print(hist0.items(), hist1.items())
    if amax < 1 and equal_histograms(hist0, hist1): return 1
    for t in range(2, len(s)//2+1):
        hist0[s[len(s)-2*t]] += 1
        hist0[s[len(s)-2*t+1]] += 1
        hist0[s[len(s)-t]] -= 1
        hist1[s[len(s)-t]] += 1
        # print(hist0.items(), hist1.items())
        if amax < t and equal_histograms(hist0, hist1): return t
    return -1

def empirical_entropy(s):
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    h = 0
    for c in d:
        pc = d[c]/len(s)
        h += pc*math.log(1/pc, 2)
    return h

if __name__ == "__main__":
    alphabet = "abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c = 50
    if len(sys.argv) >= 2:
        c = int(sys.argv[1])
        if c > len(alphabet):
            print("Error: max alphabet size is {}".format(len(alphabet)))
            sys.exit(-1)
    alphabet = alphabet[:c]

    amax = c//2
    if len(sys.argv) >= 3:
        amax = int(sys.argv[2])

    hmax = math.log(c, 2) - 1
    s = ""
    erejections = 0
    arejections = 0
    iterations = 0
    while 1 < 2:
        s += random.choice(alphabet)
        iterations += 1
        if high_entropy_suffix(s, hmax) >= 0:
            s = s[:len(s)-1]
            erejections += 1
        t = anagram_suffix(s, amax)
        if t > 0:
            s = s[:len(s)-t]
            arejections += t

        # # output long strings
        # if iterations % 10000 == 0:
        #     filename = ""
        #     with("")

        # sanity check
        if len(s) < 500 and iterations % 100 == 0:
            for i in range(len(s)-1):
                for j in range(i+1, len(s)):
                    if empirical_entropy(s[i:j]) > hmax:
                        print("Fatal error, string has high entropy substring")
                        sys.exit(-3)
                    if 2*amax < j-i and is_anagram(s[i:j]):
                        print("Fatal error, string contains anagram: {}".format(s[i:j]))
                        sys.exit(-2)

        # This produces gnuplot output
        print("{:10} {:10} {:10} {:10} {}".format(iterations, len(s), erejections, arejections, empirical_entropy(s)))
