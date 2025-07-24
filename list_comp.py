simplle_dic = {
    'a': 1,
    'b': 4
}
my_dictionary = {k:v*v for k,v in simplle_dic.items()}
my_list = [num*2 for num in range(1,100) if num %2 == 0]
# print(my_list)
# print(my_dictionary)
some_list = ['a', 'a', 'b', 'c', 'c', 'd', 'g', 'g', 'g']
no_dup = list(set([num for num in some_list if some_list.count(num) > 1]))
print(no_dup)
