class UI:
    def __init__(self, service):
        self.__service = service

    def print_board(self):
        print(self.__service)

    @staticmethod
    def print_menu_options():
        menu = "Welcome to Connect-4 !\n"
        return menu

    @staticmethod
    def print_first_player():
        player_text = "Do you want to start first?\n"
        player_text += "1.Yes\n" \
                       "0.No"
        return player_text

    @staticmethod
    def lines_columns_values():
        """
        Gets user input for the number of lines and columns
        :return: returns the number of lines and columns of the created board
        """
        while True:
            try:
                lines = int(input("Enter the number of lines of the board (at least 4): "))
                columns = int(input("Enter the number of columns of the board (at least 4): "))
                if lines >= 4 and columns >= 4:  # minimum condition for the game to be functional
                    break
                else:
                    print("Lines and columns must be at least of value 4!\n")
            except ValueError as ve:
                print(ve)
        return lines, columns

    def run_app(self):
        print(self.print_first_player())
        player_option = int(input(">>"))
        if player_option == 1:
            turn = "human"
        else:
            turn = "cpu"
        while True:
            try:
                self.print_board()
                if turn == "human":
                    column = int(input("It's your turn! Choose a column: "))
                    self.__service.move(column, "human")
                    turn = "cpu"
                    if self.__service.check_winner("human"):
                        print("Congratulations! You've won!")
                        self.print_board()
                        break
                else:
                    print("...It's the computer's turn now...")
                    self.__service.cpu_move(1)
                    turn = "human"
                    if self.__service.check_winner("cpu"):
                        print("You lost! Maybe try harder next time :)")
                        self.print_board()
                        break
            except ValueError as ve:
                print(ve)
