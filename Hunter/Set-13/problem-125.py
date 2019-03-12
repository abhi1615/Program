if __name__ == "__main__":
    s = input()
    con = []
    a=s
    for i in s:
        if i in con:
            a=a.replace(i,'')
        else:
            con.append(i)
    print(a)
