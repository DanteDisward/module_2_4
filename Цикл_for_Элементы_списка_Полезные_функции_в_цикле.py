#numbers = range(1, 200) #Для теста
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for item in numbers:
    remains = 0
    for i in range(item, 0, -1):
        if item % i == 0:
            remains += 1
        if remains > 2:
            break
    if remains > 2:
        not_primes.append(item)
    elif remains == 2:
        primes.append(item)
print(primes)
print(not_primes)