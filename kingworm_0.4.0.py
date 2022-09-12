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
#bank new in_bank image
#run in RESIZABLE MODERN
#minimap must be turned off
#start with inv tab closed (ie no tab open, just playscreen)
#face due north, and have view zoomed all the way out. 
#take new in_bank image
# maybe update the offscreen point? There's a tool in sandbox
#start in bank_prep position

#dev notes
#images and masks for stop 2,3,4, boat_out, and worm_prep were all taken with windows night light active. It seems not to have fucked them up, but there's a problem with image recognition that's likely it. 

#thresholds
BANK_THRESHOLD = .8
IN_BANK_THRESHOLD = .8
BANK_DUMP_THRESHOLD = .8
BANK_STAM_POT_THRESHOLD = .8
INV_STAM_POT_THRESHOLD =.8
STOP_1_OUT_THRESHOLD =.8
STOP_2_OUT_THRESHOLD =.5
STOP_3_OUT_THRESHOLD =.5
STOP_4_OUT_THRESHOLD =.5
BOAT_OUT_THRESHOLD = .5
WORM_PREP_THRESHOLD =.5
WORM_SOURCE_THRESHOLD =.5 
INV_WORM_THRESHOLD = .99
BOAT_IN_THRESHOLD =.5
STOP_4_IN_THRESHOLD =.5 
STOP_3_IN_THRESHOLD =.5
STOP_2_IN_THRESHOLD =.5
STOP_1_IN_THRESHOLD =.5
BANK_PREP_THRESHOLD = .5

MAX_WORM_CLICK_TIME = 32.4 #after this time is elapsed it will stop the worm click grind no matter what
BOAT_OUT_CHECK_THRESHOLD = .8 #I don't think I used this, but it has to be defined for some reason



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
stop_2_out_face_size = [37,40]
stop_2_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out_click_mask.png',0)
stop_2_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_out.png', click_mask= stop_2_out_click_mask, face_size= stop_2_out_face_size)
stop_2_out_meta_action = Meta_Action(vision_object = stop_2_out_vision, action_object = stop_2_out_action, threshold = STOP_2_OUT_THRESHOLD, name = 'stop_2_out', look_timeout = 3)


#stop 3 out
#stop_3_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out_vision_mask.png', cv.IMREAD_COLOR)
stop_3_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_3_out_vision_mask)
stop_3_out_face_size = [30,32]
stop_3_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out_click_mask.png',0)
stop_3_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_out.png', click_mask= stop_3_out_click_mask, face_size= stop_3_out_face_size)
stop_3_out_meta_action = Meta_Action(vision_object = stop_3_out_vision, action_object = stop_3_out_action, threshold = STOP_3_OUT_THRESHOLD, name = 'stop_3_out', look_timeout = 3)

#stop 4 out
stop_4_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out_vision_mask.png', cv.IMREAD_COLOR)
stop_4_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=stop_4_out_vision_mask)
stop_4_out_face_size = [28,40]
stop_4_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out_click_mask.png',0)
stop_4_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_out.png', click_mask= stop_4_out_click_mask, face_size= stop_4_out_face_size)
stop_4_out_meta_action = Meta_Action(vision_object = stop_4_out_vision, action_object = stop_4_out_action, threshold = STOP_4_OUT_THRESHOLD, name = 'stop_4_out', look_timeout = 3)

#boat out
#boat_out_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out_vision_mask.png', cv.IMREAD_COLOR)
boat_out_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=boat_out_vision_mask)
boat_out_face_size = [27,44]
boat_out_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out_click_mask.png',0)
boat_out_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out.png', click_mask= boat_out_click_mask, face_size= boat_out_face_size)
boat_out_meta_action = Meta_Action(vision_object = boat_out_vision, action_object = boat_out_action, threshold = BOAT_OUT_THRESHOLD, name = 'boat_out', look_timeout = 3)


#boat out check
boat_out_check_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_out_check.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)
boat_out_check_meta_action = Meta_Action(vision_object = boat_out_check_vision, threshold = BOAT_OUT_CHECK_THRESHOLD, name = 'boat_out_check', look_timeout = 3)

#worm prep
worm_prep_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep_vision_mask.png', cv.IMREAD_COLOR)
worm_prep_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=worm_prep_vision_mask)
worm_prep_face_size = [20,20]
worm_prep_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep_click_mask.png',0)
worm_prep_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_prep.png', click_mask= worm_prep_click_mask, face_size= worm_prep_face_size)
worm_prep_meta_action = Meta_Action(vision_object = worm_prep_vision, action_object = worm_prep_action, threshold = WORM_PREP_THRESHOLD, name = 'worm_prep', look_timeout = 3)
#(scroll 30 clicks in between calling prev and next actions and open inv. tab)

#worm_source
worm_source_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source_vision_mask.png', cv.IMREAD_COLOR)
worm_source_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=worm_source_vision_mask)
worm_source_face_size = [9,9]
worm_source_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source_click_mask.png',0)
worm_source_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\worm_source.png', click_mask= worm_source_click_mask, face_size= worm_source_face_size)
worm_source_meta_action = Meta_Action(vision_object = worm_source_vision, action_object = worm_source_action, threshold = WORM_SOURCE_THRESHOLD, name = 'worm_source', look_timeout = 3)

