import random, math, time

cores = { 'terminar': '\033[m' ,
          'vermelho': '\033[1;31m' ,
          'Azul claro': '\033[1;36m',
          'Amarelo': '\033[1;33m',
          'Verde': '\033[1;32m',
          'Roxo': '\033[1;35m',
          'Cinza':'\033[1;37m'}
COL1='-----------------------------------------------------------------------------------------------------------------'

user01 = 'guest'
user02 = []

senha01 = '123'
senha02 = []


COL2='-----------------------------------------------------------------------------------------------------------------'
ini = int(input('Comandos: (1)\033[1;36mLogar\033[m (2)\033[1;35mCadastrar-se\033[m''\n\n\033[1;37mDigite aqui:\033[m'))
if ini != 1 and ini!= 2:

  for c in range(0, 999):
      if ini != 1 and ini != 2: print(('Digite um comando válido.'))
      if ini == 1 or ini == 2: break
      ini = int(input('Comandos: (1)\033[1;36mLogar\033[m (2)\033[1;35mCadastrar-se\033[m''\n\n\033[1;37mDigite aqui:\033[m'))

cad1 = 000000000000
cad2 = 000000000000
cad3 = 000000000000


if ini == 2: print ('\033[1;35m-'*15 ,'CADASTRO', '-'*15)

if ini == 2: cad1 = (input('\033[1;35mDigite um login:\033[m'))
user02.append(cad1)
senha02.append(cad2)

if ini == 2 and cad1 == user01 or cad1 == user02:
    for c in range(0, 9999999):
        print('Essa conta já existe. Por favor, digite um login válido.')
        if ini == 2: cad1 = (input('\033[1;35mDigite um login:\033[m'))
        if ini == 2 and cad1 != user01 and cad1 != user02: break

if ini == 2: cad2 = (input('\033[1;35mDigite uma senha:\033[m'))
for c in range (1,9999999):
    if ini == 2: cad3 = (input('\033[1;35mDigite sua senha novamente:\033[m'))
    if ini == 2 and cad2 != cad3: print('\033[1;37mA senha deve ser a mesma em ambos os campos.\033[m')
    if ini == 2 and cad2 == cad3: break


if ini == 2: print ('\033[1;37mConta criada com sucesso!\033[m')

ini = 1

if ini == 1: print ( '\033[1;36m-'*15 ,' LOGIN ', '-'*15,'\033[m')


if ini == 1: login = (input('\033[1;36mlogin: \033[m'))

if login != cad1 and login != user01 and login != user02:
    for c in range(0, 9999999):
        print('Essa conta não existe.')
        login = (input('\033[1;36mlogin: \033[m'))
        if login == cad1: break
        if login == user01: break
        if login == user02: break


senha = (input('\033[1;36mSenha: \033[m'))

if login == cad1 and senha == cad2: print('\033[1;37mLogado com sucesso.\033[m')
contador = 3
for c in range(0, 9999999):
    if senha != cad2 and senha != senha01 and senha != senha02 and contador == 3  and cad2 == cad3 : print('Senha incorreta! Você tem mais {} tentativas.'.format(contador))
    if senha != cad2 and senha != senha01 and senha != senha02 and contador == 2  and cad2 == cad3 : print('Senha incorreta! Você tem mais {} tentativas.'.format(contador))
    if senha != cad2 and senha != senha01 and senha != senha02 and contador == 1 and cad2 == cad3: print('Senha incorreta! Você tem mais {} tentativa.'.format(contador))
    if senha == senha02 or senha == senha01 or senha == cad2: contador = contador
    if senha != cad2 and senha != senha01 and senha != senha02: contador += -1

    if contador == -1: exit('\033[1;37mUsuario não encontrado.\033[m')
    if senha == cad2: break
    if senha == senha01 and login == user01 or senha == senha02 and login == user02: break
    senha = (input('\033[1;36mSenha: \033[m'))


if login == user01 and senha == senha01 : print('\033[1;37mLogado com sucesso.\033[m')
if login == user01 and senha == senha01 : print( 'Olá, {}{}{}. Bem vindo! '.format(cores['vermelho'], login , cores['terminar']))
if login == user01 and senha != senha01 and senha != cad2: exit('\033[1;37mUsuario não encontrado.\033[m')

if login == user02 and senha == senha02 : print('\033[1;37mLogado com sucesso.\033[m')
if login == user02 and senha == senha02 : print( 'Olá, {}{}{}. Bem vindo! '.format(cores['vermelho'], login , cores['terminar']))
if login == user02 and senha != senha02 and senha != cad2: exit ('\033[1;37mUsuario não encontrado.\033[m')


if login == cad1 and senha == cad2: print  ( 'Olá, {}{}{}. Bem vindo! '.format(cores['vermelho'], login , cores['terminar']))
if login == 'guest' and senha == cad3: exit ('\033[1;37mUsuario não encontrado.\033[m')
if login == user02 and senha == cad3: exit ('\033[1;37mUsuario não encontrado.\033[m')

COL3='-----------------------------------------------------------------------------------------------------------------'


print( 'Comandos: (1)\033[1;33m Financiamento\033[m \n          (2)\033[1;31m Desconectar-se\033[m\n' )

for c in range(1,999999):
    cmd = float(input('\033[1;37mDigite aqui: \033[m'))
    if cmd == 2: exit('\033[1;37mDesconectado do sistema.\033[m')
    if cmd != 1 and cmd !=2: print('\033[1;37mComando inválido.\033[m')
    if cmd != 1 and cmd !=2: print('Comandos: (1)\033[1;33m Financiamento\033[m \n          (2)\033[1;31m Desconectar-se\033[m\n')
    if cmd == 2: exit('\033[1;37mDesconectado do sistema.\033[m')
    if cmd == 1 or cmd == 2: break

if cmd == 1: print ('\033[1;37mAguarde...\033[m\n')

if cmd == 1: print ('\033[1;33m-'*15,'FINANCIAMENTO','-'*15)
if cmd == 1: time.sleep(1)
if cmd == 1: valorcasa = int (input('\033[1;33mDigite o valor do produto a ser financiado: \033[m'))
if cmd == 1: sal = int (input('\033[1;33mDigite seu salario:\033[m'))
if cmd == 1: ano = int (input ('\033[1;33mEm quantos anos pretende pagar:\033[m'))
if cmd == 1: c = ano * 12
if cmd == 1: pm = valorcasa / (ano * 12)
if cmd == 1 and sal / 3.33 < valorcasa / c  : print ('\033[1;37mFinanciamento negado.\033[m')
elif cmd == 1 and sal / 3.33 > valorcasa / c : print ('\033[1;37mFinanciamento pode ser realizado.\033[m\nValor da prestação mensal:\033[1;32m R${:.2f}\033[m'.format(pm))




