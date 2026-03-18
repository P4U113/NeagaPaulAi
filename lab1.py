name='Paul';
age=21
print(f'eu sunt {name}')
print(f'eu am {age} de ani')
print(2+5)
print(5/5)
print(5*5)
print('I/`m thirsty')
if(7>4):
    print('mai mare')
else:
    print('mai mic')

if (2 > 4 and 8>4) :
        print('adv')
else:
        print('fls')

print('i`m alone     '.strip())
print('i-m alone'.strip('a'))
print('afdsdaw dawdafds fsefsdfse sefefs'.split())

a='afdsdaw dawdafds fsefsdfse sefefs'.split()
b='jnewjaneja w dikajwdoiawd wadioahnwd'.split()

print(len(a))


print(bool(2>1))
print(bool(2>6))
print(bool(len(a)>len(b)))
my_dict = {'name': 'Neaga', 'age': 21, 'magic_power': False}

print(my_dict['name'])
print(len(my_dict))
list(my_dict.keys())
list(my_dict.values())
list(my_dict.items())

my_dict['favourite_snack'] = 'Grapes'

my_dict.get('age')
my_dict.get('ages', 0)

my_tuple = ('mar', 'pere', 'mango', 'pere')

mar, pere, mango, pere = my_tuple

print(len(my_tuple))

my_tuple[2]

print(my_tuple.count('pere'))

new_list = [1,2,3,3,3,4,4,5,6,1]

set(new_list)

print(new_list)
print(new_list.remove(1))
set1 = {1,2,3}

set2 = {3,4,5}
set3= set1.union(set2)
print(set3)

set4 = set1.intersection(set2)
print(set4)
set5 = set1.difference(set2)

set6 = set1.symmetric_difference(set2)

set1.issubset(set2)

set1.issuperset(set2)
print(set1)
set1.isdisjoint(set2)
