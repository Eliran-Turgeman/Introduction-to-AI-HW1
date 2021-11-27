from Robot import *
from MazeProblem import *
from Animation import Animation
from Heuristics import *
from Utilities import *
from Experiments import *


if __name__ == "__main__":
    for k in [2,4,6,8]:
        test_robot(WAStartRobot, [3, 4], heuristic=ShorterRobotHeuristic, k = k)
