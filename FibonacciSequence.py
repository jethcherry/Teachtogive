# Write a program to generate the Fibonacci sequence up to 100.


def fibonacci(limit):
    sequence = [0, 1]

    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

fib_100 = fibonacci(100)

print("Fibonacci :")
print(fib_100)


