list1 = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d')]

list1 = [t for t in list1 if t]
print(list1)