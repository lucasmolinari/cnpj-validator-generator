import cnpj

if __name__ == "__main__":
    # cnpj funcional -> 04.252.011/0001-10
    cnpj_og = input('Insira seu CNPJ ou digite [gerar]: ')

    if cnpj_og.lower() == 'gerar':
        quantidade = input('Quantos deseja gerar? [Máximo 100]: ')
        cnpjs = open('cnpjs.txt', 'w')
        if quantidade.isnumeric():
            quantidade = int(quantidade)
            if quantidade <= 100:
                for i in range(quantidade):
                    cnpjs.write(cnpj.gera())
                    cnpjs.write('\n' + '-' * 50 + '\n')
            else:
                print(f'Não é possível gerar {quantidade} CNPJ')
        else:
            print('Insira apenas números positivos.')
        print('Arquivo .txt criado.')
        cnpjs.close()
    else:
        teste_cnpj = cnpj.formata_cnpj(cnpj_og)
        if teste_cnpj.isnumeric():
            cnpj1 = teste_cnpj[:-2]
            cnpj1 += str(cnpj.calcula_total(cnpj1))
            cnpj2 = cnpj1
            cnpj2 += str(cnpj.calcula_total(cnpj1))

            valido = cnpj.valida(teste_cnpj, cnpj2)
            if valido:
                print('CNPJ válido.')
            else:
                print('CNPJ inválido.')

        else:
            print('Insira números ou escreva [gerar].')
