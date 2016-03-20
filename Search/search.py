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
    a=Stack()
    expand=set([])
    enque=[]
    #parent=[]
    start_state=problem.getStartState()
    #state_id={0:start_state}
    #path=[]
    a.push((start_state,[]))
    #iden=0
    while (a.isEmpty()==False):
        state,actions=a.pop()
        if problem.isGoalState(state)==True:
            return actions
        b=problem.getSuccessors(state)
        expand.add(state)
        for i in b:
            if i[0] not in expand:
                a.push((i[0],actions + [i[1]]))
                #state_id[iden]=i[0]
                #q=state,i[1]
                #parent.append(q)
                #iden+=1
    '''while(state!=start_state):
        s=0
        for ID,sta in state_id.items():
            if sta==state:
                s=ID
                break
        path.append(parent[s][1])
        state=parent[s][0]
    #return state_id
    return path[::-1]  '''      
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
    a=PriorityQueue()
    path=[]
    visit=[]
    start_state=problem.getStartState()
    state_id={}
    cost={start_state:heuristic(start_state)}
    a.push(start_state,0)
    while (a.isEmpty()==False):
       state=a.pop()
       if problem.isGoalState(state)==True:
           path.append(state)
           break
       if state not in visit:
           b=problem.getSuccessors(state)
           visit.append(state)
           path.append(state)
           for i in b:
               cost[i[0]] =cost[state] + i[2] +heuristic(i[0])
               a.push(i[0],cost[i[0]])
