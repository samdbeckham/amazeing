from line import Line
from point import Point

def get_midpoint(a, b):
    if (a > b):
        (a, b) = (b, a)
    return ((b - a) / 2) + a

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = -1
        self.x2 = -1
        self.y1 = -1
        self.y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        color_foregreound = "black"
        color_background = "white"

        top_color = color_foregreound if self.has_top_wall else color_background
        left_color = color_foregreound if self.has_left_wall else color_background
        bottom_color = color_foregreound if self.has_bottom_wall else color_background
        right_color = color_foregreound if self.has_right_wall else color_background

        if self.__win is None:
            return

        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), top_color)
        self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), left_color)
        self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), bottom_color)
        self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), right_color)

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        fill = "gray" if undo else "red"
        x1 = get_midpoint(self.x1, self.x2)
        x2 = get_midpoint(to_cell.x1, to_cell.x2)
        y1 = get_midpoint(self.y1, self.y2)
        y2 = get_midpoint(to_cell.y1, to_cell.y2)

        self.__win.draw_line(Line(Point(x1, y1), Point(x2, y2)), fill)
