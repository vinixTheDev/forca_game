import os
import random

lista_palavras = ['arroz','aveia', 'besouro', 'cobertor', 'medo', 'beterraba', 'navio', 'perfume']
palavra = random.choice(lista_palavras)
letra_certa = ""
tentativas = -1
palavra_formada = ""
start = 'Digite qualquer letra pra iniciar e descubrir o tamanho da palavra.'

while True:
    if tentativas < 0:
        print(start)
    entrada = input('Digite uma letra: ').lower()
    palavra_formada = ""
    
    

    if len(entrada) > 1:
        print('Digite apenas uma letra mané.')
        continue
    
    if entrada in palavra:
        letra_certa += entrada
    else: 
        tentativas += 1
    for letra_secreta in palavra:
        if letra_secreta in letra_certa:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    os.system('cls')
    print(f'Palavra formada: ', palavra_formada) 
    if palavra_formada == palavra:
        print(f'============================== \
              \nParabens, voce venceu meu game. \
              \nEssa é a palavra certa {palavra} \
              \nTentativas = {tentativas}')
        break       
