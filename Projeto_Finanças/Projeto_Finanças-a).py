#variaveis para guardar dados fora do while.
meta_salva = ""
ano_salvo = 0
meses_salvo = 0
simulacao_feita = False #(flag-A bandeira)
#___Agora usamos o mundo 3 para o histórico___
historico_metas = [] #Lista vazia que guardara os dicionarios

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
        tot_meses = int(valor // aporte_mensal) #(o (int) antes envolvendo a conta vai garantir que apareca somente numeros inteiros )
        anos = tot_meses // 12 # (// vai fazer a conta para apontar os anos inteiros)
        meses_restantes = tot_meses % 12 #(% vai fazer a conta para apontar os meses)

        # salvando os dados nas variáveis de fora.
        meta_salva = meta
        ano_salvo = int(anos) # garantindo que não apareca o ".0"
        meses_salvo = int(meses_restantes)
        simulacao_feita = True
        #criando o dicionário de meta atual (Padrão Mundo 3!)
        meta_atual = {
            'nome': meta,
            'anos': int(anos),
            'meses': int(meses_restantes)
        }
        #Histórico de metas
        historico_metas.append(meta_atual)
        print('-='*30)
        print(f'Para atingir a Meta :{meta}')
        print(f'Você precisara de {anos} ano(s) e {meses_restantes} mês(es)! ')

    elif opcao == '2':
        print('Veja o Resumo do Plano')
        print('-='*30)
        # Se o tamanho do len da lista for 0, significa que a lista está vazia
        if len(historico_metas) == 0:
            print('\033[31mNenhuma simulação encontrada!\033[m ')
        # SENAO , varremos a lista e mostramos o dicionario
        else:
            print ('--- SUAS METAS CADASTRADAS ---')
            for meta in historico_metas:
                print(f' Meta: {meta["nome"]} - Tempo: {meta["anos"]} ano(s) e {meta["meses"]} meses')

    elif opcao == '3':
        print('Saindo do Sistema')
        break
    else:
        print('Opção invalida!')


