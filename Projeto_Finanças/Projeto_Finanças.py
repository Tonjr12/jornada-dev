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
        tot_meses = int(valor/aporte_mensal)
        anos = tot_meses // 12
        meses_restantes = tot_meses % 12
        print('-='*30)
        print(f'Para atingir a Meta :{meta}')
        print(f'Você precisara de {anos} ano(s) e {meses_restantes} mês(es)! ')



    elif opcao == '2':
        print('Veja o Resumo do Plano')

    elif opcao == '3':
        print('Saindo do Sistema')
        break
    else:
        print('Opção invalida!')


