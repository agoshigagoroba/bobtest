#teste se consigo editar
import re


# definição das duas funções geradoras dos vetores de números (por extenso e numero cardinal)

# definição vetor números por extenso
def numeros_por_extenso():
    extenso_completo = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                        'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                        'dezenove', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta',
                        'noventa', 'cem', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                        'setecentos', 'oitocentos', 'novecentos', 'mil']

    for i in range(1000):
        if (i > 20 and i < 30):
            extenso_completo.insert(i, ('vinte e ' + extenso_completo[i - 20]))
        if (i > 30 and i < 40):
            extenso_completo.insert(i, ('trinta e ' + extenso_completo[i - 30]))
        if (i > 40 and i < 50):
            extenso_completo.insert(i, ('quarenta e ' + extenso_completo[i - 40]))
        if (i > 50 and i < 60):
            extenso_completo.insert(i, ('cinquenta e ' + extenso_completo[i - 50]))
        if (i > 60 and i < 70):
            extenso_completo.insert(
                i, ('sessenta e ' + extenso_completo[i - 60]))
        if (i > 70 and i < 80):
            extenso_completo.insert(
                i, ('setenta e ' + extenso_completo[i - 70]))
        if (i > 80 and i < 90):
            extenso_completo.insert(
                i, ('oitenta e ' + extenso_completo[i - 80]))
        if (i > 90 and i < 100):
            extenso_completo.insert(
                i, ('noventa e ' + extenso_completo[i - 90]))
        if (i > 100 and i < 200):
            extenso_completo.insert(
                i, ('cento e ' + extenso_completo[i - 100]))
        if (i > 200 and i < 300):
            extenso_completo.insert(
                i, ('duzentos e ' + extenso_completo[i - 200]))
        if (i > 300 and i < 400):
            extenso_completo.insert(
                i, ('trezentos e ' + extenso_completo[i - 300]))
        if (i > 400 and i < 500):
            extenso_completo.insert(
                i, ('quatrocentos e ' + extenso_completo[i - 400]))
        if (i > 500 and i < 600):
            extenso_completo.insert(
                i, ('quinhentos e ' + extenso_completo[i - 500]))
        if (i > 600 and i < 700):
            extenso_completo.insert(
                i, ('seiscentos e ' + extenso_completo[i - 600]))
        if (i > 700 and i < 800):
            extenso_completo.insert(
                i, ('cinquenta e ' + extenso_completo[i - 700]))
        if (i > 800 and i < 900):
            extenso_completo.insert(
                i, ('cinquenta e ' + extenso_completo[i - 800]))
        if (i > 900 and i < 1000):
            extenso_completo.insert(
                i, ('novecentos e ' + extenso_completo[i - 900]))
    return (extenso_completo)


# definição vetor números cardinais
def numeros_cardinais():
    cardinais_completo = []
    for i in range(1001):
        cardinais_completo.append('%s' % i)
    return (cardinais_completo)


# VETORES POR EXTENSO E CARDINAIS
cardinais_completo = numeros_cardinais()
extenso_completo = numeros_por_extenso()

# Abertura do arquivo
with open('pagina_do_planalto.txt', 'r', encoding='utf-8') as f:
    conteudo_pagina = f.read()

    # REGEX

    # REGEX DAS OCORRÊNCIAS
    extenso_completo_pedacos = '|'.join(extenso_completo)

    regecs_1 = re.compile(rf'.* (\d+) ?\(?({extenso_completo_pedacos}).*\b(dias|dia|mês|meses|anos|ano)\b')
    regecs_2 = re.compile(rf'.*({extenso_completo_pedacos}) \b(dias|dia|mês|meses|anos|ano)\b')
    regecs_3 = re.compile(r'.* (\d+) \b(dias|dia|mês|meses|anos|ano)\b')

    questoes_prazos_iter1 = regecs_1.finditer(conteudo_pagina)
    questoes_prazos_iter2 = regecs_2.finditer(conteudo_pagina)
    questoes_prazos_iter3 = regecs_3.finditer(conteudo_pagina)

    questoes_prazos = []
    questoes_enunciado = []

    for ocorrencia in questoes_prazos_iter3:
        print(ocorrencia.group(0))
    # for ocorrencia in questoes_prazos_iter2:
    #    questoes_prazos.append(ocorrencia)
    #
    # for ocorrencia in questoes_prazos_iter3:
    #    questoes_prazos.append(ocorrencia)

    # for i in range(numeros_ocorrencias_prazos):
    #     print(numeros_ocorrencias_prazos[i])
    for elemento in questoes_prazos:
        if (elemento in extenso_completo):
            # print('sim')
            pass
        else:
            # print('nao')
            pass
    # print(cardinais_completo[15])
    # print(extenso_completo)
    # feito os regex como aplicar eles nos vetores e salvar
