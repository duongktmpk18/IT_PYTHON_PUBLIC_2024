a = tuple(map(int, input().split()))

for i in range(0, len(a) - 1):
    cnt = 0
    if a[i] != a[i + 1] or a[-2] == a[-1]:
        for j in range(0, len(a)):
            if a[i] == a[j]:
                cnt += 1
        if cnt % 5 == 0 and cnt % 10 != 0: 
            print(a[i])
    