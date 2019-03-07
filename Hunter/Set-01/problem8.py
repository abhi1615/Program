n = int(input())
list = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if (list[i]+list[j]) in list:
            print(list[i], list[j], list[i]+list[j])

