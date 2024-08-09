my_dict = {'Ivan': 2001, 'Tim': 2003, 'Slavik': 2005, 'Dima': 2007}
print('Dict:', (my_dict))
print('Existing value:', (my_dict['Slavik']))
print('Not existing value:', (my_dict.get('JoRa')))
my_dict.update({'Koly': 2009, 'Vasy': 1999})
print('Deleted value:', (my_dict.pop('Ivan')))
print('Modified dictionary:', (my_dict))

my_set = {1,2,3,4,5,1,2,3,4, 'Tin', False, (1,2,3)}
print('Set:',(my_set))
my_set.add('Potato')
my_set.add(6)
my_set.discard(3)
print('Modified set:', (my_set))
