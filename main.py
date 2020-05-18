def print_board(str_list):
    print('---------')
    for index in range(0,3):
        subline = str_list[index*3:index*3+3]
        print(f'| {" ".join(subline)} |')
    print('---------')
    range

def three_in_row(line):
    if line == 'XXX':
        return 'X'
    elif line == 'OOO':
        return 'O'
    else:
        return None

def validate_game(str_list):
    x_count = 0
    o_count = 0
    for l in str_list:
        if l == 'X':
            x_count += 1
        if l == 'O':
            o_count += 1
    if(abs(x_count - o_count ) >= 2):
        return False
    else:
        return True

def judge(str_list):
    if not validate_game(str_list):
        return 'Impossible'
        
    sublines = []
    x_win = False
    o_win = False
    result = None

    for index in range(0,3):
        sublines.append(''.join(str_list[index*3:index*3+3]))
        sublines.append(''.join([str_list[index], str_list[index + 3], str_list[index + 6]]))   

    sublines.append(''.join([str_list[0], str_list[4], str_list[8]]))
    sublines.append(''.join([str_list[2], str_list[4], str_list[6]]))
    
    # loop all the possible rows
    for line in sublines:
        result = three_in_row(line)
        if result == 'X':
          x_win = True
        if result == 'O':
          o_win = True

    if x_win and o_win:
        return 'Impossible'
    elif x_win or o_win:
        return 'X wins' if x_win else 'O wins'
    elif '_' in str_list:
        return 'Game not finished'
    else:
        return 'Draw'

def is_int(val):
    try:
        _ = int(val)
    except ValueError:
        return False
    return True

def verify_move(current, move_input, player):
  move = move_input.split(' ')
  for t in move:
    if not is_int(t):
      return False, 'You should enter numbers!'
    if int(t) > 3 or int(t) < 1:
      return False, 'Coordinates should be from 1 to 3!'
  
  # find current location
  move_int = [int(move[0]), int(move[1])]
  loc = 3* (3 - move_int[1]) + move_int[0] - 1
  loc_state = current[loc]
  if loc_state != '_':
    return False, 'This cell is occupied! Choose another one!'
  else:
    current[loc] = player
    return True, current

def init_game():
    return list('_________')

def user_input(game_state, player):
    valid_move = False
    while(not valid_move):
        move_input = input("Enter the coordinates: > ")
        valid,result = verify_move(game_state, move_input, player)
        if not valid:
            print(result)
            valid_move = False
        else:
            game_state = result
            valid_move = True
    return game_state
    
    
# start game
game_over = False
player = ['X', 'O']
rounds = 0 
game_state = init_game()

while(not game_over):
    print_board(game_state)
    game_state = user_input(game_state, player[rounds % 2])
    verdict = judge(game_state)
    rounds += 1
    if 'wins' in verdict or verdict == 'Draw':
        print_board(game_state)
        print(verdict)
        game_over = True
