def creatingSquare(n):
    shivam = [[0 for x in range(n)]
                   for y in range(n)]
    r = n // 2
    c = n - 1
    num = 1
    while num <= (n * n):
        if r == -1 and c == n:
            c = n - 2
            r = 0
        else:
            if c == n:
                c = 0
            if r < 0:
                r = n - 1
 
        if shivam[int(r)][int(c)]:
            c= c - 2
            r= r+ 1
            continue
        else:
            shivam[int(r)][int(c)] = num
            num = num + 1
 
        c = c + 1
        r = r - 1
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) // 2, "\n")
 
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (shivam[i][j]),
                  end='')


            if j == n - 1:
                print()
 
n = int(input("enter no. of rows and columns"))
creatingSquare(n)