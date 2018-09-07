import unittest
import demo

class GameTest(unittest.TestCase):
    def test_winner_in_row(self):
        board = [
            ['.', 'O', '.'],
            ['X', 'X', 'X'],
            ['O', '.', '.']
        ]
        self.assertEqual('X', demo.get_winner(board))

    def test_valid_move(self):
        board = [
            ['.', 'O', '.'],
            ['X', 'X', 'X'],
            ['O', '.', '.']
        ]
        self.assertEqual(True, demo.is_valid(board, (0, 0)))

    def test_invalid_move(self):
        board = [
            ['.', 'O', '.'],
            ['X', 'X', 'X'],
            ['O', '.', '.']
        ]
        self.assertEqual(False, demo.is_valid(board, (0, 1)))

    def test_move_outside_board(self):
        board = [
            ['.', 'O', '.'],
            ['X', 'X', 'X'],
            ['O', '.', '.']
        ]
        self.assertEqual(False, demo.is_valid(board, (5, 5)))


    def test_winner_in_col(self):
        board = [
            ['O', 'O', '.'],
            ['O', 'X', 'X'],
            ['O', 'X', '.']
        ]
        self.assertEqual('O', demo.get_winner(board))

    def test_game_over(self):
        board = [
            ['O', 'O', 'O'],
            ['O', 'X', 'X'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(True, demo.game_over(board))

    def test_game_not_over(self):
        board = [
            ['.', 'O', 'O'],
            ['.', '.', '.'],
            ['O', 'X', 'X']
        ]
        self.assertEqual(False, demo.game_over(board))


if __name__ == '__main__':
    unittest.main()
