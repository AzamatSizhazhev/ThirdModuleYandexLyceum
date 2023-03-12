def is_prime(n):
    if type(n) != int:
        raise TypeError
    if n < 2:
        raise ValueError
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    num = input()
    try:
        num = int(num)
        if is_prime(num):
            print('YES')
        else:
            print('NO')
    except ValueError or TypeError:
        print('NO')
