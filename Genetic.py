import Board
import random


class Genetic:
    def __init__(self, n):
        self.step = 0
        self.boards = [Board.Board(n) for _ in range(8)]
        max_fit = self.boards[0].n_queen * (self.boards[0].n_queen - 1) // 2
        fits = [0]
        self.steps = 0
        for board in self.boards:
            board.set_queens()
            board.fitness()
            board.encoding()
        while max(fits) != max_fit:
            self.selection()
            for x in range(8):
                self.mutation(self.boards[x])
            self.update_boards()
            fits = []
            for board in self.boards:
                board.fitness()
                fits.append(board.fit)
            self.steps += 1
        ind = fits.index(max(fits))
        print("Number of steps: " + str(self.steps))
        self.boards[ind].show()

    def update_boards(self):
        for board in self.boards:
            for row in range(len(board.encode)):
                board.map[row] = [0 for _ in range(len(board.map[row]))]
                board.map[row][int(board.encode[row])] = 1

    def selection(self):
        # fitSum=0
        total = 0
        for board in self.boards:
            total += board.fit
        for board in self.boards:
            board.perc = board.fit / total
        pairs = []
        for i in range(8):
            r = random.random()
            if r < self.boards[0].perc:
                pairs.append(self.boards[0])
            elif r > self.boards[0].perc and r < self.boards[0].perc + self.boards[1].perc:
                pairs.append(self.boards[1])
            elif r > self.boards[0].perc + self.boards[1].perc and r < self.boards[0].perc + self.boards[1].perc + self.boards[2].perc:
                pairs.append(self.boards[2])
            elif r > self.boards[0].perc + self.boards[1].perc + self.boards[2].perc and r < self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc:
                pairs.append(self.boards[3])
            elif r > self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc and r < self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc + self.boards[4].perc:
                pairs.append(self.boards[4])
            elif r > self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc + self.boards[4].perc and r < self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc + self.boards[4].perc + self.boards[5].perc:
                pairs.append(self.boards[5])
            elif r > self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc + self.boards[4].perc + self.boards[5].perc and r < self.boards[0].perc + self.boards[1].perc + self.boards[2].perc + self.boards[3].perc + self.boards[4].perc + self.boards[5].perc + self.boards[6].perc:
                pairs.append(self.boards[6])
            else:
                pairs.append(self.boards[7])
        self.crossover(pairs[0], pairs[1])
        self.crossover(pairs[2], pairs[3])
        self.crossover(pairs[4], pairs[5])
        self.crossover(pairs[6], pairs[7])

    def crossover(self, A, B):
        cpoint = random.randint(0, A.n_queen - 1)
        right = A.encode[cpoint:]
        A.encode = A.encode[0:cpoint] + B.encode[cpoint:]
        B.encode = B.encode[:cpoint] + right

    def mutation(self, board):
        index = random.randint(0, board.n_queen-1)
        board.encode = board.encode[:index] + str(random.randint(0, board.n_queen-1)) + board.encode[index + 1:]


if __name__ == '__main__':
    g = Genetic(5)

    # home = Board.Board(5)
    # s = HillClimb.Hill_Climb(home)
    # s.board.show()
    # s.solve_board()
    # s.board.show()
    # g = Genetic(4)
    # st = "324231"