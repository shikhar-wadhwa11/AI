from abc import ABCMeta,abstractmethod
from util import *
import numpy as np
from collections import defaultdict

class SearchProblem:
    __metaclass__=ABCMeta
    @abstractmethod 
    def getStartState(self):
        pass
    @abstractmethod
    def isGoalState(self, state):
        pass
    @abstractmethod
    def getSuccessors(self, state):
        pass
    @abstractmethod
    def getCostOfActions(self, actions):
        pass
def depthFirstSearch(problem):
    a=Stack() #fringe
    expand=set([])
    enque=[]

    start_state=problem.getStartState()
    a.push((start_state,[]))
    while (a.isEmpty()==False):
        state,actions=a.pop()
        if problem.isGoalState(state)==True:
            return actions
        b=problem.getSuccessors(state)
        expand.add(state)
        for i in b:
            if i[0] not in expand:
                a.push((i[0],actions + [i[1]])) 
    return []
def breadthFirstSearch(problem):
    a=Queue()
    visit=[]
    enque=[]
    start_state=problem.getStartState()
    a.push((start_state,[]))
    while (a.isEmpty()==False):
        state,actions=a.pop()
        if problem.isGoalState(state)==True:
            return actions
        b=problem.getSuccessors(state)
        visit.append(state)
        
        for i in b:
            if i[0] not in enque:
                enque.append(i[0])
                a.push((i[0],actions + [i[1]]))
    return []
def uniformCostSearch(problem):
    a=PriorityQueue()
    visit=[]
    expand=[]
    start_state=problem.getStartState()
    
    a.push((start_state,[],0),0)
    while (a.isEmpty()==False):
       state,actions,cost_State=a.pop()
       if problem.isGoalState(state)==True:
           return state,cost_State,actions
       if state not in expand: 
           b=problem.getSuccessors(state)
           expand.append(state)
           for i in b:
               if i[0] not in expand:
                   total_cost=cost_State + i[2]
                   a.push((i[0],actions + [i[1]] , total_cost),total_cost)
    return path
def astarSearch(problem,heuristic):
    expandedStates = set([])
	startState = problem.getStartState()

	fringe = util.PriorityQueue()
	startHeurisitc = heuristic(startState, problem)
	fringe.push((startState,[], 0), startHeurisitc)

	while not fringe.isEmpty():
		state, actions, costSoFar = fringe.pop()

		if(problem.isGoalState(state)):
			return actions

		if state in expandedStates:
			continue

		expandedStates.add(state)
		for nextState, action, cost in problem.getSuccessors(state):
			totalCost = costSoFar + cost + heuristic(nextState, problem)
			backwardCost = costSoFar + cost
			fringe.push((nextState, actions + [action], backwardCost), totalCost)

	return []
