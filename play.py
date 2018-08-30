def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))

'''
def factorial(n):
    if n <= 1:
        return 1
        
    return n * factorial(n - 1)

'''
# fibonacci nums:
# 1, 1, 2, 3, 5, 8, 13, 21, ...


def fib_num(limit):
    nums = []

    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums


for n in fib_num(100):
    print(n, end=',')


def fib_num_co(limit):
    current = 0
    next = 1
    while current < limit:
        current, next = next, next + current
        yield current


for n in fib_num_co(100):
    print(n, end=',')
