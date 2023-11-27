from Heuristica import evaluate_board
from Logica_jogo import is_terminal, get_moves, make_move, get_other_player

def minimax_alpha_beta_material(board, player, profundidade, alpha, beta):
    if profundidade == 0 or is_terminal(board):
        return None, evaluate_board(board)

    best_move = None
    best_value = float("-inf") if board.turn == player else float("inf")

    for move in get_moves(board, player):
        new_board = make_move(board, move)
        _, value = minimax_alpha_beta_material(new_board, get_other_player(player), profundidade - 1, alpha, beta)

        if board.turn == player:
            if value > best_value:
                best_move = move
                best_value = value
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
        else:
            if value < best_value:
                best_move = move
                best_value = value
            beta = min(beta, best_value)
            if beta <= alpha:
                break

    return best_move, best_value