import sys
from math import log2


if __name__ == "__main__":
    a = dict()
    with open('irreducible.txt') as fp:
        for line in fp:
            (n, an) = line.split()
            a[int(n)] = int(an)
    print(a)

    for n in range(1, 400):
        print(n, log2(a[n])/n)

    c = int(sys.argv[1])
    weights = [log2(c/2)*n-log2(a[n]) for n in range(1, c+1)]
    krafts = [1/2**w for w in weights]
    print(weights)
    print(krafts)
    print("kraft sum = ", sum(krafts))
    print("free kraft = ", 1-sum(krafts))
    print("free kraft - 1/2**(4/5) = ", 1-sum(krafts)-1/2**(4/5))
