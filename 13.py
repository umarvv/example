sonlar = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

sonlar = [a[::-1] + (100, ) for a in sonlar]
print(sonlar)