n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo Valor: '))
opção = 0
while opção != 3:
    print('''O que você deseja fazer?
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] NOVOS NÚMERO ''')
    opção = int(input('Qual a sua opção?  '))
    if opção == 1:
        soma = n1 + n2
        print('A soma é igual a {}.'.format(soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multilicação é igual a {}.'.format(produto))
    elif opção == 3:
        print('Recomece o programa.')
    else:
        print('Opção Inválida.')
    print('_'* 10)
print('Fim! Até a próxima!')
