import chess

def definirLado():
    lado = input('Defina o seu lado (W/B): ').upper()
    if lado == 'W':
        return chess.WHITE
    elif lado == 'B':
        return chess.BLACK
    else:
        print('Lado inválido. Escolha W para branco ou B para preto.')
        return definirLado() 
    
def jogadaOponente(board):
    while True:
        resposta = input('Informe a jogada do oponente (use a notação de casas): ').lower()
        if len(resposta) == 4  and resposta.isalnum():
            jogada = chess.Move.from_uci(resposta)
            if jogada in board.legal_moves:
                board.push(jogada)
                break
            else:
                print("Jogada ilegal. Tente novamente.")
        else:
            print("Jogada inválida. A notação UCI deve ter 4 ou 5 caracteres.")