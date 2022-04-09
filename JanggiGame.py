# Name: Victoria Zavala
# Date: 02/27/2021
# Description: This program creates a game of Janggi, or Korean chess. The program contains various classes for the
# the game as well as for keeping track of all of the pieces on the board.


class JanggiGame:
    """This class is responsible for operating and managing the game board. It initializes the current state of the
        game, initializes the game board, tracks the player moves, and checks to see if the red or blue player is
        currently in check"""

    def __init__(self):
        """Initializes game pieces, starting positions for each piece, game state, check status, column and row
        values"""

        self._game_state = "UNFINISHED"
        self._pturn = "Blue"

        self._blue_gen = General("Blue", "G", [1, 5])
        self._blue_g1 = Guard("Blue", "G1", [0, 4])
        self._blue_g2 = Guard("Blue", "G2", [0, 6])
        self._blue_s1 = Soldier("Blue", "S1", [3, 1])
        self._blue_s2 = Soldier("Blue", "S2", [3, 3])
        self._blue_s3 = Soldier("Blue", "S3", [3, 5])
        self._blue_s4 = Soldier("Blue", "S4", [3, 7])
        self._blue_s5 = Soldier("Blue", "S5", [3, 9])
        self._blue_h1 = Horse("Blue", "H1", [0, 2])
        self._blue_h2 = Horse("Blue", "H2", [0, 8])
        self._blue_e1 = Elephant("Blue", "E1", [0, 3])
        self._blue_e2 = Elephant("Blue", "E2", [0, 7])
        self._blue_ch1 = Chariot("Blue", "CH1", [0, 1])
        self._blue_ch2 = Chariot("Blue", "CH2", [0, 9])
        self._blue_cn1 = Cannon("Blue", "CN1", [2, 2])
        self._blue_cn2 = Cannon("Blue", "CN2", [2, 8])

        self._red_gen = General("Red", "G", [8, 5])
        self._red_g1 = Guard("Red", "G1", [9, 4])
        self._red_g2 = Guard("Red", "G2", [9, 6])
        self._red_s1 = Soldier("Red", "S1", [6, 1])
        self._red_s2 = Soldier("Red", "S2", [6, 3])
        self._red_s3 = Soldier("Red", "S3", [6, 5])
        self._red_s4 = Soldier("Red", "S4", [6, 7])
        self._red_s5 = Soldier("Red", "S5", [6, 9])
        self._red_h1 = Horse("Red", "H1", [9, 2])
        self._red_h2 = Horse("Red", "H2", [9, 8])
        self._red_e1 = Elephant("Red", "E1", [9, 3])
        self._red_e2 = Elephant("Red", "E2", [9, 7])
        self._red_ch1 = Chariot("Red", "CH1", [9, 1])
        self._red_ch2 = Chariot("Red", "CH2", [9, 9])
        self._red_cn1 = Cannon("Red", "CN1", [7, 2])
        self._red_cn2 = Cannon("Red", "CN2", [7, 8])

        self._blue_in_check = False
        self._red_in_check = False

        self._jboard = [[self._red_ch1, self._red_h1, self._red_e1, self._red_g1, "", self._red_g2, self._red_e2,
                         self._red_h2, self._red_ch2, ],
                        ["", "", "", "", self._red_gen, "", "", "", ""],
                        ["", self._red_cn1, "", "", "", "", "", self._red_cn2, "", ],
                        [self._red_s1, "", self._red_s2, "", self._red_s3, "", self._red_s4, "", self._red_s5],
                        ["", "", "", "", "", "", "", "", ""],
                        ["", "", "", "", "", "", "", "", ""],
                        [self._blue_s1, "", self._blue_s2, "", self._blue_s3, "", self._blue_s4, "", self._blue_s5],
                        ["", self._blue_cn1, "", "", "", "", "", self._blue_cn2, "", ],
                        ["", "", "", "", self._blue_gen, "", "", "", ""],
                        [self._blue_ch1, self._blue_h1, self._blue_e1, self._blue_g1, "", self._blue_g2, self._blue_e2,
                         self._blue_h2, self._blue_ch2, ]
                        ]

    def get_game_state(self):
        """Returns the current state of the game either UNFINISHED, BLUE WON or RED WON"""
        return self._game_state

    def update_jboard(self, row, col, update):
        self._jboard[col][row] = update

    def get_pturn(self):
        """Returns whose turn it is, either red or blue"""
        return self._pturn

    def get_jboard(self, col, row):
        """Returns the game board"""
        return self._jboard[col][row]

    def change_turn(self):
        """Alternates turns between players"""
        if self._pturn == "Blue":
            self._pturn = "Red"
        else:
            self._pturn = "Blue"

    def is_in_check(self, team):
        """Takes as a parameter the blue or red player and returns True if that player is in check and returns False
        otherwise"""

        if team != "Red":
            return self._blue_in_check
        elif team != "Blue":
            return self._red_in_check
        else:
            return False

    def winner(self):
        if self._pturn != "Blue":
            self._game_state = "RED_WON"
        elif self._pturn != "Red":
            self._game_state = "BLUE_WON"

    def make_move(self, move_from, move_to):
        """takes two parameters - strings that represent the square to move from and the square to move to.  If the
        square being moved from does not contain a piece belonging to the player whose turn it is, or if the indicated
        move is not legal, or if the game has already been won, then it should just return False.  Otherwise it should
        make the indicated move, remove any captured piece, update the game state if necessary, update whose turn it is,
         and return True."""

        col_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        row_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # Get Row Coordinate of start
        if len(move_from) == 2:
            s_row = int(move_from[1]) - 1
        elif len(move_from) == 3:
            if move_from[1] == '1' and move_from[2] == '0':
                s_row = 9
            else:
                return False

        # Get Column Coordinate of start
        if move_from[0] in col_list:
            s_col = col_list.index(move_from[0])
        else:
            return False

        # Get Row Coordinate of End
        if len(move_to) == 2:
            e_row = int(move_to[1]) - 1
        elif len(move_to) == 3:
            if move_to[1] == '1' and move_to[2] == '0':
                e_row = 9
            else:
                return False

        # Get Column Coordinate of End
        if move_to[0] in col_list:
            e_col = col_list.index(move_to[0])
        else:
            return False

        # call the board and get the piece that is currently on the occupied space
        curr_space = self.get_jboard(s_row, s_col)
        # if the current space is empty, it is an invalid move
        if curr_space == "":
            return False

        # call the current color of the piece occupying the space
        curr_space_team = curr_space.get_team()

        # call the current player's turn either red or blue
        curr_turn = self.get_pturn()

        if move_to[0] in col_list:
            c_start = col_list.index(move_to[0])

        if len(move_to) == 2:
                r_start = int(move_to[1]) - 1
        elif len(move_to) == 3:
            if move_to[1] == "1" and move_to[2] == "0":
                r_start = 9
            return True
        else:
            return False

        if self.get_game_state() != "UNFINISHED":
            return False

        if curr_space_team != curr_turn:
            return False

        if move_from[0] in col_list:
            c_end  = col_list.index(move_from[0])

        if len(move_from) == 2:
                r_end = int(move_from[1]) - 1
        elif len(move_from) == 3:
            if move_from[1] == "1" and move_from[2] == "0":
                r_end = 9
            return True
        else:
            return False

        future_space = self.get_jboard(s_row, s_col)

        if future_space != " ":
            future_space_team = future_space.get_team()
            if future_space_team == curr_space_team:
                return False
            else:
                return True

        # Cannot have the same current and future space
        if future_space == curr_space:
            return False

        if curr_space.check_moves(self, jboard, s_row, s_col, e_row, e_col) is True:
            if future_space == " ":

                self.update_jboard(e_row, e_col, curr_space)

                self.update_jboard(s_row, s_col, " ")

