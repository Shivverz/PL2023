import re


valid_coins = ['10c', '20c', '50c', '1e', '2e']
invalid_coins = []
balance = 0
euros = 0
cents = 0
phone_number = None
poor = False

opt = input("maq: Bem vindo ao sistema Public Cabine!\nmaq: Por favor insira, \"LEVANTAR\" para iniciar a sua experiência:")

while opt != "LEVANTAR":
    opt = input("maq: " + opt + " não é uma opção válida no momento!\nmaq: Por favor insira, \"LEVANTAR\" para iniciar a sua experiência:")

while True:
    if balance == 0:
        print("maq: Introduza moedas.")

    opt = input()
    choice = re.findall(r'(\w+)=?', opt)
    
    if choice[0] == "T":
        choice.pop(0)
        phone_number = re.search(r'(\d{2})?(\d{3})(\d{3})(\d{3})', choice[0])

        if phone_number.group(1) == "00" and len(choice[0]) != 11 or phone_number.group(1) != "00" and len(choice[0]) != 9:
            print("maq: Número inválido. Queira discar novo número!")
        else:
            poor = False
            
            if phone_number.group(2) == "601" or phone_number.group(2) == "641":
                print("maq: Esse número não é permitido neste telefone. Queira discar novo número!")
            
            if phone_number.group(1) == "00" and balance >= 150:
                balance -= 150
            elif phone_number.group(2)[0] == "2" and balance >= 25:
                balance -= 25
            elif phone_number.group(2) == "808" and balance >= 10:
                balance -= 10
            elif phone_number.group(2) == "800": balance -= 0
            else:
                print("maq: Saldo insuficiente! Necessita de mais crédito para realizar esta chamada!")
                poor = True

            if not poor:
                euros = int(balance / 100)
                cents = int(balance // 10 % 10 * 10 ) + int(balance % 10)

                if euros != 0:
                    print("maq: saldo = " + str(euros) + 'e' + str(cents) + 'c')
                else:
                    print("maq: saldo = " + str(cents) + 'c')
          

    elif choice[0] == "MOEDAS":
        choice.pop(0)

        for coin in choice:
            if coin not in valid_coins:
                invalid_coins.append(coin)
            elif coin[-1] == "e": 
                balance += int(re.findall(r'\d+', coin)[0]) * 100
            else:
                balance += int(re.findall(r'\d+', coin)[0])

        euros = int(balance / 100)
        cents = int(balance // 10 % 10 * 10 ) + int(balance % 10)
        if euros != 0:
            print("maq:" + ' '.join(invalid_coins) + " - moeda(s) inválida(s); saldo = " + str(euros) + 'e' + str(cents) + 'c')
        else:
            print("maq:" + ' '.join(invalid_coins) + " - moeda(s) inválida(s); saldo = " + str(cents) + 'c')
            
        invalid_coins = []

    elif opt == "POUSAR" or opt == "ABORTAR": break
    else:
        print("Opção inválida!")


if euros != 0:
    print("maq: troco = " + str(euros) + 'e' + str(cents) + 'c; Volte sempre!')
else:
    print("maq: troco = " + str(cents) + 'c; Volte sempre!')