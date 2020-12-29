class MatrixTraversal():
    def __init__(self, grid, look_ahead, wrap_around=False):
        self.grid = grid
        self.look_ahead = look_ahead
        self.wrap_around = wrap_around

    def cannot_go_up(self, index, look_ahead=None, grid=None):
        return index[0] < look_ahead-1

    def cannot_go_down(self, grid, index, look_ahead):
        return index[0] + look_ahead > grid.shape[0]

    def cannot_go_left(self, grid, index, look_ahead):
        return index[1] < look_ahead-1

    def cannot_go_right(self, grid, index, look_ahead):
        return index[1] + look_ahead > grid.shape[1]

    def up(self, index, look_ahead=None, grid=None, wrap_around=False):
        print("GG")


obj = MatrixTraversal("Gg", 4, True)
obj.up("gg", 4, 4)
