#src/mdp.py

import track

#Default MDP values
discount_factor = .90
action_probability = .90

class MDP:
    '''Stores the plan'''
    def __init__(self, car):
        self.buildActions()
        self.car = car
        self.track = self.car.track

        self.policy = []
        self.state_list = []

    def buildActions(self):
        self.acction_list = []
        for x in [1,0,-1]:
            for y in [1,0,-1]:
                self.action_list.append([x,y])


