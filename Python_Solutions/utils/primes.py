def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    pass


def prime_numbers_between_range(number):
    primes = []
    for p in range(number):
        if is_prime(p):
            primes.append(p)
    return primes


def prime_factor(number):
    p = 2
    primes = []
    while number >= p**2:
        if number % p == 0:
            number = number/p
            primes.append(p)
        else:
            p = p+1
    # finally the number remaining is the largest prime factor
    primes.append(int(number))
    return primes
