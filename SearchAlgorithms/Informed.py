from math import inf
from queue import PriorityQueue
from Helpers import check_state_is_goal, get_neighbours, euclidian_distance


def _get_path(path, initial_state):
    fwdPath = {}
    cell = (1, 1)
    while cell != initial_state:
        fwdPath[path[cell]] = cell
        cell = path[cell]
    return fwdPath


def a_star(maze_map, grid, initial_state):

    actual_scores = {cell: inf for cell in grid}
    heuristic_scores = {cell: inf for cell in grid}

    actual_scores[initial_state] = 0
    heuristic_scores[initial_state] = euclidian_distance(initial_state)

    open_list = PriorityQueue()
    open_list.put((heuristic_scores[initial_state], heuristic_scores[initial_state], initial_state))

    path = {}

    while not open_list.empty():
        cell = open_list.get()[2]

        if check_state_is_goal(cell):
            return _get_path(path, initial_state)

        neighbours = get_neighbours(maze_map, cell)

        for neighbour in neighbours:
            temp_actual_cost = actual_scores[cell] + 1
            temp_heuristic_cost = temp_actual_cost + euclidian_distance(neighbour)

            if temp_heuristic_cost < heuristic_scores[neighbour]:
                path[neighbour] = cell
                actual_scores[neighbour] = temp_actual_cost
                heuristic_scores[neighbour] = temp_heuristic_cost
                open_list.put((temp_heuristic_cost, euclidian_distance(neighbour), neighbour))



