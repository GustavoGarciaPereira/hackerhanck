

es = 2
number = 17
for i in range(1, number+1):
    es = len(bin(number+1)[2:])

    print(f"{i}".rjust(es), f"{oct(i)[2:]}".rjust(es), f"{hex(i)[2:]}".upper().rjust(es), f"{bin(i)[2:]}".rjust(es))
    #print(f"{i} {oct(i)[2:]} {hex(i)[2:]} {bin(i)[2:]}")
