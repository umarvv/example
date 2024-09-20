import math

def tub_sonmi(son):
    if son < 2:
        return False
    for i in range(2, int(math.sqrt(son)) + 1):
        if son % i == 0:
            return False
    return True

son = int(input("Sonni kiriting: "))

if tub_sonmi(son):
    print(f"{son} tub son")
else:
    print(f"{son} tub son emas")

#masalani to'liq bajara olmadim faqat shungacha