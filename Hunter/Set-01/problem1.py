n = int(input())
arr = list(map(int,input().split()))
arr.sort()
res = []
for i in range(n-1):
    if (arr[i] not in res) and arr[i]==arr[i+1]:
        res.append(arr[i])
if len(res) == 0:
    print("unique")
else:
    print(*res)