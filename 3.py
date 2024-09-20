def saralash(list1):
    TEXT = [x for x in list1 if isinstance(x,str)]
    OTHER = [x for x in list1 if not  isinstance(x, str)]

    TEXT.sort()

    OTHER.sort(reverse=True)

    return TEXT, OTHER

list1 = ['salom', 123, True, 'Hayr', 'world', 3.14, '7214']

TEXT, OTHER = saralash(list1)
print("TEXT =", TEXT, "\nOTHER = ", OTHER)