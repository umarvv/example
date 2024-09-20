def binary(son):

    ikkilik = bin(son)[2:]

    nollar = ikkilik.count('0')

    return nollar

son = int(input("Sonni kiriting: "))

print(binary(son))

#bin foydalandim