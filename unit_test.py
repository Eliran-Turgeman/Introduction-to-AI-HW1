from MazeProblem import MazeProblem, create_problem
from Robot import BreadthFirstSearchRobot as BFS, UniformCostSearchRobot, BestFirstSearchRobot
from Animation import Animation
import sys
import argparse

EXPECTED_RESULTS = {'bfs': [(36, 57), (51, 362), (216, 1212), (88, 2430), (123, 1209), (376, 5299)],
                    'ucs': [(36, 51), (47, 312), (216, 1212), (84, 2447), (123, 1205), (376, 5299)]}

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--index', type=str, default=None, help="maze index")
    parser.add_argument('-m', '--methods', type=str, default='all', help="search methods (separated by ,")
    parser.add_argument('--animate', action='store_true')
    return parser.parse_args()


def main_test(test_index, methods, animate):
    maze_name = 'maze_' + str(test_index)
    maze_problem = create_problem(maze_name)


    solutions = {}
    if 'bfs' in methods:
        bfs = BFS()
        bfs_solution = bfs.solve(maze_problem)
        solutions['bfs'] = {'algorithm': bfs, 'solution': bfs_solution}

    if 'ucs' in methods:
        ucs = UniformCostSearchRobot()
        ucs_solution = ucs.solve(maze_problem)
        solutions['ucs'] = {'algorithm': ucs, 'solution': ucs_solution}

    for key, search_alg_data in solutions.items():
        solution = search_alg_data['solution']
        assert EXPECTED_RESULTS[key][int(test_index)][0] == solution.cost, f"cost equals {solution.cost} in test {test_index} of {key}"
        assert EXPECTED_RESULTS[key][int(test_index)][1] == solution.n_node_expanded, f"node expanded equals {solution.n_node_expanded} in test {test_index} of {key}"
        print(f"TEST {test_index} for {key} PASSED")

    if animate:
        try:
            for key, search_alg_data in solutions.items():
                solution = search_alg_data['solution']
                search_algo = search_alg_data['algorithm']
                animation = Animation(solution, maze_problem, search_algo,
                                      maze_name, blit=False)
                animation.show()
        except:
            print('No solution!')


def test_wrapper(args):
    if args.methods == 'all':
        methods = [k for k in EXPECTED_RESULTS.keys()]
    else:
        methods = args.methods.split(',')

    test_index = -1
    if args.index is None:
        print("Running all tests")
    else:
        test_index = args.index

    if test_index == -1:
        for test_idx in range(0, 6):
            main_test(test_idx, methods, animate=args.animate)
    else:
        main_test(test_index, methods, animate=args.animate)


if __name__ == '__main__':
    args = parse()
    test_wrapper(args)


