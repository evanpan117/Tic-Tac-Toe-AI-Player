# --------- Global Variables -----------
import random
import time
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
move_count = 0
current_player = "X"
player = "O"
AI = "X"
# ------------- Functions ---------------
# Play a game of tic tac toe
def play_game():
  global move_count
  display_board()  #display game board
  who_go_first()    #determe the move sequence
  while move_count < 9: #when the board is not full the game goes
    # Handle a turn
    if current_player == AI:
        AI_move()
        if isWinner(board,AI):
            print("AI won!!! You lost!")
            move_count = 10
        else:
            move_count += 1
    else:
        player_turn()
        if isWinner(board, player):
            print("You won!!! You are amazing!")
            move_count = 10
        else:
            move_count += 1
    flip_player()                       # change to the other player
  if move_count != 10:
    print("Tie. Good game!")

# Define who goes first
def who_go_first():
    global player
    global AI
    print("Pick your turn.")              # Get position from player
    choose = input("X goes first, O second: ")
    if choose == 'X' or choose =='x':
        player = 'X'
        AI = 'O'

# Display the game board to the screen
def display_board():
  print("\n")
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
  print("\n")

# Define AI move algorithm
def AI_move():
    global board
    time.sleep(0.6)                 #time delay
    board[AI_algorithm()] = AI;    #AI's move based on the algorithm
    print("AI master(" + AI +")'s move'")
    display_board()

#Algorithm of the compuer play
def AI_algorithm():
    possibleMoves = [x for x, letter in enumerate(board) if letter == '-' ] # Create a list of possible moves
    #Check for possible winning move to take or to block opponents winning move
    for let in [AI,player]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                return i
    #Try to take the center
    if 4 in possibleMoves:
        return 4
    #Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        if i in [0,2,6,8]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        return random.choice(cornersOpen)
     #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [1,3,5,7]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        return random.choice(edgesOpen)

# Handle a turn for an arbitrary player
def player_turn():
  print("It's your turn(" + player + ")" )
  valid = False
  while not valid:
    position = int(input("Choose a position from 1-9: "))
    if board[position-1] == "-":
        board[position-1] = player    # Put the game piece on the board
        valid = True
    else:
      print("You can't go there. Go again.")
  display_board()

#to check winning position
def isWinner(bo, le):
    # Given a board and a player’s letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don’t have to type as much.
    return ((bo[0] == bo[1] == bo[2] == le) or # across the top
            (bo[3] == bo[4] == bo[5] == le) or # across the middle
            (bo[6] == bo[7] == bo[8] == le) or # across the bottom
            (bo[0] == bo[3] == bo[6] == le) or # down the left side
            (bo[1] == bo[4] == bo[7] == le) or # down the middle
            (bo[2] == bo[5] == bo[8] == le) or # down the right side
            (bo[0] == bo[4] == bo[8] == le) or # diagonal
            (bo[2] == bo[4] == bo[6] == le))   # diagonal

# Flip the current player from X to O, or O to X
def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"

# ------------ Start Execution -------------
play_game()         # Play a game of tic tac toe
