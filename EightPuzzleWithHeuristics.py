#<METADATA>
QUIET_VERSION = "0.2"
PROBLEM_NAME = "Eight Puzzle"
PROBLEM_VERSION = "0.2"
PROBLEM_AUTHORS = ['Chiho Kim']
PROBLEM_CREATION_DATE = "19-APR-2017"
PROBLEM_DESC=\
'''This formulation of the Eight Puzzle problem uses generic
Python 3 constructs and has been tested with Python 3.6.1
It is designed to work according to the QUIET tools interface, Version 0.2.
'''
#</METADATA>

#<STATE>
class State():
  def __init__(self, p):
    self.p = p

  def __str__(self):
    p = self.p
    txt = "["
    for i in range(len(p)):
        txt += str(p[i])
        if i < len(p)-1:
            txt += ","
    return txt+"]"

  def __eq__(self, s2):
    if not (type(self)==type(s2)): return False
    p1 = self.p; p2 = s2.p
    if len(p1) != len(p2): return False
    for i in range(len(p1)):
        if p1[i] != p2[i]: return False
    return True

  def __hash__(self):
    return (str(self)).__hash__()

  def __copy__(self):
    news = State([])
    for i in range(len(self.p)):
      news.p.append(self.p[i])
    return news
#</STATE>

#<INITIAL_STATE>
# puzzle0:
INITIAL_STATE = State([4, 5, 0, 1, 2, 8, 3, 7, 6])
CREATE_INITIAL_STATE = lambda: INITIAL_STATE
'''
puzzle0:
CREATE_INITIAL_STATE = lambda x: [0, 1, 2, 3, 4, 5, 6, 7, 8]
puzzle1a:
CREATE_INITIAL_STATE = lambda x: [1, 0, 2, 3, 4, 5, 6, 7, 8]
puzzle2a:
CREATE_INITIAL_STATE = lambda x: [3, 1, 2, 4, 0, 5, 6, 7, 8]
puzzle4a:
CREATE_INITIAL_STATE = lambda x: [1, 4, 2, 3, 7, 0, 6, 8, 5]
puzzle10a:
CREATE_INITIAL_STATE = lambda: [4, 5, 0, 1, 2, 3, 6, 7, 8]
puzzle12a:
CREATE_INITIAL_STATE = lambda: [3, 1, 2, 6, 8, 7, 5, 4, 0]
puzzle14a:
CREATE_INITIAL_STATE = lambda: [4, 5, 0, 1, 2, 8, 3, 7, 6]
puzzle16a:
CREATE_INITIAL_STATE = lambda: [0, 8, 2, 1, 7, 4, 3, 6, 5]
'''
#</INITIAL_STATE>

#<COMMON_CODE>
def can_move(s, From, To):
    start = int(From)
    end = int(To)
    p = s.p
    if p[end] != 0:
        return False
    if start%3 == 0:
        if end == start+1 or end == start+3 or end == start-3:
            return True
    if start%3 == 1:
        if end == start+1 or end == start-1 or end == start+3 or end == start-3:
            return True
    if start%3 == 2:
        if end == start-1 or end == start+3 or end == start-3:
            return True
    return False

def move(s,From,To):
    start = int(From)
    end = int(To)
    news = s.__copy__() # start with a deep copy.
    p1 = s.p[start]
    p2 = s.p[end]
    news.p[start] = p2
    news.p[end] = p1
    return news # return new state

def goal_test(s):
    goal = True
    for i in range(len(s.p)):
        if s.p[i] != i:
            return False
    return goal

def goal_message(s):
  return "The Eight Puzzle is solved!"

class Operator:
  def __init__(self, name, precond, state_transf):
    self.name = name
    self.precond = precond
    self.state_transf = state_transf

  def is_applicable(self, s):
    return self.precond(s)

  def apply(self, s):
    return self.state_transf(s)

import math

def h_euclidean(state):
    sum = 0
    for i in range(len(state.p)):
        x,y = findDist(i,state.p[i])
        temp = math.sqrt(x*x+y*y)
        sum += temp
    return sum

def h_hamming(state):
    count = 0
    for i in range(len(state.p)):
        if i != state.p[i]:
            count += 1
    return count

def h_manhattan(state):
    sum = 0
    for i in range(len(state.p)):
        x,y = findDist(i,state.p[i])
        sum += x+y
    return sum

def h_custom(state):
    return h_hamming(state)+h_manhattan(state)

def findDist(a,b):
    x = abs(a%3 - b%3)
    y = abs(a//3 - b//3)
    return x,y

#</COMMON_CODE>

#<OPERATORS>
combinations = []
for i in range(9):
    for j in range(9):
        if i != j:
            combinations.append((str(i),str(j)))
OPERATORS = [Operator("Move block from "+p+" to "+q,
                      lambda s,p1=p,q1=q: can_move(s,p1,q1),
                      lambda s,p1=p,q1=q: move(s,p1,q1) )
             for (p,q) in combinations]
#</OPERATORS>

#<GOAL_TEST>
GOAL_TEST = lambda s: goal_test(s)
#</GOAL_TEST>

#<GOAL_MESSAGE_FUNCTION>
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
#</GOAL_MESSAGE_FUNCTION>

#<HEURISTICS>
HEURISTICS = {'h_euclidean': h_euclidean, 'h_hamming':h_hamming,
    'h_manhattan':h_manhattan, 'h_custom':h_custom}
#</HEURISTICS>