my_list = [5,4,3]

my_list2 = [(5,3),(0,0), (5,6),(3,2)]

print(list(map(lambda item:item*item, my_list)))
my_list2.sort(key = lambda item:item[1])
print(my_list2)
