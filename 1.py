def juft(a, b):
    sonlar = [x for x in range(a, b) if x % 2 == 0 ]
    return sonlar

a = int(input("A sonini kiriting: "))
b = int(input("B sonini kiriting: "))

natija = juft(a, b)
print(natija)