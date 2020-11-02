from disk import Disk
from check_win import Check_Win
from winners import Winners
import random


# define constants
ZERO = 0
ONE = 1
TWO = 2
FOUR = 4
SEVEN = 7
TEN = 10
COUNTDOWN = 20
ROW = 6
COLUMN = 7
HALF_HUDR = 50
ONE_HUDR = 100
MAX_DROP_HEIGHT = 650


# define text constant
TEXT_FILL = 255
TEXT_SIZE = 50


class GameController:

    def __init__(self, SPACE):
        self.SPACE = SPACE
        self.matrix = [[ZERO]*ROW for x in range(COLUMN)]
        self.disk_ball = None
        self.total_disk = ZERO
        self.ai_side = False
        self.winning = False
        self.countdown = COUNTDOWN

    def update(self):
        '''display disks in the current matrix and check winning status'''
        # display the disks in the list matrix
        for column in self.matrix:
            for disk in column:
                if disk != ZERO:
                    disk.draw_me(disk.x, disk.y)

        # check tie if the matrix is full of disks
        if self.total_disk == COLUMN * ROW:
            fill(TEXT_FILL)
            textSize(TEXT_SIZE)
            text("TIE!",
                 self.SPACE['w']/TWO - ONE_HUDR, self.SPACE['h']/TEN)
            # end loop
            noLoop()

        # check result's status
        result = Check_Win(self.matrix).check_win()
        # if human side win:
        if result == "R":
            fill(TEXT_FILL)
            textSize(TEXT_SIZE)
            text("YOU WIN!",
                 self.SPACE['w']/TWO - ONE_HUDR, self.SPACE['h']/TEN)
            # trigger to update winner's score.txt
            self.winning = True

        # if machine side win:
        if result == "Y":
            fill(TEXT_FILL)
            textSize(TEXT_SIZE)
            text("MACHINE WIN! YOU LOSE!",
                 self.SPACE['w']/FOUR - (ONE_HUDR + HALF_HUDR),
                 self.SPACE['h']/TEN)
            # end loop
            noLoop()

    def place_ball(self, mouseX, mouseY):
        '''get x and y coordinates of the mouse
        and show the disk in the upper grey area'''
        # get the column index of where the pressed mouse points to
        col = self.get_column_index(mouseX)
        # check if that column if full
        if not self.is_row_full(col):
            # create human side disk object
            self.disk_ball = Disk("R")
            # get the column index by passing mouse X location
            # calculate where to draw the disk
            # draw the disk
            col_tem = self.get_column_index(mouseX)
            draw_x = col_tem * ONE_HUDR + HALF_HUDR
            draw_y = HALF_HUDR
            self.disk_ball.draw_me(draw_x, draw_y)

    def release_ball(self):
        '''calculate x and y coordinates and drop the disk'''
        drop_height_index = None
        # get the column index
        col = self.get_column_index(self.disk_ball.x)
        # check if the column is full
        if not self.is_row_full(col):
            # get the row index of the targeted place for dropped disk
            drop_height_index = self.matrix_update(col)
            # calculate the targeted dropped height
            drop_height = MAX_DROP_HEIGHT - drop_height_index * ONE_HUDR
            # drop the disk
            self.disk_ball.down(drop_height)
            # total disks in the matrix add 1
            self.total_disk += 1
            # trigger AI's side
            print("It's AI's turn:")
            self.ai_side = True

    def release_AI(self):
        '''release disk in the AI side'''
        # create AI side disk object
        self.disk_ball = Disk("Y")
        # randomly generate the column for dropping AI side disk
        # check if the column can drop AI side disk
        can_drop = True
        while can_drop:
            # column minus one as it's a closed range
            col = random.randint(0, (COLUMN - ONE))
            if not self.is_row_full(col):
                drop_height_index = self.matrix_update(col)
                # total disks in the matrix add 1
                self.total_disk += 1
                # end the while when can drop
                can_drop = False
            else:
                continue
        # pass x and y coordinates for AI side disk
        draw_x = col * ONE_HUDR + HALF_HUDR
        draw_y = HALF_HUDR
        self.disk_ball.draw_me(draw_x, draw_y)
        # calculate the targeted dropped height
        drop_height = MAX_DROP_HEIGHT - drop_height_index * ONE_HUDR
        # drop the disk
        self.disk_ball.down(drop_height)
        # trigger human side
        print("It's your turn:")
        self.countdown = COUNTDOWN
        self.ai_side = False

    def get_column_index(self, mouse_x):
        '''get x coordinate of mouse and return the column index'''
        col_index = int(mouse_x // ONE_HUDR)
        return col_index

    def is_row_full(self, col):
        '''check if the specifc column is full'''
        row_count = 0
        for row in range(len(self.matrix[col])):
            if self.matrix[col][row] != ZERO:
                row_count += 1
        # if row count == 7 or not
        if row_count == ROW:
            return True
        else:
            return False

    def matrix_update(self, col):
        '''check if there is blank space in the specific column,
        add disk object to the matrix, return the row index'''
        for row in range(len(self.matrix[col])):
            if self.matrix[col][row] == ZERO:
                self.matrix[col][row] = self.disk_ball
                break
        return row

    def update_winners(self):
        '''if human wins, get user's name, and update the score.txt'''
        # delay for showing the complete winning texts
        if self.winning:
            self.countdown -= 1
        if self.countdown == 0:
            while self.winning:
                # get user's name
                answer = self.input("Please enter your name: ")
                if answer:
                    print('Hi ' + answer.title() + "! You Win!")
                    self.winning = False  # end while loop
                    win = Winners()  # call class
                    filename = "score.txt"  # input filename
                    win.winners_update(answer.title(), filename)  # update dic
                    win.winners_rewrite(filename)  # rewrite file
                elif answer == '':
                    print('Please enter your name for records: ')
                else:
                    print(answer)  # Canceled dialog will print None
                    self.winning = False
                # end loop
                noLoop()

    def input(self, message=''):
        '''for user to input his/her name'''
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
