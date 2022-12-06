import string

a = []
ab = []

# a = ['c']
# a = ['c','b','c']
# a = ['c','b','a','b','c']

# print('-'.join(a))

for i in reversed(range(0,5)):
    a.insert(0, string.ascii_lowercase[i])
    esquerda = '-'.join(list(reversed(a)))
    direita = '-'.join(a[1:])
    # print(f{})
    print("{}-{}".format(esquerda, direita).center(17,'-'))
# '-'.join(a[1:])

a = []



for i in range(1,5):
    print(string.ascii_lowercase[i].center(17,'-'))
    # a.insert(0, string.ascii_lowercase[i])
    # esquerda = '-'.join(list(reversed(a)))
    # direita = '-'.join(a[1:])
    # # print(f{})
    # print("{}-{}".format(esquerda, direita).center(17,'-'))