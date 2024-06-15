my_dict = {'Artem': 1988, 'July': 2002, 'Tommy': 2023}
print(my_dict)
print(my_dict['Tommy'])
print(my_dict.get('Tim'))
my_dict.update ({'Tany': 2002, 'Olya': 1970})
print(my_dict)
del my_dict['Artem']
print(my_dict)

set_ = {1, 2, 2, 3, 4, 1, 5}
print(set_)
list_ = [10, 12]
set_.update(list_)
print(set_)
print(set_.discard(1))
print(set_)