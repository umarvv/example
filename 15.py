list1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

sorting = sorted(list1, key = lambda x: float(x[1]), reverse=True)

print(sorting)
