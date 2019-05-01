def touch(preview):
	import struct
	import time
	import sys

	infile_path = "/dev/input/event0"
	FORMAT = 'llHHI'
	EVENT_SIZE = struct.calcsize(FORMAT)
	in_file = open(infile_path, "rb")
	event = in_file.read(EVENT_SIZE)

	x=0
	y=0
	global screen_w
	global screen_h

	touchscreen_res=4000
	last_touch = 0

	while event:
		(tv_sec, tv_usec, typee, code, value) = struct.unpack(FORMAT, event)
		if typee != 0 or code != 0 or value != 0:
			#print("valid touch")
			#print("Event typee %u, code %u, value %u at %d.%d" % \
			#(typee, code, value, tv_sec, tv_usec)
			if typee==3:																	#is it a valid touch input
				if code==0:
					x=value
					x = int( float(x)/float(touchscreen_res)*float(screen_w) )        			#convert from touch to pixel
				if code==1:
					y=value
					y = int( float(y)/float(touchscreen_res)*float(screen_h) )         		#convert from touch to pixel
				if x!=0 and y!=0:														#we got a VALID TOUCH INPUT
					tv_sec_usec = tv_sec*1000000+tv_usec
					global minimized
					if minimized:
						if touch_is_in_button(renderer_rec,x,y):
							minimize(False)
					global dragging
					detect_drag(last_touch,tv_sec_usec,x,y)								#is it dragging?
					if dragging:
						reposition_preview(x,y+40)
					if camera.preview.fullscreen:
						if detect_double_tap(tv_sec_usec): 								#if it's full screen
							exit_full_screen()
					elif touch_is_in_camera(preview,x,y): 									#is also inside the window
						if is_first_touch(last_touch,tv_sec_usec):
							if touch_is_in_button(renderer_button1,x,y):
								button1()
							if touch_is_in_button(renderer_button2,x,y):
								button2()
							elif touch_is_in_button(renderer_button3,x,y):
								button3()
							else:
								show_button(renderer_button1,True)
								show_button(renderer_button2,True)
								show_button(renderer_button3,True)
					else:
						show_button(renderer_button1,False)
						show_button(renderer_button2,False)
						show_button(renderer_button3,False)
					x=0
					y=0
					last_touch=tv_sec_usec

		event = in_file.read(EVENT_SIZE)
	in_file.close()

clicked = 0
clicktime = 0
def detect_double_tap(tv_sec_usec):
	global clicked
	global clicktime
	clickdelay = 0.5
	clicked=clicked+1
	if clicked == 1:
		clicktime = tv_sec_usec;
	if (clicked > 1) and (100000 < tv_sec_usec - clicktime < clickdelay*1000000):
		clicked = 0
		clicktime = 0
		print("Double CLick")
		return True
	elif (clicked > 2) or (tv_sec_usec - clicktime > 1):
		clicked = 0
	return False

first_x = 0
first_y = 0
dragging = False

def is_first_touch(last_touch,tv_sec_usec):
	return tv_sec_usec-last_touch>50000

def detect_drag(last_touch,tv_sec_usec,x,y):
	#dragging=False
	global first_x
	global first_y
	global dragging
	if is_first_touch(last_touch,tv_sec_usec):
		first_x=x
		first_y=y
		dragging =False

	if (first_x-x)*(first_x-x) + (first_y-y)*(first_y-y) > 80*80:
		if touch_is_in_camera(renderer_preview,first_x,first_y):
			dragging = True

def touch_is_in_button(preview,x,y):
	margin=10
	if preview.window[0]-margin < x < preview.window[0]+preview.window[2] + margin:
		if preview.window[1]-margin < y < preview.window[1] +preview.window[3] + margin:
			return 1
	return 0

def touch_is_in_camera(preview,x,y):
	margin=0
	if preview.window[0]-margin < x < preview.window[0]+preview.window[2] + margin:
		if preview.window[1]-margin < y < preview.window[1]+preview.window[3] + margin:
			return 1
	return 0

def reposition_preview(x,y):
	buttton_size = 50
	adjust=15

	renderer_preview.window = (x-renderer_preview.window[2]/2, y-renderer_preview.window[3]/2, renderer_preview.window[2], renderer_preview.window[3])
	renderer_rec.window = renderer_preview.window[0]+adjust, renderer_preview.window[1]+adjust, renderer_rec.window[2], renderer_rec.window[3]

	buttons_y = renderer_preview.window[1]+renderer_preview.window[3]-buttton_size-adjust
	renderer_button1.window = renderer_preview.window[0]+adjust, buttons_y,renderer_button1.window[2], renderer_button1.window[3]
	renderer_button2.window = renderer_preview.window[0]+renderer_preview.window[2]/2-renderer_button2.window[2]/2, buttons_y, renderer_button2.window[2], renderer_button2.window[3]
	renderer_button3.window = renderer_preview.window[0]+renderer_preview.window[2]-renderer_button3.window[2]-15, buttons_y, renderer_button2.window[2], renderer_button2.window[3]

def button1():
	print('button1')
	minimize(True)

def button2():
	print('button 2')
	enter_full_screen()

