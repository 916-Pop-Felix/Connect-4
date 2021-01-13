class Circle:
    def __init__(self, x, y, player):
        """

        :param x: x axis on the board-matrix
        :param y: y axis on the board-matrix
        :param player: one of cpu or human, denotes who is the owner of the circle
        """
        self.__x = x
        self.__y = y
        self.player = player

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y


    def __str__(self):
        if self.player == "human":
            return '\033[31m' + "⬤" + '\033[0m'
        elif self.player == "cpu":
            return '\033[33m' + "⬤" + '\033[0m'
        return "○"
