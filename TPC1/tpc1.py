import math


def file_parser():
    with open('myheart.csv') as file:
        content = file.read()

    lines = content.split("\n")
    lines.pop(0)
    lines.pop(len(lines) - 1)
    data = []

    for line in lines:
        data.append(line.split(','))

    return data


def infected_by_gender():
    data = file_parser()
    struct = {'M': (0, 0), 'F': (0, 0)} # Cada key vai estar associada a um tuplo cujo primeiro elemento é o número de infetados e o segundo elemento é o número de ocorrências (total de indivíduos, infetados ou não)

    for _, gender, _, _, _, isInfected in data:
        struct[gender] = (struct[gender][0], struct[gender][1] + 1)
        if int(isInfected):
            struct[gender] = (struct[gender][0] + 1, struct[gender][1])

    #print(struct)
    return struct


# Função que calcula a distribuição da doença em relação a um critério numérico, apresentando os resultados em intervalos específicos
def infected_by_numeric_criteria(criteria, interval):
    data = file_parser()
    struct = dict() # Cada key vai estar associada a um tuplo cujo primeiro elemento é o número de infetados e o segundo elemento é o número de ocorrências (total de indivíduos, infetados ou não)

    for info in data:
        value = int(info[criteria-1]) # Recolhemos o valor do critério desejado
        lower = 0
        higher = interval - 1

        # Verificamos se o valor atual é superior a 0 e recalculamos os limites do intervalo
        # (para evitar obter valores negativos no intervalo que eram obtidos com 0)
        if value > 0:
            lower = interval * (math.ceil(value / interval) - 1)
            higher = (interval * math.ceil(value / interval)) - 1

        key = f"{lower}-{higher}"

        # Verificamos se a chave atual já se encontra no dicionário (retornamos None caso esta não exista)
        if not struct.get(key, None):
            struct[key] = (0, 0)

        struct[key] = (struct[key][0], struct[key][1] + 1)
        if int(info[5]):
            struct[key] = (struct[key][0] + 1, struct[key][1])

    struct = dict(sorted(struct.items(), key=lambda item: int(item[0].split('-')[0]))) # Ordenamos o dicionário por ordem ascendente de intervalos (maior legibilidade)
    #print(struct)
    return struct


def print_distribution(distribution):
    infected = 0
    total_pop = 0
    total_ratio = 0

    print("_"*55)
    print(f"|{' '*9}|  Infetados  |  População  |  Percentagem  |")
    print("-"*55)

    for data in distribution:
        value, population = distribution[data]
        ratio = round((value / population) * 100, 2)

        infected += value
        total_pop += population

        print(f"|{' '*(int((10 - len(data)) / 2))}{data}{' '*(int((9 - len(data)) / 2))}"
              f"|{' '*(int((13 - len(str(value)) ) / 2))}{value}{' '*(int((12 - len(str(value)) ) / 2))} "
              f"|{' '*(int((13 - len(str(population)) ) / 2))}{population}{' '*(int((12 - len(str(population)) ) / 2))} "
              f"|{' '*(int((15 - len(str(ratio)) ) / 2))}{ratio}%{' '*(int((14 - len(str(ratio)) ) / 2))}|")
        print("-"*55)

    total_ratio = round((infected / total_pop) * 100, 2)
    print(f"|  TOTAL  |"
          f"{' '*(int((13 - len(str(infected)) ) / 2))}{infected}{' '*(int((12 - len(str(infected)) ) / 2))} "
          f"|{' '*(int((13 - len(str(total_pop)) ) / 2))}{total_pop}{' '*(int((12 - len(str(total_pop)) ) / 2))} "
          f"|{' '*(int((15 - len(str(total_ratio)) ) / 2))}{total_ratio}%{' '*(int((14 - len(str(total_ratio)) ) / 2))}|")
    print("-" * 55)


print("\033[1m" + '-> DISTRIBUIÇÃO DA DOENÇA POR IDADE' + "\033[0m")
print_distribution(infected_by_numeric_criteria(1, 5))
print("\033[1m" + '-> DISTRIBUIÇÃO DA DOENÇA POR GÉNERO' + "\033[0m")
print_distribution(infected_by_gender())
print("\033[1m" + '-> DISTRIBUIÇÃO DA DOENÇA POR TENSÃO' + "\033[0m")
print_distribution(infected_by_numeric_criteria(3, 15))
print("\033[1m" + '-> DISTRIBUIÇÃO DA DOENÇA POR COLESTEROL' + "\033[0m")
print_distribution(infected_by_numeric_criteria(4, 10))
print("\033[1m" + '-> DISTRIBUIÇÃO DA DOENÇA POR BATIMENTO CARDÍACO' + "\033[0m")
print_distribution(infected_by_numeric_criteria(5, 27))
