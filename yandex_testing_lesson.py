def is_prime(n):
    counter = 0
    for i in range(2, n):
        if n % i != 0:
            counter += 1
    return counter == n - 2
