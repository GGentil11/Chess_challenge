import chess
from Heuristica import avaliar_tabuleiro
from Logica_jogo import is_terminal, get_jogadas, fazer_jogada, get_oponente

def minimax_alpha_beta(board, lado_jogador, profundidade, alpha, beta):
    if (profundidade == 0 or is_terminal(board)) and lado_jogador == chess.WHITE:
        return None, avaliar_tabuleiro(board)
    
    elif (profundidade == 0 or is_terminal(board)) and lado_jogador == chess.BLACK:
        return None, -avaliar_tabuleiro(board)

    melhor_jogada = None
    if board.turn == lado_jogador:
        melhor_valor = float("-inf")
    else:
        melhor_valor = float("inf")

    for jogada in get_jogadas(board):
        new_board = fazer_jogada(board, jogada)
        _, valor = minimax_alpha_beta(new_board, get_oponente(lado_jogador), 
                                      profundidade - 1, alpha, beta)

        if (board.turn == lado_jogador and valor > melhor_valor) or (board.turn != lado_jogador and valor < melhor_valor):
            melhor_jogada = jogada
            melhor_valor = valor

        if board.turn == chess.WHITE:
            alpha = max(alpha, melhor_valor)
            if alpha >= beta:
                break
        else:
            beta = min(beta, melhor_valor)
            if beta <= alpha:
                break

    return melhor_jogada, melhor_valor

