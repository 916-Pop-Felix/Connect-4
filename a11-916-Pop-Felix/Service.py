from copy import deepcopy

smol_value = -100
from random import choice


class BoardService:
    def __init__(self, board):
        self.__board = board

    def move(self, column, player):
        self.__board.move(column - 1, player)

    def check_winner(self, player):
        return self.__board.check_winner(player)

    def board_is_full(self):
        return self.__board.board_is_full()

    def check_column(self, column):
        return self.__board.check_column(column)

    @staticmethod
    def player_opponent(player):
        if player == "cpu":
            return "human"
        elif player == "human":
            return "cpu"

    def is_terminal(self):
        return self.__board.check_winner("human") or self.__board.check_winner("cpu") or self.__board.board_is_full()

    def get_valid_locations(self):
        valid_locations = []
        for col in range(self.__board.columns):
            if self.check_column(col):
                valid_locations.append(col)
        return valid_locations

    def potential_picks(self):
        """
        This function provides us a list of potential column picks from which the ai will have to choose
        The function will check if the cpu can win from a move, and then it will simulate all the counterattack
        possibilities for the human player, in order to make sure the human will not win from a simple move
        1 - denotes a winning move for the ai
        0 - denotes neither a winning nor losing move
        -1 - denotes a move from which the human player will win
        -2 - denotes invalid move
        :return: the list containing the above values for each particular column
        """
        potential_picks = [0] * self.__board.columns
        opponent = self.player_opponent("cpu")
        for i in range(self.__board.columns):
            copy_board = deepcopy(self.__board)
            if not copy_board.check_column(i):
                continue
            copy_board.move(i, "cpu")
            if copy_board.check_winner("cpu"):
                potential_picks[i] = 1
                break
            else:
                if copy_board.board_is_full():
                    break
                else:
                    for j in range(self.__board.columns):
                        copy_board_opponent = deepcopy(copy_board)
                        if not copy_board_opponent.check_column(j):
                            continue
                        copy_board_opponent.move(j, opponent)
                        if copy_board_opponent.check_winner(opponent):
                            potential_picks[i] = -1
                            break
        return potential_picks



    def cpu_move(self, difficulty):
        """
        This function goes through the potential_picks list created by calling the function above and
        finds the maximum value
        If there are multiple maximum values (stored in the list best_moves) a random column will be selected
        and returned

        :return: the column in which the cpu will make its move
        """
        potential_picks = self.potential_picks()
        valid_picks = self.get_valid_locations()
        best_moves = []
        best_pick = smol_value

        if difficulty == 0:
            self.move(choice(valid_picks), "cpu")
            return choice(valid_picks)
        elif difficulty == 1:
            for i in range(len(potential_picks)):
                best_pick = max(potential_picks[i], best_pick)

            for i in range(len(potential_picks)):
                if potential_picks[i] == best_pick and self.__board.check_column(i):
                    best_moves.append(i)

            final_move = choice(best_moves) + 1
            self.move(final_move, "cpu")
            return final_move

    def board(self):
        return self.__board

    def __str__(self):
        return str(self.__board)
