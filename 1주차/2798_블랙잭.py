import sys
input = sys.stdin.readline


def sol():
    global maxN
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    maxN = -1e9

    def dfs(L, s, tot):
        global maxN
        if tot > m:
            return
        if L == 3:
            if tot > maxN:
                maxN = tot
        else:
            for i in range(s, n):
                dfs(L+1, i+1, tot+a[i])

    dfs(0, 0, 0)
    print(maxN)


sol()
