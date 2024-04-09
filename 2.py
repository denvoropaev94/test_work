def prime_numbers(min, max):
    primes = []
    for num in range(min, max + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0: 
                    break
            else:
                primes.append(num)
    return primes

print(prime_numbers(10, 20))