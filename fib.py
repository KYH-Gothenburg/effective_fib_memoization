import time


def fib_effective(n, mem={}):
    if n == 0 or n == 1:
        return n
    if n-1 in mem:
        n1 = mem[n-1]
    else:
        n1 = fib_effective(n - 1)
        mem[n-1] = n1
    if n-2 in mem:
        n2 = mem[n-2]
    else:
        n2 = fib_effective(n - 2)
        mem[n-2] = n2

    return n1 + n2


def fib_ineffective(n):
    if n == 0 or n == 1:
        return n
    return fib_ineffective(n-1) + fib_ineffective(n-2)


def main():
    start = time.time()
    print(fib_ineffective(36))
    end = time.time()
    print("Ineffective fib took", end-start, "seconds")
    start = time.time()
    print(fib_effective(36))
    end = time.time()
    print("Effective fib took", end-start, "seconds")


if __name__ == '__main__':
    main()
