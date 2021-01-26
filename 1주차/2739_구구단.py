import sys
input = sys.stdin.readline


def sol():
    n = int(input())

    for i in range(1, 10):
        print("%d * %d = %d" % (n, i, n*i))


sol()
