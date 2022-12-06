# N, M = input().split()
N, M = 11 , 33
p = '-'
e = ".|."

for i in range(1,N,2):
    print((e*i).center(M, p))

print('WELCOME'.center(M, p))


for i in reversed(range(1,N,2)):
    print((e*i).center(M, p))