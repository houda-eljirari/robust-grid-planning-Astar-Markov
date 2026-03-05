from src.grid import Grid
from src.astar import best_first_search
from src.markov import MarkovSimulator
import matplotlib.pyplot as plt


if __name__ == "__main__":

    # =========================
    # PHASE A*
    # =========================

    grid = Grid()

    result = best_first_search(grid, mode="astar")
    path = result["path"]

    print("\n===== RESULTATS A* =====")
    print("Coût :", result["cost"])
    print("Chemin A* :", path)

    # Construction de la politique
    policy = {}

    for i in range(len(path) - 1):
        policy[path[i]] = path[i + 1]

    # =========================
    # PHASE MARKOV
    # =========================

    print("\n===== ANALYSE MARKOV =====")

    epsilons = [0.0, 0.1, 0.2, 0.3]

    probs = []
    times = []

    for eps in epsilons:

        simulator = MarkovSimulator(grid, policy, epsilon=eps)

        prob, mean_time = simulator.simulate(N=1000)

        probs.append(prob)
        times.append(mean_time)

        print(f"\nEpsilon = {eps}")
        print("Probabilité d'atteindre le goal :", prob)
        print("Temps moyen :", mean_time)

    # ========================
    # Figure 1 : Probabilité
    # ========================

    plt.figure()

    plt.plot(epsilons, probs)

    plt.xlabel("Epsilon (incertitude)")
    plt.ylabel("Probabilité d'atteindre le goal")

    plt.title("Robustesse de la politique A*")

    plt.savefig("figures/markov_probability.png")

    plt.close()

    # ========================
    # Figure 2 : Temps moyen
    # ========================

    plt.figure()

    plt.plot(epsilons, times)

    plt.xlabel("Epsilon (incertitude)")
    plt.ylabel("Temps moyen pour atteindre le goal")

    plt.title("Impact de l'incertitude sur le temps")

    plt.savefig("figures/markov_time.png")

    plt.close()

    # ========================
    # Evolution Markov
    # ========================

    simulator = MarkovSimulator(grid, policy, epsilon=0.1)

    probabilities = simulator.markov_evolution(steps=20)

    print("\nEvolution de la probabilité d'être dans GOAL :")

    print(probabilities)

    print("\nFigures Markov générées dans le dossier figures/")