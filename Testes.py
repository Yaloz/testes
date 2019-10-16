import random, math, time

print('######### JOGO DA FORCA #########')
palavras = ['ovo','colher','mesa','lustre','aparelho','cidade','museu','livro','coelho','ventilador','rato']
palsecreta = random.choice(palavras)

acertou = False

forca = ['-' for letra in palsecreta]

chances = 6
print('Palavra:', forca)
while(not acertou):

    chute = (input('Digite uma letra:'))
    chute = chute.strip()
    posicao = 0

    for letra in palsecreta:
        if chute.upper() == letra.upper():
           forca[posicao] = letra
        posicao = posicao + 1

    if chances != 1 and acertou == False: print('Palavra:' ,forca)

    if chute.upper() not in palsecreta.upper():  chances += -1
    if chute.upper() not in palsecreta.upper() and chances != 0: print('Você errou! Restam {} tentativas.'.format(chances))
    acertou = '-' not in forca

    if chances == 0: exit('GAME OVER')
    if acertou != False: exit('Parabéns, você ganhou!!!')

