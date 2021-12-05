lines = open("Day04/input.txt").read().split('\n')
BOARD_ROWS_COUNT = 5

def parse_board_line(line):
    return [int(x) for x in line.split(' ') if len(x)]

def parse(lines):
    numbers_queue = [int(x) for x in lines[0].split(",")]
    boards_lines = lines[1:]
    boards = []
    while len(boards) * (BOARD_ROWS_COUNT + 1) < len(boards_lines):
        current_index = len(boards)
        first_row_index = current_index * (BOARD_ROWS_COUNT + 1) + 1
        current_board_lines = boards_lines[first_row_index:first_row_index + BOARD_ROWS_COUNT]
        board = [parse_board_line(x) for x in current_board_lines]
        boards.append(board)
    return numbers_queue, boards

numbers_queue, boards = parse(lines)

def get_marked_number(n, number):
    return None if number == None or number == n else number


def mark_number(n, boards):
    for board in (boards):
        for row in board:
            for i, number in enumerate(row):
                row[i] = None if number == None or number == n else number

def check_all_none(row):
    return len([x for x in row if x != None]) == 0

def check_win(board):
    for row in board:
        if check_all_none(row):
            return True

    for i in range(BOARD_ROWS_COUNT):
        if len([1 for row in board if row[i] != None]) == 0:
            return True

    return False

def try_get_winner_board(boards):
    for i, board in enumerate(boards):
        if check_win(board):
            return board, i
    return None, None

def get_unmarked_numners(board):
    result = []
    for row in board:
        result = result + [x for x in row if x != None]
    return result

def calculate_result(board, number):
    unmarked_numbers = get_unmarked_numners(board)
    return sum(unmarked_numbers) * number

# part 1
def play_game_1(boards, numbers_queue):
    for n in numbers_queue:
        mark_number(n, boards)
        winner, index = try_get_winner_board(boards)
        if winner:
            return winner, n
    return None, None

winner_board, winner_number = play_game_1(boards, numbers_queue)
print(calculate_result(winner_board, winner_number))

# part 2

def play_game_2(boards, numbers_queue):
    for n in numbers_queue:
        mark_number(n, boards)

        while True:
            winner, index = try_get_winner_board(boards)
            if winner == None:
                break

            if len(boards) > 1:
                del boards[index]
            else:
                return winner, n

winner_board, winner_number = play_game_2(boards, numbers_queue)
print(calculate_result(winner_board, winner_number))