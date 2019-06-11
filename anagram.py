# Very inefficient code for generating low-entropy anagram-free strings
import random
import collections
import math
import sys

def is_anagram(s):
    return len(s) % 2 == 0 and sorted(s[:len(s)//2]) == sorted(s[len(s)//2:])

def entropy(hist):
    h = 0
    n = sum(hist.values())
    for c in hist:
        pc = hist[c]/n
        h += pc*math.log(1/pc, 2)
    return h

def high_entropy_suffix(s, t):
    """Return the length of the shortest suffix of s whose entropy exceeds t or return -1 if no such suffix exists"""
    hist = collections.defaultdict(int)
    for i in range(len(s)-1, -1, -1):
        hist[s[i]] += 1
        if entropy(hist) >= t: return len(s)-i
    return -1

def equal_histograms(hist0, hist1):
    for c in hist0:
        if hist0[c] != hist1[c]: return False
    for c in hist1:
        if hist0[c] != hist1[c]: return False
    return True

def anagram_suffix(s, amax):
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

def string_histogram(s):
    hist = collections.defaultdict(int)
    for l in s:
        hist[l] += 1
    return hist

def empirical_entropy(s):
    return entropy(string_histogram(s))

def show_histogram(fp, hist):
    n = sum(hist.values())
    for l in sorted(list(hist)):
        p = hist[l]*100/n
        fp.write("{}: {:2.1f}% {}\n".format(l, p, "*" * int(p)))
    fp.write("Empirical entropy: {:1.4f}\n".format(entropy(hist)))


if __name__ == "__main__":
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

    s = ''
    erejections = 0
    arejections = 0
    iterations = 0
    rejection_hist = collections.defaultdict(int)
    while 1 < 2:
        s += random.choice(alphabet)
        iterations += 1
        t = anagram_suffix(s, amax)
        rejection_hist[t] += 1
        if t > 0:
            # if len(s) < 20:
            #     print(s, t, s[len(s)-2*t:], s[:len(s)-t])
            s = s[:len(s)-t]
            arejections += t

        if random.random() < .001:
            filename = "s-{}-{}.txt".format(c, amax)
            with open(filename, 'w') as fp:
                fp.write(s)
            filename = "af-{}-{}.stats".format(c, amax)
            with open(filename, 'w') as fp:
                fp.write("Alphabet size {} ({}), maximum anagram length {}\n".format(c, alphabet, amax))
                fp.write("iterations: {}\n".format(iterations))
                if len(s) >= 50:
                    fp.write("s = '{}...{}'\n".format(s[:20], s[-20:]))
                else:
                    fp.write("s = '{}'".format(s))
                fp.write("string length: {} ({:2.1f}%)\n".format(len(s), len(s)*100/iterations))
                fp.write("deletions: {} ({:2.1f}%)\n".format(arejections, arejections*100/iterations))
                fp.write("Histogram of full string\n")
                show_histogram(fp, string_histogram(s))
                # if len(s) >= 100*c:
                #     fp.write("Histogram of middle string\n")
                #     ss = s[len(s)//2-50*c:len(s)//2+50*c]
                #     show_histogram(fp, string_histogram(ss))
                total_rejections = sum([a*b for (a,b) in rejection_hist.items()])
                fp.write("Total deletions: {}\n".format(total_rejections))
                fp.write("Longest deletion: {}\n".format(max(rejection_hist.keys())))
                fp.write("Average deletion: {}\n".format(total_rejections/iterations))
                fp.write("Average non-empty deletion: {}\n".format(total_rejections/sum(rejection_hist.values())))
                fp.write("Deletion entropy {:1.4f}\n".format(entropy(rejection_hist)))
                fp.write("Deletion histogram\n")
                show_histogram(fp, rejection_hist)


        # This produces output suitable for gnuplot
        print("{:10} {:10} {:10} {:10} {}".format(iterations, len(s), erejections, arejections, empirical_entropy(s)))