#inv_worm
inv_worm_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm_vision_mask.png', cv.IMREAD_COLOR)
inv_worm_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=inv_worm_vision_mask)
#inv_worm_face_size = [48,93]
#inv_worm_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\inv_worm_click_mask.png',0)

#scrol 30 clicks out between calling prve and next actions and close inv. tab)

#boat in
boat_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in_vision_mask.png', cv.IMREAD_COLOR)
boat_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=boat_in_vision_mask)
boat_in_face_size = [37,25]
boat_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in_click_mask.png',0)
boat_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\boat_in.png', click_mask= boat_in_click_mask, face_size= boat_in_face_size)
boat_in_meta_action = Meta_Action(vision_object = boat_in_vision, action_object = boat_in_action, threshold = BOAT_IN_THRESHOLD, name = 'boat_in', look_timeout = 3)

#stop 4 in
#stop_4_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in_vision_mask.png', cv.IMREAD_COLOR)
stop_4_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_4_in_vision_mask)
stop_4_in_face_size = [34,34]
stop_4_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in_click_mask.png',0)
stop_4_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_4_in.png', click_mask= stop_4_in_click_mask, face_size= stop_4_in_face_size)
stop_4_in_meta_action = Meta_Action(vision_object = stop_4_in_vision, action_object = stop_4_in_action, threshold = STOP_4_IN_THRESHOLD, name = 'stop_4_in', look_timeout = 3)

#stop 3 in
#stop_3_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in_vision_mask.png', cv.IMREAD_COLOR)
stop_3_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_3_in_vision_mask)
stop_3_in_face_size = [31,22]
stop_3_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in_click_mask.png',0)
stop_3_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_3_in.png', click_mask= stop_3_in_click_mask, face_size= stop_3_in_face_size)
stop_3_in_meta_action = Meta_Action(vision_object = stop_3_in_vision, action_object = stop_3_in_action, threshold = STOP_3_IN_THRESHOLD, name = 'stop_3_in', look_timeout = 3)

#stop 2 in
#stop_2_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in_vision_mask.png', cv.IMREAD_COLOR)
stop_2_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_2_in_vision_mask)
stop_2_in_face_size = [53,31]
stop_2_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in_click_mask.png',0)
stop_2_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_2_in.png', click_mask= stop_2_in_click_mask, face_size= stop_2_in_face_size)
stop_2_in_meta_action = Meta_Action(vision_object = stop_2_in_vision, action_object = stop_2_in_action, threshold = STOP_2_IN_THRESHOLD, name = 'stop_2_in', look_timeout = 3)

#stop 1 in
#stop_1_in_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in_vision_mask.png', cv.IMREAD_COLOR)
stop_1_in_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR)#, search_mask=stop_1_in_vision_mask)
stop_1_in_face_size = [28,21]
stop_1_in_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in_click_mask.png',0)
stop_1_in_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\stop_1_in.png', click_mask= stop_1_in_click_mask, face_size= stop_1_in_face_size)
stop_1_in_meta_action = Meta_Action(vision_object = stop_1_in_vision, action_object = stop_1_in_action, threshold = STOP_1_IN_THRESHOLD, name = 'stop_1_in', look_timeout = 3)

#bank prep
bank_prep_vision_mask= cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep_vision_mask.png', cv.IMREAD_COLOR)
bank_prep_vision= Vision('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep.png', method = cv.TM_CCOEFF_NORMED, imread = cv.IMREAD_COLOR, search_mask=bank_prep_vision_mask)
bank_prep_face_size = [14,11]
bank_prep_click_mask = cv.imread('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep_click_mask.png',0)
bank_prep_action = Action('C:\\Users\\Jeff C\\Downloads\\Code\\OpenCV files\\king worm\\image library\\bank_prep.png', click_mask= bank_prep_click_mask, face_size= bank_prep_face_size)
bank_prep_meta_action = Meta_Action(vision_object = bank_prep_vision, action_object = bank_prep_action, threshold = BANK_PREP_THRESHOLD, name = 'bank_prep', look_timeout = 3)




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
BOAT_OUT_CHECK_THRESHOLD = .8

OFFSCREEN_POINT = [383,825]

worm_time_mean = np.random.uniform(.2,.7)
worm_time_stddev = np.random.uniform(.2,.5)
print('worm_time_mean %s | worm_time_stddev %s' %(worm_time_mean, worm_time_stddev))

    
#enter the bank from the bankprep position
print('entering bank from bankprep position')
banking = bank_meta_action.look_click_color()
in_banking = in_bank_meta_action.look_color()

if in_banking == 'timeout':
    print('in_bank search timeout. attempting bank relick')
    banking = bank_meta_action.look_click_color()

in_banking = in_bank_meta_action.look_color()
if in_banking == 'timeout':
    print('in_banking timeout 2rd time. tried moving mouse and reclicking bank, no good. exitting...')
    exit()

