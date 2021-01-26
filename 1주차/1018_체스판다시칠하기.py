import sys
input = sys.stdin.readline

case1 = [  # 흰색이 맨왼위
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
]

case2 = [  # 검정색이 맨왼위
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
    ["B", "W", "B", "W", "B", "W", "B", "W"],
    ["W", "B", "W", "B", "W", "B", "W", "B"],
]


def sol():
    n, m = map(int, input().split())
    board = [list(input())[:m] for _ in range(n)]
    minN = 1e9

    for i in range(n-7):
        for j in range(m-7):
            tmp = [board[i+x][j:j+8] for x in range(8)]

            cnt1 = 0
            for k in range(8):
                for l in range(8):
                    if tmp[k][l] != case1[k][l]:
                        cnt1 += 1

            cnt2 = 0
            for k in range(8):
                for l in range(8):
                    if tmp[k][l] != case2[k][l]:
                        cnt2 += 1
            if minN > min(cnt1, cnt2):
                minN = min(cnt1, cnt2)

    print(minN)


sol()
