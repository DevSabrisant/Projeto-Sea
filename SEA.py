import calendar
from datetime import date


#Criando o Calendario que não serviu pra krlh nenhum
def switch_case(month):
    switch = {
        1: 31,  # janeiro
        2: 29 if date.today().year % 4 == 0 else 28,  # fevereiro
        3: 31,  # março
        4: 30,  # abril
        5: 31,  # maio
        6: 30,  # junho
        7: 31,  # julho
        8: 31,  # agosto
        9: 30,  # setembro
        10: 31, # outubro
        11: 30, # novembro
        12: 31, # dezembro

    }
    data_hoje = date.today()
    mes_cont = switch_case(data_hoje.month)
    return switch.get(month, "Erro: Mês inválido")

#VALORES DOS PLANOS
def plan250 ():
    return 110/30
def plan350 ():
    return 130/30
def plan450 ():
    return 160/30
def plan700 ():
    return 210/30

data_hoje = date.today() ##PEGANDO LOGO A DATA DE HOJE PRA SAPORRA TODA

#FUNÇÕES DE CACULO DE VENCIMENTO
def Calcularven1(pAtual, pNovo):

    Day = data_hoje.day - 1
    DayPlAtual = globals()[f"plan{pAtual}"]() * (data_hoje.day - 1)
    RestanteDayNovo = 31 - data_hoje.day
    DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

    ValorTotal = DayPlAtual + DayPlNovo

    IniConsumo = date(date.today().year,date.today().month,1)
    IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
    Ate = date(date.today().year, date.today().month, Day)
    AteBr = Ate.strftime("%d/%m/%Y")

    #SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
    SLA, quantidade_dias = calendar.monthrange( data_hoje.year,data_hoje.month)
    FinalConusmo = date(data_hoje.year,data_hoje.month, quantidade_dias)
    FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

    print(f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal-(ValorTotal*0.1):.2f}.\nDesconto de: {ValorTotal*0.1:.2f} ")

    return "FIM"
def Calcularven2(pAtual, pNovo):
        # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 10:
            Day = data_hoje.day + 19
            DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 31 - (data_hoje.day + 20)
            DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month-1, 11)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day-1)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            print(f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal-(ValorTotal*0.1):.2f}.\nDesconto de: {ValorTotal*0.1:.2f}  ")


            return "FIM"
        # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        elif data_hoje.day >= 10:
            Day = data_hoje.day - 10
            DayPlAtual = (data_hoje.day - 10) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 30 - (data_hoje.day - 10)
            DayPlNovo = (30 - (data_hoje.day - 10)) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month, 11)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
            AteBr = Ate.strftime("%d/%m/%Y")

            ProxAtual = (data_hoje.month % 12) + 1
            FinalConusmo = date(data_hoje.year +1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            print(f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal-(ValorTotal*0.1):.2f}.\nDesconto de: {ValorTotal*0.1:.2f}")


            return "FIM"
def Calcularven3(pAtual, pNovo):
         # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
        if data_hoje.day <= 20:
            Day = data_hoje.day + 9
            DayPlAtual =  (data_hoje.day + 9) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 31 - (data_hoje.day + 10)
            DayPlNovo = (31 - (data_hoje.day + 10)) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month - 1, 21)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, 20)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            print(f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal-(ValorTotal*0.1):.2f}.\nDesconto de: {ValorTotal*0.1:.2f}  ")
            return "FIM"


         # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
        elif data_hoje.day >= 20:
            Day = data_hoje.day - 20
            DayPlAtual = (data_hoje.day - 20) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 30 - (data_hoje.day - 20)
            DayPlNovo = (30 - (data_hoje.day - 20)) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month, 21)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
            AteBr = Ate.strftime("%d/%m/%Y")

            ProxAtual = (data_hoje.month % 12) + 1
            FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 20)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            print(f"{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal-(ValorTotal*0.1):.2f}.\nDesconto de: {ValorTotal*0.1:.2f} ")


            return "FIM"
'''def Mudancaven1(pVen, pVenNovo):

    if (pVen == 5 or 10):
        IniConsumo = date(date.today().year, date.today().month, 1)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")

        # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
        SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)

        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        print(IniConsumoBr,FinalConusmoBr,"5 e 10")

    elif (pVen == 15 or 20):
        IniConsumo = date(date.today().year, date.today().month - 1, 11)
        IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")

        FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        print(IniConsumoBr, FinalConusmoBr)

        return "FIM"

    return  "FIM MUDANCAVEN1"'''

