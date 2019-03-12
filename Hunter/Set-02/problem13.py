def main():
    s = input()
    stack = []
    mark = True
    n = len(s)
    for i in range((n//2)):
        stack.append(s[i])
    for i in range((n//2),n):
        if s[i] != stack.pop():
            print('NO')
            mark = False
            break
    if mark:
        print('YES')
main()