board=[" " for i in range(9)]

def print_board():
	print()
	print("|{}|{}|{}|".format(board[0],board[1],board[2]))
	print("|{}|{}|{}|".format(board[3],board[4],board[5]))
	print("|{}|{}|{}|".format(board[6],board[7],board[8]))
	print()


def play_move(icon):
	if icon=='X':
		number=1
	if icon=='O':
		number=2
	print("Your turn player {}".format(number))
	choice=int(input("Enter your move(1-9): "))
	if board[choice-1]==" ":
		board[choice-1]=icon
	else:
		print("This is taken, select another move")
	

def victory(icon):
	if(board[0]==icon and board[1]==icon and board[2]==icon) or \
	  (board[3]==icon and board[4]==icon and board[5]==icon) or \
	  (board[6]==icon and board[7]==icon and board[8]==icon) or \
	  (board[0]==icon and board[3]==icon and board[6]==icon) or \
	  (board[1]==icon and board[4]==icon and board[7]==icon) or \
	  (board[2]==icon and board[5]==icon and board[8]==icon) or \
	  (board[1]==icon and board[4]==icon and board[8]==icon) or \
	  (board[2]==icon and board[4]==icon and board[6]==icon):
		return True 



def draw_game():
	if " " not in board:
		return True
	
while True:
	print_board()
	play_move('X')
	print_board()
	if victory('X'):
		print_board()
		print("Player X wins! Congratulations!")
		break
	elif draw_game():
		print("Game draw!")
		break
		
	play_move('O')
	if victory('O'):
		print_board()
		print("Player O wins! Congratulations!")
		break
	elif draw_game():
		print("Game draw!")
		break
