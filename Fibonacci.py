# Ü3. Fibonacci Zahlen (mittel)

import time
from prettytable import PrettyTable

def rec_fib(n):
    if n == 1 or n == 2:
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

def rec_fib_time(n):
    start = time.time()
    rec_fib(n)
    end = time.time()
    duration = end - start
    return round(duration,4)


def it_fib(n):
    start = time.time()
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    end = time.time()
    duration = end - start
    return round(duration,4)

table = PrettyTable(["fib(n)", "iter", "rec"])
for i in range(35,41):
    table.add_row([i, it_fib(i), rec_fib_time(i)])
print(table)

