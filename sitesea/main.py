
from flask import Flask , render_template, request
import calendar
from datetime import date
app = Flask(__name__)


@app.route("/", methods=['POST','GET'])
def homepage():
    resultado = venc(pVen = request.form.get('vencimento'),pAtual= request.form.get('planoAtual'),pNovo= request.form.get('planoNovo'),checkA=request.form.get('cidadeAnanindeua'))

    return render_template("homepage.html", resultado=resultado)

@app.route("/homepage2",methods=['POST','GET'])
def homepage2():
    resultadoVencimento = MudarVen(vAtual = request.form.get('vencimentoAtual'), vNovo=request.form.get('vencimentoNovo'), vPlano= request.form.get('planoCliente'),checkA=request.form.get('cidadeAnanindeua'))

    return  render_template("homepage2.html", resultadoVencimento = resultadoVencimento)




# PLANOS - CRIA UMA FUNÇÃO NOVA PARA UM PLANO NOVO - SEGUE O PADRÃO K7
def plan500():
    return 110 / 30
def plan600():
    return 130 / 30
def plan700():
    return 160 / 30
def plan800():
    return 210 / 30

data_hoje = date.today()  ##PEGANDO LOGO A DATA DE HOJE PRA SAPORRA TODA

# FUNÇÕES DE CACULO DE PLANO -  AQUI ATÉ O PYTHON DEMORA INTERPRETAR
def Calcularven1(pAtual, pNovo):
    if data_hoje.day != 1:
            Day = data_hoje.day - 1
            DayPlAtual = globals()[f"plan{pAtual}"]() * (data_hoje.day - 1)
            RestanteDayNovo = 31 - data_hoje.day
            DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, date.today().month, 1)
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, Day)
            AteBr = Ate.strftime("%d/%m/%Y")

            # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
            SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
            FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} são totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "

    else:
        RestanteDayNovo = 31 - data_hoje.day
        DayPlNovo = globals()[f"plan{pNovo}"]() * (31 - data_hoje.day)

        # SLA É A VARIAVEL QUE EU NÃO FAÇO A MENOR IDEIA DO QUE FAZ, MAIS EU SÓ PRECISO DA QUANTIDADE DE DIAS ENTT FDS
        SLA, quantidade_dias = calendar.monthrange(data_hoje.year, data_hoje.month)
        FinalConusmo = date(data_hoje.year, data_hoje.month, quantidade_dias)
        FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

        r = f"De {pAtual}mb para {pNovo}mb: \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} dias totalizando: {DayPlNovo:.2f}.\nO valor final será: {DayPlNovo:.2f}.\nCom 10% será: {DayPlNovo - (DayPlNovo * 0.1):.2f}.\nDesconto de: {DayPlNovo * 0.1:.2f} "


    return r
def Calcularven2(pAtual, pNovo):
    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
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
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= 10:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
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
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
    else:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
        else:
                Day = data_hoje.day + 19
                DayPlAtual = (data_hoje.day + 19) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + 20)
                DayPlNovo = (31 - (data_hoje.day + 20)) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, 10)
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
def Calcularven3(pAtual, pNovo,pVen):
    DadosVen = [
        (11, 10, 19, 20) if pVen == "15"
        else (11, 10, 19, 20) if pVen == "20"
        else (21, 20, 9, 10) if pVen == "25"
        else (21, 20, 9, 10) if pVen == "30"
        else None]

    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][2])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= DadosVen[0][1]:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (data_hoje.day - DadosVen[0][1]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (30 - (data_hoje.day - DadosVen[0][1])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f} "
            
                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][2])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= DadosVen[0][1]:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (data_hoje.day - DadosVen[0][1]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (30 - (data_hoje.day - DadosVen[0][1])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
    else:
        if data_hoje.month != 1:
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][2])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][2])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            elif data_hoje.day > DadosVen[0][1]:
                Day = data_hoje.day - DadosVen[0][2]
                DayPlAtual = (data_hoje.day - DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][2])
                DayPlNovo = (30 - (data_hoje.day - DadosVen[0][2])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
        else:
            Day = data_hoje.day + DadosVen[0][2]
            DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
            RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][2])
            DayPlNovo = (31 - (data_hoje.day + DadosVen[0][2])) * globals()[f"plan{pNovo}"]()

            ValorTotal = DayPlAtual + DayPlNovo

            IniConsumo = date(date.today().year, 12, DadosVen[0][0])
            IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
            Ate = date(date.today().year, date.today().month, data_hoje.day)
            AteBr = Ate.strftime("%d/%m/%Y")

            FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
            FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

            r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

            return r
        

