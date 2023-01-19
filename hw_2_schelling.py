
import random
import matplotlib.pyplot as plt
from IPython import display
import time

random.seed(32) # for reproducible random numbers

#####################
### DO THIS FIRST ###
#####################

# replace each pass statement with the appropriate code
# make sure to add New_List_of_Agents (line 41)
# fill it in or copy the code from lab

class Agent():
    pass # LAB PROB 1

agent1 = Agent(22, 55)
agent2 = Agent(66, 88)

def map_all_agents(listofagents):
    pass # LAB PROB 4; COPY ONLY THE FUNCTION (NOT THE FUNCTION CALLS)

agents_list = [agent1, agent2]

def moveagents(listofagents):
    pass # LAB PROB 6; COPY ONLY THE FUNCTION (NOT THE FUNCTION CALLS)

def make_agents_dance(agentslist, num_steps=10):
    pass # LAB PROB 8; COPY ONLY THE FUNCTION (NOT THE FUNCTION CALLS)

### add New_List_of_Agents from LAB PROB 9

class AgentNew(Agent):
    pass # LAB PROB 10; COPY ONLY THE FUNCTION (NOT THE FUNCTION CALLS)


#############################
### THIS IS YOUR HOMEWORK ###
#############################

'''Problem #1'''

# The class AgentNew randomly picks whether an agent will be purple or gold.
# We may want to specify that instead, so lets create two subclasses of AgentNew.
# Let's call them PurpleAgents and GoldAgents.
# Below is flawed code for the subclass PurpleAgents.
# You can fix it simply by deleting/editing the mistakes I have made.
# You don't have to add any new lines.
# Once it's fixed, go ahead and create an analogous subclass called GoldAgents,
# which has the default group="Gold".

class (PurpleAgents(AgentNew)):
    def super().__init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
        AgentNew.__init(self, xlocation, ylocation, group, status)

b1 = PurpleAgents(3,6)
print(b1.group)


'''Problem #2'''

# Let's test our new classes and see if they work.
# If you complete the code below you should get a figure that looks like Plot7
# in the pdf.

random.seed(15)
List_of_PurpleAgents = [???]  ### using list comprehension, make 12 PurpleAgents
List of GoldAgents = ??? ### using list comprehension, make 12 GoldAgents
CombinedList = ???  ### using your knowledge of list methods, combine these into one list

def map_colorful_agents():  # what argument should go in this function?

    Purple_XCoordinate = [___.x for _____ in _______ if agent.group=="Purple"] ### fill in the blanks to make this list comprehension work
    Purple_YCoordinate = [???] # model this after the above list comprehension
    Gold_XCoordinate = [???]
    Gold_YCoordinate = [???]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

### call the function appropriately


'''Problem #3'''

# Now that we have some agents of different groups, let's go back and add a
# method to AgentNew that allows agents to move if they are unhappy.

random.seed(38)
class AgentNew():

### PASTE IN YOUR CONSTRUCTOR

    def move_if_unhappy(?????):  # what arguement(s) are needed here?
        if self.status="unhappy":  ### there is a mistake in this command - fix it
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

a55 = AgentNew(24,11,"Purple")

a55.move_if_unhappy  ### there is something wrong with this command - fix it

print(a55.x)  ### if your class is set up right the printed answer should be 81 (not 24)


'''Problem #4'''

# Now we are going to make our most complicated method.
# We're going to build a method called 'check_neighbors' which will identify
# the agents that are within 10 x-coordinate AND 10 y-coordinate spaces of a
# given agent. Once those agents are identified, we'll calculate if enough of
# them are of the same group to meet our pre-determined threshold.
# MAKE SURE TO USE A LAMBDA FUNCTION WHERE INDICATED.
# MAKE SURE TO USE LIST COMPREHENSIONS WHERE INDICATED.
# Fill in the code below.

class AgentNew():

    ### PASTE IN YOUR CONSTRUCTOR

    ### paste in move_if_unhappy method

    def check_neighbors(self, agentlist):  # note this method needs not only the self attributes - it also needs a list of agents
        zlist = ### here, use a filter and a lambda function to find all agents in a list who are within 10 spaces in the X direction of the agent that is calling the method
        zlist = ### do the same thing now to filter for agents within 10 spaces in the y direction - what list do you want to apply this lambda function to?
        same_group_neighbor =  ### use list comprehension to only keep members of zlist who are of the same group as this agent
        opposite_group_neighbor = ### use list comprehension to only keep members of zlist who are of the opposite group as this agent
        # print(len(same_group_neighbor), "same group neighbors, and ", len(zlist), " total neibhors" ) # this is commented out but you can use this as a diagnostic to make sure its working
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: # this command works; it checks the percentage of same group neighbors against some threshold to determine the agents happiness
            self.status="happy"
        else:
            self.status="unhappy"


'''Problem #5'''

# Now that you've added some methods to the class AgentNew, can you call them
# from the child class? Why or why not?
# Test the code below and find out. If necessary, add some code to make those
# methods available to objects from the classes PurpleAgents and GoldAgents.

random.seed(34)
p32 = PurpleAgent(14,55)
p32.move_if_unhappy()
print(p32.x)  # what do you expect the output to be?


'''Problem #6a'''

# Now we're ready to put it all together and run a few simulations.
# First, let's run a simulation in which there are 200 Purple agents and
# 200 Gold agents.
# Notice the group_affinity_threshold is set at .51.
# This means each purple or gold agent wants to be in a 'block' in which they
# are in the majority group.
# What happens after 15 turns?
# To make sure you're running this simulation correctly, test against Plot8
# and Plot9 in the pdf.

random.seed(2021)
group_affinity_threshold = .51
testlist = ??? ### create a testlist that has 200 PurpleAgents and 200 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors()  # does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


'''Problem #6b'''

# What happens if we run it again but with a threshold of only 0.4?
# Let's run this simulation with 400 of each type of agent.
# Modify the code below to test it out.

random.seed(202)
group_affinity_threshold = .4
testlist = ??? ###### create a testlist that has 400 PurpleAgents and 400 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors()  #does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


'''Problem #7'''

# Even if people don't mind being a minority in their neighborhood, you still
# get segregation pretty easily according to this model. For a long time models
# such as this were used to argue that some degree of segregation was
# inevitable, and therefore it should not be a target of policy.

# Let's challenge that assumption.
# Make 2 new subclasses, 'PurpleDiversitySeekers' and 'GoldDiversitySeekers'.
# Please use those exact names to allow for autograding.
# For these subclasses, make them seek out diversity instead of avoid it.
# Run some simulations with 300 traditional PurpleAgents, 300 traditional
# GoldAgents, 100 PurpleDiversitySeekers, and 100 GoldDiversitySeekers.
# What happens now?

random.seed(11)

### use this space to run the additional simulations