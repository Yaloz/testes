import random, math, time
cores = { 'terminar': '\033[m' ,
          'vermelho': '\033[1;31m' ,
          'Azul claro': '\033[1;36m',
          'Amarelo': '\033[1;33m',
          'Verde': '\033[1;32m',
          'Roxo': '\033[1;35m',
          'Cinza':'\033[1;37m'}

print('########## JOGO TESTE #########')

credito = 100
print('Moedas: ${}'.format(credito))

for c in range(1,999999):
    tele = 0
    if tele == 0:

     print('\n----------- MENU -----------')


     menu = int(input('(1) Jogar\n(2) Sair\n(3) Loja\n(4) Comandos\n\nDigite aqui:'))

     if menu == '/moedas': print('Moedas: ${}'.format(credito))
     if menu == 1:
         tele = 1

         print ('Iniciando...')

         vida = 100
         mana = 100

         print(' \n Vida:', vida, '\n', 'Mana:', mana)



     if menu == 2: exit('Desconectado')
     if menu == 3:
        tele = 2

        Itens = ['Capacete(1) = $50', 'Chapéu(2) = $20', 'Elmo(3) = $100', 'Armadura(4) = $200' , 'Faca(5) = $30', 'Espada curta(6) = $100, Espada Longa(7) = $250', 'Arco e flecha(8) = $200']
        print(Itens)
        print('\nPara comprar um item digite o número dele.')
        compra = int ((input('Digite aqui:')))
        if compra == 1 and credito < 50: print('Você não tem créditos suficientes.')
        if compra == 1 and credito >= 50: print('Capacete comprado com sucesso!\n-$50')
        if compra == 1 and credito >= 50: credito +=  -50
        if compra == 1: c1 = print('Moedas: ${}'.format(credito))

        if compra == 2 and credito < 20: print('Você não tem créditos suficientes.')
        if compra == 2 and credito >= 20: print('Chapéu comprado com sucesso!\n-$20')
        if compra == 2 and credito >= 20: credito +=  -20
        if compra == 2: c2 =  print('Moedas: ${}'.format(credito))

        if compra == 3 and credito < 100: print('Você não tem créditos suficientes.')
        if compra == 3 and credito >= 100: print('Elmo comprado com sucesso!\n-$100')
        if compra == 3 and credito >= 100: credito +=  -100
        if compra == 3: c3 =  print('Moedas: ${}'.format(credito))

        if compra == 4 and credito < 200: print('Você não tem créditos suficientes.')
        if compra == 4 and credito >= 200: print('Armadura comprada com sucesso!\n-$200')
        if compra == 4 and credito >= 200: credito +=  -200
        if compra == 4: c4 =  print('Moedas: ${}'.format(credito))

        if compra == 5 and credito < 30: print('Você não tem créditos suficientes.')
        if compra == 5 and credito >= 30: print('Faca comprada com sucesso!\n-$30')
        if compra == 5 and credito >= 30: credito +=  -30
        if compra == 5: c5 =  print('Moedas: ${}'.format(credito))

        if compra == 6 and credito < 100: print('Você não tem créditos suficientes.')
        if compra == 6 and credito >= 100: print('Espada Curta comprada com sucesso!\n-$100')
        if compra == 6 and credito >= 100: credito +=  -100
        if compra == 6: c6 =  print('Moedas: ${}'.format(credito))

        if compra == 7 and credito < 250: print('Você não tem créditos suficientes.')
        if compra == 7 and credito >= 250: print('Espada Longa comprada com sucesso!\n-$250')
        if compra == 7 and credito >= 250: credito +=  -250
        if compra == 7: c7 =  print('Moedas: ${}'.format(credito))

        if compra == 8 and credito < 200: print('Você não tem créditos suficientes.')
        if compra == 8 and credito >= 200: print('Arco e flecha comprado com sucesso!\n-$200')
        if compra == 8 and credito >= 200: credito +=  -200
        if compra == 8: c8 =  print('Moedas: ${}'.format(credito))

        tele = 0
     if menu == 4:
      print('\n----------- COMANDOS -----------')
      tele = 3

      print('Comando 1: Use /moedas para ver a sua quantidade de moedas.')
      cmds = str ((input('\nDigite aqui:')))
      if cmds == '/moedas': print('Moedas: ${}'.format(credito))

      tele = 0


    if tele == 0: continue

    if menu == 1 or menu == 2 or menu == 3 or menu == 4: break

    if menu != 1 or menu != 2 and menu !=  3 and menu != 4 and cmds != str: print('Digite um comando válido.')

    if menu == 1 or 2 or 3 or 4: break


