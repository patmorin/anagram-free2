import collections
import sys


if __name__ == "__main__":
    filename = sys.argv[1]
    s = open(filename).read()
    hist = collections.defaultdict(int)
    for c in s:
        hist[c] += 1
    for c in hist:
        hist[c] /= len(s)
    for c in sorted(list(hist)):
        print("{}: {:.1f}% {}".format(c, hist[c]*100, "*" * int(hist[c]*100) ))
