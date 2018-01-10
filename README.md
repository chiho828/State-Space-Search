# State-Space-Search

ItrDFS.py, ItrBFS.py, and Astar.py use Depth First Search, Breadth First Search, and A* Search algorithms to find solutions in the EightPuzzle and Tower of Hanoi game.

The BFS algorithm finds the shortest path to solve a problem, and the A* search finds this shortest path in fewer steps than in the BFS with the use of heuristics (Euclidean, Hamming, Manhattan). These heuristics must be admissible, i.e. they should not overestimate the cost of reaching the goal state, and they help making a good guess on the next step to examine.
