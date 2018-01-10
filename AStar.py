# Astar.py, April 2017 
# Based on ItrDFS.py, Ver 0.3, April 11, 2017.

# A* Search of a problem space.
# The Problem should be given in a separate Python
# file using the "QUIET" file format.
# See the TowerOfHanoi.py example file for details.
# Examples of Usage:

# python3 AStar.py EightPuzzleWithHeuristics h_manhattan

import sys
from queue import PriorityQueue

# DO NOT CHANGE THIS SECTION 
if sys.argv==[''] or len(sys.argv)<2:
    import EightPuzzleWithHeuristics as Problem
    heuristics = lambda s: Problem.HEURISTICS['h_manhattan'](s)
    
else:
    import importlib
    Problem = importlib.import_module(sys.argv[1])
    heuristics = lambda s: Problem.HEURISTICS[sys.argv[2]](s)

print("\nWelcome to AStar")
COUNT = None
BACKLINKS = {}
PRI = []

# DO NOT CHANGE THIS SECTION
def runAStar():
    #initial_state = Problem.CREATE_INITIAL_STATE(keyVal)
    initial_state = Problem.CREATE_INITIAL_STATE()
    print("Initial State:")
    print(initial_state)
    global COUNT, BACKLINKS
    COUNT = 0
    BACKLINKS = {}
    PRI = []
    path, name = AStar(initial_state)
    print(str(COUNT)+" states examined.")
    return path, name

# A star search algorithm
# TODO: finish A star implementation
def AStar(initial_state):
    global COUNT, BACKLINKS
    # TODO: initialze and put first state into 
    # priority queue with respective priority
    # add any auxiliary data structures as needed
    OPEN = []
    CLOSED = []
    BACKLINKS[initial_state] = -1
    OPEN.append(initial_state)
    PRI.append(0)
    G = {}
    F = {}
    G[initial_state] = 0

    while len(OPEN) > 0:
        index = findMin()
        S = OPEN[index]
        del OPEN[index]
        del PRI[index]
        while S in CLOSED:
            index = findMin()
            S = OPEN[index]
            del OPEN[index]
            del PRI[index]
        CLOSED.append(S)
        
        # DO NOT CHANGE THIS SECTION: begining 
        if Problem.GOAL_TEST(S):
            print(Problem.GOAL_MESSAGE_FUNCTION(S))
            path = backtrace(S)
            return path, Problem.PROBLEM_NAME
        # DO NOT CHANGE THIS SECTION: end

        # TODO: finish A* implementation
        COUNT += 1
        for op in Problem.OPERATORS:
            if op.precond(S):
                new_state = op.state_transf(S)
                if not (new_state in OPEN) and not (new_state in CLOSED):
                    G[new_state] = G[S] + 1
                    F[new_state] = G[new_state] + heuristics(new_state)
                    BACKLINKS[new_state] = S
                    OPEN.append(new_state)
                    PRI.append(F[new_state])
                elif BACKLINKS[new_state] != -1:
                    other_parent = BACKLINKS[new_state]
                    temp = F[new_state]-G[other_parent]+G[S]
                    if temp < F[new_state]:
                        G[new_state] = G[new_state]-F[new_state]+temp
                        F[new_state] = temp
                        BACKLINKS[new_state] = S
                        if new_state in CLOSED:
                            OPEN.append(new_state)
                            PRI.append(F[new_state])
                            CLOSED.remove(new_state)

def findMin():
    min = PRI[0]
    index = 0
    for i in range(len(PRI)):
        if PRI[i] < min:
            min = PRI[i]
            index = i
    return index

# DO NOT CHANGE
def backtrace(S):
    global BACKLINKS
    path = []
    while not S == -1:
        path.append(S)
        S = BACKLINKS[S]
    path.reverse()
    print("Solution path: ")
    for s in path:
        print(s)
    print("\nPath length = "+str(len(path)-1))
    return path    

if __name__=='__main__':
    path, name = runAStar()



