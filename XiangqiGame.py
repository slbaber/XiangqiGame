# Author: Sara Baber
# Date: 03/03/2020
# Description: CS162 Portfolio Project, replicates Xiangqi chinese checkers game.

class Piece:
    '''creates a class for our Pieces.  Parent class to the individual piece types that are also classes'''

    def __init__(self):
        '''uses composition to call methods from the board to get information about pieces'''
        self._board = Board()

    def is_legal_move(self, current, target):
        '''contains rules for each piece and determines if a move is legal from current position and target position
        given those rules.  conditionals below do not check for all the rules (like if the target position is
        occupied by an empty or enemy piece.  Those conditions are checked before method is executed via make_move.'''

        position = current
        current = self._board.get_piece(current)
        color = current[0]
        kind = current[1]

        if kind == 'horse':
            # moves one point orthogonally then one point diagonally away from current position unless blocked
            # conditions below allow for movement up, down, left, and right unless blocked
            if target[0] == position[0] + 2:
                if target[1] == position[1] - 1:
                    x = position[0] + 1
                    y = position[1]
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

                if target[1] == position[1] + 1:
                    x = position[0] - 1
                    y = position[1]
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

            if target[0] == position[0] - 2:
                if target[1] == position[1] + 1:
                    x = target[0] + 1
                    y = position[1]
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

                if target[1] == position[1] - 1:
                    x = target[0] - 1
                    y = position[1]
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

            if target[1] == position[1] + 2:
                if target[0] == position[0] - 1:
                    x = position[0]
                    y = position[1] + 1
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

                if target[0] == position[0] + 1:
                    x = position[0]
                    y = position[1] + 1
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

            if target[1] == position[1] - 2:
                if target[0] == position[0] - 1:
                    x = position[0]
                    y = position[1] - 1
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

                if target[0] == position[0] + 1:
                    x = position[0]
                    y = position[1] - 1
                    if self._board.get_piece([x, y]) == [0, 0]:
                        return True
                    else:
                        return False

        if kind == 'chariot':
            # moves and captures any distance orthogonally but cannot jump pieces of any color
            # conditions below allow for movement up, down, left, and right if there are no pieces between current
            # and target locations

            if position[1] == target[1] or position[0] == target[0]:
                if position[1] == target[1]:
                    if abs(position[0] - target[0]) == 1:
                        return True

                    if (position[0] - target[0]) < -1:
                        y = position[1]
                        for i in range(position[0]+1, target[0]):
                            if self._board.get_piece([i, y]) != [0, 0]:  # doesn't allow for player pieces in path
                                return False
                        else:
                            return True

                    if (position[0] - target[0]) > 1:
                        y = position[1]
                        for i in range(target[0] + 1, position[0]):
                            if self._board.get_piece([i, y]) != [0, 0]:  # doesn't allow for player pieces in path
                                return False
                        else:
                            return True

                else:
                    if position[0] == target[0]:
                        if abs(position[1] - target[1]) == 1:
                            return True

                        if (position[1] - target[1]) < -1:
                            x = position[0]
                            for i in range(position[1] + 1, target[1]):
                                if self._board.get_piece([x, i]) != [0, 0]:  # doesn't allow for player pieces in path
                                    return False
                            else:
                                return True

                        if (position[1] - target[1]) > 1:
                            x = position[0]
                            for i in range(target[1] + 1, position[1]):
                                if self._board.get_piece([x, i]) != [0, 0]:  # doesn't allow for player pieces in path
                                    return False
                            else:
                                return True

        if kind == 'soldier':
            # moves and captures by advancing one point until it crosses the river (center row of the board).
            # Then, it is allowed to also move and capture left and right conditions below allow for movement
            # up(for red) and down(for black) before the river is reached then allows for left and right movement
            # once the river is crossed

            if target[1] == position[1]:
                if color == 'red':
                    if position[0] == target[0] - 1:
                        return True
                    else:
                        False

                if color == 'black':
                    if target[0] == position[0] - 1:
                        return True
                    else:
                        False

            if target[0] == position[0]:

                if color == 'red' and position[0] > 4:  # doesn't allow left/right movement if on red side of river
                    if target[1] == position[1] + 1 or target[1] == position[1] - 1:
                        return True
                    else:
                        return False

                if color == 'black' and position[0] < 5:  # doesn't allow left/right movement if on right side of river
                    if target[1] == position[1] - 1 or target[1] == position[1] + 1:
                        return True
                    else:
                        return False

            return False

        if kind == 'general':
            # only allows for orthogonal movement (up, down, left, and right) within the palace.
            # the palace is a 3X3 area that starts at the middle edge (row 1 for red, row 10 for black)
            # of the board.  Conditions below allows for this movement and nothing else.

            if target[0] in [0, 1, 2, 9, 8, 7] and target[1] in [3, 4, 5]:
                if position[0] == target[0]:
                    if target[1] == position[1] + 1 or target[1] == position[1] - 1:
                        return True
                    else:
                        return False

                if position[1] == target[1]:
                    if target[0] == position[0] - 1 or target[0] == position[0] + 1:
                        return True
                    else:
                        return False
                else:
                    return False

        if kind == 'advisor':
            # advisors start on either side of the generals and can move/capture one point diagonally.Like generals,
            # advisors cannot leave the palace.  The conditionals below restrict the advisor to the palace and only
            # allows for diagonal movements (up, down, left, or right)

            if target[0] in [0, 1, 2, 9, 8, 7] and target[1] in [3, 4, 5]:
                if position[0] != target[0] and position[1] != target[1]:
                    if target[1] == position[1] + 1 or target[1] == position[1] - 1:
                        if target[0] == position[0] + 1 or target[0] == position[0] - 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

        if kind == 'elephant':
            # can move up, down, left, or right diagonally by two spots exactly but cannot cross the river.
            # If a player of any color exists in the location between the current and target positions, then the
            # elephant is blocked from making its move.

            if color == 'red' and target[0] < 5 or color == 'black' and target[0] > 4:
                # restricts red to its side of the river and black to the other side of the river

                if target[0] == position[0] + 2:
                    if target[1] == position[1] + 2:
                        x = position[0] + 1
                        y = position[1] - 1
                        if self._board.get_piece([x, y]) == [0, 0]:
                            return True
                        else:
                            return False

                    if target[1] == position[1] - 2:
                        x = position[0] + 1
                        y = position[1] - 1
                        if self._board.get_piece([x, y]) == [0, 0]:
                            return True
                        else:
                            return False

                if target[0] == position[0] - 2:
                    if target[1] == position[1] + 2:
                        x = position[0] - 1
                        y = position[1] + 1
                        if self._board.get_piece([x, y]) == [0, 0]:
                            return True
                        else:
                            return False

                    if target[1] == position[1] - 2:
                        x = position[0] + 1
                        y = position[1] - 1
                        if self._board.get_piece([x, y]) == [0, 0]:
                            return True
                        else:
                            return
                else:
                    return False
            else:
                return False

        if kind == 'cannon':
            # canons move like chariots, any distance orthogonally without jumping, but can only capture
            # by jumping a single piece of any color.

            target_space = self._board.get_piece(target)
            if position[1] == target[1] or position[0] == target[0]:
                if position[1] == target[1]:
                    if position[0] - target[0] == 0:
                        return True

                    if (position[0] - target[0]) < 0:
                        y = position[1]
                        count = 0
                        for i in range(position[0]+1, target[0]):
                            if self._board.get_piece([i, y]) != [0, 0]:
                                # counts how many player pieces are in cannons path
                                count += 1

                        if count == 0 and target_space[0] == 0:
                            return True

                        if count == 1 and target_space[0] != 0:  # allows for a single piece jump
                            return True

                        else:
                            return False
                    else:
                        y = position[1]
                        count = 0
                        for i in range(target[0] + 1, position[0]):
                            if self._board.get_piece([i, y]) != [0, 0]:
                                count += 1

                        if count == 0 and target_space[0] == 0:
                            return True

                        if count == 1 and target_space[0] != 0:
                            return True

                        else:
                            return False

                else:
                    if position[0] == target[0]:
                        if position[1] - target[1] == 0:
                            return True

                        if (position[1] - target[1]) < 0:
                            x = position[0]
                            count = 0
                            for i in range(position[1] + 1, target[1]):
                                if self._board.get_piece([x, i]) != [0, 0]:
                                    count += 1
                            if count == 0 and target_space[0] == 0:
                                return True

                            if count == 1 and target_space[0] != 0:
                                return True

                            else:
                                return False

                        else:
                            x = position[0]
                            count = 0
                            for i in range(target[1] + 1, position[1]):
                                if self._board.get_piece([x, i]) != [0, 0]:
                                    count += 1

                            if count == 0 and target_space[0] == 0:
                                return True

                            if count == 1 and target_space[0] != 0:
                                return True

                            else:
                                return False


