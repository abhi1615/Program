def display(sol):
    for i in sol:
        print(i , end='')

def main():
    s = input()
    res = []
    for i in s:
        if i == ' ':
            res.append(i)
            display(res)
            res = []
        else:
            res.insert(0,i)
    display(res)
main()