def CalculoA(pAtual,pNovo,pVen):

    DadosVen = [(6, 5, 24, 25) if pVen == "5" else (11, 10, 19, 20) if pVen == "10" else (16, 15, 14, 15) if pVen == "15" else (21, 20, 9, 10) if pVen == "20" else (26, 25, 4, 5) if pVen == "25" else None]

    if data_hoje.day != 1:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][3])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= DadosVen[0][1]:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (data_hoje.day - DadosVen[0][1]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (30 - (data_hoje.day - DadosVen[0][1])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
        else:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
            if data_hoje.day <= DadosVen[0][1]:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][3])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, 11)
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
            # RETIRANDO UMA DIA DO PLANO NOVO AQUI POIS ELE ENTRA EM CONTATO DEPOIS DO VENCIMENTO
            elif data_hoje.day >= DadosVen[0][1]:
                Day = data_hoje.day - DadosVen[0][1]
                DayPlAtual = (data_hoje.day - DadosVen[0][1]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 30 - (data_hoje.day - DadosVen[0][1])
                DayPlNovo = (30 - (data_hoje.day - DadosVen[0][1])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day - 1)
                AteBr = Ate.strftime("%d/%m/%Y")

                ProxAtual = (data_hoje.month % 12) + 1
                FinalConusmo = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, ProxAtual, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}"

                return r
    else:
        if data_hoje.month != 1:
            # RETIRANDO UMA DIA DO PLANO ATUAL AQUI POIS ELE ENTRA EM CONTATO ANTES DO VENCIMENTO
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][3])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, date.today().month - 1, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
        else:
                Day = data_hoje.day + DadosVen[0][2]
                DayPlAtual = (data_hoje.day + DadosVen[0][2]) * globals()[f"plan{pAtual}"]()
                RestanteDayNovo = 31 - (data_hoje.day + DadosVen[0][3])
                DayPlNovo = (31 - (data_hoje.day + DadosVen[0][3])) * globals()[f"plan{pNovo}"]()

                ValorTotal = DayPlAtual + DayPlNovo

                IniConsumo = date(date.today().year, 12, DadosVen[0][0])
                IniConsumoBr = IniConsumo.strftime("%d/%m/%Y")
                Ate = date(date.today().year, date.today().month, data_hoje.day)
                AteBr = Ate.strftime("%d/%m/%Y")

                FinalConusmo = date(data_hoje.year, data_hoje.month, DadosVen[0][1])
                FinalConusmoBr = FinalConusmo.strftime("%d/%m/%Y")

                r = f"De {pAtual}mb para {pNovo}mb: \n{IniConsumoBr} -- {AteBr} são {Day} dias totalizando: {DayPlAtual:.2f} \n{data_hoje.strftime('%d/%m/%Y')} -- {FinalConusmoBr} são {RestanteDayNovo} totalizando: {DayPlNovo:.2f}.\nO valor final será: {ValorTotal:.2f}.\nCom 10% será: {ValorTotal - (ValorTotal * 0.1):.2f}.\nDesconto de: {ValorTotal * 0.1:.2f}  "

                return r
    return r


# FUNÇÃO DE MUDANÇA DE VENICMENTO - TEM NADA HAVER COM OS CAULOS ACIMA

