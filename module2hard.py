def generate_passworld(n):
    passworld = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                passworld += str(i) + str(j)
    return passworld
for n in range(3, 21):
    passworld = generate_passworld(n)
    print(f'{n} - {passworld}')
    