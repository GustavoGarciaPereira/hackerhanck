def funcao(val):
    return val[1]


def funcao_nome(val):
    return val[0]


def ordena(name, score):
    lista = [[name[i], score[i]] for i in range(len(name))]
    lista.sort(key=funcao_nome)
    lista.sort(key=funcao)
    listaa = [lista[i][1] for i in range(len(name))]
    listaa = list(set(listaa))
    listaa.sort()
    
    num = listaa[1]
    lista_f = [lista[i][0] for i in range(len(name)) if lista[i][1] == num]
    for i in lista_f:
        print(i)


if __name__ == '__main__':

    name = [
        'Harry',
        'Berry',
        'Tina',
        'Akriti',
        'Harsh'
        # 'Harsh',
        # 'Beria',
        # 'Varun',
        # 'Kakunami',
        # 'Vikas',
    ]
    score = [
        37.21,
        37.21,
        37.21,
        41,
        39,

        # 20,
        # 20,
        # 19,
        # 19,
        # 21,
    ]

    ordena(name, score)
