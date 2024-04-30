import os
import random
import oxo_data

class Game:
    def __init__(self):
        self._game = self._newGame()

    def _newGame(self):
        ' return new empty game'
        return list(" " * 9)

    def saveGame(self):
        ' save game to disk '
        oxo_data.saveGame(self._game)

    def restoreGame(self):
        ''' restore previously saved game.
        If game not restored successfully return new game'''
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                self._game = game
            else:
                self._game = self._newGame()
        except IOError:
            self._game = self._newGame()

    def _generateMove(self):
        ''' generate a random cell from those available.
        If all cells are used return -1'''
        options = [i for i in range(len(self._game)) if self._game[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _isWinningMove(self):
        wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                (0, 4, 8), (2, 4, 6))             # Diagonals

        for a, b, c in wins:
            chars = self._game[a] + self._game[b] + self._game[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False



    def userMove(self, cell):
        if self._game[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self._game[cell] = 'X'
        if self._isWinningMove():
            return 'X'
        else:
            return ""

    
    def computerMove(self):
        cell = self._generateMove()
        if cell == -1:
            return ''  # Return empty string if no move is possible
        else:
            self._game[cell] = 'O'
            if self._isWinningMove():
                return 'O'
            else:
                return 'O'




    def test(self):
        result = ""
        self._game = self._newGame()
        while not result:
            print(self._game)
            try:
                result = self.userMove(self._generateMove())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computerMove()

            if not result:
                continue
            elif result == 'D':
                print("Its a draw")
            else:
                print("Winner is:", result)
            print(self._game)


if __name__ == "__main__":
    game = Game()
    game.test()
