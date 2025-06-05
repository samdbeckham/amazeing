from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        root = Tk()
        root.title = "Some kind of title"
        self.__root = root

        canvas = Canvas()
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
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


def main():
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == '__main__':
    main()
