n = int(input())
a = list(map(int, input().split()))
sum_arr = [0] * (n + 1)
ans = 0
for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i - 1] + a[i - 1]
for i in range(1, n):
    if sum_arr[i] == sum_arr[n] - sum_arr[i]:
        ans += 1
print(ans)