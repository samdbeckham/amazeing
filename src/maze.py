import time
import random
from cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        animated=0,
        seed=None
    ):
        if seed is not None: 
            random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.animated = animated
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()
        self.solve()

    def __create_cells(self):
        for i in range(self.num_cols):
            self.__cells.append([])
            for j in range(self.num_rows):
                self.__cells[i].append(Cell(self.win))
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        x = self.x1 + self.cell_size_x * i
        y = self.y1 + self.cell_size_y * j
        self.__cells[i][j].draw(x, y, x + self.cell_size_x, y + self.cell_size_y)
        self.__animate()

    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        if self.animated > 0:
            time.sleep(self.animated)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        current_cell = self.__cells[i][j]
        current_cell.visited = True
        
        while True:
            directions = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                directions.append(("LEFT", i - 1, j))
            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                directions.append(("RIGHT", i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                directions.append(("UP", i, j - 1))
            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                directions.append(("DOWN", i, j + 1))
            if len(directions) == 0:
                self.__draw_cell(i, j)
                return

            (dir, new_i, new_j) = directions[random.randrange(len(directions))]

            match dir:
                case "UP":
                    current_cell.has_top_wall = False
                    self.__cells[new_i][new_j].has_bottom_wall = False
                case "RIGHT":
                    current_cell.has_right_wall = False
                    self.__cells[new_i][new_j].has_left_wall = False
                case "DOWN":
                    current_cell.has_bottom_wall = False
                    self.__cells[new_i][new_j].has_top_wall = False
                case "LEFT":
                    current_cell.has_left_wall = False
                    self.__cells[new_i][new_j].has_right_wall = False
                case _:
                    raise Exception("No direction specified")

            self.__break_walls_r(new_i, new_j)

    def __reset_cells_visited(self):
        for col in self.__cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        current = self.__cells[i][j]
        current.visited = True

        if i >= self.num_cols - 1 and j >= self.num_rows - 1:
            return True

        if j > 0:
            x = i
            y = j - 1
            target = self.__cells[x][y]
            if not target.has_bottom_wall and not target.visited:
                current.draw_move(target)
                if self.__solve_r(x, y):
                    return True
                else:
                    target.draw_move(current, undo=True)

        if i < self.num_cols - 1:
            x = i + 1
            y = j
            target = self.__cells[x][y]
            if not target.has_left_wall and not target.visited:
                current.draw_move(target)
                if self.__solve_r(x, y):
                    return True
                else:
                    target.draw_move(current, undo=True)

        if j < self.num_rows - 1:
            x = i
            y = j + 1
            target = self.__cells[x][y]
            if not target.has_top_wall and not target.visited:
                current.draw_move(target)
                if self.__solve_r(x, y):
                    return True
                else:
                    target.draw_move(current, undo=True)

        if i > 0:
            x = i - 1
            y = j
            target = self.__cells[x][y]
            if not target.has_right_wall and not target.visited:
                current.draw_move(target)
                if self.__solve_r(x, y):
                    return True
                else:
                    target.draw_move(current, undo=True)

        return False

