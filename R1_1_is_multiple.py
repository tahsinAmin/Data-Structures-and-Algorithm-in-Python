def is_multiple(n, m):
    for i in range(n):
        # print("Value of i is %d" %i)
        if (i*m) == n:
            return True
        if (i*m) > n:
            return False


n, m = list(map(int, input().split()))
flag = is_multiple(n, m)
print(flag)