def MudarVen(vAtual, vNovo,vPlano,checkA):

    if not checkA:

        MensagemFatura = f"Não possui pagamento proximo, Proporcional irá para proxima fatura."

        # QUANTIDADE DE DIAS NO MÊS

        quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]

        # PROXIMO MÊS

        ProxAtual = (data_hoje.month % 12) + 1

        # CICLO DE 1 ATÉ 10
        IniVenc01 = date(data_hoje.year, data_hoje.month, 1)
        IniVenc01Br = IniVenc01.strftime("%d/%m/%Y")
        FinalVenc30 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, data_hoje.month, quantidade_dias)
        FinalVenc30Br = FinalVenc30.strftime("%d/%m/%Y")

        # CICLO DE 11 ATÉ 10
        IniVenc11 = date(data_hoje.year, data_hoje.month, 11)
        IniVenc11Br = IniVenc11.strftime("%d/%m/%Y")
        FinalVenc10 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (data_hoje.month % 12) + 1, 10)
        FinalVenc10Br = FinalVenc10.strftime("%d/%m/%Y")

        # CICLO DE 21 ATÉ 20
        IniVenc21 = date(data_hoje.year, data_hoje.month, 21)
        IniVenc21Br = IniVenc21.strftime("%d/%m/%Y")
        FinalVenc20 = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (data_hoje.month % 12) + 1, 20)
        FinalVenc20Br = FinalVenc20.strftime("%d/%m/%Y")

        # CONDIÇÕES DE TROCA DE VENCIMENTO

        if (vAtual == '5' or vAtual == '10') and (vNovo == '5' or vNovo == '10'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r
        elif (vAtual == '5' or vAtual == '10') and (vNovo == '15' or vNovo == '20'):
            Qtd = quantidade_dias + FinalVenc10.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais próximo:\n{IniVenc01Br} -- {date(data_hoje.year, data_hoje.month, 10).strftime('%d/%m/%Y')}. São {Qtd - 30} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if ValorDiferenca > 50                               else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd - 30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        elif (vAtual == '5' or vAtual == '10') and (vNovo == '25' or vNovo == '30'):
            Qtd = quantidade_dias + FinalVenc20.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo:\n{IniVenc01Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if ValorDiferenca > 50                              else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc01Br} -- {FinalVenc10Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd - 30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        # VENCIMENTO 15 OU 20

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '15' or vNovo == '20'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '25' or vNovo == '30'):
            Qtd = (quantidade_dias - 10) + FinalVenc20.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30) * globals()[f'plan{vPlano}']()
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo:\n{IniVenc11Br} -- {date(data_hoje.year,data_hoje.month,20).strftime('%d/%m/%Y')}. São {Qtd-30} dias -- Proporcional:  {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}  1" if ValorDiferenca > 50                                 else f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc20Br}. São {Qtd} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de {Qtd-30} dias: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
            return r

        elif (vAtual == '15' or vAtual == '20') and (vNovo == '5' or vNovo == '10'):
            Qtd = (quantidade_dias - 10)
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd - 30)*-1 * globals()[f'plan{vPlano}']()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 11)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 10)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc11Br} -- {FinalVenc30Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}"
            return r

        # VENCIMENTO 25 OU 30

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '25' or vNovo == '30'):
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\nNÃO TERÁ MUDANÇA NO VALOR DA FATURA"
            return r

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '15' or vNovo == '20'):
            Qtd = (quantidade_dias - 20) + FinalVenc10.day
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30)*-1 * globals()[f'plan{vPlano}']()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 21)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 20)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc21Br} -- {FinalVenc10Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}" 
            return r

        elif (vAtual == '25' or vAtual == '30') and (vNovo == '5' or vNovo == '10'):
            Qtd = (quantidade_dias - 20)
            Valor = Qtd * globals()[f"plan{vPlano}"]()
            Valo_plan_completo = 30 * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (Qtd-30)*-1 * globals()[f'plan{vPlano}']()
            Mes_anterior = date(data_hoje.year-1 if (data_hoje.month == 1) else data_hoje.year,(data_hoje.month % 12) + 1 if data_hoje.month != 1 else 12, 21)
            Mes_anteriorBr = Mes_anterior.strftime("%d/%m/%Y")
            Mes_atual = date(data_hoje.year,data_hoje.month, 20)
            Mes_atualBr = Mes_atual.strftime("%d/%m/%Y")
            r = f"Plano: {vPlano}Megas\nVencimento: {vAtual} para {vNovo}\n\n{IniVenc21Br} -- {FinalVenc30Br}. São {Qtd} dias -- Proporcional: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento deste mês:\n{Mes_anteriorBr} -- {Mes_atualBr}. São 30 dias -- totalizando:  {Valo_plan_completo:.2f}\nCom desconto de 10%: {Valo_plan_completo - (Valo_plan_completo * 0.1):.2f}\nDesconto de: {Valo_plan_completo * 0.1:.2f}"
            return r
    else:
        if (vAtual == "30") or (vNovo == "30"):
            r = f"A CIDADE NÃO POSSUI ESSE VENCIMENTO!"
        else:

            # QUANTIDADE DE DIAS NO MÊS

            quantidade_dias = calendar.monthrange(date.today().year, date.today().month)[1]


            DadosVenA = [(6, 5) if vNovo == "5"
            else (11, 10) if vNovo == "10"
            else (16, 15) if vNovo == "15"
            else (21, 20) if vNovo == "20"
            else (26, 25) if vNovo == "25"
            else "None"]

            DadosVenB = [(6, 5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15, quantidade_dias+20) if vAtual == "5"
            else (11, 10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10, quantidade_dias+15) if vAtual == "10"
            else (16, 15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5, quantidade_dias+10) if vAtual == "15"
            else (21, 20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias, quantidade_dias+5) if vAtual == "20"
            else (26, 25, quantidade_dias-20, quantidade_dias-15, quantidade_dias-10, quantidade_dias-5, quantidade_dias) if vAtual == "25"
            else "None"]

            Contador = 2 if vNovo == "5" else 3 if vNovo == "10" else 4 if vNovo == "15" else 5 if vNovo == "20" else 6 if vNovo == "25" else "None"

            # PROXIMO MÊS

            ProxAtual = (data_hoje.month % 12) + 1

            IniVenc = date(date.today().year, date.today().month, DadosVenB[0][0])
            IniVencBr = IniVenc.strftime("%d/%m/%Y")
            FinalVenc = date(data_hoje.year + 1 if ProxAtual == 1 else data_hoje.year, (date.today().month % 12) + 1,
                             DadosVenA[0][1])
            FinalVencBr = FinalVenc.strftime("%d/%m/%Y")

            Valor = DadosVenB[0][Contador] * globals()[f"plan{vPlano}"]()
            ValorDiferenca = (int(vNovo) - int(vAtual)) * globals()[f'plan{vPlano}']()
            MensagemFatura = f"Não possui pagamento proximo, Proporcional irá para proxima fatura."

            if vAtual == vNovo:
                r = f"NÃO TERÁ ALTERAÇÃO NA FATURA!"
            else:
                if int(vAtual) < int(vNovo):
                    FinalVencMaisProx = date(data_hoje.year, date.today().month, DadosVenA[0][1])

                    FinalVencMaisProxBr = FinalVencMaisProx.strftime("%d/%m/%Y")

                    if (IniVenc.day < DadosVenA[0][1]):
                        if ValorDiferenca < 50:
                            r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de: {ValorDiferenca:.2f}\n\n{MensagemFatura}"
                        else:
                            r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nVencimento mais proximo: \n{IniVencBr} -- {FinalVencMaisProxBr}. São {int(vNovo) - int(vAtual)} dias -- Proporcional: {ValorDiferenca:.2f}\nCom desconto de 10%: {ValorDiferenca - (ValorDiferenca * 0.1):.2f}\nDesconto de: {ValorDiferenca * 0.1:.2f}"

                else:
                    r = f"Do {vAtual} para {vNovo}: \n{IniVencBr} -- {FinalVencBr}. São {DadosVenB[0][Contador]} dias -- totalizando: {Valor:.2f}\nCom desconto de 10%: {Valor - Valor * 0.1:.2f}\nDesconto de: {Valor * 0.1:.2f}\n\nProporcional de: {ValorDiferenca*-1:.2f}\n\n{MensagemFatura}"

        return r
# FUNÇÃO PARA SABER QUAL CALCULO SE DEVE USAR
def venc(pVen, pAtual, pNovo,checkA):
        if checkA:
            return CalculoA(pAtual, pNovo,pVen)  # VENCIMENTO DE ANANINDEUA
        elif pVen in ["5", "10"]:
            return Calcularven1(pAtual, pNovo)  # VENCIMENTO 5 OU 10
        elif pVen in ["15", "20"]:
            return Calcularven2(pAtual, pNovo)  # VENCIMENTO 15 OU 20
        elif pVen in ["25", "30"]:
            return Calcularven3(pAtual, pNovo,pVen)  # VENCIMENTO 25 OU 30


if __name__ == "__main__":
    app.run(debug=True)