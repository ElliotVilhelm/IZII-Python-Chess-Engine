from engine.move import move_at_state
from react.react_chess_to_IZII_state import react_chess_board_to_IZII_board
from engine.search import best_move
from engine.utils import print_board
from engine.utils import int_sq120_sq64, sq64_to_RF, RF_sq64, sq64_to_sq120
from engine.gen_moves import get_all_moves_at_state
import sys


try:
    # State = {board, turn, en pass, half move, full move, castle perms, wk sq, bk sq]}
    # init_state = [init_board, 0, -1, 0, 1, [0, 0, 0, 0], init_board.index('K'), init_board.index('k')]
    if sys.argv[1] == 'undefined':
        print("undefined args")
        exit(1)

    state = [0, 0, 0, 0, 0, 0, 0, 0]
    state[0] = react_chess_board_to_IZII_board(sys.argv[1])
    state[1] = int(sys.argv[2])
    state[2] = int(sys.argv[3])
    state[3] = 0
    state[4] = 0
    castle_perms = sys.argv[6]
    state[5] = [int(castle_perms[0]), int(castle_perms[1]), int(castle_perms[2]), int(castle_perms[3])]  # for now
    state[6] = state[0].index('K')
    state[7] = state[0].index('k')

    all_moves = get_all_moves_at_state(state)
    from_sq = sys.argv[7]
    to_sq = sys.argv[8]
    from_sq = sq64_to_sq120(RF_sq64(from_sq[0], from_sq[1]))
    to_sq = sq64_to_sq120(RF_sq64(to_sq[0], to_sq[1]))
    move = [from_sq, to_sq]

    if move in all_moves:
        print("true")
    else:
        print("false")

except Exception as e:
    print(e)
    print("EXCEPTION")
    exit()



