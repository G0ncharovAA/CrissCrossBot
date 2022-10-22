board = list(map(str, range(1, 10)))
win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def reset():
    global board
    board = list(map(str, range(1, 10)))


def draw_board():
    output = ""
    output += ('-' * 20)
    for i in range(3):
        output += "\n"
        for k in range(3):
            output += f"[ {board[k + i * 3]} ]"
            output += " "
        output += f"\n{'-' * 20}"
    output += "\n"
    return output


def place_sign(token, position):
    global board
    output = "ok"
    if position.isdigit() and int(position) in range(1, 10):
        answer = int(position)
        pos = board[answer - 1]
        if pos not in (chr(10060), chr(11093)):
            board[answer - 1] = chr(10060) if token == 0 else chr(11093)
        else:
            output = f"This cell is already occupied{chr(9995)}{chr(129292)}"
    else:
        output = f"Incorrect input{chr(9940)}, Are you sure you entered a correct number?"
    return output


def check_win():
    n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
    return n[0] if n else n
