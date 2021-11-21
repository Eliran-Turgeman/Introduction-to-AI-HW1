from MazeProblem import MazeProblem, create_problem
from Robot import BreadthFirstSearchRobot as BFS
from Animation import Animation
import sys
import pdb

maze_name = 'maze_' + str(sys.argv[1])
maze_problem = create_problem(maze_name)
bfs = BFS()
solution = bfs.solve(maze_problem)
try:
    animation = Animation(solution, maze_problem, bfs, maze_name, blit=False)
    animation.show()
except:
    print('No solution!')
# pdb.set_trace()