def button3():
	print('button 3')
	action_with_arg = partial(open_video_manager)
	t3 = threading.Thread(target=action_with_arg)
	t3.start()
from video_manager import *
def open_video_manager():
	print('button 3')
	t = Interface()

global minimized
minimized = False
def minimize(state):
	if state:
		icon_size = 30
		icon_offset=20
		renderer_preview.window = (0,0,0,0)
		renderer_rec.window = screen_w-icon_size-icon_offset, icon_offset, icon_size, icon_size
		global minimized
		minimized = True
	else:
		global renderer_preview_size
		renderer_preview.window = renderer_preview_size
		reposition_preview(screen_w-renderer_preview_size[2]/2,renderer_preview_size[3]/2)
		minimized = False

def enter_full_screen():
	print('enter full screen')
	camera._set_preview_fullscreen(True)
	camera._set_preview_alpha(255)
	show_button(renderer_rec,False)
	show_button(renderer_button1,False)
	show_button(renderer_button2,False)
	show_button(renderer_button3,False)

def exit_full_screen():
	camera._set_preview_fullscreen(False)
	camera._set_preview_alpha(100)
	show_button(renderer_button1,True)
	show_button(renderer_button2,True)
	show_button(renderer_button3,True)

def show_button(renderer,state):
	if state:
		renderer.window = renderer.window[0],renderer.window[1],renderer.window[2],renderer.window[2]
	else:
		renderer.window = renderer.window[0],renderer.window[1],renderer.window[2],0

def timestamp(camera):
	camera.start_recording(path_h264+"/"+start_now_string+".h264")
	while (dt.datetime.now() - start_now).seconds < recording_length:
		camera.annotate_text = dt.datetime.now().strftime(format)

		#blink button
		if not camera.preview.fullscreen:
			if renderer_rec.window[3]!=0:
				show_button(renderer_rec,False)
			else:
				show_button(renderer_rec,True)

		camera.wait_recording(1)
	print("stop")
	camera.stop_recording()
	camera.close()
	if record_on_loop:
		timestamp(camera)
	else:
		quit()

global screen_w
global screen_h
global renderer_preview_size
global record_on_loop

######CHANGE THESE VARIABLES FOR CUSTOMIZATION#####
screen_w=800
screen_h=400
recording_length=1*60*60;
recording_length=10;
cam_resolution=(960,720)
renderer_preview_size=250
start_minimized = True
record_on_loop = True
#################################




import picamera
camera = picamera.PiCamera(resolution=cam_resolution, framerate=12)
format = '%Y_%m_%d_%H_%M_%S'

import os
import subprocess
path = os.path.dirname(os.path.abspath(__file__))
path_h264 = path+'/h264'
if not os.path.exists(path_h264):
	omxprocess = subprocess.Popen(['mkdir', '-m','777', path_h264], stdin=subprocess.PIPE)

import datetime as dt
import time
camera.annotate_background = picamera.Color('black')
start_now = dt.datetime.now()
start_now_string = dt.datetime.now().strftime(format)
camera.annotate_text = start_now_string
ratio = float(cam_resolution[0])/float(cam_resolution[1])
renderer_preview_size=100,100,renderer_preview_size,int(renderer_preview_size/ratio)
renderer_preview=camera.start_preview(fullscreen=False, window = renderer_preview_size, alpha=200)

buttton_size = 50
from PIL import Image

img_rec = Image.open(path+'/icons/ico_recording.png')
renderer_rec = picamera.PiOverlayRenderer(camera, img_rec.tobytes(), img_rec.size,format=None,fullscreen=False,window = (0,0,25,25),layer=5,alpha=255)
img_button1 = Image.open(path+'/icons/ico_down.png')
renderer_button1 = picamera.PiOverlayRenderer(camera, img_button1.tobytes(), img_button1.size,format=None,fullscreen=False,window = (0,0,buttton_size,buttton_size),layer=5,alpha=255)
img_button2 = Image.open(path+'/icons/ico_full.png')
renderer_button2 = picamera.PiOverlayRenderer(camera, img_button2.tobytes(), img_button2.size,format=None,fullscreen=False,window=(0,0,buttton_size,buttton_size),layer=5,alpha=255)
img_button3 = Image.open(path+'/icons/ico_play.png')
renderer_button3 = picamera.PiOverlayRenderer(camera, img_button3.tobytes(), img_button3.size,format=None,fullscreen=False,window=(0,0,buttton_size,buttton_size),layer=5,alpha=255)


time.sleep(.5)
reposition_preview(screen_w-renderer_preview_size[2]/2,renderer_preview_size[3]/2)

show_button(renderer_button1,False)
show_button(renderer_button2,False)
show_button(renderer_button3,False)

if start_minimized:
	minimize(True)


import threading
from multiprocessing import Queue
from functools import partial
import time

if __name__ == '__main__':
	action_with_arg = partial(timestamp,camera)
	t1 = threading.Thread(target=action_with_arg)
	t1.start()
	#action_with_arg = partial(touch,renderer_preview)
	#t2 = threading.Thread(target=action_with_arg)
	#t2.start()
	touch(renderer_preview)