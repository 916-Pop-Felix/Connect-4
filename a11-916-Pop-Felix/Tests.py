import unittest
from Circle import Circle
from Board import Board
from Service import BoardService


class TestConnect4(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCircle(self):
        a = Circle(1, 1, "human")
        self.assertEqual(a.x, 1)
        self.assertEqual(a.y, 1)
        self.assertEqual(str(a), '\033[31m' + "⬤" + '\033[0m')
        b = Circle(2, 1, "cpu")
        self.assertEqual(str(b), '\033[33m' + "⬤" + '\033[0m')
        c = Circle(3, 3, "stuff")
        self.assertEqual(str(c), "○")

    def testBoard(self):
        b = Board(4, 4)
        self.assertEqual(b.lines, 4)
        self.assertEqual(b.columns, 4)
        for i in range(4):
            b.board[i][0].player = "human"
        self.assertEqual(b.check_column(0), False)
        self.assertEqual(b.check_column(-12), False)
        self.assertEqual(b.check_column(1), True)
        b.board[3][2].player = "cpu"
        self.assertEqual(b.column_height(2), 2)
        self.assertRaises(ValueError, b.move, 0, "player")
        self.assertRaises(ValueError, b.move, 10, "player")
        b.move(1, "human")
        self.assertEqual(b.board[3][1].player, "human")
        self.assertTrue(b.check_winner("human"))
        self.assertFalse(b.check_winner("cpu"))
        self.assertFalse(b.board_is_full())
        b.clear()
        for i in range(4):
            b.board[3][i].player = "human"
        self.assertTrue(b.check_winner("human"))
        for i in range(4):
            b.board[i][i].player = "cpu"
        self.assertTrue(b.check_winner("cpu"))
        b.clear()
        for i in range(4):
            for j in range(4):
                b.board[i][j].player = "human"
        self.assertTrue(b.board_is_full())
        print(b)

    def testService(self):
        b = Board(6, 4)
        service = BoardService(b)
        self.assertFalse(service.board_is_full())
        self.assertFalse(service.check_winner("cpu"))
        self.assertEqual(service.player_opponent("cpu"), "human")
        self.assertEqual(service.player_opponent("human"), "cpu")
        for i in range(3):
            service.move(1, "human")
        potential_picks = service.potential_picks()
        self.assertEqual(len(potential_picks), 4)
        self.assertEqual(potential_picks[0], 0)  # denotes a neutral pick
        self.assertEqual(potential_picks[1], -1)  # denotes a bad pick, from which the opponent will win
        final_move=service.cpu_move(1)
        self.assertTrue(final_move==1 or final_move==2 or final_move==3)  # due to random
        service.move(1,"cpu")

        for i in range(1,4):
            service.move(2,"cpu")
        potential_picks = service.potential_picks()
        self.assertEqual(potential_picks[1],1)  # denotes the winning pick, opponent will lose

        print(service)