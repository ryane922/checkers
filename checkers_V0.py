import tkinter
from tkinter import *

#################################################################################################################################################################################
# 					
#					!!!problem for tomarrow is figuing out a tripple with recursion?? and getting rid of non-kill moves during double jump !!!
#
# 		to change it to one function for checking have the board be a 3D array instead of a 2D array with a value for piece type and a value for color 
#
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

def play_2player_checkers():   
############# setting up the board ################
	global moves
	current_piece = ['*','*']
	turn_num = 0
	moves = []
	window = tkinter.Tk()    
	board = Canvas(window, width=640, height=640)
	board.pack()
	game_state = make_board()
	# game_state=[['red_piece', None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, None, None],
	# 			[None, None, None, None, None, None, 'black_piece', None]]

	display_board(board,game_state)
############# defining turns ###############################
	board.bind("<Button-1>",lambda event: turn0(board,game_state,event))	
	window.mainloop()

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

def turn0(board,game_state,event):
	global moves
	i = event.x//80
	j = event.y//80
	if turn_num%2 ==0: #red's turn
		if [i,j] in moves:
			num_black = count_black(game_state) 
			game_state = update_game_state(board,game_state,i,j)
			display_board(board,game_state)
			moves = []
		else:
			moves = show_moves(board,game_state,i,j,'red')
	else: #black' turn
		if [i,j] in moves:
			num_black = count_black(game_state) 
			game_state = update_game_state(board,game_state,i,j)
			display_board(board,game_state)
			moves = []
		else:
			moves = show_moves(board,game_state,i,j,'black')




