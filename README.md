# Exam First Term - Informed and Uninformed Search

Melgar F, Caballero Z, Villalpando R, Vargas J, Palmerín D.

*Instituto Tecnológico y de Estudios Superiores de Monterrey*


## Abstract. 
Problem-solving agents are goal-based agents which allow going from an initial state to a goal. In this project, 
we compare how the algorithms Breadth First Search and A* solve random mazes.

## Prerequisites
We use Pyamaze package to create random mazes. You can install it with the following command on the terminal:

`>> pip install pyamaze`

## Arguments
You can specify the function arguments in the “Parameters” field. The available options are “--size”, “--x”, “--y”, and 
“--algorithm”. Size will allow you to change the size of the maze. You can change the coordinates of the initial state 
with x and y. Finally, you can choose between Breadth First Search (BFS) or A* (Astar) algorithms.

You can specify the parameters with any of the following flags followed by an integer or text for the algorithm.

```
--size INTEGER
--x INTEGER_LESS_OR_EQUAL_TO_SIZE
--y INTEGER_LESS_OR_EQUAL_TO_SIZE
--algorithm BFS_OR_Astar
```
The default parameters are `[size = 15, x = 15, y = 15, algorithm = Astar]`

### Example
`python main.py --size 10 --algorithm BFS --x 5 --y 5`

or

`python main.py --size 13 --algorithm Astar`



 
