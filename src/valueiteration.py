# ./src/valueiteration

import track
import mdp

error_magnitude = .001

class ValueIteration:
    '''
    Performs a Value Iteration on the given car/track
    '''
    def __init__(self, mdp):
        self.mdp = mdp
        self.car = mdp.car
        self.track = mdp.car.track
        
        self.state_list = mpd.state_list

    def initV(self):
        '''Create 4D array''' 
        self.v = []
        for x in range(self.track.track_dem[0]):
            for y in range(self.track.track_dem[1]):
                self.v.append([self.mdp.action_list[:]])
    
    def argMax(q, state){
        maxAction

    def createMDP(maxt=
