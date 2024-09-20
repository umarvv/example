list1 = [int(x) for x in input("1-listni kiriting ").split()]
list2 = [int(x) for x in input("2-listni kiriting: ").split()]
list3 = [int(x) for x in input("3-listni kiriting: ").split()]
list4 = [int(x) for x in input("4-listni kiriting: ").split()]

lists = [list1, list2, list3, list4]

max = max(lists, key=sum)

print(max)
