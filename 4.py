def indeks(lst, son):

    natija = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == son:
                natija.append((i, j))

    if natija:
        for i, j in natija:
            print(f"Index: {i}, {j}")

lst = [1, 2, 33, 5, 6, 7, 7]
son = int(input("Sonni kiriting: "))

indeks(lst, son)

