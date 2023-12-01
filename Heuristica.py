import chess

def valores_pecas():
    valores_peca = {
        chess.PAWN: 10,
        chess.KNIGHT: 30,
        chess.BISHOP: 30,
        chess.ROOK: 50,
        chess.QUEEN: 90,
        chess.KING: 900
    }
    return valores_peca

def avaliar_tabuleiro(board):
    # Valores para as peças
    valores_peca = valores_pecas()
    # Avaliação baseada no material
    pontuacao_material = sum(
        valores_peca[peca.piece_type] * (1 if peca.color == chess.WHITE else -1)
        for _, peca in board.piece_map().items()
    )

    # Avaliação baseada na mobilidade
    pontuacao_mobilidade = sum(
        len(list(board.legal_moves)) * (1 if peca.color == chess.WHITE else -1)
        for _, peca in board.piece_map().items()
    )

    # Quadrados centrais
    quadrados_centrais = {chess.D4, chess.D5, chess.E4, chess.E5}
    pontuacao_controle_centro = sum(
        (1 if quadrado in quadrados_centrais else 0) * (1 if peca.color == chess.WHITE else -1)
        for quadrado, peca in board.piece_map().items()
    )

    # Estrutura de peões
    pontuacao_estrutura_peoes = sum(
        (1 if board.is_pinned(peca.color, quadrado) else 0) * (1 if peca.color == chess.WHITE else -1)
        for quadrado, peca in board.piece_map().items() if peca.piece_type == chess.PAWN
    )

    # Ameaça
    ameaca_valor = 0
    for square, piece in board.piece_map().items():
        if piece and piece.color == chess.WHITE:
            attackers = board.attackers(chess.BLACK, square)
            ameaca_valor += len(attackers)
            if piece.piece_type == chess.KING or piece.piece_type == chess.QUEEN:
                ameaca_valor += 1

        if piece and piece.color == chess.BLACK:
            attackers = board.attackers(chess.WHITE, square)
            ameaca_valor += len(attackers)
            if piece.piece_type == chess.KING or piece.piece_type == chess.QUEEN:
                ameaca_valor += 1
            ameaca_valor = -(ameaca_valor)

    # Desenvolvimento das peças
    pontuacao_desenvolvimento = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None and piece.color == chess.WHITE:
            pontuacao_desenvolvimento += 1 if piece.piece_type != chess.PAWN else 0
        elif piece is not None and piece.color == chess.BLACK:
            pontuacao_desenvolvimento -= 1 if piece.piece_type != chess.PAWN else 0

    # Pesos para cada componente
    peso_material = 0.6
    peso_mobilidade = 0.1
    peso_controle_centro = 0.2
    peso_estrutura_peoes = 0.1
    peso_ameaca = 0.1
    peso_desenvolvimento = 0.1

    # Pontuação total ponderada
    pontuacao_total = (
        peso_material * pontuacao_material +
        peso_mobilidade * pontuacao_mobilidade +
        peso_controle_centro * pontuacao_controle_centro +
        peso_estrutura_peoes * pontuacao_estrutura_peoes +
        peso_ameaca * ameaca_valor +
        peso_desenvolvimento * pontuacao_desenvolvimento
    )
    return pontuacao_total