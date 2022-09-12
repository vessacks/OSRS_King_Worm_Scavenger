#king worm

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
from meta_action import Meta_Action



#run notes
#run in RESIZABLE MODERN
#minimap must be turned off
#start with inv tab closed (ie no tab open, just playscreen)
#face due north, and have view zoomed all the way out. 
#take new in_bank image
# maybe update the offscreen point? There's a tool in sandbox

#thresholds
BANK_THRESHOLD = .8
IN_BANK_THRESHOLD = .8
BANK_DUMP_THRESHOLD = .8
BANK_STAM_POT_THRESHOLD = .8
INV_STAM_POT_THRESHOLD =.8
STOP_1_OUT_THRESHOLD =.8
STOP_2_OUT_THRESHOLD =.5
STOP_3_OUT_THRESHOLD =.8
STOP_4_OUT_THRESHOLD =.8
BOAT_OUT_THRESHOLD = .8
WORM_PREP_THRESHOLD =.8
WORM_SOURCE_THRESHOLD =.8 
INV_WORM_THRESHOLD = .8
BOAT_IN_THRESHOLD =.8
STOP_4_IN_THRESHOLD =.8 
STOP_3_IN_THRESHOLD =.8
STOP_2_IN_THRESHOLD =.8
STOP_1_IN_THRESHOLD =.8
BANK_PREP_THRESHOLD = .8



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

def key_press(key):
    pyautogui.keyDown(key)
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    pyautogui.keyUp(key)
    time.sleep(.15 + abs(np.random.normal(.1,.05)))
    tick_dropper()
    print('pressed %s key' % key)


# initialize the Vision and Action classes together

#bank
#bank_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_vision_mask.png', cv.IMREAD_COLOR)
bank_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=bank_vision_mask)
bank_face_size = [15,14]
bank_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_click_mask.png',0)
bank_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank.png', click_mask= bank_click_mask, face_size= bank_face_size)
bank_meta_action = Meta_Action(vision_object = bank_vision, action_object = bank_action, threshold = BANK_THRESHOLD, name = 'bank', look_timeout = 3)


# in bank
#in_bank_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\in_bank_vision_mask.png', cv.IMREAD_COLOR)
in_bank_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\in_bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=in_bank_vision_mask)
in_bank_meta_action = Meta_Action(vision_object = in_bank_vision, threshold = IN_BANK_THRESHOLD, name = 'in_bank', look_timeout = 2.5)

#bank dump
#bank_dump_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_dump_vision_mask.png', cv.IMREAD_COLOR)
bank_dump_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_dump.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=bank_dump_vision_mask)
#bank_dump_face_size = [48,93]
#bank_dump_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_dump_click_mask.png',0)
bank_dump_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_dump.png')#, click_mask= bank_dump_click_mask, face_size= bank_dump_face_size)
bank_dump_meta_action = Meta_Action(vision_object = bank_dump_vision, action_object = bank_dump_action, threshold = BANK_DUMP_THRESHOLD, name = 'bank_dump', look_timeout = 2.5)

'''
#bank stam pot
bank_stam_pot_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_stam_pot_vision_mask.png', cv.IMREAD_COLOR)
bank_stam_pot_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=bank_stam_pot_vision_mask)
bank_stam_pot_face_size = [48,93]
bank_stam_pot_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_stam_pot_click_mask.png',0)
bank_stam_pot_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_stam_pot.png', click_mask= bank_stam_pot_click_mask, face_size= bank_stam_pot_face_size)
bank_stam_pot_meta_action = Meta_Action(vision_object = bank_stam_pot_vision, action_object = bank_stam_pot_action, threshold = BANK_STAM_POT_THRESHOLD, name = 'bank_stam_pot', look_timeout = 3)

#inv stamina pot
inv_stam_pot_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_stam_pot_vision_mask.png', cv.IMREAD_COLOR)
inv_stam_pot_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=inv_stam_pot_vision_mask)
inv_stam_pot_face_size = [48,93]
inv_stam_pot_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_stam_pot_click_mask.png',0)
inv_stam_pot_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_stam_pot.png', click_mask= inv_stam_pot_click_mask, face_size= inv_stam_pot_face_size)
inv_stam_pot_meta_action = Meta_Action(vision_object = inv_stam_pot_vision, action_object = inv_stam_pot_action, threshold = INV_STAM_POT_THRESHOLD, name = 'inv_stam_pot', look_timeout = 3)
'''
#stop 1 out
#stop_1_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_out_vision_mask.png', cv.IMREAD_COLOR)
stop_1_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_1_out_vision_mask)
stop_1_out_face_size = [36,38]
stop_1_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_out_click_mask.png',0)
stop_1_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_out.png', click_mask= stop_1_out_click_mask, face_size= stop_1_out_face_size)
stop_1_out_meta_action = Meta_Action(vision_object = stop_1_out_vision, action_object = stop_1_out_action, threshold = STOP_1_OUT_THRESHOLD, name = 'stop_1_out', look_timeout = 3)


