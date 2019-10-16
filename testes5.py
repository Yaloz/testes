import math, random, time


veterano = ''  #nome do homem mais velho
idadevelho = 0 #idade do homem mais velho
mulheres = 0 #mulher com menos de 20 anos
somatoria = 0 #somatoria idades
for c in range(1,3):

    nome = str (input('Digite o nome da {} pessoa:'.format(c))).strip().title()
    idade = int(input('Digite a idade da {} pessoa: '.format(c)))
    genero = int(input('Digite seu gênero da {} pessoa: (1) para MASCULINO\n                               (2) Para FEMININO'.format(c)))
    somatoria += idade
    print('=' * 50)
    if genero == 1 and c == 1:
        veterano = nome
        idadevelho = idade

    elif genero == 1 and c != 1:
       if idade > idadevelho:
          veterano = nome
          idadevelho = idade

    if genero == 2 and idade < 20: mulheres += 1



média = somatoria / 2
print ('A média de idade é: {}'.format(média))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(mulheres))
print('O nome do homem mais velho é: {} com {} anos'.format(veterano, idadevelho))

