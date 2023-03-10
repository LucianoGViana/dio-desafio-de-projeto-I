jogo = [['7','8','9'],
        ['4','5','6'],
        ['1','2','3']]

venceu = False

for jogada in jogo:
    print(jogada)
print()

validos = []
for posicoes in jogo:
    validos.extend(posicoes)
    
for contagem in range(9):
    while True:
        if contagem%2 == 0:
            jogador = 'Jogador 1'
            simbolo = 'X'
        else:
            jogador = 'Jogador 2'
            simbolo = 'O'
            
        escolha = input(f'{jogador} - {[simbolo]} - Escolha uma posição (Tecle S para saír do jogo): ').lower()
        if escolha == 's':#Para sair do while
            break
        elif escolha not in validos:
            print('Posição indisponível ou inválida. Digite uma posição disponível ou válida')
            print()
        else:
            if escolha in validos:
                validos.remove(escolha)#para evitar escolher uma posição mais de uma vez
            if escolha == '1':
                jogo[2][0] = simbolo
            elif escolha == '2':
                jogo[2][1] = simbolo
            elif escolha == '3':
                jogo[2][2] = simbolo
            elif escolha == '4':
                jogo[1][0] = simbolo
            elif escolha == '5':
                jogo[1][1] = simbolo
            elif escolha == '6':
                jogo[1][2] = simbolo
            elif escolha == '7':
                jogo[0][0] = simbolo
            elif escolha == '8':
                jogo[0][1] = simbolo
            elif escolha == '9':
                jogo[0][2] = simbolo
            break

    if escolha == 's':#Para sair do FOR
        print('\nJogo interrompido!')
        break
        
    for jogada in jogo:
        print(jogada)
    print()

    if jogo[0][0]==jogo[0][1]==jogo[0][2]== simbolo:
        venceu = True
    elif jogo[1][0]==jogo[1][1]==jogo[1][2]== simbolo:
        venceu = True
    elif jogo[2][0]==jogo[2][1]==jogo[2][2]== simbolo:
        venceu = True        
    elif jogo[0][0]==jogo[1][0]==jogo[2][0]== simbolo:
        venceu = True
    elif jogo[0][1]==jogo[1][1]==jogo[2][1]== simbolo:
        venceu = True
    elif jogo[0][2]==jogo[1][2]==jogo[2][2]== simbolo:
        venceu = True
    elif jogo[0][0]==jogo[1][1]==jogo[2][2]== simbolo:
        venceu = True
    elif jogo[2][0]==jogo[1][1]==jogo[0][2]== simbolo:
        venceu = True

    if venceu:
        print(f'Fim de jogo. Vencedor: {jogador}\n')
        break

if contagem >= 8 and venceu == False:
    print('Fim de jogo. Houve empate! DEU VELHA!')
