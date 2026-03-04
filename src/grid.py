class Grid:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        
        self.start = (0, 0)
        self.goal = (9, 9)

        # Obstacles fixes (exemple intéressant)
        self.obstacles = {
            (1, 2), (2, 2), (3, 2),
            (5, 5), (5, 6), (5, 7),
            (7, 3), (8, 3), (9, 3)
        }

    def in_bounds(self, state):
        x, y = state
        return 0 <= x < self.width and 0 <= y < self.height

    def is_free(self, state):
        return state not in self.obstacles

    def neighbors(self, state):
        x, y = state
        
        candidates = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]
        
        valid = []
        for s in candidates:
            if self.in_bounds(s) and self.is_free(s):
                valid.append(s)
        
        return valid