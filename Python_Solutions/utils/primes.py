from collections import Counter


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


def prime_numbers_between_range(number):
    """Returns all the prime numbers up to the given number"""
    primes = []
    for p in range(number):
        if is_prime(p):
            primes.append(p)
    return primes


def prime_factors(number):
    """Returns the prime-factor of a given number"""
    p = 2
    primes = []
    while number >= p**2:
        if number % p == 0:
            number = number/p
            primes.append(p)
        else:
            p = p+1
    # The remainder is the final prime number.
    primes.append(int(number))
    return primes


def number_of_factors(number):
    """ You can find the number of factors/divisors of a given number by first
    finding the prime factors. ie N = p_1^a * p_2^b * p_3^b;
    Then the factors = (a+1)(b+1)(c+1)... since every factor can occur zero upto
    "a" (or b,c..) times
    Eg: 12 = 2^2 * 3^1 so number of factors = 3*2 = 6; 
    which are 1,2,3,4,6,12
    """
    prime_factors_count = dict(Counter(prime_factors(number)))
    factors_count = 1
    for key, value in prime_factors_count.items():
        factors_count *= value+1
    return factors_count


if __name__ == "__main__":
    print(number_of_factors(76576500))
