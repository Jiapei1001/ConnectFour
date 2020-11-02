from game_controller import GameController


# define constants
SPACE = {'w': 700, 'h': 700}
gc = GameController(SPACE)
RATE = 20
SEVEN = 7
EIGHT = 8
ONE_HUDR = 100
TWO_HUDR = 200

# define grid constants
STROKE = (0, 0, 255)
STROKE_WEIGHT = 12

LINE_ONE = (0, 100, 700, 100)
LINE_TWO = (0, 200, 700, 200)
LINE_THREE = (0, 300, 700, 300)
LINE_FOUR = (0, 400, 700, 400)
LINE_FIVE = (0, 500, 700, 500)
LINE_SIX = (0, 600, 700, 600)
LINE_SEVEN = (0, 700, 700, 700)
LINE_V_ONE = (0, 100, 0, 700)
LINE_V_TWO = (100, 100, 100, 700)
LINE_V_THREE = (200, 100, 200, 700)
LINE_V_FOUR = (300, 100, 300, 700)
LINE_V_FIVE = (400, 100, 400, 700)
LINE_V_SIX = (500, 100, 500, 700)
LINE_V_SEVEN = (600, 100, 600, 700)
LINE_V_EIGHT = (700, 100, 700, 700)
line_lst = [
    LINE_ONE, LINE_TWO, LINE_THREE, LINE_FOUR, LINE_FIVE, LINE_SIX, LINE_SEVEN,
    LINE_V_ONE, LINE_V_TWO, LINE_V_THREE, LINE_V_FOUR, LINE_V_FIVE, LINE_V_SIX,
    LINE_V_SEVEN, LINE_V_EIGHT]
'''
x1 = 0
y1 = 100
x2 = 700
y2 = 100

line = (x1, y1, x2, y2)
line_lst = []
line_lst.append(line)
for _ in range(SEVEN):
    print(line)
    y1 += 100
    y2 += 100
    line_lst.append(line)'''


def setup():
    # define window size
    size(SPACE['w'], SPACE['h'])
    # define frame update rate
    frameRate(RATE)


def draw():
    # define background as grey
    background(TWO_HUDR)

    # getting updated info about current disks and if any side wins
    gc.update()

    # show human side disk if mousePressed and mouseY <= 100:
    if mousePressed and mouseY <= ONE_HUDR:
        gc.place_ball(pmouseX, pmouseY)

    # AI's turn and delay the drop
    if gc.ai_side:
        gc.countdown -= 1
    if gc.countdown == 0:
        gc.release_AI()

    # draw grid
    grid()

    # update the winner
    gc.update_winners()


def mouseReleased():
    # if mouse is released in the upper grey area, then release the disk
    if mouseY <= ONE_HUDR:
        gc.release_ball()
    # draw grid
    grid()


def grid():
    # draw the grid
    stroke(*STROKE)
    strokeWeight(STROKE_WEIGHT)
    for l in line_lst:
        line(*l)