#stop 2 out
stop_2_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out_vision_mask.png', cv.IMREAD_COLOR)
stop_2_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_2_out_vision_mask)
stop_2_out_face_size = [48,93]
stop_2_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out_click_mask.png',0)
stop_2_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out.png', click_mask= stop_2_out_click_mask, face_size= stop_2_out_face_size)
stop_2_out_meta_action = Meta_Action(vision_object = stop_2_out_vision, action_object = stop_2_out_action, threshold = STOP_2_OUT_THRESHOLD, name = 'stop_2_out', look_timeout = 3)

'''
#stop 3 out
stop_3_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out_vision_mask.png', cv.IMREAD_COLOR)
stop_3_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_3_out_vision_mask)
stop_3_out_face_size = [48,93]
stop_3_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out_click_mask.png',0)
stop_3_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out.png', click_mask= stop_3_out_click_mask, face_size= stop_3_out_face_size)
stop_3_out_meta_action = Meta_Action(vision_object = stop_3_out_vision, action_object = stop_3_out_action, threshold = STOP_3_OUT_THRESHOLD, name = 'stop_3_out', look_timeout = 3)

#stop 4 out
stop_4_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out_vision_mask.png', cv.IMREAD_COLOR)
stop_4_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_4_out_vision_mask)
stop_4_out_face_size = [48,93]
stop_4_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out_click_mask.png',0)
stop_4_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out.png', click_mask= stop_4_out_click_mask, face_size= stop_4_out_face_size)
stop_4_out_meta_action = Meta_Action(vision_object = stop_4_out_vision, action_object = stop_4_out_action, threshold = STOP_4_OUT_THRESHOLD, name = 'stop_4_out', look_timeout = 3)

#boat out
boat_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out_vision_mask.png', cv.IMREAD_COLOR)
boat_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=boat_out_vision_mask)
boat_out_face_size = [48,93]
boat_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out_click_mask.png',0)
boat_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out.png', click_mask= boat_out_click_mask, face_size= boat_out_face_size)
boat_out_meta_action = Meta_Action(vision_object = boat_out_vision, action_object = boat_out_action, threshold = BOAT_OUT_THRESHOLD, name = 'boat_out', look_timeout = 3)

#worm prep
worm_prep_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep_vision_mask.png', cv.IMREAD_COLOR)
worm_prep_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=worm_prep_vision_mask)
worm_prep_face_size = [48,93]
worm_prep_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep_click_mask.png',0)
worm_prep_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep.png', click_mask= worm_prep_click_mask, face_size= worm_prep_face_size)
worm_prep_meta_action = Meta_Action(vision_object = worm_prep_vision, action_object = worm_prep_action, threshold = WORM_PREP_THRESHOLD, name = 'worm_prep', look_timeout = 3)
#(scroll 30 clicks in between calling prev and next actions and open inv. tab)

#worm_source
worm_source_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source_vision_mask.png', cv.IMREAD_COLOR)
worm_source_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=worm_source_vision_mask)
worm_source_face_size = [48,93]
worm_source_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source_click_mask.png',0)
worm_source_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source.png', click_mask= worm_source_click_mask, face_size= worm_source_face_size)
worm_source_meta_action = Meta_Action(vision_object = worm_source_vision, action_object = worm_source_action, threshold = WORM_SOURCE_THRESHOLD, name = 'worm_source', look_timeout = 3)

#inv_worm
inv_worm_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm_vision_mask.png', cv.IMREAD_COLOR)
inv_worm_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=inv_worm_vision_mask)
inv_worm_face_size = [48,93]
inv_worm_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm_click_mask.png',0)

#scrol 30 clicks out between calling prve and next actions and close inv. tab)

#boat in
boat_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in_vision_mask.png', cv.IMREAD_COLOR)
boat_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=boat_in_vision_mask)
boat_in_face_size = [48,93]
boat_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in_click_mask.png',0)
boat_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in.png', click_mask= boat_in_click_mask, face_size= boat_in_face_size)
boat_in_meta_action = Meta_Action(vision_object = boat_in_vision, action_object = boat_in_action, threshold = BOAT_IN_THRESHOLD, name = 'boat_in', look_timeout = 3)

#stop 4 in
stop_4_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in_vision_mask.png', cv.IMREAD_COLOR)
stop_4_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_4_in_vision_mask)
stop_4_in_face_size = [48,93]
stop_4_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in_click_mask.png',0)
stop_4_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in.png', click_mask= stop_4_in_click_mask, face_size= stop_4_in_face_size)
stop_4_in_meta_action = Meta_Action(vision_object = stop_4_in_vision, action_object = stop_4_in_action, threshold = STOP_4_IN_THRESHOLD, name = 'stop_4_in', look_timeout = 3)

#stop 3 in
stop_3_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in_vision_mask.png', cv.IMREAD_COLOR)
stop_3_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_3_in_vision_mask)
stop_3_in_face_size = [48,93]
stop_3_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in_click_mask.png',0)
stop_3_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in.png', click_mask= stop_3_in_click_mask, face_size= stop_3_in_face_size)
stop_3_in_meta_action = Meta_Action(vision_object = stop_3_in_vision, action_object = stop_3_in_action, threshold = STOP_3_IN_THRESHOLD, name = 'stop_3_in', look_timeout = 3)

#stop 2 in
stop_2_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in_vision_mask.png', cv.IMREAD_COLOR)
stop_2_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_2_in_vision_mask)
stop_2_in_face_size = [48,93]
stop_2_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in_click_mask.png',0)
stop_2_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in.png', click_mask= stop_2_in_click_mask, face_size= stop_2_in_face_size)
stop_2_in_meta_action = Meta_Action(vision_object = stop_2_in_vision, action_object = stop_2_in_action, threshold = STOP_2_IN_THRESHOLD, name = 'stop_2_in', look_timeout = 3)

#stop 1 in
stop_1_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in_vision_mask.png', cv.IMREAD_COLOR)
stop_1_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_1_in_vision_mask)
stop_1_in_face_size = [48,93]
stop_1_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in_click_mask.png',0)
stop_1_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in.png', click_mask= stop_1_in_click_mask, face_size= stop_1_in_face_size)
stop_1_in_meta_action = Meta_Action(vision_object = stop_1_in_vision, action_object = stop_1_in_action, threshold = STOP_1_IN_THRESHOLD, name = 'stop_1_in', look_timeout = 3)

#bank prep
bank_prep_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep_vision_mask.png', cv.IMREAD_COLOR)
bank_prep_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=bank_prep_vision_mask)
bank_prep_face_size = [48,93]
bank_prep_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep_click_mask.png',0)
bank_prep_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep.png', click_mask= bank_prep_click_mask, face_size= bank_prep_face_size)
bank_prep_meta_action = Meta_Action(vision_object = bank_prep_vision, action_object = bank_prep_action, threshold = BANK_PREP_THRESHOLD, name = 'bank_prep', look_timeout = 3)


'''

