#src/track.py

import random

track_key = {'road':     '.',
             'wall':     '#',
             'start':    's',
             'finish':   'f',
            }

class track(object):
    '''
    Stores all track related values
    '''
    def __init__(self, track_file):
        self.loadtrack(track_file)

    def loadtrack(self, track_file):
        '''Builds track from track file'''
        self.track = [[]]

        self.finish_list = []
        self.start_list = []

        self.road_list = []
        self.wall_list = []

        track_line = track_file.readline()

        temp_dem  = track_line.split(',')
        self.track_dem = [int(temp_dem[0]), int(temp_dem[1])]

        for x in range(self.track_dem[0]):

            track_line = track_file.readline()
            for y in range(self.track_dem[1]):
                
                y_point = track_line[y]
                
                self.track[x].append(y_point)

                # Build Lists for faster searching
                if y_point == track_key['road']:
                    self.road_list.append([x,y])

                elif y_point == track_key['wall']:
                    self.wall_list.append([x,y])
                
                elif y_point == track_key['start']:
                    self.start_list.append([x,y])
                
                elif y_point == track_key['finish']:
                    self.finish_list.append([x,y])
                else:
                    raise IOError('Unknown Charactor: {0}'.format(y_point))

    def __str__(self):
        string = ""
        for x in self.track:
            for y in x:
                string += y
            string += '\n'

        return string

class car(object):
    '''
    Stores and moves the car
    '''
    def __init__(self,track,start):
        self.track = track
        self.pos = start
        self.speed = [0,0]
        self.path = [[start]]

    def acc(self, change):
        '''Tries to accelerate the car'''
        if random.random() < .90:
            changespeed(change)
            return True
        return False

    def changespeed(self, acc):
        self.speed[0] += acc[0]
        self.speed[1] += acc[1]

        self.checkspeed(self)

    def checkspeed(self):
        if self.speed[0] > 5:
            self.speed[0] = 5
        elif self.speed[0] < -5:
            self.speed[0] = -5

        if self.speed[1] > 5:
            self.speed[1] = 5
        elif self.speed[1] < -5:
            self.speed[1] = -5

    def gametick(self, acc=None):
        '''Triggers on time tick, return the cost'''
        if acc:
            self.acc(acc)
        
    def move(self, pos):
        '''Moves the car to the next location'''
        self.path.append(pos)
        self.pos = pos

    def getpaths(old, new, path=None):
        '''returns a set of valid paths for the given route'''
        
        # Start path if not given
        if not path:
            path = []
        
        # Add current 
        path.append(old)

        # Return if new = old
        if old == new:
            path.append(old)
            return path

        diff_xy = [old[0]-new[0], old[1]-new[1]]

        # Call recusivly based on ratio
        # If ratio = 1 split path(aka diaganal path)
        if abs(diff_xy[0] / diff_xy[1]) == 1:
            #Move horiz
            new_old = list(old)
            new_old[0] += diff_xy[0] / abs(diff_xy[0])
            return self.getpaths(new_old, new, list(path))

        # TODO finish path cration logic
            
