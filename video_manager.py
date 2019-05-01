import time, threading
from Tkinter import *
import subprocess

class Interface:
	def __init__(self):
		#threading.Thread.__init__(self)
		self.attrib1 = "Attrib from Interface class"
		#Main Window
		self.mainWindow = Tk()
		self.mainWindow.geometry("200x200")
		self.mainWindow.title("My GUI Title")
		self.mainWindow.protocol("WM_DELETE_WINDOW", self.quit)
		self.mainWindow.attributes('-fullscreen', True)
		#Label
		lbCommand = Label(self.mainWindow, text="Hello world", font=("Courier New", 16)).place(x=20, y=20)
		populate(self)
		self.mainWindow.mainloop()

	def update(self):
		self.mainWindow.destroy()
		self.mainWindow.quit()
		t = Interface()

	def quit(self):
		self.mainWindow.destroy()
		self.mainWindow.quit()
		sys.exit(0)


def play_video(video_mkv):
	import webbrowser
	webbrowser.open(video_mkv)
	print('trying')

def convert_video(self,video_h264,video_mkv):
	print('Converting' + video_h264+ ' to '+video_mkv)
	omxprocess = subprocess.Popen(['avconv', '-i', video_h264, '-r','12', '-vcodec','copy',video_mkv], stdin=subprocess.PIPE)
	omxprocess.wait()
	try:
		omxprocess.kill()
	except:
		print('couldnt kill')
	self.update()

def delete_old_videos():
	import os
	import glob

	path_h264 = os.path.dirname(os.path.abspath(__file__))+'/h264'
	videos_h264 = glob.glob(path_h264+"/*.h264")

	format = '%Y_%m_%d_%H_%M_%S'
	from datetime import datetime

	for video in videos_h264:
		video_name = os.path.split(video)[-1] #delete path
		video_name = os.path.splitext(video_name)[0] #delete extension
		video_age = datetime.now()-datetime.strptime(video_name,format)
		if video_age.days>30:
			omxprocess = subprocess.Popen(['rm', video], stdin=subprocess.PIPE)
			print("Deleted "+video_name)

delete_old_videos()

def populate(self):
	import os
	import glob
	from functools import partial

	path = os.path.dirname(os.path.abspath(__file__))
	path_h264 = path+'/h264'
	path_mkv = path+'/mkv'

	if not os.path.exists(path_mkv):
		omxprocess = subprocess.Popen(['mkdir', '-m','777', path_mkv], stdin=subprocess.PIPE)
		#os.makedirs(path_mkv,777)

	videos_h264 = glob.glob(path_h264+"/*.h264")
	videos_mkv = glob.glob(path_mkv+"/*.mkv")
	videos = videos_h264 + videos_mkv


	videos[:] = [os.path.split(x)[-1] for x in videos] #delete path
	videos[:] = [os.path.splitext(x)[0] for x in videos] #delete extensions
	videos=list(set(videos))              #eliminate duplicates
	videos.sort(reverse = True)

	buttons = list()
	i=0

	action_with_arg = partial(self.quit)
	buttons.append(Button(self.mainWindow,height=3, width=30,text="BACK", command=action_with_arg))
	buttons[-1].grid(row=i,column=0)
	i=i+1

	for video in videos:
		video_h264 = path_h264+"/"+video+".h264"
		video_mkv = path_mkv+"/"+video+".mkv"

		action_with_arg = partial(play_video,video_mkv)
		buttons.append(Button(self.mainWindow,height=1, width=30,text=video, command= action_with_arg))
		if not os.path.isfile(video_mkv):
			buttons[-1]['state']='disabled'
		buttons[-1].grid(row=i,column=0)

		action_with_arg = partial(convert_video,self,video_h264,video_mkv)
		buttons.append(Button(self.mainWindow,height=1, width=5,text="Convert", command= action_with_arg))
		if os.path.isfile(video_mkv):
			buttons[-1]['state']='disabled'
		buttons[-1].grid(row=i,column=1)

		i=i+1