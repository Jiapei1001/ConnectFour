from disk import Disk
ZERO = 0
TEN = 10
ONE_HURD = 100
x = 100
y = 200


def test_constructor():
    # Test minimal required constructor args
    test_color = "R"
    dk = Disk(test_color)
    assert dk.x == ZERO and \
        dk.y == ZERO and \
        dk.y_vel == TEN and \
        dk.radius == ONE_HURD and \
        dk.color == "R" and \
        dk.__class__.__name__ == "Disk"

# draw_me(x, y), and draw_red(x, y), and draw_yellow(x, y), and down(height)
# concerned only with graphics