#SWITCH PARA VENCIMENTO
def venc(pVen):
    if pVen in {5, 10}:
        return Calcularven1(pAtual, pNovo)  # VENCIMENTO 5 OU 10
    elif pVen in {15, 20}:
        return Calcularven2(pAtual, pNovo)  # VENCIMENTO 15 OU 20
    elif pVen in {25, 30}:
        return Calcularven3(pAtual, pNovo)  # VENCIMENTO 25 OU 30
    else:
        return "Opção de vencimento inválida"


#ENTRADA DE DADOS
while True:
        pAtual = int(input("Qual seu plano Atual?(250,350,450,700): "))
        if pAtual in {250,350,450,700}:
            break
        else:print("Por favor, insira um plano válido.")
while True:
        pNovo = int(input("Qual seu novo plano?(250,350,450,700): "))
        if pNovo in {250,350,450,700}:
            break
        else:print("Por favor, insira um novo plano válido.")
while True:
        pVen = int(input("Qual vencimento?(05, 10, 15, 20, 25 ou 30): "))
        if pVen in {5, 10, 15, 20, 25, 30}:
            print(venc(pVen))
            break
        else:print("Por favor, insira um vencimento válido.")

def MudarVen(pVen, pVenNovo):
    #QUANTIDADE DE DIAS NO MÊS
    quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]

    #PROXIMO MÊS
    ProxAtual = (data_hoje.month % 12) + 1

    # CICLO DE 01 ATÉ 30

    IniVenc01 = date(date.today().year, date.today().month, 1)
    IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
    FinalVenc30 = date(data_hoje.year +1 if ProxAtual == 1 else data_hoje.year, date.today().month, quantidade_dias)
    FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

    # CICLO DE 11 ATÉ 10

    IniVenc11 = date(date.today().year, date.today().month, 11)
    IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
    FinalVenc10 = date(data_hoje.year +1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 10)
    FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

    # CICLO DE 21 ATÉ 20

    IniVenc21 = date(date.today().year, date.today().month, 21)
    IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
    FinalVenc20 = date(data_hoje.year +1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1, 20)
    FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

    # CONDIÇÕES DE TROCA DE VENCIMENTO
    if (pVen == 5 or pVen == 10) and (pVenNovo == 5 or pVenNovo == 10):
        print(f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA")

    if (pVen == 5 or pVen == 10) and (pVenNovo == 15 or pVenNovo == 20):
        QtdDias = FinalVenc10 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()
        print(f"{IniVenc01Br} -- {FinalVenc30Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")
    elif (pVen == 5 or pVen == 10) and (pVenNovo == 25 or pVenNovo == 30):
        QtdDias = FinalVenc20 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()
        print(f"{IniVenc01Br} -- {FinalVenc20}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")

    # VENCIMENTO 15 OU 20
    elif (pVen == 15 or pVen == 20) and (pVenNovo == 15 or pVenNovo == 20):
        print(f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA")
    elif (pVen == 15 or pVen == 20) and (pVenNovo == 25 or pVenNovo == 30):
        QtdDias = FinalVenc20 - IniVenc11
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()
        print(f"{IniVenc11Br} -- {FinalVenc20Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")
    elif (pVen == 15 or pVen == 20) and (pVenNovo == 5 or pVenNovo == 10):
        QtdDias = FinalVenc30 - IniVenc11    #quantidade de dias
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()
        print(f"{IniVenc11Br} -- {FinalVenc30Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")

    # VENCIMENTO 25 OU 30
    elif (pVen == 25 or pVen == 30) and (pVenNovo == 25 or pVenNovo == 30):
        print(f"NÃO TERÁ MUDANÇA NO VALOR DA FATURA")
    elif (pVen == 25 or pVen == 30) and (pVenNovo == 25 or pVenNovo == 30):
        QtdDias = FinalVenc20 - IniVenc11
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()

        print(f"{IniVenc21Br} -- {FinalVenc10Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")
    elif (pVen == 25 or pVen == 30) and (pVenNovo == 5 or pVenNovo == 10):
        QtdDias = FinalVenc20 - IniVenc01
        Valor = QtdDias.days * globals()[f"plan{pAtual}"]()
        print(f"{IniVenc21Br} -- {FinalVenc30Br}. São {QtdDias.days} dias -- totalizando: {Valor:.2f}")

    return "FIM"


Escolha = int(input("Deseja mudar de vencimento?:1(SIM) 2(NÃO)"))
if Escolha == 1:
        while True:
                pVenNovo = int(input("Qual Novo vencimento?(05, 10, 15, 20, 25 ou 30): "))
                if pVenNovo in {5, 10, 15, 20, 25, 30}:
                    print(MudarVen(pVen,pVenNovo))
                    break
                else:print("Por favor, insira um vencimento válido.")
else: print("FIM")








