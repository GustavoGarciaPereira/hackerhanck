import operator


def person_lister(f):
    def idade(lista):
        return int(lista.split(' ')[2])
    def inner(people):
        l = []
        people = people[1:]
        people.sort(key=idade)
        for p in people:
            nome = f"{p.split(' ')[0]} {p.split(' ')[1]}"
            if p.split(' ')[3] == 'F':
                l.append('Ms. '+nome)
            else:
                l.append('Mr. '+nome)
        return l
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    #people = [input().split() for i in range(int(input()))]
    people = ['3',
'Mike Thomson 20 M',
'Robert Bustle 32 M',
'Andria Bustle 30 F'
]
    print(*name_format(people), sep='\n')