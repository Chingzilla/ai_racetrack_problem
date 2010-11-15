#!/usr/bin/env python
# src/track_test.py

import unittest
import track

class TestVerify(unittest.TestCase):
    '''This class tests all track and car methods'''
    def setUp(self):
        self.track_o = track.track(open("../data/O-track.txt",'r'))
        self.track_l = track.track(open("../data/L-track.txt",'r'))
        self.track_r = track.track(open("../data/R-track.txt",'r'))
        self.track_strait = track.track(open("../data/strait-track.txt",'r'))

    def test_toString(self):
        print self.track_o
        print self.track_l
        print self.track_r
        print self.track_strait

if __name__ == '__main__':
    unittest.main()
