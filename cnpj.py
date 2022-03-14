from random import randint


def formata_cnpj(string):
    cnpj_formatado = ''
    for caracter in string:
        if caracter == '.' or caracter == '/' or caracter == '-':
            continue
        else:
            cnpj_formatado += caracter
    return cnpj_formatado


def identifica_sequencia(string):
    sequencia = string[0] * len(string)
    if sequencia == string:
        return True
    else:
        return False


def valida(cnpj_og, cnpj):
    sequencia = identifica_sequencia(cnpj)
    if sequencia:
        return False
    elif cnpj == cnpj_og:
        return True
    else:
        return False


def calcula_total(cnpj):  # 042520110001
    total = 0
    reversos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    reversos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if len(cnpj) == reversos1:
        for i in range(len(cnpj)):
            total += reversos1[i] * int(cnpj[i])
        total = 11 - (total % 11)
        if total > 9:
            total = 0
        return total
    else:
        for i in range(len(cnpj)):
            total += reversos2[i] * int(cnpj[i])
        total = 11 - (total % 11)
        if total > 9:
            total = 0
        return total


def gera():
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = '0001'

    cnpj_invalidado = f'{primeiro_digito}{segundo_digito}{segundo_bloco}{terceiro_bloco}{quarto_bloco}'
    validacao_1 = str(calcula_total(cnpj_invalidado))
    validacao_2 = calcula_total(f'{cnpj_invalidado}{validacao_1}')

    cnpj = f'{primeiro_digito}{segundo_digito}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-' \
           f'{validacao_1}{validacao_2}'
    return cnpj
