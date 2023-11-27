import chess

def evaluate_board(board):
    # Dicionário de valores relativos das peças
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 1000
    }

    # Avaliação baseada no material
    material_score = sum(
        piece_values[piece.piece_type] * (1 if piece.color == chess.WHITE else -1)
        for piece in board.piece_map().values()
    )

    # Avaliação baseada na mobilidade
    mobility_score = sum(
        len(list(board.legal_moves)) * (1 if piece.color == chess.WHITE else -1)
        for piece in board.piece_map().values()
    )

    # Avaliação baseada no controle do centro
    center_squares = {chess.D4, chess.D5, chess.E4, chess.E5}
    center_control_score = sum(
        (1 if board.piece_at(square) and square in center_squares else 0) * (1 if board.piece_at(square).color == chess.WHITE else -1)
        for square in center_squares if board.piece_at(square)
    )

    # Avaliação baseada na estrutura de peões
    pawn_structure_score = sum(
        (1 if board.is_pinned(piece.color, square) else 0) * (1 if piece.color == chess.WHITE else -1)
        for square, piece in board.piece_map().items() if piece and piece.piece_type == chess.PAWN
    )


    # Pontuações ponderadas
    weighted_material_score = 0.6 * material_score
    weighted_mobility_score = 0.1 * mobility_score
    weighted_center_control_score = 0.2 * center_control_score
    weighted_pawn_structure_score = 0.1 * pawn_structure_score

    total_score = weighted_material_score + weighted_mobility_score + weighted_center_control_score + weighted_pawn_structure_score

    return total_score