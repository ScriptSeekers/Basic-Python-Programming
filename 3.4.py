i = 2
while i <= 100:
    prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            prime = False
            break
    if prime:
        print('Prime num', i)
    i += 1
