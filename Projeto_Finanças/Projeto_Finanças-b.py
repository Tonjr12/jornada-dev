# 1. Area de funções Mundo 3!
#========================================================
def exibir_menu():
    """Função resposável apenas de mostrar o menu na tela"""
    print('============= SISTEMA DE METAS v2.0 =============')
    print('1 - Simular Meta Financeira')
    print('2 - Ver Resumo do Plano')
    print('3 - Sair do Sistema')
    print('=================================================')



#=========================================================
# 2.HISTÓRICO E VARIÁVEIS GLOBAL
#=========================================================
historico_metas = []

#=========================================================
# 3. O LOOP PRINCIPAL(CONTROLADOR)
#=========================================================
while True:
    # Em vez de um monte de prints, chamamos a função!
    exibir_menu()

    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        print('Vamos simular a meta financeira')
        #(Por enquanto mantendo o código da opção 1, aqui)
        meta = input('Digite o Nome da Meta Financeira: ')
        valor = float(input('Digite o valor da Meta Financeira: '))
        aporte_mensal = float(input('Digite o valor do Aporte mensal: '))
        total_meses = int(valor // aporte_mensal)
        anos = int(total_meses // 12)
        meses_restantes = total_meses % 12

        meta_atual = {
            'nome': meta,
            'anos': int(anos),
            'meses':int(meses_restantes),
        }
        historico_metas.append(meta_atual)
        print('-='*30)
        print(f'Para atingir a Meta {meta}')
        print(f'Você precisara de {anos} anos e {meses_restantes} meses')


    elif opcao == '2':
        print('Veja o Resumo do Plano')
        print('-='*30)
        if len (historico_metas) == 0:
            print('\033[31mNenhuma Simulação encontrada!\033[m')
        else:
            print('--- SUAS METAS CADASTRADAS ---')
            for meta in historico_metas:
                print(f'Meta : {meta["nome"]} - Tempo : {meta["anos"]} ano(s) e {meta["meses"]} meses')
    elif opcao == '3':
        print('Saindo do Sistema')
        break
    else:
        print('OPÇÃO INVALIDA!')
