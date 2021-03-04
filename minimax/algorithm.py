from copy import deepcopy
import pygame

RED = (255,0,0)
WHITE = (255, 255, 255)

global numMinMax 
numMinMax = 0

def getNum():
    global numMinMax 
    print("BRANCHES EVALUEATED:	" + str(numMinMax))
    numMinMax = 0

# maxplayer = True --> white
# maxplayer = False --> Red
# Returns: evaluation, board
def minimax(board, depth, max_player, game, alpha, beta):
	# If depth 0 then evaluate
    global numMinMax 
    numMinMax += 1

    if depth == 0 or board.winner() != None:
        return board.evaluate(), board

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(board,WHITE,game):
            score, testMove = minimax(move, depth-1, False,game,alpha,beta)
            if score > maxEval:
                maxEval = score
                best_move = move
            alpha = max(alpha,score)
            if(beta <= alpha):
                break
        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(board,RED,game):
            score, testMove = minimax(move, depth-1, True,game,alpha,beta)
            if score < minEval:
                minEval = score
                best_move = move
            beta = min(beta,score)
            if(beta <= alpha):
                break
        return minEval, best_move

#Returns a list of board objects
def get_all_moves(board, color, game):
	moves = []
	for piece in board.get_all_pieces(color):
		new_moves = board.get_valid_moves(piece)

		for move, skip in new_moves.items():
			temp_board = deepcopy(board)
			temp_piece = temp_board.get_piece(piece.row,piece.col)
			new_board = simulate_move(temp_piece, move,temp_board,game,skip)
			moves.append(new_board)

	return moves

def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board