def turn(board,game_state,event): #maxes at a double jump - needs lots of work
	global moves
	global death
	i = event.x//80
	j = event.y//80
	if turn_num%2 ==0: #red's turn
		if death:
			if [i,j] == current_piece:
				death = False
			elif [i,j] in moves:
				num_black = count_black(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_black > count_black(game_state):
					death = True
					moves = show_moves(board,game_state,i,j,'red')
				else:
					death = False
		else:
			if [i,j] in moves:
				num_black = count_black(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_black > count_black(game_state):
					death = True
					moves = show_moves(board,game_state,i,j,'red')
				else:
					death = False
			else:
				moves = show_moves(board,game_state,i,j,'red')
	else: #black' turn
		if death:
			if [i,j] == current_piece:
				death = False
			elif [i,j] in moves:
				num_black = count_black(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_black > count_black(game_state):
					death = True
					moves = show_moves(board,game_state,i,j,'black')
				else:
					death = False
		else:
			if [i,j] in moves:
				num_red = count_red(game_state) 
				game_state = update_game_state(board,game_state,i,j)
				display_board(board,game_state)
				moves = []
				if num_red > count_red(game_state):
					death = True
					moves = show_moves(board,game_state,i,j,'black')
				else:
					death = False
			else:
				moves = show_moves(board,game_state,i,j,'black')

def print_game_state(game_state):
	for column in game_state:
		print(column)
	print('')

def update_game_state(game_state,i,j):
	global turn_num
	print_game_state(game_state)
	game_state = move_to(game_state,i,j)
	print_game_state(game_state)
	game_state = make_kings(game_state)
	print_game_state(game_state)
	if death:
		return game_state
		print('something died')
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

def move_to(game_state,i2,j2): #douplicating peices domwtimes
	i1 = current_piece[0]
	j1 = current_piece[1]
	piece = game_state[i1][j1]
	print(i1,j1,'to',i2,j2)
	print(piece)
	while i1!=i2:
		if i1>i2:
			if j1>j2: # kill up left
				game_state[i1][j1] = None
				j1 -=1
				i1 -=1
				print('up left')
				print_game_state(game_state)
			elif j1<j2: #kill down left
				game_state[i1][j1] = None
				j1 +=1
				i1 -=1
				print('down left')
				print_game_state(game_state)
		elif i1<i2:
			if j1>j2: # kill up right
				game_state[i1][j1] = None
				j1 -=1
				i1 +=1
				print('up right')
				print_game_state(game_state)
			elif j1<j2: # kill down right
				game_state[i1][j1] = None
				j1 +=1
				i1 +=1
				print('down right')
				print_game_state(game_state)
	print('placing pieces')
	game_state[i2][j2] = piece
	print_game_state(game_state)
	return game_state

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
				return [[i+2,j-2]]
		else:
			return [[i+1,j-1]] + red_king_check_top_right(game_state,i+1,j-1)

	def red_king_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'black_piece' or  game_state[i-1][j-1] == 'black_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2]]
		else:
			return [[i-1,j-1]] + red_king_check_top_left(game_state,i-1,j-1)

	def red_king_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king':
			if (i+2==8 or j+2==8) or (game_state[i+2][j+2] != None): #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2]]
		else:
			return [[i+1,j+1]] + red_king_check_bottom_right(game_state,i+1,j+1)

	def red_king_check_bottom_left(game_state,i,j):		
		if i==0 or j==7:
			return []
		if game_state[i-1][j+1] == 'red_piece' or game_state[i-1][j+1] == 'red_king' : #blocked
			return []
		elif game_state[i-1][j+1] == 'black_piece' or  game_state[i-1][j+1] == 'black_king':
			if (i-2==-1 or j+2==8) or game_state[i-2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j+2]]
		else:
			return [[i-1,j+1]] + red_king_check_bottom_left(game_state,i-1,j+1)

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
				return [[i+2,j-2]]
		else:
			return [[i+1,j-1]] + black_king_check_top_right(game_state,i+1,j-1)

	def black_king_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'black_piece' or game_state[i-1][j-1] == 'black_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2]]
		else:
			return [[i-1,j-1]] + black_king_check_top_left(game_state,i-1,j-1)

	def black_king_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king':
			if (i+2==8 or j+8==7) or game_state[i+2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2]]
		else:
			return [[i+1,j+1]] + black_king_check_bottom_right(game_state,i+1,j+1)

	def black_king_check_bottom_left(game_state,i,j):
		if i==0 or j==7:
			return []
		if game_state[i-1][j+1] == 'black_piece' or game_state[i-1][j+1] == 'black_king' : #blocked
			return []
		elif game_state[i-1][j+1] == 'red_piece' or game_state[i-1][j+1] == 'red_king':
			if (i-2==-1 or j+2==8) or game_state[i-2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j+2]]
		else:
			return [[i-1,j+1]] + black_king_check_bottom_left(game_state,i-1,j+1)

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
				return [[i+2,j-2]]
		else:
			return [[i+1,j-1]]

	def red_piece_check_bottom_right(game_state,i,j):
		if i==7 or j==7:
			return []
		if game_state[i+1][j+1] == 'red_piece' or game_state[i+1][j+1] == 'red_king': #blocked
			return []
		elif game_state[i+1][j+1] == 'black_piece' or game_state[i+1][j+1] == 'black_king':
			if (i+2==8 or j+2==8) or game_state[i+2][j+2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i+2,j+2]]
		else:
			return [[i+1,j+1]]

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
				return [[i-2,j+2]]
		else:
			return [[i-1,j+1]]

	def black_piece_check_top_left(game_state,i,j):
		if i==0 or j==0:
			return []
		if game_state[i-1][j-1] == 'black_piece' or game_state[i-1][j-1] == 'black_king': #blocked
			return []
		elif game_state[i-1][j-1] == 'red_piece' or game_state[i-1][j-1] == 'red_king':
			if (i-2==-1 or j-2==-1) or game_state[i-2][j-2] != None: #blocked
				return []
			else:  #captured a piece
				return [[i-2,j-2]]
		else:
			return [[i-1,j-1]]
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

#play_2player_checkers()


game_state= make_board()
current_piece = [2,2]
update_game_state(game_state,3,3)