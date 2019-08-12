import tkinter
from tkinter import *


#################################################################################################################################################################################
# 					
#					problem for later is figuing out a tripple jump with recursion?
#
#				figure out how to get rid of the double click after kills and button clicks
#
# 		to change it to one function for checking have the board be a 3D array instead of a 2D array with a value for piece type and a value for color 
#
#		figure out how to program a minimax algorithm for checkers
#
#############################################################################################################################################################################################

global death
death = False
global moves
moves = []
global current_piece
current_piece = ['*','*']
global turn_num 
turn_num = 0
global cur_pos
cur_pos = [1000,1000]

def clicker(event):
	global cur_pos
	cur_pos = [event.x,event.y]

def play_1player_checkers(window,board):
	board.delete(tkinter.ALL)
	board.create_text(320,320,text= "Please come back later")
	while cur_pos == [1000,1000]:
		window.update_idletasks()
		window.update()
	display_menu(window,board)


def display_menu(window,board):	# buttons aren't working right
	global cur_pos
	board.delete(tkinter.ALL)
	board.create_rectangle(0,0,640,640, fill = 'coral')
	board.create_text(320,50,text="Edgar's Wonderful",font=('Comic Sans MS',40))
	board.create_text(320,110,text="Checkers",font=('Comic Sans MS',40))
	board.create_rectangle(245,175,395,250, fill = 'gray')
	board.create_rectangle(245,275,395,350, fill = 'gray')
	board.create_rectangle(245,375,395,450, fill = 'gray')
	board.create_rectangle(245,475,395,550, fill = 'gray')
	board.create_text(320,212,text="1 Player",font=('Comic Sans MS',20))
	board.create_text(320,312,text="2 Player",font=('Comic Sans MS',20))
	board.create_text(320,412,text="Rules",font=('Comic Sans MS',20))
	board.create_text(320,512,text="Exit",font=('Comic Sans MS',20))
	while (not((cur_pos[0] in range(245,396)) and (cur_pos[1] in range(175,251)))) and (not((cur_pos[0] in range(245,396)) and (cur_pos[1] in range(275,351)))) and (not((cur_pos[0] in range(245,396)) and (cur_pos[1] in range(375,451)))) and (not((cur_pos[0] in range(245,396)) and (cur_pos[1] in range(475,551)))):
		window.update_idletasks()
		window.update()
	if (cur_pos[0] in range(245,396)) and (cur_pos[1] in range(175,251)):
		cur_pos = [1000,1000]
		play_1player_checkers(window,board)
	elif (cur_pos[0] in range(245,396)) and (cur_pos[1] in range(275,351)):
		cur_pos = [1000,1000]
		play_2player_checkers(window,board)
	elif (cur_pos[0] in range(245,396)) and (cur_pos[1] in range(375,451)):
		cur_pos = [1000,1000]
		display_rules(window,board)
	elif (cur_pos[0] in range(245,396)) and (cur_pos[1] in range(475,551)):
		pass

def display_rules(window,board): 	# buttons aren't working right
	global cur_pos
	board.delete(tkinter.ALL)
	board.create_rectangle(0,0,640,640, fill = 'coral')
	board.create_text(320,50,text="Rules",font=('Comic Sans MS',40))
	board.create_rectangle(245,475,395,550,fill = 'gray')
	board.create_text(320,512, text = "Back", font = ('Comic Sans MS', 40))
	board.create_text(320,130,text = "Objective", font= ('Comic Sans MS',20), fill = 'black')
	board.create_text(320,165,text = "To win you must capture all of your oponent's piece", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,205,text = "Peices", font= ('Comic Sans MS',20), fill = 'black')
	board.create_text(320,235,text = "-Peices can only move forwards on diagonals", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,255,text = "-Kings can move as far as they want in any direction", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,290,text = "How to play", font= ('Comic Sans MS',20), fill = 'black')
	board.create_text(320,315,text = "-You can capture an oponent's piece by jumping over it", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,335,text = "-If a piece makes it across the board it becomes a king", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,355,text = "-Peices are blocked if there is a peice infont of them that they", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,375,text = "can't jump over", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,395,text = "-You can not jump over your own piece or an oponent's piece if", font= ('Comic Sans MS',15), fill = 'black')
	board.create_text(320,415,text = "there is another piece behind them", font= ('Comic Sans MS',15), fill = 'black')
	while not((cur_pos[0] in range(245,396)) and (cur_pos[1] in range(475,551))):
		window.update_idletasks()
		window.update()
	cur_pos = [1000,1000]
	display_menu(window,board)

