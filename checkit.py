import collections
import sys


if __name__ == "__main__":
    filename = sys.argv[1]
    s = open(filename).read()
    for k in range(1, len(s)//2):
        print("Checking for anagrams of length {}".format(2*k))
        for i in range(len(s)-2*k):
            if sorted(s[i:i+k]) == sorted(s[i+k:i+2*k]):
                print("Has anagram: s[{}:s{}] = {}".format(i, i+2*k, s[i:i+2*k]))
                sys.exit(-1)
