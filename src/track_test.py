#!/usr/bin/env python
# src/track_test.py

import unittest
import track

class TestTrack(unittest.TestCase):
    '''This class tests all track methods'''
    def setUp(self):
        self.track_o = track.Track("../data/O-track.txt")
        self.track_l = track.Track("../data/L-track.txt")
        self.track_r = track.Track("../data/R-track.txt")
        self.track_strait = track.Track("../data/strait-track.txt")

    def test_toString(self):
        print (self.track_o)
        print (self.track_l)
        print (self.track_r)
        print (self.track_strait)

class TestCar(unittest.TestCase):
    '''This class tests all car methods'''
    def setUp(self):
        simple_track = track.Track("../data/strait-track.txt")
        self.car = track.Car(simple_track,simple_track.start_list[0])

    def test_acceleration(self):
        count = 0
        for i in range(1000):
            if self.car.acceleration([2,2]):
                count += 1
        # See works more then 85% of the time
        self.assertTrue(count > 850)

        # Insure that the speed is changed
        self.car.speed = [0,0]
        acc = [5,5]
        while not self.car.acceleration(acc): pass
        self.assertEqual(self.car.speed, acc)

    def test_checkspeed(self):
        '''test checkspeed and changespeed methods'''
        self.car.speed = [0,0]

        self.car.changespeed([1,1])
        self.assertEqual(self.car.speed, [1,1])

        self.car.changespeed([10,-10])
        self.assertEqual(self.car.speed, [5,-5])

        

if __name__ == '__main__':
    unittest.main()
