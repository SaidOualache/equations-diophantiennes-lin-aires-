def is_prime(n):
    """Kanchofo wach premier wla la b3da"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



num = int(input("entrer un nombre entre 1 to 100: "))

# kan 9ado variables li han7tajo
numbers = list(range(num + 1))
deleted = [False] * (num + 1)

# Print liste lwla
print("\nListe initial:")
print(*numbers[1:])

p = 2  # kanbdaw b juj

while p * p <= num:
    if not deleted[p]: 
        # knms7o P w moda3afat tw3ha
        for multiple in range(p, num + 1, p):
            deleted[multiple] = True
        
        print("\nmn mor mams7na", p, "w moda3afat dyawlha:")
        line = []
        for i in range(1, num + 1):
            if deleted[i]:
                line.append("X")
            else:
                line.append(str(i))
        print(" ".join(line))

    # doz ra9m li morah
    p += 1

# Final primes
print("\nNombres premiers :")
print([i for i in range(2, num + 1) if is_prime(i)])
