from Circle import Circle


class Board:
    def __init__(self, lines, columns):
        """
        :param lines: number of lines
        :param columns: number of columns
        """
        self.__lines = lines
        self.__columns = columns
        self.board = self.create_board()

    def create_board(self):
        """
        :return: the game board in the form of a matrix containing Circle objects
        """
        board = []
        for i in range(self.__lines):
            board.append([])
            for j in range(self.__columns):
                board[i].append(Circle(i, j, " "))
        return board

    def board_is_full(self):
        for i in range(self.__lines):
            for j in range(self.__columns):
                if self.board[i][j].player == ' ':
                    return False
        return True

    def check_column(self, column):
        if column < 0 or column >= self.__columns or self.board[0][column].player != ' ':
            return False
        return True

    def column_height(self, column):
        """
        Used for move to determine at which line the circle will be dropped
        :param column:
        :return: the first line of a column that has an empty circle
        """
        for i in range(self.__lines):
            if self.board[self.__lines - i - 1][column].player == ' ':
                return self.__lines - i - 1

    def move(self, column, player):
        if self.check_column(column):
            self.board[self.column_height(column)][column].player = player
        else:
            raise ValueError("Invalid or full column!")



    def check_winner(self, player):
        for i in range(self.__lines):  # line check
            for j in range(self.__columns - 3):
                if self.board[i][j
                ].player == self.board[i][j + 1].player == self.board[i][j + 2
                ].player == self.board[i][j + 3].player == player:
                    return True

        for j in range(self.__columns):  # column check
            for i in range(self.__lines - 3):
                if self.board[i][j].player == self.board[i + 1][j].player == self.board[
                    i + 2][j].player == self.board[i + 3][j].player == player:
                    return True

        for i in range(self.__lines - 3):  # first diagonal
            for j in range(self.__columns - 3):
                if self.board[i][j].player == self.board[i + 1][j + 1].player == self.board[i + 2][j + 2
                ].player == self.board[i + 3][j + 3].player == player:
                    return True

        for i in range(self.__lines - 3):  # second diagonal
            for j in range(3, self.__columns):
                if self.board[i][j].player == self.board[i + 1][j - 1].player == self.board[i + 2][j - 2
                ].player == self.board[i + 3][j - 3].player == player:
                    return True

        return False

    @property
    def lines(self):
        return self.__lines

    @property
    def columns(self):
        return self.__columns

    def clear(self):
        self.board=self.create_board()

    def __str__(self):
        board = ''
        for i in range(self.__lines):
            for j in range(self.__columns):
                board += "--"
                if j%2:
                    board+="-"
            board += "\n"
            for j in range(self.__columns):
                board += "|"
                board += str(self.board[i][j])
                if j == self.__columns - 1:
                    board += "|"
            board += "\n"
        return board
