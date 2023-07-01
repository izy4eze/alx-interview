def Pascal_triangle(n):
    for line in range(0, n) :
        for i in range(0, line + 1) :
            print(binomialCoeff(line, i),
                " ", end = "")

            def binomialCoeff(n, k) :
    res = 1
    if (n <= 0) :
        return n()
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
     return res

 n = 7
Pascal_triangle(n)

