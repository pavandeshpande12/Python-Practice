import time


def timeit(func):
    def timed():
        ts = time.time()
        result = func()
        te = time.time()
        print("Time taken %3.2f ms" % ((te - ts) * 10 * 6))
        return result

    return timed


@timeit
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


num = int(input("Enter the size for Fibonacci series: "))
fibonacci = fib()
for x in range(num):
    print(next(fibonacci))
