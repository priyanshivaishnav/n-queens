from Board import Board


class HillClimb:
    def __init__(self, board):
        self.step = 0
        self.N = 5000
        self.board = board
        self.board.set_queens()
        self.board.fitness()
        self.map = self.board.map

    def solve_board(self):
        ideal_fit = self.board.n_queen * (self.board.n_queen - 1) // 2
        j = 0
        n = 0
        while self.board.fit != ideal_fit:
            if n > self.N:
                j = 0
                n = 0
                self.board.map = [[0 for j in range(self.board.n_queen)] for i in range(self.board.n_queen)]
                self.board.set_queens()
                self.map = self.board.map
            j = 0 if j == 4 else j
            self.fits = [_ for _ in range(self.board.n_queen)]  # list comprehension
            # for x in range(self.board.n_queen):
            #     self.fits[x] = x
            for i in range(self.board.n_queen):
                self.move_queen(j, i)
                self.board.fitness()
                self.fits[i] = self.board.fit
            index = self.fits.index(max(self.fits))
            self.move_queen(j, index)
            self.board.fitness()
            j += 1
            n += 1

    def move_queen(self, row, col):
        for x in range(self.board.n_queen):
            if self.board.map[row][x] == 1:
                self.board.map[row][x] = 0
        self.board.map[row][col] = 1


if __name__ == "__main__":
    home = Board(5)
    s = HillClimb(home)
    s.board.show()
    s.solve_board()
    s.board.show()
