n = 10
for i in range(n):
    print(" " * (n - i), end="")
    print(" *" * i)
    
for i in range(n):
    print(" " * i, end="")
    print(" *" * (n - i))