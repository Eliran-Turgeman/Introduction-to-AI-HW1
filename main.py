from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    # for k in [2, 4, 6, 8]:
    #     test_robot(WAStartRobot, [3, 4], heuristic=ShorterRobotHeuristic, k=k)

    # for k in range(2, 6):
    #     shorter_robot_heuristic_experiment(k)
    for k in range(0, 3):
        w_experiment(k)
