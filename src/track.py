#src/track.py

import random
from mdp import action_probability

track_key = {'road':     '.',
             'wall':     '#',
             'start':    'S',
             'finish':   'F',
            }

class Track(object):
    '''
    Stores all track related values
    '''
    def __init__(self, file):
        track_file = open(file, 'r');
        self.loadtrack(track_file)
        self.file_name = file;

    def loadtrack(self, track_file):
        '''Builds track from track file'''
        self.track = []

        self.finish_list = []
        self.start_list = []

        self.road_list = []
        self.wall_list = []

        track_line = track_file.readline()

        temp_dem  = track_line.split(',')
        self.track_dem = [int(temp_dem[0]), int(temp_dem[1])]

        for x in range(self.track_dem[0]):

            track_line = track_file.readline()
            self.track.append([])

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
                    raise IOError('Unknown Charactor: {0} @ {1}'.format(y_point, str([x,y])))
        
        #Close file, save resources :)
        track_file.close()

    def __str__(self):
        string = ""
        for x in self.track:
            for y in x:
                string += y
            string += '\n'
        return string

class Car(object):
    '''
    Stores and moves the car
    '''
    def __init__(self,track,start=None,crash=None):
        self.track = track
        self.speed = [0,0]
        #Set the crash setup
        if crash == None:
            self.crash = self.crashbackup

        #Set up start point if not given
        if start==None:
            self.start = self.track.start_list[0];
        else:
            self.start = start
        self.path = [[start]]

    def crashbackup(current_path):
        self.speed = [0,0]
        temp_pos = current_path[0]
        for x in current_path:
            if x in self.track.wall:
                return temp_pos
            temp_pos = x
        print("crashbackup: Error no wall found")

    def crashrestart(current_path):
        self.speed = [0,0]
        return self.path[0]

    def acceleration(self, new_acc):
        '''Tries to accelerate the car'''
        if random.random() < action_probability:
            self.changespeed(new_acc)
            return True
        return False

    def changespeed(self, acc):
        if acc[0]:
            self.speed[0] += acc[0]/abs(acc[0])
        if acc[0]:
            self.speed[1] += acc[1]/abs(acc[1])

        self.checkspeed()

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
        new_pos_x = self.speed[0] + self.pos[0]
        new_pos_y = self.speed[1] + self.pos[1]
        move([new_pos_x, new_pos_y])

        #Check if at finish line
        if pos in track.finish_list:
            return 0
        else:
            return -1
        
    def move(self, pos):
        '''Moves the car to the next location'''
        self.path.append(pos)
        travel_path = getpaths(self.pos, pos);
        #check if car passed finish line
        for temp in travel_path:
            if temp in self.track.finish_list:
                self.pos = temp
                return

        #check if car crashes
        for x in travel_path:
            if x in self.track.wall_list:
                pos = self.crash(travel_path)
                return
                
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
        if abs(diff_xy[0] / diff_xy[1]) >= 1:
            #Move horiz
            new_old = list(old)
            new_old[0] += diff_xy[0] / abs(diff_xy[0])
            return self.getpaths(new_old, new, list(path))
        else:
            #Move vertical
            new_old = list(old)
            new_old[1] += diff_xy[1] / abs(diff_xy[1])
            return self.getpaths(new_old, new, list(past))

    def __str__(self):
           return track 
