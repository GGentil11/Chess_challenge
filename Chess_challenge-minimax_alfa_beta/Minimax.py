import chess
from Heuristica import avaliarTabuleiro
from Logica_jogo import is_terminal, get_moves, make_move, get_oponente
from Avaliacao import avaliarTabuleiro_2

def minimax_alpha_beta_material(board, lado_jogador, profundidade, alpha, beta):
    if profundidade == 0 or is_terminal(board):
        return None, avaliarTabuleiro_2(board)

    best_move = None
    best_value = float("-inf") if board.turn == lado_jogador else float("inf")

    for move in get_moves(board, lado_jogador):
        new_board = make_move(board, move)
        _, value = minimax_alpha_beta_material(new_board, get_oponente(lado_jogador), profundidade - 1, alpha, beta)

        if (board.turn == lado_jogador and value > best_value) or (board.turn != lado_jogador and value < best_value):
            best_move = move
            best_value = value

        if (board.turn == lado_jogador) and (board.turn == chess.WHITE):
            if value > best_value:
                best_move = move
                best_value = value
            alpha = max(alpha, best_value)
            if alpha >= beta:
                print("Realizando poda alfa")
                break
        elif (board.turn == lado_jogador) and (board.turn == chess.BLACK):
            if value < best_value:
                best_move = move
                best_value = value
            beta = min(beta, best_value)
            if beta <= alpha:
                print("Realizando poda beta")
                break
    return best_move, best_value