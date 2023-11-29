import chess

def is_terminal(board):
    return board.is_checkmate() or board.is_stalemate()

def get_moves(board, lado_jogador):
    for move in board.legal_moves:
        if board.turn == lado_jogador and move.uci().isalnum():
            yield move

def make_move(board, move):
    new_board = board.copy()
    new_board.push(move)
    return new_board

def get_oponente(lado_jogador):
    return chess.WHITE if lado_jogador == chess.BLACK else chess.BLACK