# Chris Infante
# Week 2 Prove: Solo Code Submission
# Tic-Tac-Toe Game


# Make the Board (Define playing locations and number of moves)
location = ['1','2','3','4','5','6','7','8','9']
played = [0,1,2,3,4,5,6,7,8]

# Print the location
def gamelocation():
    print(' ')
    print( location[0] + ' | ' + location[1] + ' | ' + location[2])
    print('--+---+--')
    print( location[3] + ' | ' + location[4] + ' | ' + location[5])
    print('--+---+--')
    print( location[6] + ' | ' + location[7] + ' | ' + location[8])
    print(' ')
    
# Troubleshooting
'''    print(location[0])
    print(location[1])
    print(location[2])
    print(location[3])
    print(location[4])
    print(location[5])
    print(location[6])
    print(location[7])
    print(location[8]) '''

# Adding some color
class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# function to validate and enter input from players
def playerMove(player):
  playerCharacter = ['X','O']
  validInput = True

  player == 1
  symbol = playerCharacter[player]
  playerNo = player +1
  moveLocation = int(input('Player # ' + str(playerNo) + "'s turn! Choose a location to place a " + symbol + ': '))
  # Changing the named location to the actual location of the array
  position = moveLocation -1

  if location[position] == 'X' or location[position] == 'O':
    validInput = False
  
  if not validInput:
    print(color.RED + 'This spot is already taken, try again' + color.END)
    playerMove(player)
  else:
    played.remove(position)
    location[position] = playerCharacter[player] 
    return 1

# function to check if the game is over
def gameWon():
  # define players symbols and winning combinations
  playerCharacter = ['X','O']
  winningCombos =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  #check all winning possibilities for matches
  for check in winningCombos:
    character1 = location[check[0]]
    if character1 != ' ':
      won = True
      for point in check:
        if location[point] !=  character1:
          won = False
          break
      if won:
        if character1 == playerCharacter[0]:
          gamelocation()
          print()
          print(color.GREEN + 'Player 1 wins!' + color.END)
          print()
        else:
          gamelocation()
          print()
          print(color.GREEN + 'Player 2 wins!' + color.END)
          print()
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1

#function to play game
def main():
  player = 0
  while played and gameWon():    
    gamelocation()
    playerMove(player)
    player = int(not player)
  if not played:
    print()
    print(color.YELLOW + 'This game is a Draw! Better luck next time!' + color.END)
    print()

main()