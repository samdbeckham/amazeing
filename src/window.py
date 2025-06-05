from tkinter import Tk, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("aMAZEing")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack()

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
        line.draw(self.__canvas, fill)
