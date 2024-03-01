from bisect import bisect_right
n, d = map(int, input().split())
v = list(map(int, input().split()))
ans = 0
for i in range(len(v)):
    pts = bisect_right(v, v[i] + d)
    pts = pts - i - 1
    if pts > 1:
        ans += (pts * (pts - 1)) // 2
print(ans)