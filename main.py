from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB

    def draw(self, canvas, fill):
        canvas.create_line(
            self.pointA.x,
            self.pointA.y,
            self.pointB.x,
            self.pointB.y,
            fill=fill,
            width=2
        )

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMAZEing")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        canvas = Canvas(self.__root, bg="white", height=height, width=width)
        canvas.pack()
        self.canvas = canvas

        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill):
        line.draw(self.canvas, fill)

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")




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
