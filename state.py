

class State:
    def __init__(self):
        self.scale = 10
        self.cur_pos = [0, 0]
        self.grid = 1
        
    def get_grid(self):
        return self.grid

    def get_scale(self):
        return self.scale

    def get_cursor_position(self):
        return self.cur_pos

    def increase_scale(self):
        if (int(self.scale/2) > 0):
            self.scale = self.scale / 2

    def decrease_scale(self):
        self.scale = self.scale * 2

state = State()
