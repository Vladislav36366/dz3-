numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
one = []
for i in numbers:
    is_prime = True
    if i == 1:
        one = i
        continue
    if i < 2:
        is_prime = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)

