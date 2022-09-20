from typing import List, Dict


def check_state_is_goal(state):
    return state == (1,1)


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


def breadth_first_search(maze_map, visited, cell, queue):
    queue.append(cell)
    visited.append(cell)
    path = []
    while queue:
        state = queue.pop(0)
        path.append(state)
        if check_state_is_goal(state):
            return path
        neighbours = get_neighbours(maze_map, state)
        for n in neighbours:
            if n not in visited:
                visited.append(n)
                queue.append(n)