class Board:
    '''creates a class for our board.  Has methods to get pieces by position and determine if the generals
     can see eachother'''

    def __init__(self, board=[[['red', 'chariot'], ['red', 'horse'], ['red', 'elephant'], ['red', 'advisor'], ['red', 'general'], ['red', 'advisor'], ['red', 'elephant'],['red', 'horse'], ['red', 'chariot']],
                              [[0, 0], [0, 0], [0, 0], [0,0], [0, 0], [0,0], [0, 0], [0, 0], [0, 0]],
                              [[0, 0], ['red', 'cannon'], [0, 0], [0, 0], [0,0], [0,0], [0, 0], ['red', 'cannon'], [0, 0]],
                              [['red', 'soldier'], [0,0], ['red', 'soldier'], [0, 0], ['red', 'soldier'], [0, 0], ['red', 'soldier'], [0,0], [0, 0]],
                              [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                              [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                              [['black', 'soldier'], [0, 0], ['black', 'soldier'], [0, 0], ['black', 'soldier'], [0, 0], ['black', 'soldier'], [0, 0], ['black', 'soldier']],
                              [[0, 0], ['black', 'cannon'], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], ['black', 'cannon'], [0, 0]],
                              [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                              [['black', 'chariot'], ['black', 'horse'], ['black', 'elephant'], ['black', 'advisor'], ['black', 'general'], ['black', 'advisor'], ['black', 'elephant'],['black', 'horse'], ['black', 'chariot']]]):
        '''initializes the board to have the red and black pieces in their starting positions'''

        self._board = board

    def get_board(self):
        '''returns the board and current positions of its pieces'''

        return self._board

    def get_piece(self, location):
        '''returns the [color, type] of a location on the board.  If no piece present, returns [0, 0]'''

        board = self.get_board()
        if board[location[0]][location[1]] == [0, 0]:
            return [0, 0]

        else:
            piece = board[location[0]][location[1]]
            return piece

    def can_generals_see(self, current, target):
        '''determines if a move will result in the generals seeing each other.  takes the current and target positions
        as a parameter and returns True or False accordingly'''

        generals = []
        blockers = []
        board = self.get_board()

        for i in range(len(board)):
            for x in range(8):
                if board[i][x][1] == 'general':
                    generals.append([i, x])

        diff = abs(generals[0][0] - generals[1][0])

        for i in range(0, diff+1):
            if board[i][generals[0][1]] != [0, 0]:
                blockers.append([i,generals[0][1]])

        for i in blockers:  # takes any generals found in blockers out of blockers
            if i in generals:
                blockers.remove(i)

        if len(blockers) > 1:  # if there is more than one player between the generals, returns false
            return False

        if current in blockers and target[1] == current[1] or current not in blockers:
            # allows current to be the only piece in blockers as long as current is moving to a position between
            # the two generals
            return False

    def set_piece(self, current, target):
        '''places the piece at current to the location of target and then makes current [0,0] to complete the move'''

        board = self.get_board()
        new = board[current[0]][current[1]]
        board[current[0]][current[1]] = [0, 0]
        board[target[0]][target[1]] = new


    def print_board(self):
        '''prints the board for testing purposes'''

        for i in self.get_board():
            print(i)


class XiangqiGame:
    '''creates a chinese chess class that controls the game.  Can check for a winner, request moves, and return the
     state of the game.'''

    def __init__(self, current_state='UNFINISHED'):
        '''initializes current state to UNFINISHED and uses composition to reference Piece and Board's methods'''

        self._current_state = current_state
        self._piece = Piece()
        self._board = Board()
        self._turn = 'red'
        self._count = 1
        self._check_moves = []

    def is_stalemate(self, color):
        '''determines if a given player is in stalemate by their color.  Returns True/False accordingly'''

        board = self._board.get_board()
        pieces = []

        for i in range(len(board)):
            for x in range(8):
                piece = board[i][x]
                piece_color = piece[0]
                if piece_color == color:
                    pieces.append([i, x])

        for i in range(len(board)):
            for y in range(8):
                for piece in pieces:
                    if self._piece.is_legal_move(piece, [i, y]) is True:
                        return False
        else:
            return True

    def get_game_state(self):
        '''returns the current game state'''

        return self._current_state

    def set_game_state(self, state):
        '''sets the current game state'''

        self._current_state = state

    def get_check_moves(self):
        '''returns the moves found in is_in_check for use in our make_move method later on'''

        return self._check_moves

    def set_check_moves(self, move):
        '''sets the check moves list'''

        self._check_moves.append(move)
        return self._check_moves

    def is_in_check(self, color):
        '''determines if a player is in check by their color'''

        red = []
        black = []
        generals = []
        check_moves_red = []
        check_moves_black = []
        board = self._board.get_board()

        for i in range(len(board)):  # finds pieces of specified color
            for x in range(8):
                piece = board[i][x]
                piece_color = piece[0]
                if piece_color == 'red':
                    red.append([i, x])
                if piece_color == 'black':
                    black.append([i, x])

        for i in range(len(board)):  #  finds general positions
            for x in range(8):
                if board[i][x][1] == 'general':
                    generals.append([i, x])

        piece = self._piece
        for i in black:
            for x in generals:
                if x != i:
                    general = self._board.get_piece(x)
                    if general[0] == 'red':
                        if piece.is_legal_move(i, x) is True:
                            check_moves_red.append([i, x])  # finds moves that will put red in check

        for i in red:
            for x in generals:
                if x != i:
                    general = self._board.get_piece(x)
                    if general[0] == 'black':
                        if piece.is_legal_move(i, x) is True:
                            check_moves_black.append([i, x])  # finds moves that will put black in check

        if len(check_moves_red) >= 1 and color == 'red':  # adds moves to check moves and returns True if any were found
            for i in check_moves_red:
                self.set_check_moves(i)

            return True

        if len(check_moves_black) >= 1 and color == 'black':  # adds moves to check moves, returns True if move found
            for i in check_moves_black:
                self.set_check_moves(i)

            return True

        else:
            return False

    def set_turn(self, x):
        '''sets whose turn it is after a move is made'''

        self._count += x
        if self._count % 2 != 0:
            self._turn = 'red'

        else:
            self._turn = 'black'

    def get_turn(self):
        '''returns the color of the player whose turn it is'''

        return self._turn

    def make_move(self, current, target):
            '''makes a move on the board if and only if the current location's piece is the correct color, the target
            location is a legal move, the move won't put the current player's general in check or let the generals
             see each other, and the inputs are valid'''

            if self.get_game_state() != 'UNFINISHED':
                return False

            if self.get_game_state() == 'UNFINISHED':

                movedict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8}
                movedict_row = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '0': 9}

                if current[0] not in movedict or current[-1] not in movedict_row:
                    return False

                else:

                    num = 0
                    for i in movedict_row:
                        if i == current[-1]:  # allows for column inputs of 1-10
                            num += int(movedict_row.get(i))

                    for i in movedict:
                        if i == current[0]:
                            current = [num, (movedict.get(i))]

                if target[0] not in movedict or target[-1] not in movedict_row:
                    return False

                else:
                    num = 0
                    for i in movedict_row:
                        if i == target[-1]:  # allows for column inputs of 1-10
                            num += int(movedict_row.get(i))

                    for i in movedict:
                        if i == target[0]:
                            target = [num, (movedict.get(i))]

                if self._board.get_piece(current) == [0, 0]:  # can't move a piece that isn't there
                    return False

                else:
                    piece = self._board.get_piece(current)
                    color = piece[0]
                    target_piece = self._board.get_piece(target)
                    target_color = target_piece[0]

                    if target_color != color and color == self.get_turn():  # target color must not equal current color
                        if self._piece.is_legal_move(current, target) is True and self._board.can_generals_see(current, target) is False:
                            self._board.set_piece(current, target)
                            if self.is_in_check(color) is True:  # undo move/returns false if move puts player in check
                                self._board.set_piece(target, current)
                                return False

                            else:
                                self.set_turn(1)

                                if self.is_stalemate(self.get_turn()) is True:
                                    return False

                                if self.is_in_check(self.get_turn()) is True and len(self.get_check_moves()) > 1:
                                    # if check moves length is greater than one, there's no way for the opponent to win
                                    if color == 'red':
                                        self.set_game_state('RED_WON')
                                        return True

                                    if color == 'black':
                                        self.set_game_state('BLACK_WON')
                                        return True
                                else:
                                    return True
                        else:
                            return False
                    else:
                        return False


if __name__ == "__main__":  # allows for the outside use of the methods/classes in this program
    XiangqiGame()

game = XiangqiGame()