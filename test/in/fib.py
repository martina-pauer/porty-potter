def fibonacci(n):
    if n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 2)

print(fibonacci(10))