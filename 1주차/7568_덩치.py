import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    a = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append((x, y))

    cnt = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[j][0] > a[i][0] and a[j][1] > a[i][1]:
                cnt[i] += 1

    for i in range(n):
        print(cnt[i]+1, end=" ")


sol()
