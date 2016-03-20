import math 
import subprocess
import networkx as nx
import matplotlib.pyplot as plt
from random import *
from copy import deepcopy

class Annealer:
	
	def __init__(self, init_state, costfn, local_move, cool_func, disp=-1):
		self.costfn=costfn
		self.local_move=local_move
		self.cool_func=cool_func
		
		self.best_state=init_state
		self.best_cost=self.costfn(init_state)
		self.disp=disp
		

	def accept(self, delta, temp):
		if delta<0:
			return 1.0
		return math.exp(-delta/temp)
	
	def anneal(self, temp):
		
		current_state=self.best_state
		current_cost=self.best_cost

		iters=-1
		while(temp > 1):
			
			print "BEST: %f  T: %f   C: %f "%(self.best_cost, temp, current_cost)
			if self.disp>0 and iters%self.disp==0:
				display_G(current_state)
			iters+=1

			(state, delta)=self.local_move(current_state)
			
			if self.accept(delta, temp) > random():
				current_state=state
				current_cost+=delta
				
				if current_cost<self.best_cost:
					self.best_cost=current_cost
					self.best_state=state
						
			temp=self.cool_func(temp)


def display_G(state):
	plt.clf()
	nx.draw(nxG, nxPos, node_color=state)
	plt.pause(0.5)



#--------------Parsing is a bi*** apparently-------------#
N, E=map(int,raw_input().split())
G={}
for i in range(E):
	u, v=map(int, raw_input().split())
	if u in G:
		G[u].append(v)
	else:
		G[u]=[v]
		
	if v in G:
		G[v].append(u)
	else:
		G[v]=[u]
		

#--------------Make an NX graph for prettiness-----------#
nxG=nx.Graph()
for node in G:
	nxG.add_node(node)
	for nbh in G[node]:
		nxG.add_edge(node,nbh)
nxPos=nx.spring_layout(nxG)



#--------------YOU NEED TO EDIT THESE FUNCTIONS AND VALUES-------------#
colours=2
init_state=tuple([0]*N) #you can leave this, or make it a random state
init_temp=100


'''
Remember, ANY local move works. Even extremely trivial ones.
We're hoping you'll come up with a decently complex local move --
with a good balance of computational expensiveness and utility.
The more complex local moves will help the solution converge faster,
and that's what you should be aiming to do
'''
def local_move(state):
	#FILL IN YOUR CODE HERE- and return the new state and the delta value
        new_state=[0]*N
        new_state=list(new_state)
        graph=deepcopy(G)
        palette=[[i for i in range(1,colours+1)] for x in range(N)]
        i=0
        while (i<N):
                #new_state[i+1]=state[i]
                #new_state[i]=randint(1,colours)
                if len(palette[i])!=0:
                        new_state[i]= choice(palette[i])
                        for j in G[i]:
                                if new_state[i] in palette[j]:
                                        palette[j].remove(new_state[i])
                        i+=1
                else:
                        '''new_state[i-1]=0
                        for j in G[i-1]:
                                if new_state[i-1] not in palette[j]:
                                        palette[j].append(new_state[i-1])
                        i-=1'''
                        return state,0
        
        #new_state[0]=state[N-1]
        new_state=tuple(new_state)
        delta=cost_fn(new_state)-cost_fn(state)
        #print palette
	return new_state, delta

'''
Try out all the temperature functions you can think of- Slow, fast, sinusoidal.
No, not sinusoidal.
'''
def cool_func(temp):
	#FILL IN YOUR CODE HERE- and return the new temperature value
        new_temp=temp-.1
	return new_temp

'''
Find a good objective function to MINIMIZE.
Remember, your ideal, best, amazing solution needs to have the
lowest function value
'''
def cost_fn(state):
	#FILL IN YOUR CODE HERE- and return the value of the state
        cost=0
        for i in range(0,N):
             for j in G[i]:
                     if state[j]!=state[i]:
                             cost+=0
                     else:
                             cost+=1
	return cost + .1*len(set(state))

#---------------------------------------------------------------------#


'''
disp controls after how many iterations you want to see your graph
set it to a negative number if you don't want to see it at all
(you'll still see your final graph)
'''
gc=Annealer(init_state, cost_fn, local_move, cool_func, disp=-1)
gc.anneal(init_temp)
print gc.best_state
print gc.best_cost
print len(set(gc.best_state))
display_G(gc.best_state)
#Save a picture of your result, to show off to your friends
plt.savefig('result.png')
plt.pause(100)