def run_checkers():
	window = tkinter.Tk()    
	board = Canvas(window, width=640, height=640)
	board.pack()
	board.bind("<Button-1>", clicker)	
	display_menu(window,board)

	

def play_2player_checkers(window,board):   
	global moves
	global cur_pos
	global turn_num
	global current_piece
	current_piece = ['*','*']
	turn_num = 0
	moves = []

	# game_state=[['red_piece', None, 'red_piece', None, 'red_piece', None, 'red_piece', None], #normal game state
	# 			[None, 'red_piece', None, 'red_piece', None, 'red_piece', None, 'red_piece'],
	# 			['red_piece', None, 'red_piece', None, 'red_piece', None, 'red_piece', None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, 'black_piece', None, 'black_piece', None, 'black_piece', None, 'black_piece'],
	# 			['black_piece', None, 'black_piece', None, 'black_piece', None, 'black_piece', None],
	# 			[None, 'black_piece', None, 'black_piece', None, 'black_piece', None, 'black_piece']]

	game_state=[['red_king', None, None, None, None, None, None, None], #test state
				[None, 'black_piece', None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None],
				[None, None, None, None, None, None, None, None]]


	display_board(board,game_state)
	board.bind("<Button-1>",lambda event: turn(board,game_state,event))	
	while(count_black(game_state)!=0 and count_red(game_state)!=0):
		#print(count_black(game_state)!=0 or count_red(game_state)!=0)
		window.update_idletasks()
		window.update()
	board.delete(tkinter.ALL)
	board.create_rectangle(0,0,640,640, fill='coral')
	if count_black(game_state)==0:
		board.create_text(320,320, text="Red Wins",font=('Comic Sans MS',40))
	elif count_red(game_state)==0:
		board.create_text(320,320, text="Black Wins",font=('Comic Sans MS',40))
	board.create_rectangle(150,400,300,475, fill = 'gray')
	board.create_rectangle(340,400,490,475, fill = 'gray')
	board.create_text(225,437,text="Play again",font=('Comic Sans MS',20))
	board.create_text(415,437,text="Menu",font=('Comic Sans MS',20))
	board.bind("<Button-1>", clicker)	
	cur_pos = [1000,1000]
	while (not((cur_pos[0] in range(150,301)) and (cur_pos[1] in range(400,476))) and not((cur_pos[0] in range(340,491)) and (cur_pos[1] in range(400,476)))):
		window.update_idletasks()
		window.update()
	if ((cur_pos[0] in range(150,301)) and (cur_pos[1] in range(400,476))):
		cur_pos = [1000,1000]
		play_2player_checkers(window,board)
	elif ((cur_pos[0] in range(340,491)) and (cur_pos[1] in range(400,476))):
		cur_pos = [1000,1000]
		display_menu(window,board)

def show_tile(event):
	row = event.x//80
	column = event.y//80
	print('row is',row)
	print('column is', column)

def count_red(game_state):
	num = 0
	for i in game_state:
		num += (i.count('red_king') + i.count('red_piece'))
	return num

def count_black(game_state):
	num = 0
	for i in game_state:
		num += (i.count('black_king') + i.count('black_piece'))
	return num

