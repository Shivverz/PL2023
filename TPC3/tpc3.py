import re


def al_1():
    # Alínea a)
    with open('processos.txt') as file:
        content = file.read()
        year = dict()

    for elem in re.findall(r':(\d+)', content):
        if not year.get(elem, None):
            year[elem] = 1
        else:
        year[elem] += 1

    year = dict(sorted(year.items(), key=lambda item: item[0]))
    print(year)
        

def al_2():
    # Alínea b)
    with open('processos.txt') as file:
        content = file.read()
        centuries = dict()

    # TODO: Pensar se o findall é a melhor opção para resolver o problema
    for elem in re.findall(r':(\w+)|([a-zA-Z]+)[:,]', content):
    first, surname = elem
    
    if first != '':
        if first.isnumeric():
            current = str((int(first)) // 100 + 1)
            if not centuries.get(str(current), None):
                centuries[current] = (dict(), dict())
        else:
            #print(first)
            if not centuries[current][0].get(first, None):
                centuries[current][0][first] = 1
            else:
                centuries[current][0][first] += 1
    elif surname != '':
        if not centuries[current][1].get(surname, None):
            centuries[current][1][surname] = 1
        else:
            centuries[current][1][surname] += 1

    for century in centuries.keys():
        first_names, last_names = centuries[century]
        first_names = dict(sorted(first_names.items(), key=lambda item: 1/item[1])[:5])
        last_names = dict(sorted(last_names.items(), key=lambda item: 1/item[1])[:5])
        centuries[century] = (first_names, last_names)

    centuries = dict(sorted(centuries.items(), key=lambda item: item[0]))
    print(centuries)


def al_3():
    # Alínea c)
    with open('processos.txt') as file:
        content = file.read()
        relatives = dict()

    for elem in re.findall(r'(?i:irmao)|(?i:irma)|(?i:tio)|(?i:tia)|(?i:primo)|(?i:prima)|(?i:pai)|(?i:mae)|(?i:avo)|(?i:avo)|(?i:sobrinho)|(?i:sobrinha)', content):
        elem = elem.lower()
        if not relatives.get(elem, None):
            relatives[elem] = 1
        else:
            relatives[elem] += 1

    relatives = dict(sorted(relatives.items(), key=lambda item: 1/item[1]))
    print(relatives)