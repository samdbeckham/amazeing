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
        self.__root.title("Some kind of title")
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

def main():
    win = Window(800, 600)
    pointA = Point(50,50)
    pointB = Point(400,50)
    pointC = Point(50,400)
    lineAB = Line(pointA, pointB)
    lineBC = Line(pointC, pointB)
    lineCA = Line(pointA, pointC)
    win.draw_line(lineAB, "black")
    win.draw_line(lineBC, "red")
    win.draw_line(lineCA, "black")
    win.wait_for_close()

if __name__ == '__main__':
    main()
