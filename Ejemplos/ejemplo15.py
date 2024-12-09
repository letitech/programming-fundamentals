n = 10

for i in range(n):
    if i == 0:
        print("*" * n)
    elif i == n - 1:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" " * (n - 2), end="")
        print("*")