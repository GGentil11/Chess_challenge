import chess

def is_terminal(board):
    return board.is_checkmate() or board.is_stalemate()

def get_moves(board, player):
    for move in board.legal_moves:
        if board.turn == player and move.uci().isalnum():
            yield move

def make_move(board, move):
    new_board = board.copy()
    new_board.push(move)
    return new_board

def get_other_player(player):
    return chess.WHITE if player == chess.BLACK else chess.BLACK