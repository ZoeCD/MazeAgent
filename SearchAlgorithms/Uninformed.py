from Helpers import check_state_is_goal, get_neighbours


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


