import matplotlib.pyplot as plt
from src.grid import Grid

if __name__ == "__main__":
    grid = Grid()
    
    # Créer la figure
    fig, ax = plt.subplots(figsize=(6,6))
    
    # Dessiner la grille
    for x in range(grid.width):
        for y in range(grid.height):
            rect = plt.Rectangle((x, y), 1, 1, fill=False, edgecolor='gray')
            ax.add_patch(rect)
    
    # Dessiner obstacles
    for obs in grid.obstacles:
        rect = plt.Rectangle(obs, 1, 1, color='black')
        ax.add_patch(rect)
    
    # Dessiner start
    ax.add_patch(plt.Rectangle(grid.start, 1, 1, color='green'))
    ax.text(grid.start[0]+0.5, grid.start[1]+0.5, 'Start', ha='center', va='center', color='white', fontsize=8)
    
    # Dessiner goal
    ax.add_patch(plt.Rectangle(grid.goal, 1, 1, color='red'))
    ax.text(grid.goal[0]+0.5, grid.goal[1]+0.5, 'Goal', ha='center', va='center', color='white', fontsize=8)
    
    ax.set_xlim(0, grid.width)
    ax.set_ylim(0, grid.height)
    ax.set_aspect('equal')
    ax.invert_yaxis()  # pour correspondre à la disposition matricielle
    plt.title("Grille 10x10 avec Start, Goal et Obstacles")
    plt.savefig("figures/grid_initial.png")
    plt.show()