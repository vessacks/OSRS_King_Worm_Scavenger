from msilib.schema import Feature
import cv2 as cv
from cv2 import threshold
from cv2 import _InputArray_STD_BOOL_VECTOR
import numpy as np
import os
from windmouse import wind_mouse
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from pyHM import Mouse
import time
from action import Action

# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Vessacks')

def speed():
    speed = np.random.normal(.7,.3)
    while speed > .85 or speed < .6:
        speed = np.random.normal(.75,.08)
    return speed


def tick_dropper(odds=20):
    if np.random.randint(0,odds) == 1:
        
        drop = np.random.uniform(.6,2)
        print('tick dropper! sleeping %s' %drop)
        time.sleep(drop)
    return

def wait():
    wait = (.06 + abs(np.random.normal(0,.05)))
    return wait


class Meta_Action:
    def __init__(self, vision_object=None, action_object=None, threshold=None, name = '\'no name given\'', look_timeout = 5):
        self.vision_object = vision_object
        self.action_object = action_object
        self.threshold = threshold
        self.name = name
        self.look_timeout = look_timeout
    
    def look_color(self):
        print('looking for %s' % self.name)
        self.start_time = time.time()
        while True:
            screenshot = wincap.get_screenshot() 
            self.look_allPoints, self.look_bestPoint, self.look_confidence = self.vision_object.find(screenshot, threshold = self.threshold, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            if self.look_confidence > self.threshold:
                print('found %s | searched %s | confidence %s | returning True' %(self.name, round(time.time() - self.start_time,2),self.look_confidence))
                return True
            if time.time() - self.start_time > self.look_timeout:
                print(' %s search timed out | ran %ss | last conf. %s | returning \'timeout\'')
                return 'timeout' 

    def look_click_color(self):
        #returns 'timeout' if timed out of search
        print('looking for %s' % self.name)
        self.start_time = time.time()
        while True:    
            screenshot = wincap.get_screenshot() 
            self.look_allPoints, self.look_bestPoint, self.look_confidence = self.vision_object.find(screenshot, threshold = self.threshold, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                exit()
            if self.look_confidence > self.threshold:
                print('found %s | searched %s | confidence %s | clicking...' %(self.name, round(time.time() - self.start_time,2),self.look_confidence))
                break

            if time.time() - self.start_time > self.look_timeout:
                print(' %s search timed out | ran %ss | last conf. %s | returning \'timeout\'' %(self.name, round(time.time() - self.start_time,2),self.look_confidence))
                return 'timeout'

        self.screenpoint = wincap.get_screen_position(self.look_bestPoint)
        self.clickpoint = self.action_object.click(self.screenpoint, speed = speed(), wait=wait(), tick_dropper_odds= 100)
        tick_dropper()
        return self.clickpoint
