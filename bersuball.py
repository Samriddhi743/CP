n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()
b.sort()
pairs = 0
for i in range(n):
    for j in range(m):
        if abs(a[i] - b[j]) < 2:
            b[j] = 1000
            pairs += 1
            break
print(pairs)