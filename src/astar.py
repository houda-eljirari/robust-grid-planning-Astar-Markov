import heapq
import time
from src.heuristics import manhattan


def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def best_first_search(grid, mode="astar"):
    start = grid.start
    goal = grid.goal

    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    closed_set = set()
    nodes_expanded = 0

    start_time = time.time()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current in closed_set:
            continue

        closed_set.add(current)
        nodes_expanded += 1

        if current == goal:
            end_time = time.time()
            path = reconstruct_path(came_from, current)
            return {
                "path": path,
                "cost": g_score[current],
                "nodes_expanded": nodes_expanded,
                "time": end_time - start_time
            }

        for neighbor in grid.neighbors(current):
            tentative_g = g_score[current] + 1

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                came_from[neighbor] = current

                if mode == "ucs":
                    f = tentative_g
                elif mode == "greedy":
                    f = manhattan(neighbor, goal)
                else:  # astar
                    f = tentative_g + manhattan(neighbor, goal)

                heapq.heappush(open_list, (f, neighbor))

    return None