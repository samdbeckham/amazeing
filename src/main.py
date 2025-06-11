from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(96, 84, 24, 16, 38, 18, win)

    win.wait_for_close()

if __name__ == '__main__':
    main()
