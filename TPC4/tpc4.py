import json
import re


def create_labels(line):
    aDict = dict()
    limDict = dict()
    func = None

    for elem in re.finditer(r'(?P<label>\w+)(?:\{(?P<inf>\d+)(?:,(?P<sup>\d+))?\})?(?:::(?P<sub>\w+))?', line):
        key = elem.group('label')

        if not aDict.get(key, None):
            if elem.group('sub'):
                key += '_' + elem.group('sub')
                func = elem.group('sub')

            aDict[key] = None

        if not limDict.get(key, None):
            limDict[key] = (elem.group('inf'), elem.group('sup'))

    return aDict, limDict, func


def setUp_json(aDict, limDict, func, lines):
    # Separação das linhas do ficheiro pelo caracter '\n'
    for line in re.split(r'\n', lines):
        current = 0  # Elemento atual da linha
        arr = []  # Array que armazena a lista a colocar no ficheiro json
        elems = re.findall(r'(\w+(?:[ ]?(\w+))*)', line)

        # Ciclo que percorre todas as labels presentes no ficheiro json e recolhe os respetivos dados
        for key in aDict.keys():
            low, high = limDict[
                key]  # Limites inferior e superior do nº de elementos da lista de valores (caso o presente elemento espere uma lista)

            # Condição que testa se estamos na presença de uma lista existe o nº mínimo de elementos pedidos
            if low and len(elems) - current >= int(low):
                # Definição do limite superior do ciclo que recolha de dados (podemos ter apenas o limite inferior!)
                if high:
                    lim = high
                else:
                    lim = low

                # Ciclo que recolhe os dados da lista (o nº de entradas tem de estar dentro do limite especificado)
                for i in range(int(lim)):
                    if current < len(elems):
                        arr.append(int(elems[current][0]))
                        current += 1
                    else:
                        break

                # Condição que testa se a label atual é uma lista com pelo menos o nº mínimo de elementos requiridos
                if len(arr) >= int(low):
                    # Condição que testa se estamos na presença de uma label com uma função associada
                    if func:
                        if func == 'sum':
                            aDict[key] = sum(arr)
                        elif func == 'media':
                            aDict[key] = sum(arr) / len(arr)
                    else:
                        aDict[key] = arr
            else:
                aDict[key] = elems[current][0]
                current += 1

        print(json.dumps(aDict, indent=2, ensure_ascii=False))  # Escrevemos os dados da nova entrada no ficheiro json


def csv_to_json(filename):
    with open(filename) as file:
        first_line = file.readline()
        lines = file.read()

    aDict, limDict, func = create_labels(first_line)

    setUp_json(aDict, limDict, func, lines)


csv_to_json("alunos5.csv")
