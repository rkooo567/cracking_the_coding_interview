def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib[i % 2] = fib[0] + fib[1]
    return fib[n % 2]
n = int(input())
print(fibonacci(n))