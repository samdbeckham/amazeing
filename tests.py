import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_maze_many_rows(self):
        num_cols = 1
        num_rows = 99
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._Maze__cells), num_cols)
        self.assertEqual(len(m1._Maze__cells[0]), num_rows)

    def test_break_e_and_e(self):
        m1 = Maze(0, 0, 10, 10, 10, 10)
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[-1][-1].has_bottom_wall)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 2, 2, 10, 10)
        self.assertFalse(m1._Maze__cells[0][0].visited)
        self.assertFalse(m1._Maze__cells[1][0].visited)
        self.assertFalse(m1._Maze__cells[0][1].visited)
        self.assertFalse(m1._Maze__cells[1][1].visited)

if __name__ == "__main__":
    unittest.main()
