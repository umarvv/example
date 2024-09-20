son = input("Son kiriting: ")
matn = input("Matnni kiriting: ")

a = [x for x in son.split(',')]

natija = [f'{matn}{elem}' for elem in a]

print(natija)