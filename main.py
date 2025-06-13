from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(48, 48, 12, 16, 44, 42, win, animated=0.01)

    win.wait_for_close()

if __name__ == '__main__':
    main()
