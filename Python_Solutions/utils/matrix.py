import numpy as np


class MatrixTraversal():
    def __init__(self, grid, look_ahead, wrap_around=False):
        self.grid = grid
        self.look_ahead = look_ahead
        self.wrap_around = wrap_around

    def cannot_go_up(self, index, look_ahead):
        return index[0] < look_ahead-1

    def cannot_go_down(self, index, look_ahead):
        return index[0] + look_ahead > self.grid.shape[0]

    def cannot_go_left(self, index, look_ahead):
        return index[1] < look_ahead-1

    def cannot_go_right(self, index, look_ahead):
        return index[1] + look_ahead > self.grid.shape[1]

    def up(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            # if look ahead is greater, limit it
            if self.cannot_go_up(index, look_ahead):
                look_ahead = index[0]+1

            # +1 is to include the current index
            up = grid[index[0]+1-look_ahead: index[0]+1, index[1]]
            return up.astype(np.float)

        else:
            pass

    def down(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            down = grid[index[0]: index[0]+look_ahead, index[1]]
            return down.astype(np.float)

        else:
            pass

    def right(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            right = grid[index[0], index[1]:index[1]+look_ahead]
            return right.astype(np.float)

        else:
            pass

    def left(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            if self.cannot_go_left(index, look_ahead):
                look_ahead = index[1]+1
            left = grid[index[0], index[1]+1-look_ahead:index[1]+1]
            return left.astype(np.float)

        else:
            pass

    def diagonal_right_down(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            # Check if it can go right and down else change the look ahead
            if self.cannot_go_right(index, look_ahead) or self.cannot_go_down(index, look_ahead):
                look_ahead = min(
                    grid.shape[0]-index[0], grid.shape[1]-index[1])

            diagonal = np.zeros(look_ahead)
            for i in range(look_ahead):
                diagonal[i] = grid[index[0]+i, index[1]+i]
            return diagonal

        else:
            pass

    def diagonal_right_up(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            if self.cannot_go_right(index, look_ahead) or self.cannot_go_up(index, look_ahead):
                look_ahead = min(index[0]+1, grid.shape[1]-index[1])
            diagonal = np.zeros(look_ahead)

            for i in range(look_ahead):
                diagonal[i] = grid[index[0]-i, index[1]+i]
            return diagonal

        else:
            pass

    def diagonal_left_down(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        index = list(index)
        if not wrap_around:
            if self.cannot_go_left(index, look_ahead) or self.cannot_go_down(index, look_ahead):
                look_ahead = min(grid.shape[0]-index[0], index[1]+1)
            diagonal = np.zeros(look_ahead)

            for i in range(look_ahead):
                diagonal[i] = grid[index[0]+i, index[1]-i]
            return diagonal

        else:
            pass

    def diagonal_left_up(self, index, grid=None, look_ahead=None, wrap_around=None):
        if grid is None:
            grid = self.grid
        if look_ahead is None:
            look_ahead = self.look_ahead
        if wrap_around is None:
            wrap_around = self.wrap_around

        # worst case
        index = list(index)
        if not wrap_around:
            if self.cannot_go_left(index, look_ahead):
                look_ahead = index[1]+1
            elif self.cannot_go_up(index, look_ahead):
                look_ahead = index[0]+1
            elif self.cannot_go_left(index, look_ahead) and self.cannot_go_up(index, look_ahead):
                look_ahead = min(index[0]+1, index[1]+1)

            diagonal = np.zeros(look_ahead)

            for i in range(look_ahead):
                diagonal[i] = grid[index[0]-i, index[1]-i]
            return diagonal

        else:
            pass


if __name__ == "__main__":
    pass
