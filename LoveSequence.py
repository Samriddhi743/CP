
n = int(input())
v = list(map(int, input().split()))
l = [0] * n
m = [0] * n
l[0] = 0
m[n - 1] = 0
p = 0
for i in range(1, n):
    if v[i] <= v[i - 1]:
        l[i] = i - p
        p = i
    else:
        l[i] = i - p
p = n - 1
for i in range(n - 2, -1, -1):
    if v[i] >= v[i + 1]:
        m[i] = p - i
        p = i
    else:
        m[i] = p - i
ans = 0
for i in range(n):
    if i > 0 and i < n - 1 and v[i + 1] - v[i - 1] > 1:
        ans = max(ans, l[i] + m[i] + 1)
    else:
        ans = max(ans, 1 + l[i], 1 + m[i])
    print(ans)