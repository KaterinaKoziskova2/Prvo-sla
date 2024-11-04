import time
import math

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def simple_prime_check(n):
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

def compare_prime_algorithms(N_values):
    results = []
    
    for N in N_values:
        start_time = time.time()
        sieve_of_eratosthenes(N)
        sieve_time = time.time() - start_time

        start_time = time.time()
        simple_prime_check(N)
        simple_time = time.time() - start_time

        results.append((N, sieve_time, simple_time))

    return results

N_values = [10**3, 10**4, 10**5, 10**6]

results = compare_prime_algorithms(N_values)

for N, sieve_time, simple_time in results:
    print(f"N = {N}: Eratosthenovo síto = {sieve_time:.6f}s, Jednoduchý algoritmus = {simple_time:.6f}s")
