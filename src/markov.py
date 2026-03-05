import random
import numpy as np


class MarkovSimulator:

    def __init__(self, grid, policy, epsilon=0.1):

        self.grid = grid
        self.policy = policy
        self.epsilon = epsilon

        # Construction de l'ensemble des états
        self.states = self.build_states()

        # Index des états
        self.index = {s: i for i, s in enumerate(self.states)}

        # Construction de la matrice de transition
        self.P = self.build_transition_matrix()

    # ============================
    # Construction des états
    # ============================

    def build_states(self):

        states = []

        for x in range(self.grid.width):
            for y in range(self.grid.height):

                s = (x, y)

                if self.grid.is_free(s):
                    states.append(s)

        return states

    # ============================
    # Construction matrice P
    # ============================

    def build_transition_matrix(self):

        n = len(self.states)

        P = np.zeros((n, n))

        for s in self.states:

            i = self.index[s]

            neighbors = self.grid.neighbors(s)

            if not neighbors:
                P[i, i] = 1
                continue

            intended = self.policy.get(s, s)

            for nb in neighbors:

                j = self.index[nb]

                if nb == intended:
                    P[i, j] += 1 - self.epsilon
                else:
                    P[i, j] += self.epsilon / len(neighbors)

        return P

    # ============================
    # Simulation Monte Carlo
    # ============================

    def step(self, state):

        neighbors = self.grid.neighbors(state)

        if not neighbors:
            return state

        intended = self.policy.get(state, state)

        if random.random() < 1 - self.epsilon:
            return intended
        else:
            return random.choice(neighbors)

    def simulate(self, N=1000, max_steps=200):

        successes = 0
        times = []

        for _ in range(N):

            state = self.grid.start
            t = 0

            while state != self.grid.goal and t < max_steps:

                state = self.step(state)
                t += 1

            if state == self.grid.goal:
                successes += 1
                times.append(t)

        prob = successes / N
        mean_time = np.mean(times) if times else float("inf")

        return prob, mean_time

    # ============================
    # Evolution π(n) = π(0) P^n
    # ============================

    def markov_evolution(self, steps=20):

        n = len(self.states)

        pi = np.zeros(n)

        start_index = self.index[self.grid.start]

        pi[start_index] = 1

        goal_index = self.index[self.grid.goal]

        probabilities = []

        for _ in range(steps):

            pi = pi @ self.P

            probabilities.append(pi[goal_index])

        return probabilities