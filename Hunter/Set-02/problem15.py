from math import inf

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    super_star = max(arr)
    arr.append(-inf)
    sol = []
    for i in range(n-1,-1,-1):
        if arr[i] == super_star:
            sol.insert(0,arr[i])
            break
        else:
            if arr[i] > max(arr[i+1:]):
                sol.insert(0,arr[i])
    print(*sol)
    print(super_star)


main()