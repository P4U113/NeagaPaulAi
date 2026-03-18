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