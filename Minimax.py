import chess
from Heuristica import avaliar_tabuleiro
from Logica_jogo import is_terminal, get_jogadas, fazer_jogada, get_oponente

def hashable_board(board):
    return board.fen()

def id(hashable_board):
    return hashable_board

cache = {}

def minimax_alpha_beta(board, lado_jogador, profundidade, alpha, beta):
    jogada = None
    if (profundidade == 0 or is_terminal(board)):
        if lado_jogador == chess.WHITE:
            return None, avaliar_tabuleiro(board)
        else:
            return None, -avaliar_tabuleiro(board)

    hash_board = hashable_board(board)
    hash_id = id(hash_board)

    melhor_jogada = None
    melhor_valor = None
    if hash_id in cache:
        return cache[hash_id][0], cache[hash_id][1]
    
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

    cache[hash_id] = melhor_jogada, valor
    return melhor_jogada, melhor_valor