def turn(board,game_state,event): #maxes at a double jump
	global moves
	global death
	global turn_num
	i = event.x//80
	j = event.y//80
	if turn_num%2 ==0: #red's turn
		if death:
			if len(moves) != 0:
				if [i,j] == current_piece:
					death = False
					turn_num += 1
				elif [i,j,True] in moves:
					num_black = count_black(game_state) 
					game_state = update_game_state(board,game_state,i,j)
					display_board(board,game_state)
					moves = []
					if num_black > count_black(game_state):
						death = True
						moves = show_kill_moves(board,game_state,i,j,'red')
						if len(moves) ==0:
							death = False
							turn_num += 1
					else:
						death = False

			else:
				death = False
		else:
			if [i,j,True] in moves or [i,j,False] in moves:
				num_black = count_black(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_black > count_black(game_state):
					death = True
					moves = show_kill_moves(board,game_state,i,j,'red')
				else:
					death = False
			else:
				moves = show_moves(board,game_state,i,j,'red')
	else: #black' turn
		if death:
			if len(moves) != 0:
				if [i,j] == current_piece:
					death = False
				elif [i,j,True] in moves:
					num_black = count_black(game_state) 
					game_state = update_game_state(board,game_state,i,j)
					display_board(board,game_state)
					moves = []
					if num_black > count_black(game_state):
						death = True
						moves = show_kill_moves(board,game_state,i,j,'black')
					else:
						death = False
			else:
				death = False
		else:
			if [i,j,True] in moves or [i,j,False] in moves:
				num_red = count_red(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_red > count_red(game_state):
					death = True
					moves = show_kill_moves(board,game_state,i,j,'black')
				else:
					death = False
			else:
				moves = show_moves(board,game_state,i,j,'black')
	#print(moves)

def update_game_state(board,game_state,i,j):
	global turn_num
	game_state = move_to(game_state,i,j)
	game_state = make_kings(game_state)
	if death:
		return game_state
	else:
		turn_num +=1
		return game_state

def make_kings(game_state):
	for row in range(8):
		if game_state[0][row] == 'black_piece':
			game_state[0][row] = 'black_king'
		if game_state[7][row] == 'red_piece':
			game_state[7][row] = 'red_king'
	return game_state

def move_to(game_state,i2,j2):
	i1 = current_piece[0]
	j1 = current_piece[1]
	piece = game_state[i1][j1]
	while i1!=i2:
		if i1>i2:
			if j1>j2: # kill up left
				game_state[i1][j1] = None
				j1 -=1
				i1 -=1
			elif j1<j2: #kill down left
				game_state[i1][j1] = None
				j1 +=1
				i1 -=1
		elif i1<i2:
			if j1>j2: # kill up right
				game_state[i1][j1] = None
				j1 -=1
				i1 +=1
			elif j1<j2: # kill down right
				game_state[i1][j1] = None
				j1 +=1
				i1 +=1
	game_state[i2][j2] = piece
	return game_state

def show_kill_moves(board,game_state,i,j,player):
	display_board(board,game_state)
	global current_piece
	kill_moves = []
	if player == 'red': #red's turn
		if  game_state[i][j] == 'red_piece':
			moves = check_moves_red_piece(game_state,i,j)
			for move in moves:
				if move[2]:
					kill_moves += [move]
					x = move[0]
					y = move[1]
					board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
			
		elif game_state[i][j] == 'red_king':
			moves = check_moves_red_king(game_state,i,j)
			for move in moves:
				if move[2]:
					kill_moves += [move]
					x = move[0]
					y = move[1]
					board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		else:
			moves = []
	else: #black's turn
		if  game_state[i][j] == 'black_piece':
			moves = check_moves_black_piece(game_state,i,j)
			for move in moves:
				if move[2]:
					kill_moves += [move]
					x = move[0]
					y = move[1]
					board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		elif game_state[i][j] == 'black_king':
			moves = check_moves_black_king(game_state,i,j)
			for move in moves:
				if move[2]:
					kill_moves += [move]
					x = move[0]
					y = move[1]
					board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		else:
			kill_moves = []
	current_piece = [i,j]
	return kill_moves

def show_moves(board,game_state,i,j,player):
	display_board(board,game_state)
	global current_piece
	if player == 'red': #red's turn
		if  game_state[i][j] == 'red_piece':
			moves = check_moves_red_piece(game_state,i,j)
			for move in moves:
				x = move[0]
				y = move[1]
				board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
			
		elif game_state[i][j] == 'red_king':
			moves = check_moves_red_king(game_state,i,j)
			for move in moves:
				x = move[0]
				y = move[1]
				board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		else:
			moves = []
	else: #black's turn
		if  game_state[i][j] == 'black_piece':
			moves = check_moves_black_piece(game_state,i,j)
			for move in moves:
				x = move[0]
				y = move[1]
				board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		elif game_state[i][j] == 'black_king':
			moves = check_moves_black_king(game_state,i,j)
			for move in moves:
				x = move[0]
				y = move[1]
				board.create_rectangle(80*x,80*y,80*(x+1),80*(y+1), fill='green')
		else:
			moves = []
	current_piece = [i,j]
	return moves

def check_moves_red_king(game_state,i,j): #next iteration will have a color imput

	def red_king_check_top_right(game_state,i,j):
		if i==7 or j==0:
			return []
		if game_state[i+1][j-1] == 'red_piece' or game_state[i+1][j-1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j-1] == 'black_piece' or game_state[i+1][j-1] == 'black_king':
			if (i+2==8 or j-2==-1) or game_state[i+2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j-2,True]]
		else:
			return [[i+1,j-1,False]] + red_king_check_top_right(game_state,i+1,j-1)

	def red_king_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'black_piece' or  game_state[i-1][j-1] == 'black_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2,True]]
		else:
			return [[i-1,j-1,False]] + red_king_check_top_left(game_state,i-1,j-1)

	def red_king_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king':
			if (i+2==8 or j+2==8) or (game_state[i+2][j+2] != None): #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2,True]]
		else:
			return [[i+1,j+1,False]] + red_king_check_bottom_right(game_state,i+1,j+1)

	def red_king_check_bottom_left(game_state,i,j):		
		if i==0 or j==7:
			return []
		if game_state[i-1][j+1] == 'red_piece' or game_state[i-1][j+1] == 'red_king' : #blocked
			return []
		elif game_state[i-1][j+1] == 'black_piece' or  game_state[i-1][j+1] == 'black_king':
			if (i-2==-1 or j+2==8) or game_state[i-2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j+2,True]]
		else:
			return [[i-1,j+1,False]] + red_king_check_bottom_left(game_state,i-1,j+1)

	# i'm not sure if i need this if tree but better safe than sorry
	if i == 0: # left side
		if j == 0: # top left corner
			return red_king_check_bottom_right(game_state,i,j)
		elif j == 7:	 #bottom left corner
			return red_king_check_top_right(game_state, i,j)
		else:
			return red_king_check_top_right(game_state, i,j) + red_king_check_bottom_right(game_state, i,j)
	if i == 7: #right side
		if j ==0: # top right corner
			return red_king_check_bottom_left(game_state, i,j)
		elif j == 7: # bottom right corner
			return red_king_check_top_left(game_state, i,j)
		else:
			return red_king_check_top_left(game_state, i,j) + red_king_check_bottom_left(game_state, i,j)
	if j == 0:#top
		return red_king_check_bottom_left(game_state, i,j) + red_king_check_bottom_right(game_state, i,j)
	if j == 7:#bottom
		return red_king_check_top_left(game_state, i,j) + red_king_check_top_right(game_state, i,j)
	else:
		return red_king_check_top_left(game_state, i,j)+ red_king_check_bottom_left(game_state, i,j) + red_king_check_bottom_right(game_state, i,j) + red_king_check_top_right(game_state, i,j) ####### for all add information about the piece it captures

