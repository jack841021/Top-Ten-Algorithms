import numpy
board = numpy.array([[0,3,0,9,8,7,0,0,6],
                     [4,0,0,0,0,0,5,0,0],
                     [0,6,0,0,0,0,8,0,0],
                     [0,1,7,0,3,4,0,6,0],
                     [8,5,6,0,0,0,1,3,4],
                     [0,2,0,6,1,0,7,5,0],
                     [0,0,3,4,0,0,0,2,0],
                     [0,0,1,0,0,0,0,0,7],
                     [5,0,0,8,7,3,0,4,0]])

def solver(board):
    candidate = [(0, board)]
    while len(candidate) != 0:
        (depth, cboard) = candidate[0]
        del candidate[0]
        if depth == 81:
            for n in candidate:
                print(n[1], '\n')
            print(cboard)
            candidate.clear()
        else:
            col, row = depth // 9, depth % 9
            if cboard[col][row] != 0:
                candidate.append((depth + 1, cboard.copy()))
            else:
                moves = {1,2,3,4,5,6,7,8,9} - set(cboard[col, :]) - set(cboard[:, row]) - set(cboard[col//3*3:col//3*3+3, row//3*3:row//3*3+3].flatten())
                for n in moves:
                    nboard = cboard.copy()
                    nboard[col][row] = n
                    candidate.append((depth + 1, nboard))

solver(board)