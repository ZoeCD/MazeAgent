from math import sqrt, inf

def check_state_is_goal(state):
    return state == (1, 1)


def get_neighbours(maze_map, state):
    neighbours = []
    possible_neighbours = maze_map.get(state)

    if possible_neighbours.get('E') == 1:
        neighbours.append((state[0], state[1] + 1))
    if possible_neighbours.get('W') == 1:
        neighbours.append((state[0], state[1] - 1))
    if possible_neighbours.get('N') == 1:
        neighbours.append((state[0] - 1, state[1]))
    if possible_neighbours.get('S') == 1:
        neighbours.append((state[0] + 1, state[1]))

    return neighbours


def euclidian_distance(state):
    return sqrt(pow(state[0] - 1, 2) + pow(state[1] - 1, 2))