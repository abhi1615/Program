def main():
    n = int(input())
    mark = False
    arr = list(map(int,input().split()))
    for i in range(1,n-1):
        if sum(arr[:i]) == sum(arr[i+1:]):
            print('yes')
            mark = True
            break
    if mark == False:
        print('no')

main()