def check_moves_black_king(game_state,i,j): #next iteration will have a color imput

	def black_king_check_top_right(game_state,i,j):
		if i==7 or j==0:
			return []
		if game_state[i+1][j-1] == 'black_piece' or game_state[i+1][j-1] == 'black_king': #blocked
			return []
		elif game_state[i+1][j-1] == 'red_piece' or game_state[i+1][j-1] == 'red_king':
			if (i+2==8 or j-2==-1) or game_state[i+2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j-2,True]]
		else:
			return [[i+1,j-1,False]] + black_king_check_top_right(game_state,i+1,j-1)

	def black_king_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'black_piece' or game_state[i-1][j-1] == 'black_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2,True]]
		else:
			return [[i-1,j-1,False]] + black_king_check_top_left(game_state,i-1,j-1)

	def black_king_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king':
			if (i+2==8 or j+8==7) or game_state[i+2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2,True]]
		else:
			return [[i+1,j+1,False]] + black_king_check_bottom_right(game_state,i+1,j+1)

	def black_king_check_bottom_left(game_state,i,j):
		if i==0 or j==7:
			return []
		if game_state[i-1][j+1] == 'black_piece' or game_state[i-1][j+1] == 'black_king' : #blocked
			return []
		elif game_state[i-1][j+1] == 'red_piece' or game_state[i-1][j+1] == 'red_king':
			if (i-2==-1 or j+2==8) or game_state[i-2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j+2,True]]
		else:
			return [[i-1,j+1,False]] + black_king_check_bottom_left(game_state,i-1,j+1)

	# i'm not sure if i need this if tree but better safe than sorry
	if i == 0: # left side
		if j == 0: # top left corner
			return black_king_check_bottom_right(game_state,i,j)
		elif j == 7:	 #bottom left corner
			return black_king_check_top_right(game_state, i,j)
		else:
			return black_king_check_top_right(game_state, i,j) + black_king_check_bottom_right(game_state, i,j)
	if i == 7: #right side
		if j ==0: # top right corner
			return black_king_check_bottom_left(game_state, i,j)
		elif j == 7: # bottom right corner
			return black_king_check_top_left(game_state, i,j)
		else:
			return black_king_check_top_left(game_state, i,j) + black_king_check_bottom_left(game_state, i,j)
	if j == 0:#top
		return black_king_check_bottom_left(game_state, i,j) + black_king_check_bottom_right(game_state, i,j)
	if j == 7:#bottom
		return black_king_check_top_left(game_state, i,j) + black_king_check_top_right(game_state, i,j)
	else:
		return black_king_check_top_left(game_state, i,j)+ black_king_check_bottom_left(game_state, i,j) + black_king_check_bottom_right(game_state, i,j) + black_king_check_top_right(game_state, i,j)#need to fix these

