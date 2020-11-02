import pytest
from disk import Disk
from check_win import Check_Win


ZERO = 0
ROW = 6
COLUMN = 7

# matrix setup for running test
matrix = [[ZERO]*ROW for x in range(COLUMN)]


def test_constructor():
    ''' test constructor'''
    cw = Check_Win(matrix)
    assert cw.matrix[5][5] == 0 and \
        cw.matrix[1][2] == 0 and \
        len(cw.matrix) == 7 and \
        len(cw.matrix[5]) == 6 and \
        len(cw.matrix[6]) == 6


def test_check_win_horizontal():
    # initiate disk objects
    cw = Check_Win(matrix)
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")

    # test horizontal by placing the disks
    cw.matrix[3][5] = dk1
    cw.matrix[4][5] = dk2
    cw.matrix[5][5] = dk3
    cw.matrix[6][5] = dk4

    # get result
    re = cw.check_win()
    assert len(cw.matrix) == 7 and \
        len(cw.matrix[5]) == 6 and \
        len(cw.matrix[6]) == 6 and \
        cw.matrix[3][5] != 0 and \
        matrix[4][5] != 0 and \
        matrix[5][5] != 0 and \
        matrix[6][5] != 0 and \
        matrix[3][5].color == "test" and \
        matrix[4][5].color == "test" and \
        matrix[5][5].color == "test" and \
        matrix[6][5].color == "test" and \
        re == "test"


# matrix setup
matrix = [[ZERO]*ROW for x in range(COLUMN)]


def test_check_win_vertical():
    # initiate disk objects
    cw = Check_Win(matrix)
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    # test vertical by placing the disks
    cw.matrix[6][2] = dk1
    cw.matrix[6][3] = dk2
    cw.matrix[6][4] = dk3
    cw.matrix[6][5] = dk4
    # get result
    re = cw.check_win()
    assert len(cw.matrix) == 7 and \
        len(cw.matrix[5]) == 6 and \
        len(cw.matrix[6]) == 6 and \
        cw.matrix[6][2] != 0 and \
        matrix[6][3] != 0 and \
        matrix[6][4] != 0 and \
        matrix[6][5] != 0 and \
        matrix[6][2].color == "test" and \
        matrix[6][3].color == "test" and \
        matrix[6][4].color == "test" and \
        matrix[6][5].color == "test" and \
        re == "test"


# matrix setup
matrix = [[ZERO]*ROW for x in range(COLUMN)]


def test_check_win_increasing_diaganol():
    # initiate the disk objects
    cw = Check_Win(matrix)
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    # test increasing diaganol by placing the disks
    cw.matrix[2][2] = dk1
    cw.matrix[5][5] = dk2
    cw.matrix[4][4] = dk3
    cw.matrix[3][3] = dk4
    # get result
    re = cw.check_win()
    assert len(cw.matrix) == 7 and \
        len(cw.matrix[5]) == 6 and \
        len(cw.matrix[6]) == 6 and \
        cw.matrix[2][2] != 0 and \
        matrix[5][5] != 0 and \
        matrix[4][4] != 0 and \
        matrix[3][3] != 0 and \
        matrix[2][2].color == "test" and \
        matrix[5][5].color == "test" and \
        matrix[4][4].color == "test" and \
        matrix[3][3].color == "test" and \
        re == "test"


# matrix setup
matrix = [[ZERO]*ROW for x in range(COLUMN)]


def test_check_win_decreasing_diaganol():
    # initiate disk objects
    cw = Check_Win(matrix)
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    # test decreasing diagonal by placing the disks
    cw.matrix[0][5] = dk1
    cw.matrix[1][4] = dk2
    cw.matrix[2][3] = dk3
    cw.matrix[3][2] = dk4
    # get result
    re = cw.check_win()
    assert len(cw.matrix) == 7 and \
        len(cw.matrix[5]) == 6 and \
        len(cw.matrix[6]) == 6 and \
        cw.matrix[0][5] != 0 and \
        matrix[1][4] != 0 and \
        matrix[2][3] != 0 and \
        matrix[3][2] != 0 and \
        matrix[0][5].color == "test" and \
        matrix[1][4].color == "test" and \
        matrix[2][3].color == "test" and \
        matrix[3][2].color == "test" and \
        re == "test"