class GamePieces:
    """This is a Parent class for all game pieces on the board, respective of type and color"""

    def __init__(self, team, type, space):
        """Initializes private data members for class GamePieces"""
        self._l_moves = []
        self._team = team
        self._type = type
        self._space = space

    def get_team(self):
        """Returns color of a piece"""
        return self._team

    def get_type(self):
        """Returns type of a piece"""
        return self._type

    def get_space(self):
        """Returns current square a piece is occupying"""
        return self._space


class General(GamePieces):
    """Child class General that inherits from Parent Class GamePieces. Only stays in the palace. Can move orthogonally
    or diagonally one step per turn to any of the nine squares within the palace"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure the general can move orthogonally or diagonally one step per turn to any of the nine
        squares of the palace"""

        if self.get_team() == "Blue":
            if (e_row == 0 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 1 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 2 and (e_col == 4 or e_col == 5 or e_col == 6)):

                if ((s_row == e_row) and abs(s_col - e_col) == 1) \
                        or (abs(s_row - e_row) == 1 and (s_col == e_col)):
                    return True

                else:
                    return False

        if self.get_team() == "Red":
            if (e_row == 9 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 8 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 7 and (e_col == 4 or e_col == 5 or e_col == 6)):

                if ((s_row == e_row) and abs(s_col - e_col) == 1) \
                        or (abs(s_row - e_row) == 1 and (s_col == e_col)):
                    return True

                else:
                    return False


