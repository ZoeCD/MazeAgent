from pyamaze import maze, COLOR, agent
import argparse
from SearchAlgorithms import breadth_first_search


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', default=5, dest='size', type=int)
    parser.add_argument('--initialState', default=(5, 5), dest='initialState', type=int)
    args = parser.parse_args()

    m = maze(args.size, args.size)
    m.CreateMaze(loopPercent=50)
    maze_map = m.maze_map
    visited = []
    queue = []
    solution = breadth_first_search(maze_map, visited, args.initialState, queue)
    a = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: solution},  delay=700)
    m.run()


if __name__ == '__main__':
    main()
