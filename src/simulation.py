import numpy as np


def markov_evolution(markov, steps=50):

    P = markov.P
    start = markov.index[markov.grid.start]

    pi = np.zeros(len(markov.states))
    pi[start] = 1

    probabilities = []

    for n in range(steps):

        pi = pi @ P
        goal_index = markov.index[markov.grid.goal]

        probabilities.append(pi[goal_index])

    return probabilities