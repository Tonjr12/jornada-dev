#variaveis para guardar dados fora do while.
meta_salva = ""
ano_salvo = 0
meses_salvo = 0
simulacao_feita = False #(flag-A bandeira)

while True:
    print('============= SISTEMA DE METAS v1.0 =============')
    print('1 - Simular Meta Financeira')
    print('2 - Ver Resumo do Plano')
    print('3 - Sair do Sistema')
    print('=================================================')
    print('Escolha uma opção:')

    opcao = input('Digite  a opão desejada: ')
    if opcao == '1':
        print('Vamos Simular a Meta Financeira')
        meta = input('Digite o nome do Meta Financeira: ')
        valor = float(input('Digite o Valor do Meta Financeira: '))
        aporte_mensal = float(input('Digite o Aporte Mensal: '))
        tot_meses = int(valor // aporte_mensal) #(o (int) antes envolvendo a conta vai garantir que apareca somente numeros inteiros inteiros)
        anos = tot_meses // 12 # (// vai fazer a conta para apontar os anos inteiros)
        meses_restantes = tot_meses % 12 #(% vai fazer a conta para apontar os meses)

        # salvando os dados nas variáveis de fora.
        meta_salva = meta
        ano_salvo = int(anos) # garantindo que não apareca o ".0"
        meses_salvo = int(meses_restantes)
        simulacao_feita = True

        print('-='*30)
        print(f'Para atingir a Meta :{meta}')
        print(f'Você precisara de {anos} ano(s) e {meses_restantes} mês(es)! ')

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


