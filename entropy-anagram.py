# Very inefficient code for generating low-entropy anagram-free strings
import random
import collections
import math
import sys

def is_anagram(s):
    return len(s) % 2 == 0 and sorted(s[:len(s)//2]) == sorted(s[len(s)//2:])

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
    c = 50
    if len(sys.argv) == 2:
        c = int(sys.argv[1])
    hmax = math.log(c, 2) - 1

    alphabet = "abcedefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[:c]
    s = ""
    rejections = 0
    iterations = 0
    while 1 < 2:
        s += random.choice(alphabet)
        iterations += 1
        for t in range(len(s)):
            if t > c//2 and is_anagram(s[len(s)-1-t:]):
                s = s[:len(s)-t//2]
                break
            if empirical_entropy(s[len(s)-1-t:]) > hmax:
                # s = s[:len(s)-1-3*t//4]
                s = s[:len(s)-1]
                rejections += 1
                break

        # print("\r", empirical_entropy(s), len(s), end='')
        # print("\r{:10} {:10} {}".format(len(s), rejections, empirical_entropy(s)), end='')

        # This produces gnuplot output
        print("{:10} {:10} {:10} {}".format(iterations, len(s), rejections,
        empirical_entropy(s)))

        # if len(s) == 1000: print(s)
        # if len(s) % 1000 == 1:
        #     print("\n", s)
