from pyamaze import maze, COLOR, agent
import argparse
from SearchAlgorithms import breadth_first_search, a_star


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', default=15, dest='size', type=int)
    parser.add_argument('--x', default=15, dest='x', type=int)
    parser.add_argument('--y', default=15, dest='y', type=int)
    parser.add_argument('--algorithm', default='Astar', dest='algorithm', type=str)
    args = parser.parse_args()

    m = maze(args.size, args.size)
    m.CreateMaze(loopPercent=50)
    maze_map = m.maze_map
    if args.size < 15 and args.x == 15 or args.y == 15:
        initial_state = (m.cols, m.cols)
    else:
        initial_state = (args.x, args.y)

    if args.algorithm == 'Astar':
        solution = a_star(maze_map, m.grid, initial_state)
    elif args.algorithm == 'BFS':
        visited = []
        queue = []
        solution = breadth_first_search(maze_map, visited, initial_state, queue)
    else:
        print("Invalid algorithm, please write 'BFS' or 'Astar")
        print("Now running Astar")
        solution = a_star(maze_map, m.grid, initial_state)

    a = agent(m, footprints=True, color=COLOR.red)
    m.tracePath({a: solution},  delay=300)
    m.run()



if __name__ == '__main__':
    main()
