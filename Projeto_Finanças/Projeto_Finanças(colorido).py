# As cores ficam fora do while.
COR_BORDA = '\033[1;34m'
COR_TITULO = '\033[1;33m'
COR_NUMERO = '\033[1;32m'
COR_TEXTO = '\033[1;36m'
RESET = '\033[m'

#Criamos uma variavel de controle para o loop:
rodando = True

#variaveis para guardar dados fora do while.
meta_salva = ""
ano_salvo = 0
meses_salvo = 0
simulacao_feita = False #(flag-A bandeira)

# O while começa aqui:
while rodando:
    # Menu estilizado com as suas variáveis de cores
    print(f'{COR_BORDA}================================================={RESET}')
    print(f'{COR_BORDA}||{COR_TITULO}            SISTEMA DE METAS v1.0            {COR_BORDA}||{RESET}')
    print(f'{COR_BORDA}================================================={RESET}')
    print(f' {COR_NUMERO}1{RESET} - {COR_TEXTO}Simular Meta Financeira{RESET}')
    print(f' {COR_NUMERO}2{RESET} - {COR_TEXTO}Ver Resumo do Plano{RESET}')
    print(f' {COR_NUMERO}3{RESET} - {COR_TEXTO}Sair do Sistema{RESET}')
    print(f'{COR_BORDA}================================================={RESET}')

    # Adicionado uma corzinha roxa/magenta no input para destacar
    opcao = input('\033[1;35mDigite a opção desejada: \033[m')
    if opcao == '1':
        print(f'\n{COR_TITULO}=== Vamos Simular a Meta Financeira ==={RESET}')
        meta = input('Digite o nome da Meta Financeira: ')
        valor = float(input('Digite o Valor da Meta Financeira: R$ '))
        aporte_mensal = float(input('Digite o Aporte Mensal: R$ '))

        tot_meses = valor // aporte_mensal
        anos = tot_meses // 12
        meses_restantes = tot_meses % 12

        # salvando os dados nas variáveis de fora.
        meta_salva = meta
        ano_salvo = int(anos)  # garantindo que apareça sem o ".0"
        meses_salvo = int(meses_restantes)
        simulacao_feita = True

        print(f'{COR_BORDA}-={RESET}' * 30)
        print(f'Para atingir a Meta: {COR_TEXTO}{meta}{RESET}')
        print(f'Você precisará de {COR_NUMERO}{ano_salvo}{RESET} ano(s) e {COR_NUMERO}{meses_salvo}{RESET} mês(es)!')
        print(f'{COR_BORDA}-={RESET}' * 30)

    elif opcao == '2':
        print('Veja o Resumo do Plano')
        print('-='*30)
        # se a simulacao_feita = True mostre os dados salvos com f-string
        if simulacao_feita == True:
            print(f'Sua ultima meta simulada:{meta_salva}')
            print(f'Tempo estimado {ano_salvo} ano(s) e {meses_salvo} mês(es).')
        # SENAO(O usuario foi direto para opção 2 sem simular antes)
        else:
            print('\033[31mNenhuma simulação encontrada! Por favor faça uma simulação na opção 1 primeiro.\033[m')

    elif opcao == '3':
        print('Saindo do Sistema')
        break
    else:
        print('Opção invalida!')