#dump your stuff
print('depositing worms')
bank_dumping = bank_dump_meta_action.look_click_color()
if bank_dumping == 'timeout':
    print('bank_dump search timeout. moving mouse offscreen to reveal obscured objects')
    bank_action.moveTo(OFFSCREEN_POINT)

bank_dumping = bank_dump_meta_action.look_click_color()
if bank_dumping == 'timeout':
    print('bank_dump search timeout second time. somethings up, quitting')
    exit()

#wait a bit, get out of the bank
time.sleep(.06 + abs(np.random.normal(0,.3)))
print('exiting bank')
key_press('esc')


#go from bank prep to stop 1
print('travelling bank_prep to stop_1_out')
stop_1_outing = stop_1_out_meta_action.look_click_color()
if stop_1_outing == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go from stop 1 to stop 2
print('travelling stop_1_out to stop_2_out')
stop_2_outing = stop_2_out_meta_action.look_click_color()
if stop_2_outing == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go from stop 2 to stop 3
print('travelling stop_2_out to stop_3_out')
stop_3_outing = stop_3_out_meta_action.look_click_color()
if stop_3_outing == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go from stop 3 to stop 4
print('travelling stop_3_out to stop_4_out')
stop_4_outing = stop_4_out_meta_action.look_click_color()
if stop_4_outing == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go from stop 4 to boat out
print('travelling stop_4_out to boat_out')
boat_outing = boat_out_meta_action.look_click_color()
if boat_outing == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to worm prep
print('travelling to worm_prep')
worm_prepping = worm_prep_meta_action.look_click_color()
if worm_prepping == 'timeout':
    print('exitting because of timeout')
    exit()

#open inventory
key_press('f1')
print('opening inventory to observe inv_worms')

#time.sleep(? + abs(np.random.normal(0,!)))


#check for num worms before clicking worms
screenshot = wincap.get_screenshot() 
inv_worm_allPoints, inv_worm_bestPoint, inv_worm_confidence = inv_worm_vision.find(screenshot, threshold = INV_WORM_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()

old_num_worms = len(inv_worm_allPoints)
if old_num_worms != 0:
    print('small trouble: I see %s inv_worms before clicking any worm_source' % old_num_worms)

else: print('I see %s worms as expected' % old_num_worms)



#click the worm source
print('clicking the worm source')
worm_sourcing = worm_source_meta_action.look_click_color()
if worm_sourcing == 'timeout':
    print('exitting because of timeout')
    exit()
#wait a second to see if we got a worm
#time.sleep(? + abs(np.random.normal(0,!)))

#checking for change in number of inv_worms
print('looking for new worms')
screenshot = wincap.get_screenshot() 
inv_worm_allPoints, inv_worm_bestPoint, inv_worm_confidence = inv_worm_vision.find(screenshot, threshold = INV_WORM_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
if cv.waitKey(1) == ord('q'):
    cv.destroyAllWindows()
    exit()

new_num_worms = len(inv_worm_allPoints)

if new_num_worms == old_num_worms:
    print('big trouble: I see %s worms, same as before I clicked the worm source' % new_num_worms)

elif new_num_worms > old_num_worms: 
    print('good news: I see %s worms now.  before I saw %s. beginning worm click cycle' %(new_num_worms, old_num_worms))

#worm click cycle
start_time = time.time()
while new_num_worms < old_num_worms + 28:
    screenshot = wincap.get_screenshot() 
    inv_worm_allPoints, inv_worm_bestPoint, inv_worm_confidence = inv_worm_vision.find(screenshot, threshold = INV_WORM_THRESHOLD, debug_mode= 'rectangles', return_mode = 'allPoints + bestPoint + confidence')
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        exit()
    new_num_worms = len(inv_worm_allPoints)
    time.sleep(.1+ abs(np.random.normal(worm_time_mean,worm_time_stddev)))
    pyautogui.click()
    if time.time() - start_time > MAX_WORM_CLICK_TIME:
        print('worm click timed out after  %ss | I see %s inv_worms | breaking worm click loop but not quitting' %(time.time()- start_time, len(new_num_worms)))
        break

#go to boat_in
print('travelling worm_source to boat_in')
boat_inning = boat_in_meta_action.look_click_color()
if boat_inning == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to stop_4_in
print('travelling boat_in to stop_4_in')
stop_4_inning = stop_4_in_meta_action.look_click_color()
if stop_4_inning == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to stop_3_in
print('travelling stop_4_in to stop_3_in')
stop_3_inning = stop_3_in_meta_action.look_click_color()
if stop_3_inning == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to stop_2_in
print('travelling stop_3_in to stop_2_in')
stop_2_inning = stop_3_in_meta_action.look_click_color()
if stop_2_inning == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to stop_1_in
print('travelling stop_2_in to stop_1_in')
stop_1_inning = stop_1_in_meta_action.look_click_color()
if stop_1_inning == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))

#go to bank_prep
print('travelling from stop_1_in to bank_prep')
bank_prepping = bank_prep_meta_action.look_click_color()
if bank_prepping == 'timeout':
    print('exitting because of timeout')
    exit()
#time.sleep(? + abs(np.random.normal(0,!)))
