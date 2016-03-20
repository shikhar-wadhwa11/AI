import numpy as np
from search import *
from copy import copy,deepcopy
class eightPuzzleState:
    grid=[]
    def __init__(self):
        for i in range(0,3):
            self.grid.append([])
            for j in range(0,3):
                self.grid[i].append(0)
    def get_values(self):
        for i in range(0,3):
            for j in range(0,3):
                self.grid[i][j]=int(raw_input())
        return self.grid
class eightPuzzleProblem(SearchProblem):
    def getStartState(self):
        a=eightPuzzleState()
        state=a.get_values()   
        return state
       
    def isGoalState(self,state):
        goal1=[[1,2,3],[8,0,4],[7,6,5]]
        goal2=[[0,1,2],[3,4,5],[6,7,8]]
        goal3=[[1,2,3],[4,5,6],[7,8,0]]
        if (goal1==state) or (goal2==state) or (goal3==state):
            return True
        else:
            return False
    def getSuccessors(self, state):
        suc=[]
        for i in range(0,3):
            for j in range(0,3):
                if state[i][j]==0:
                    a=i
                    b=j
                    break
            if state[i][j]==0:
                break
        legal=[]
        if a!=2:
            legal.append('down')
        if a!=0:
            legal.append('up')
        if b!=0:
            legal.append('left')
        if b!=2:
            legal.append('right')
        for i in legal:
            if i=='down':
                state1=deepcopy(state)
                (state1[a+1][b],state1[a][b])=(state1[a][b],state1[a+1][b])
                v=state1,'DOWN',0
                suc.append(v)
            if i=='up':
                state2=deepcopy(state)
                (state2[a-1][b],state2[a][b])=(state2[a][b],state2[a-1][b])
                v=state2,'UP',0
                suc.append(v)
            if i=='right':
                state3=deepcopy(state)
                (state3[a][b+1],state3[a][b])=(state3[a][b],state3[a][b+1])
                v=state3,'RIGHT',0
                suc.append(v)
            if i=='left':
                state4=deepcopy(state)
                (state4[a][b-1],state4[a][b])=(state4[a][b],state4[a][b-1])
                v=state4,'LEFT',0
                suc.append(v)
        return suc
    def getCostOfActions(self, actions):
        pass
assert issubclass(eightPuzzleProblem, SearchProblem)

def main():
    a=eightPuzzleProblem()
    m=breadthFirstSearch(a)
    print m
    
main()


