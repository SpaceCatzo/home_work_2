# First task

var = 'PyCharm'

var_len = len(var)

index = int(var_len / 2)

if var_len % 2 != 0:
    print(var[index])
else:
    print(var[index - 1: index + 1])


# Second task

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

perfect_pairs = zip(boys, girls)

if len(boys) == len(girls):
    print('Perfect pairs:')
    for element in perfect_pairs:
        print(element)
else:
    print('Attention! Someone might be left alone!')

