from MazeProblem import MazeProblem, create_problem
from Robot import BreadthFirstSearchRobot as BFS, UniformCostSearchRobot
from Animation import Animation
import sys
import pdb

maze_name = 'maze_' + str(sys.argv[1])
maze_problem = create_problem(maze_name)

bfs = BFS()
ucs = UniformCostSearchRobot()
bfs_solution = bfs.solve(maze_problem)
ucs_solution = ucs.solve(maze_problem)

search_algorithms = [bfs, ucs]
solutions = [bfs_solution, ucs_solution]

try:
    for search_algo, solution in zip(search_algorithms, solutions):
        animation = Animation(solution, maze_problem, search_algo, maze_name, blit=False)
        animation.show()
except:
    print('No solution!')
# pdb.set_trace()