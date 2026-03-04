import os
import matplotlib.pyplot as plt
from src.grid import Grid
from src.astar import best_first_search


def run_experiment():
    grid = Grid()
    algorithms = ["ucs", "greedy", "astar"]

    results = {}

    for algo in algorithms:
        result = best_first_search(grid, mode=algo)
        results[algo] = result

    return results


def plot_results(results):
    os.makedirs("figures", exist_ok=True)

    algos = list(results.keys())
    costs = [results[a]["cost"] for a in algos]
    nodes = [results[a]["nodes_expanded"] for a in algos]
    times = [results[a]["time"] for a in algos]

    # --- Plot 1 : Nodes Expanded ---
    plt.figure()
    plt.bar(algos, nodes)
    plt.title("Nodes Expanded Comparison (10x10 Grid)")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes Expanded")
    plt.savefig("figures/nodes_comparison.png")
    plt.close()

    # --- Plot 2 : Execution Time ---
    plt.figure()
    plt.bar(algos, times)
    plt.title("Execution Time Comparison (10x10 Grid)")
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.savefig("figures/time_comparison.png")
    plt.close()


def print_table(results):
    print("\n===== EXPERIMENT RESULTS =====")
    print(f"{'Algorithm':<10} {'Cost':<5} {'Nodes':<10} {'Time (s)':<10}")
    print("-" * 40)

    for algo, res in results.items():
        print(f"{algo:<10} {res['cost']:<5} {res['nodes_expanded']:<10} {res['time']:<10.6f}")


if __name__ == "__main__":
    results = run_experiment()
    print_table(results)
    plot_results(results)