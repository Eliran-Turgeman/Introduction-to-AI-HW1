from MazeProblem import MazeProblem, create_problem
from Robot import BreadthFirstSearchRobot as BFS, UniformCostSearchRobot
from Animation import Animation
import sys
SHOW_ANIMATION = False

EXPECTED_RESULTS = {'bfs': [(36, 57), (51, 362), (216, 1212), (88, 2430), (123, 1209), (376, 5299)],
                    'ucs': [(36, 51), (47, 312), (216, 1212), (84, 2447), (123, 1205), (376, 5299)]}

test_index = sys.argv[1]
maze_name = 'maze_' + test_index
maze_problem = create_problem(maze_name)

bfs = BFS()
ucs = UniformCostSearchRobot()
bfs_solution = bfs.solve(maze_problem)
ucs_solution = ucs.solve(maze_problem)

search_algorithms = [bfs, ucs]
solutions = [bfs_solution, ucs_solution]

for solution, key in zip(solutions, EXPECTED_RESULTS.keys()):
    assert EXPECTED_RESULTS[key][int(test_index)][0] == solution.cost, f"cost equals {solution.cost} in test {test_index} of {key}"
    assert EXPECTED_RESULTS[key][int(test_index)][1] == solution.n_node_expanded, f"node expanded equals {solution.n_node_expanded} in test {test_index} of {key}"


if SHOW_ANIMATION:
    try:
        for search_algo, solution in zip(search_algorithms, solutions):
            animation = Animation(solution, maze_problem, search_algo, maze_name, blit=False)
            animation.show()
    except:
        print('No solution!')
