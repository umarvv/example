def tartib(matn):
    sozlar = matn.split()

    sozlar.sort(key = lambda x: x[0].lower())

    return ' '.join(sozlar)

print(tartib(input("matnni kiriting: ")))