#thresholds
BANK_THRESHOLD = .8
IN_BANK_THRESHOLD = .8
BANK_DUMP_THRESHOLD = .8
BANK_STAM_POT_THRESHOLD = .8
INV_STAM_POT_THRESHOLD =.8
STOP_1_OUT_THRESHOLD =.8
STOP_2_OUT_THRESHOLD =.8
STOP_3_OUT_THRESHOLD =.8
STOP_4_OUT_THRESHOLD =.8
BOAT_OUT_THRESHOLD = .8
WORM_PREP_THRESHOLD =.8
WORM_SOURCE_THRESHOLD =.8 
INV_WORM_THRESHOLD = .8
BOAT_IN_THRESHOLD =.8
STOP_4_IN_THRESHOLD =.8 
STOP_3_IN_THRESHOLD =.8
STOP_2_IN_THRESHOLD =.8
STOP_1_IN_THRESHOLD =.8
BANK_PREP_THRESHOLD = .8
OFFSCREEN_POINT = [383,825]


'''    
#testing
banking = bank_meta_action.look_click_color()
in_banking = in_bank_meta_action.look_color()

if in_banking == 'timeout':
    print('in_bank search timeout. attempting bank relick')
    banking = bank_meta_action.look_click_color()

in_banking = in_bank_meta_action.look_color()
if in_banking == 'timeout':
    print('in_banking timeout 2rd time. tried moving mouse and reclicking bank, no good. exitting...')
    exit()

bank_dumping = bank_dump_meta_action.look_click_color()
if bank_dumping == 'timeout':
    print('bank_dump search timeout. moving mouse offscreen to reveal obscured objects')
    bank_action.moveTo(OFFSCREEN_POINT)

bank_dumping = bank_dump_meta_action.look_click_color()
if bank_dumping == 'timeout':
    print('bank_dump search timeout second time. somethings up, quitting')
    exit()

time.sleep(.2 + abs(np.random.normal(0,.1)))

key_press('esc')
'''
#stop_1_outing = stop_1_out_meta_action.look_click_color()

stop_2_outing = stop_2_out_meta_action.look_click_color()

#note as of 7:38pm 9.7.22
#you've tested up to stop_2_outing. Often the bank clicker misses the mark-- I think the mask is too big or there's a problem with my click generator. If there is a problem, just shrink the mask ebcause its easier than diving into the click patterner. 
# stop_2_outing is untested. 