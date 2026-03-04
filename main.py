from src.grid import Grid

if __name__ == "__main__":
    grid = Grid()
    
    print("Start:", grid.start)
    print("Goal:", grid.goal)
    print("Neighbors of (0,0):", grid.neighbors((0,0)))
    