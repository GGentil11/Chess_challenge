import chess
import chess.polyglot
import random

def is_terminal(board):
    return board.is_checkmate() or board.is_stalemate()

def get_jogadas(board):
    for jogada in board.legal_moves:
        if jogada.uci().isalnum():
            yield jogada

def fazer_jogada(board, jogada):
    new_board = board.copy()
    new_board.push(jogada)
    return new_board

def get_oponente(lado_jogador):
    return chess.WHITE if lado_jogador == chess.BLACK else chess.BLACK

def obter_melhor_jogada(board):
    jogadas = melhores_jogadas(board)
    melhor_jogada = None
    if len(jogadas)>0:
        melhor_jogada = jogadas[0].move
    if not melhor_jogada:
        print("Não achou jogada")
        melhor_jogada = random.sample(list(board.legal_moves), 1)[0]
    return melhor_jogada

def melhores_jogadas(board):
    jogadas = []
    with chess.polyglot.open_reader("Bookfish") as reader:
        for abertura in reader.find_all(board):
            jogadas.append(abertura)
    return jogadas