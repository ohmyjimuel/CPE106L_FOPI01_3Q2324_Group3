import unittest
from unittest.mock import patch, mock_open
import tkinter as tk
import oxo_logic
import oxo_data

class TestFilePicker(unittest.TestCase):
    @patch('tkinter.filedialog.askopenfilename')
    def test_file_picker(self, mock_askopenfilename):
        mock_askopenfilename.return_value = '/path/to/file.txt'
        root = tk.Tk()
        root.withdraw()
        file_path = tk.filedialog.askopenfilename()
        self.assertEqual(file_path, '/path/to/file.txt')

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = oxo_logic.Game()

    def test_new_game(self):
        self.assertEqual(len(self.game._game), 9)
        self.assertEqual(self.game._game.count(' '), 9)

    @patch('oxo_data.saveGame')
    def test_save_game(self, mock_saveGame):
        self.game._game = ['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.game.saveGame()
        mock_saveGame.assert_called_with(['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '])

    @patch('oxo_data.restoreGame', side_effect=[['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '], ['X', 'O'], IOError()])
    def test_restore_game(self, mock_restoreGame):
        self.game.restoreGame()
        self.assertEqual(self.game._game, ['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' '])

        mock_restoreGame.side_effect = ['X', 'O']
        self.game.restoreGame()
        self.assertEqual(self.game._game, list(" " * 9))

        mock_restoreGame.side_effect = IOError()
        self.game.restoreGame()
        self.assertEqual(self.game._game, list(" " * 9))

    def test_generate_move(self):
        self.game._game = ['X', ' ', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        available_moves = [1, 3, 4, 5, 6, 7, 8]
        self.assertIn(self.game._generateMove(), available_moves)

        self.game._game = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        self.assertEqual(self.game._generateMove(), -1)

    @patch('oxo_logic.Game._generateMove')
    def test_computer_move(self, mock_generateMove):
        mock_generateMove.return_value = 0
        self.game._game = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(self.game.computerMove(), '')
        self.assertEqual(self.game._game[0], 'O')

        mock_generateMove.return_value = -1
        self.assertEqual(self.game.computerMove(), '')  # Return empty string if no move is possible

        self.game._game = ['O', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        mock_generateMove.return_value = 2
        self.assertEqual(self.game.computerMove(), 'O')

    def userMove(self, cell):
        if self.game._game[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.game._game[cell] = 'X'
        if self.game._isWinningMove():
            return 'X'
        else:
            return ''  # Return empty string upon a successful move
        
    def test_is_winning_move(self):
        # Test for a winning row for X
        self.game._game = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game._isWinningMove())

        # Test for a winning column for O
        self.game._game = [' ', ' ', 'O', ' ', 'O', ' ', ' ', 'O', ' ']
        self.assertTrue(self.game._isWinningMove())

        # Test for a winning diagonal for X
        self.game._game = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game._isWinningMove())

        # Test for no winning move
        self.game._game = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', ' ']
        self.assertFalse(self.game._isWinningMove())


if __name__ == '__main__':
    unittest.main()