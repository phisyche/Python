def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

def iterative_factorial(n):
    a = 1
    list1 = list(range(1, n + 1))
    for each in range(1,n + 1):
        a = a * each
    return a
