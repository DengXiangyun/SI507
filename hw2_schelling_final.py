import random
import matplotlib.pyplot as plt
from IPython import display
import time

group_affinity_threshold = .51

random.seed(32) # for reproducible random numbers

class Agent():
  def __init__(self, xlocation, ylocation):
    self.x = xlocation
    self.y = ylocation

agent1 = Agent(22, 55)
agent2 = Agent(66, 88)

def map_all_agents(listofagents):
    agents_XCoordinate = [] 
    agents_YCoordinate = [] 
    for agent in listofagents:
      agents_XCoordinate.append(agent.x)
      agents_YCoordinate.append(agent.y)

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor='purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

agents_list = [agent1, agent2]

def moveagents(listofagents):
    for each_agent in listofagents:
        each_agent.x = random.randint(0,100)
        each_agent.y = random.randint(0,100)

def make_agents_dance(agentslist, num_steps=10):
    for i in range(num_steps):
        moveagents(agentslist)
        map_all_agents(agentslist)
        time.sleep(1) 
        display.clear_output(wait=True) 

random.seed(44)
New_List_of_Agents = [Agent(random.randint(0,100), random.randint(0,100))for i in range(12)]

class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status="unhappy"):  
        super().__init__(xlocation, ylocation)                      
        self.group = group
        self.status = status

'''Problem #1'''

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)

b1 = PurpleAgents(3,6)
print(b1.group)

class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)

'''Problem #2'''

random.seed(15)
List_of_PurpleAgents = [PurpleAgents(random.randint(0,100), random.randint(0,100))for i in range(12)]
List_of_GoldAgents = [GoldAgents(random.randint(0,100), random.randint(0,100))for i in range(12)]
CombinedList = List_of_PurpleAgents + List_of_GoldAgents

def map_colorful_agents(listofagents): 
    Purple_XCoordinate = [agent.x for agent in listofagents if agent.group=="Purple"]
    Purple_YCoordinate = [agent.y for agent in listofagents if agent.group=="Purple"]
    Gold_XCoordinate = [agent.x for agent in listofagents if agent.group=="Gold"]
    Gold_YCoordinate = [agent.y for agent in listofagents if agent.group=="Gold"]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

map_colorful_agents(CombinedList)


'''Problem #3'''

random.seed(38)
class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status="unhappy"):  
        super().__init__(xlocation, ylocation)                      
        self.group = group
        self.status = status

    def move_if_unhappy(self):  
        if self.status == "unhappy":  
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

a55 = AgentNew(24,11,"Purple")
a55.move_if_unhappy()
print(a55.x)


'''Problem #4'''

class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status="unhappy"):  
        super().__init__(xlocation, ylocation)                      
        self.group = group
        self.status = status

    def move_if_unhappy(self): 
        if self.status == "unhappy": 
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

    def check_neighbors(self, agentlist):
        zlist = list(filter(lambda agent: abs(agent.x - self.x) < 10, agentlist))
        zlist = list(filter(lambda agent: abs(agent.y - self.y) < 10, zlist))
        same_group_neighbor = [agent for agent in zlist if agent.group == self.group]
        opposite_group_neighbor = [agent for agent in zlist if agent.group != self.group]
        print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" )
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold:
            self.status="happy"
        else:
            self.status="unhappy"


'''Problem #5'''

class PurpleAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def move_if_unhappy(self):
        return super().move_if_unhappy()
    def check_neighbors(self, agentlist):
        return super().check_neighbors(agentlist)

class GoldAgents(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def move_if_unhappy(self):
        return super().move_if_unhappy()
    def check_neighbors(self, agentlist):
        return super().check_neighbors(agentlist)

random.seed(34)
p32 = PurpleAgents(14,55)
p32.move_if_unhappy()
print(p32.x)


'''Problem #6a'''

random.seed(2021)
group_affinity_threshold = .51
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100))for i in range(200)] + [GoldAgents(random.randint(0,100), random.randint(0,100))for i in range(200)]
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist) 
    for agent in (testlist):
        agent.move_if_unhappy()
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)

'''Problem #6b'''

random.seed(202)
group_affinity_threshold = .4
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100))for i in range(400)] + [GoldAgents(random.randint(0,100), random.randint(0,100))for i in range(400)]
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  
    for agent in (testlist):
        agent.move_if_unhappy() 
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


'''Problem #7'''
random.seed(11)
class PurpleDiversitySeekers(AgentNew):
    def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def move_if_unhappy(self):
        return super().move_if_unhappy()
    def check_neighbors(self, agentlist):
        zlist = list(filter(lambda agent: abs(agent.x - self.x) < 10, agentlist))
        zlist = list(filter(lambda agent: abs(agent.y - self.y) < 10, zlist))
        same_group_neighbor = [agent for agent in zlist if agent.group == self.group]
        opposite_group_neighbor = [agent for agent in zlist if agent.group != self.group]
        print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" )
        if (len(opposite_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold:
            self.status="happy"
        else:
            self.status="unhappy"

class GoldDiversitySeekers(AgentNew):
    def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
        super().__init__(xlocation, ylocation, group, status)
    def move_if_unhappy(self):
        return super().move_if_unhappy()
    def check_neighbors(self, agentlist):
        zlist = list(filter(lambda agent: abs(agent.x - self.x) < 10, agentlist))
        zlist = list(filter(lambda agent: abs(agent.y - self.y) < 10, zlist))
        same_group_neighbor = [agent for agent in zlist if agent.group == self.group]
        opposite_group_neighbor = [agent for agent in zlist if agent.group != self.group]
        print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" )
        if (len(opposite_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold:
            self.status="happy"
        else:
            self.status="unhappy"


random.seed(202)
group_affinity_threshold = .51
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100))for i in range(300)] + [GoldAgents(random.randint(0,100), random.randint(0,100))for i in range(300)] + [PurpleDiversitySeekers(random.randint(0,100), random.randint(0,100))for i in range(100)] + [GoldDiversitySeekers(random.randint(0,100), random.randint(0,100))for i in range(100)]
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  
    for agent in (testlist):
        agent.move_if_unhappy() 
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)
