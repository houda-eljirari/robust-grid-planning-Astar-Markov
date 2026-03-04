from src.grid import Grid
from src.astar import best_first_search

if __name__ == "__main__":
    grid = Grid()

    result = best_first_search(grid, mode="astar")

    path = result["path"]

    print("\n===== RESULTATS A* =====")
    print("Coût :", result["cost"])
    print("Chemin A* :", path)
    # Construction de la politique à partir du chemin A*
    policy = {}

    for i in range(len(path) - 1):
        policy[path[i]] = path[i + 1]

    print("\nPolitique extraite :")
    for k, v in policy.items():
        print(k, "→", v)