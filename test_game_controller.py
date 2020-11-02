from game_controller import GameController
from check_win import Check_Win
from disk import Disk

ZERO = 0
ROW = 6
COLUMN = 7

# matrix setup
matrix = [[ZERO]*ROW for x in range(COLUMN)]
# initiate
gc = GameController("100 x 200")
gc.matrix = matrix


def test_contructor():
    # after initiation test the construtor
    # the window size is filled in correctly
    # length of row and column are 6 and 7 respectively
    # initial value in each grid is 0
    # default variables such as ai_side, winning are False
    # default variable disk_ball is None
    # default countdown value is 20
    assert gc.SPACE == "100 x 200" and \
        len(gc.matrix) == 7 and \
        len(gc.matrix[5]) == 6 and \
        gc.matrix[0][3] == 0 and \
        gc.matrix[5][5] == 0 and \
        gc.matrix[2][2] == 0 and \
        gc.matrix[6][5] == 0 and \
        (gc.ai_side is False) and \
        (gc.winning is False) and \
        (gc.disk_ball is None) and \
        gc.countdown == 20


def test_update():
    # call check function
    cw = Check_Win(matrix)
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    # test horizontal
    cw.matrix[3][5] = dk1
    cw.matrix[4][5] = dk2
    cw.matrix[5][5] = dk3
    cw.matrix[6][5] = dk4
    # check the returned result
    result = cw.check_win()
    assert result == "test"


# place_ball() method has linked with processing draw() function.

# release_ball() method has linked with disk_ball.down(drop_height) method
# which contains the processing draw() function.

# release_AI() methods has linked with disk_ball.down(drop_height) method
# which contains the processing draw() function.


def test_get_column_index():
    # test the calculation method will return targeted column indexes
    assert gc.get_column_index(199) == 1 and \
           gc.get_column_index(265) == 2 and \
           gc.get_column_index(578) == 5 and \
           gc.get_column_index(993) == 9 and \
           gc.get_column_index(678) == 6 and \
           gc.get_column_index(1206) == 12


def test_is_row_full():
    # initiate test
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    dk5 = Disk("test")
    dk6 = Disk("test")
    # initiate variables to the matrix for testing
    gc.matrix[6][0] = dk1
    gc.matrix[6][1] = dk2
    gc.matrix[6][2] = dk3
    gc.matrix[6][3] = dk4
    gc.matrix[6][4] = dk5
    gc.matrix[6][5] = dk6
    gc.matrix[2][0] = dk1
    gc.matrix[2][5] = dk2
    gc.matrix[5][5] = dk5
    print(gc.matrix[6][0])
    # test column 6 is full and will return True
    # test other columns are not full
    assert (gc.is_row_full(6) is True) and \
           (gc.is_row_full(0) is False) and \
           (gc.is_row_full(1) is False) and \
           (gc.is_row_full(2) is False) and \
           (gc.is_row_full(3) is False) and \
           (gc.is_row_full(4) is False) and \
           (gc.is_row_full(5) is False)


def test_matrix_update():
    # initiate test
    gc.disk_ball == "test matrix update"
    dk1 = Disk("test")
    dk2 = Disk("test")
    dk3 = Disk("test")
    dk4 = Disk("test")
    dk5 = Disk("test")
    dk6 = Disk("test")
    # initiate variables to the matrix for testing
    gc.matrix[6][0] = dk1
    gc.matrix[6][1] = dk2
    gc.matrix[6][2] = dk3
    gc.matrix[6][3] = dk4
    gc.matrix[6][4] = dk5
    gc.matrix[2][0] = dk1
    gc.matrix[2][1] = dk2
    gc.matrix[5][0] = dk5
    # test matrix update will return the correct row indexes
    # column 6 will return the row index of 5 with grid value of 0
    # column 2 will return the row index of 2 with grid value of 0
    # column 5 will return the row index of 1 with grid value of 0
    # column 3 will return the row index of 0 with grid value of 0
    assert gc.matrix_update(6) == 5 and \
        gc.matrix_update(2) == 2 and \
        gc.matrix_update(5) == 1 and \
        gc.matrix_update(1) == 0 and \
        gc.matrix_update(3) == 0


def test_update_winners():
    # test default conditions in this method
    # more update winners' test will be in the specifc test to Class winners
    assert (gc.winning is False) and \
        gc.countdown == 20 and \
        gc.update_winners.__name__ == "update_winners"


# all of Processing runs on top of a layer of Java.
# an interactive text input by defining the following input function.
# is from the input function verbatim from the description.
