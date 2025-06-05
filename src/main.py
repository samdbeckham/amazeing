from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_right_wall = False

    u = Cell(win)
    u.has_top_wall = False

    r = Cell(win)
    r.has_right_wall = False
    r.has_bottom_wall = False

    l = Cell(win)
    l.has_right_wall = False
    l.has_top_wall = False

    size = 50
    gap = 20

    c.draw(gap, gap, gap + size, gap + size)
    u.draw((gap * 2) + size, gap, (gap * 2) + (size * 2), gap + size)
    r.draw((gap * 3) + (size * 2), gap, (gap * 3) + (size * 3), gap + size)
    l.draw((gap * 4) + (size * 3), gap, (gap * 4) + (size * 4), gap + size)


    win.wait_for_close()

if __name__ == '__main__':
    main()