class Guard(GamePieces):
    """Child class Guard that inherits from Parent Class GamePieces. Confined to the palace and can move and capture 1
    point orthogonally or 1 point diagonally"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure that guard can make valid moves either orthogonally or diagonally"""

        if self.get_team() == "Blue":
            if (e_row == 0 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 1 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 2 and (e_col == 4 or e_col == 5 or e_col == 6)):

                if ((s_row == e_row) and abs(s_col - e_col) == 1) \
                        or (abs(s_row - e_row) == 1 and (s_col == e_col)):
                    return True

                else:
                    return False

        if self.get_team() == "Red":
            if (e_row == 9 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 8 and (e_col == 4 or e_col == 5 or e_col == 6)) \
                    or (e_row == 7 and (e_col == 4 or e_col == 5 or e_col == 6)):

                if ((s_row == e_row) and abs(s_col - e_col) == 1) \
                        or (abs(s_row - e_row) == 1 and (s_col == e_col)):
                    return True

                else:
                    return False


class Soldier(GamePieces):
    """Child class Soldier that inherits from Parent class GamePieces. Can move and capture 1 space horizontally or 1
    space vertically. Within the enemy palace, soldiers can move diagonally one space at a time"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure that soldiers can make valid moves either orthogonally or diagonally"""

        r_alter = e_row - s_row
        c_alter = e_col - s_col

        # check vertical and horizontal move outside of palace for blue soldier
        if self.get_team() == "Blue":
            if r_alter == 1 and c_alter == 0 \
                    or r_alter == 0 and abs(c_alter) == 1:
                return True
        else:
            return False

        # if at the end of the board, check that soldier can only move horizontally for blue soldier
        if self.get_team() == "Blue":
            if s_row > 8 and abs(c_alter) == 1:
                return True
        else:
            return False

        # if within palace, check that soldier can move diagonally 1 space at a time for blue soldier

        # check vertical and horizontal move outside of palace for red soldier
        if self.get_team() == "Red":
            if r_alter == -1 and c_alter == 0 \
                    or r_alter == 0 and abs(c_alter) == 1:
                return True
            else:
                return False

        # if at the end of the board, check that soldier can only move horizontally for red soldier
        if self.get_team() == "Red":
            if s_row < 1 and abs(c_alter) == 1:
                return True
        else:
            return False

        # if within palace, check that soldier can move diagonally 1 space at a time for blue soldier


class Elephant(GamePieces):
    """Child class Elephant that inherits from Parent Class GamePieces. Elephants may move 1 space orthogonally followed
    by two points diagonally. The elephant can be blocked by an intervening piece"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure that elephants can make valid moves orthogonally and diagonally. Also checks if elephants
        are currently being blocked by another piece"""

        r_alter = e_row - s_row
        c_alter = e_col - s_col

        # check up/right diag move

        if abs(r_alter) == 3 and abs(c_alter) == 2:
            if jboard[s_row - 1][s_col] or jboard[s_row + 1][s_col] != "":
                return False
            else:
                return True

        if abs(r_alter) == 1 and abs(c_alter) == 2:
            if jboard[s_row][s_col - 1] or jboard[s_row][s_col + 1] != "":
                return False
            else:
                return True

        # check for diag block


        # check up/left diag  move

        # check  left/up diag move

        # check left/ down diag move

        # check down/left diag move

        # check down/right diag move

        # check  right/up diag move

        # check right/ down diag move


