a = [1, 5, 15, 25, 10]
primes = []
not_primes = []
for i in a:
    is_a = True
    for j in range(2, i):
        if i % j == 0:
            is_a = False
    if is_a:
        primes.append(i)
    else:
        not_primes.append(i)

print(primes)
print(not_primes)