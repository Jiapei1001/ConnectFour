ZERO = 0
ROW = 6
COLUMN = 7


class Check_Win:
    def __init__(self, matrix):
        '''get current status of the disk matrix'''
        self.matrix = matrix

    def check_win(self):
        '''check if any side wins and return results
        loop through the targeted are in the matrix
        check if there are disks and if their colors match'''

        # check horizontal
        for c in range(COLUMN - 3):
            for r in range(ROW):
                if (self.matrix[c][r] != ZERO and
                    self.matrix[c+1][r] != ZERO and
                    self.matrix[c+2][r] != ZERO and
                    self.matrix[c+3][r] != ZERO) \
                    and \
                   (self.matrix[c][r].color ==
                    self.matrix[c+1][r].color ==
                    self.matrix[c+2][r].color ==
                        self.matrix[c+3][r].color):
                    return self.matrix[c][r].color

        # check vertical
        for c in range(COLUMN):
            for r in range(ROW-3):
                if (self.matrix[c][r] != ZERO and
                    self.matrix[c][r+1] != ZERO and
                    self.matrix[c][r+2] != ZERO and
                    self.matrix[c][r+3] != ZERO) \
                    and \
                   (self.matrix[c][r].color ==
                    self.matrix[c][r+1].color ==
                    self.matrix[c][r+2].color ==
                        self.matrix[c][r+3].color):
                    return self.matrix[c][r].color

        # check increasing diaganol
        for c in range(COLUMN-3):
            for r in range(ROW - 3):
                if (self.matrix[c][r] != ZERO and
                    self.matrix[c+1][r+1] != ZERO and
                    self.matrix[c+2][r+2] != ZERO and
                    self.matrix[c+3][r+3] != ZERO) \
                    and \
                   (self.matrix[c][r].color ==
                    self.matrix[c+1][r+1].color ==
                    self.matrix[c+2][r+2].color ==
                        self.matrix[c+3][r+3].color):
                    return self.matrix[c][r].color

        # check decreasing diaganol
        for c in range(COLUMN-3):
            for r in range(3, ROW):
                if (self.matrix[c][r] != ZERO and
                    self.matrix[c+1][r-1] != ZERO and
                    self.matrix[c+2][r-2] != ZERO and
                    self.matrix[c+3][r-3] != ZERO) \
                    and \
                   (self.matrix[c][r].color ==
                    self.matrix[c+1][r-1].color ==
                    self.matrix[c+2][r-2].color ==
                        self.matrix[c+3][r-3].color):
                    return self.matrix[c][r].color

        # if no win, keep the result as None
        return None