class Horse(GamePieces):
    """Child class Horse that inherits from Parent Class GamePieces. Horses may move 1 space orthogonally followed
    by 1 point diagonally. The horse can be blocked by an intervening piece"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure that elephants can make valid moves orthogonally and diagonally. Also checks if elephants
        are currently being blocked by another piece"""

        r_alter = e_row - s_row
        c_alter = e_col - s_col

        if self.get_team() == "Blue":
            # checks for moves up/right and checks for blocks
            if r_alter == 2 and c_alter == 1:
                if jboard[s_row + 1][s_col] != "":
                    return False
                else:
                    return True

            # checks for moves up/left and checks for blocks
            if r_alter == 2 and c_alter == -1:
                if jboard[s_row + 1][s_col] != "":
                    return False
                else:
                    return True

            # checks for moves down/right and checks for blocks
            if r_alter == -2 and c_alter == 1:
                if jboard[s_row - 1][s_col] != "":
                    return False
                else:
                    return True

            # checks for moves down/left, and checks for blocks
            if r_alter == -2 and c_alter == -1:
                if jboard[s_row - 1][s_col] != "":
                    return False
                else:
                    return True

            # checks for left/up, and checks for blocks
            if r_alter == 1 and c_alter == -2:
                if jboard[s_row][s_col - 1] != "":
                    return False
                else:
                    return True

            # checks for left/down, and checks for blocks
            if r_alter == -1 and c_alter == -2:
                if jboard[s_row][s_col - 1] != "":
                    return False
                else:
                    return True

            # checks for right/up, and checks for blocks
            if r_alter == 1 and c_alter == 2:
                if jboard[s_row][s_col + 1] != "":
                    return False
                else:
                    return True

            # checks for right/down, and checks for blocks
            if r_alter == -1 and c_alter == 2:
                if jboard[s_row][s_col + 1] != "":
                    return False
                else:
                    return True

class Cannon(GamePieces):
    """Child class that inherits from Parent class Gamepieces. Can move unlimited distance in a straight line"""

    def check_moves(self, jboard, s_row, s_col, e_row, e_col):
        """Checks to make sure that elephants can make valid moves orthogonally and diagonally. Also checks if elephants
        are currently being blocked by another piece"""

        blocker = 0
        # counts the pieces that are blocking the chariot
        if e_row == s_row and e_col > s_col: # checks for vertical + position
            for x in range(e_col + 1, s_col):
                if jboard[s_row][x] != "":
                    blocker = blocker + 1

        elif s_row == e_row and s_col > e_col: # checks for vertical - position
            for x in range(e_col + 1, s_col):
                if jboard[s_row][x] != "":
                    blocker = blocker + 1

        elif s_col == e_col and s_row < e_row: # checks for horizontal + position
            for x in range(s_row + 1, e_row):
                if jboard[x][s_col] != "":
                    blocker = blocker + 1


        elif s_col == e_col and s_row > e_row: # checks for horizontal - position
            for x in range(e_row + 1, s_row):
                if jboard[x][s_col] != "":
                    blocker = blocker + 1

        if e_row > 2 and e_col > 4 or e_col > 6: # if in palace, checks for diagonal moves
            if blocker == 0:
                for x in range(e_row - 1, s_row - 1) or (e_row - 1, s_row - 1):
                    if jboard[x][s_col] == "":
                        return True


        if jboard[e_row][e_col] == "":
            if blocker == 0:
                return True
            else:
                return False

        if jboard[e_row][e_col] != "":
            if blocker == 1:
                return True
            else:
                return False


class Chariot(GamePieces):
    """Child class that inherits from Parent class GamePieces"""




