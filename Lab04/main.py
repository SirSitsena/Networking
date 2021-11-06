def fibonacci(number):
    fib1, fib2 = 0, 1
    while fib2 < number:
        yield fib2
        fib1, fib2 = fib2, fib1+fib2

if __name__ == "__main__":
    for i in fibonacci(1000000):
        print(i)