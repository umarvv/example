def func(matn):
    sozlar = matn.split()

    for i in range(len(sozlar)):
        if len(sozlar[i]) % 2 != 0:
            sozlar[i] = sozlar[i][::-1]
    natija = ' '.join(sozlar)
    return natija

matn = input('Matnni kiriting: ')
print(func(matn))