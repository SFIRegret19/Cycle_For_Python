numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = [], []
is_prime = True

for element in numbers:
    if element == 1:
        continue
    for divisor in range(2, element):
        if element % divisor == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime == True:
        primes.append(element)
    elif is_prime == False:
        not_primes.append(element)

print(primes, not_primes)