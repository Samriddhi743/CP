N = 10**6 + 1
n = int(input())
a = list(map(int, input().split()))
cs = [0] * N
for i in range(n):
    a[i] = int(a[i])
    cs[i] -= 1
    cs[max(0, i - a[i])] += 1
for i in range(1, n):
    cs[i] += cs[i-1]
cnt = 0
for i in range(n):
    if cs[i] == 0:
        cnt += 1
print(cnt)