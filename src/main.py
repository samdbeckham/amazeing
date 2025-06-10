from tkinter import Tk, BOTH, Canvas
from window import Window
from cell import Cell

def main():
    win = Window(800, 600)

    c2 = Cell(win)
    c2.has_right_wall = False
    u2 = Cell(win)
    u2.has_top_wall = False
    r2 = Cell(win)
    r2.has_right_wall = False
    r2.has_bottom_wall = False
    l2 = Cell(win)
    l2.has_right_wall = False
    l2.has_top_wall = False
    c1 = Cell(win)
    c1.has_right_wall = False
    u1 = Cell(win)
    u1.has_top_wall = False
    r1 = Cell(win)
    r1.has_right_wall = False
    r1.has_bottom_wall = False
    l1 = Cell(win)
    l1.has_right_wall = False
    l1.has_top_wall = False

    size = 50
    gap = 20

    c1.draw(
        gap,
        gap,
        gap + size,
        gap + size
    )
    u1.draw(
        (gap * 2) + size,
        gap,
        (gap * 2) + (size * 2),
        gap + size
    )
    r1.draw((
        gap * 3) + (size * 2),
        gap,
        (gap * 3) + (size * 3),
        gap + size
    )
    l1.draw((
        gap * 4) + (size * 3),
        gap,
        (gap * 4) + (size * 4),
        gap + size
    )
    c2.draw(
        gap,
        (size * 2) + gap,
        gap + size,
        (size * 3) + gap
    )
    u2.draw(
        (gap * 2) + size,
        (size * 2) + gap,
        (gap * 2) + (size * 2),
        (size * 3) + gap
    )
    r2.draw((
        gap * 3) + (size * 2),
        (size * 2) + gap,
        (gap * 3) + (size * 3),
        (size * 3) + gap
    )
    l2.draw((
        gap * 4) + (size * 3),
        (size * 2) + gap,
        (gap * 4) + (size * 4),
        (size * 3) + gap
    )

    c1.draw_move(u1)
    u1.draw_move(l2)
    l1.draw_move(c2, undo=True)
    c2.draw_move(l2, undo=True)
    

    win.wait_for_close()

if __name__ == '__main__':
    main()
