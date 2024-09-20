def toq(a, b):
    sonlar = [x for x in range(b, a-1, -1) if x % 2 != 0]
    return sonlar

a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))


sonlar = toq(a, b)
print(sonlar)
