def para(x, y, z, n):
    lista = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
    return lista


if __name__ == '__main__':
    x = 3#int(input())
    y = 3#int(input())
    z = 3#int(input())
    n = 1#int(input())
    print(para(x, y, z, n))