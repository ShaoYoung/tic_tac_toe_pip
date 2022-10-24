from tictactoe import Board

print('Крестики-нолики')
# можно задать количество строк, столбцов и минимальное кол-во подряд идущих символов, необходимое для победы
row = 3
col = 3
win_pos = 3
board = Board((row, col), win_pos)
board.create_board()
count = 0
print(board)

while count < row * col:
    # print(f'Ходит {board.turn}')
    while True:
        attempt = input(f'Игрок {board.turn}, введите координаты (два числа, разделённые пробелом) -> ')
        if attempt.find(' ') != -1:
            attempt = attempt.split(' ')
            attempt = tuple(map(lambda x: int(x) if x.isdigit() else -1, attempt))
            if attempt[0] in range(row) and attempt[1] in range(col):
                break
    try:
        board.push(attempt)
        print(board)
        count += 1
        # т.к. в библиотеке нет варианта "НИЧЬЯ" при заполнении всего поля, то надо считать ходы и контролировать row * col
        # чтобы не переписывать код tictactoe
        if count == row * col:
            print('Боевая ничья!')
            break
        elif board.result() != None:
            print(f'Выиграл игрок {board.result()}')
            break
    except:
        print('Место занято!')


