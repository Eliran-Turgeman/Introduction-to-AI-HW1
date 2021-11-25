import numpy as np
from MazeProblem import MazeState, MazeProblem, compute_robot_direction
from Robot import UniformCostSearchRobot
from GraphSearch import NodesCollection


def tail_manhattan_heuristic(state: MazeState):
    # TODO (EX 7.2), implement heuristic, delete exception
    tail_pos = state.tail
    tail_goal = state.maze_problem.tail_goal
    forward_cost = state.maze_problem.forward_cost
    return (abs(tail_goal[0] - tail_pos[0]) + abs(tail_goal[1] - tail_pos[1])) * forward_cost


def center_manhattan_heuristic(state: MazeState):
    # TODO (EX 9.2), implement heuristic, delete exception
    center_pos = state.tail + state.head / 2
    center_goal = (state.maze_problem.tail_goal + state.maze_problem.head_goal) / 2
    return np.sum(abs(center_goal - center_pos))
    forward_cost = state.maze_problem.forward_cost
    return (abs(tail_goal[0] - tail_pos[0]) + abs(tail_goal[1] - tail_pos[1])) * forward_cost


class ShorterRobotHeuristic:
    def __init__(self, maze_problem: MazeProblem, k):
        assert k % 2 == 0, "odd must be even"
        assert maze_problem.length - k >= 3, f"it is not possible to shorten a {maze_problem.length}-length robot by " \
                                             f"{k} units because robot length has to at least 3"
        self.k = k
        ################################################################################################################
        # TODO (EX. 13.2): replace all three dots, delete exception
        shorter_robot_head_goal, shorter_robot_tail_goal = self._compute_shorter_head_and_tails(maze_problem.head_goal, maze_problem.tail_goal)
        shorter_robot_head_initial, shorter_robot_tail_initial = self._compute_shorter_head_and_tails(maze_problem.initial_state.head, maze_problem.initial_state.tail)
        self.new_maze_problem = MazeProblem(maze_map=maze_problem.maze_map,
                                            initial_head=shorter_robot_head_initial,
                                            initial_tail=shorter_robot_tail_initial,
                                            head_goal=shorter_robot_head_goal,  # doesn't matter, don't change
                                            tail_goal=shorter_robot_tail_goal)  # doesn't matter, don't change
        self.node_dists = UniformCostSearchRobot().solve(self.new_maze_problem, compute_all_dists=True)
        ################################################################################################################

        assert isinstance(self.node_dists, NodesCollection)

    def _compute_shorter_head_and_tails(self, head, tail):
        # TODO (EX. 13.1): complete code here, delete exception
        assert head[0] == tail[0] or head[1] == tail[1]

        new_head = np.copy(head)
        new_tail = np.copy(tail)

        if head[0] == tail[0]:
            diff_index = 1
        else:
            diff_index = 0

        if head[diff_index] < tail[diff_index]:
            new_head[diff_index] = new_head[diff_index] + int(self.k*0.5)
            new_tail[diff_index] = new_tail[diff_index] - int(self.k*0.5)
        else:
            new_head[diff_index] = new_head[diff_index] - int(self.k*0.5)
            new_tail[diff_index] = new_tail[diff_index] + int(self.k*0.5)

        return new_head, new_tail

    def __call__(self, state: MazeState):
        # TODO (EX. 13.3): replace each three dots, delete exception
        shorter_head_location, shorter_tail_location = self._compute_shorter_head_and_tails(state.head, state.tail)
        new_state = MazeState(self.new_maze_problem, head=shorter_head_location, tail=shorter_tail_location)
        if new_state in self.node_dists:
            node = self.node_dists.get_node(new_state)
            return node.g_value
        else:
            import pdb;
            pdb.set_trace()
            return center_manhattan_heuristic(state)
            # what should we return in this case, so that the heuristic would be as informative as possible
                        # but still admissible
