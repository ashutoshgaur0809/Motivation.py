`T = int(input("Enter No. of test cases = "))
for i in range(T):
    r = []
    s = []
    X = int(input("Enter size of memory in GB = "))
    N = int(input("Enter No. of films = "))

    for j in range(N):
        a = int(input("Enter Movie Space reqment = "))
        b = int(input("enter rating of movie = "))
        if (a <= X):
            s.append(a)
            r.append(b)
            r.sort()
    print("So the good rating is  = ", r[-1])
