import sys
input = sys.stdin.readline


def sol():
    global minN
    n = int(input())
    minN = 1e9

    for i in range(1, n):
        curr = str(i)
        tmp = i
        for j in range(len(curr)):
            tmp += int(curr[j])
        if tmp == n:
            if tmp < minN:
                minN = i
    if minN == 1e9:
        print(0)
    else:
        print(minN)


sol()
