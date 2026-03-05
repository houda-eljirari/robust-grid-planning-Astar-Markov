import random
import numpy as np


class MarkovSimulator:
    def __init__(self, grid, policy, epsilon=0.1):
        self.grid = grid
        self.policy = policy
        self.epsilon = epsilon

    def step(self, state):
        neighbors = self.grid.neighbors(state)

        if not neighbors:
            return state

        # Mouvement prévu par la politique
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