def check_moves_red_piece(game_state,i,j): #next iteration will have a color imput

	def red_piece_check_top_right(game_state,i,j):
		if i==7 or j==0:
			return []
		if game_state[i+1][j-1] == 'red_piece' or game_state[i+1][j-1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j-1] == 'black_piece' or  game_state[i+1][j-1] == 'black_king':
			if (i+2==8 or j-2==-1) or game_state[i+2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j-2,True]]
		else:
			return [[i+1,j-1,False]]

	def red_piece_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king':
			if (i+2==8 or j+2==8) or game_state[i+2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2,True]]
		else:
			return [[i+1,j+1,False]]

	if j == 0: # top side
		return red_piece_check_bottom_right(game_state, i,j)
	elif j == 7: #bottom side
		return red_piece_check_top_right(game_state, i,j)
	else:
		return red_piece_check_bottom_right(game_state, i,j) + red_piece_check_top_right(game_state, i,j)

def check_moves_black_piece(game_state,i,j): #next iteration will have a color imput

	def black_piece_check_bottom_left(game_state,i,j):
		if i==0 or j==7:
			return []
		if game_state[i-1][j+1] == 'black_piece' or game_state[i-1][j+1] == 'black_king': #blocked
			return []
		elif game_state[i-1][j+1] == 'red_piece' or game_state[i-1][j+1] == 'red_king':
			if (i-2==-1 or j+2==8) or game_state[i-2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j+2,True]]
		else:
			return [[i-1,j+1,False]]

	def black_piece_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'black_piece' or game_state[i-1][j-1] == 'black_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2,True]]
		else:
			return [[i-1,j-1,False]]
	# i'm not sure if i need this if tree but better safe than sorry
	if j == 0: # top
		return black_piece_check_bottom_left(game_state, i,j)
	if j == 7: #bottom
		return black_piece_check_top_left(game_state, i,j)
	else:
		return black_piece_check_top_left(game_state, i,j) + black_piece_check_bottom_left(game_state, i,j)

def make_board():  # creates the starting game state
	red_side = []
	black_side = []
	for i in range(3):
		row = []
		for j in range(8):
			if (i+j)%2 == 0:
				row.append('red_piece')
			else:
				row.append(None)
		red_side.append(row)
	for i in range(3):
		row = []
		for j in range(8):
			if (i+j)%2 == 1:
				row.append('black_piece')
			else:
				row.append(None)	
		black_side.append(row)
	game_state = red_side + [[None]*8]*2 + black_side
	return game_state

def display_board(board,game_state): # displays the current game state
	board.delete(tkinter.ALL)
	for i in range(8):
		for j in range(8):
			#board color
			if (i+j)%2 == 0:
				color = 'saddlebrown'
			else:
				color = 'peru'
			#pieces on board
			if game_state[i][j] == 'red_piece' :
				board.create_rectangle(80*i,80*j,80*(i+1),80*(j+1), fill=color)
				board.create_oval((80*i)+5,(80*j)+5,(80*(i+1))-5,(80*(j+1))-5, fill='red')
			elif game_state[i][j] == 'black_piece':
				board.create_rectangle(80*i,80*j,80*(i+1),80*(j+1), fill=color)
				board.create_oval((80*i)+5,(80*j)+5,(80*(i+1))-5,(80*(j+1))-5, fill='black')
			elif game_state[i][j] == 'red_king':
				board.create_rectangle(80*i,80*j,80*(i+1),80*(j+1), fill=color)
				board.create_oval((80*i)+5,(80*j)+5,(80*(i+1))-5,(80*(j+1))-5, fill='gold')
				board.create_oval((80*i)+10,(80*j)+10,(80*(i+1))-10,(80*(j+1))-10, fill='red')
			elif game_state[i][j] == 'black_king':
				board.create_rectangle(80*i,80*j,80*(i+1),80*(j+1), fill=color)
				board.create_oval((80*i)+5,(80*j)+5,(80*(i+1))-5,(80*(j+1))-5, fill='gold')
				board.create_oval((80*i)+10,(80*j)+10,(80*(i+1))-10,(80*(j+1))-10, fill='black')
			else:
				board.create_rectangle(80*i,80*j,80*(i+1),80*(j+1), fill=color) 



run_checkers()