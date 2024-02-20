def tub_b(N):
    def tekshirish(x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    found = 0
    i = 2
    while found < N:
        if not tekshirish(i):
            yield i
            found += 1
        i += 1

N = int(input("Ixtiyoriy son kiriting: "))
for num in tub_b(N):
    print(num)
