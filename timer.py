import time
import ctypes
import os
from easygui import msgbox
from playsound import playsound
from pynput.keyboard import Key, Listener

state = {
	"sound_list" : [f for f in os.listdir("./beeps")
			 if os.path.isfile(os.path.join("./beeps",f)) and f.endswith("wav")],
	"minutes" : 0,
	"mode" : 0,
	"sound_index": 0,
	}

def start():
	message =""" <<<<<<<<<< OPTIONS >>>>>>>>>>
	(1): Timer Mode
	(2): Select Sound
	(3): Exit"""
	print(message)
	state["mode"] = int(input("Enter your choice: "))
	if(state["mode"] == 1):
		timer()
	elif(state["mode"] == 2):
		choose_beep()
	elif(state["mode"] == 3):
		quit()
	else:
		print('Please enter proper Mode.')
	start()

def timer():
	try:
		state["minutes"] = int(input("Enter number of minute(s) to start: "))
		iMins = 0
		if state["minutes"] <= 0:
			raise ValueError('Please provide positive values.')
		elif state["minutes"] > 0:
			while iMins != state["minutes"]:
				print(iMins, end=" ")
				time.sleep(60)
				iMins += 1
			playsound('./beeps/'+state["sound_list"][state["sound_index"]])
			msgbox('{} minute(s) are completed.'.format(state["minutes"]))
	except:
		print("Please enter proper numeric value.")

def on_press(key):
	l = len(state["sound_list"])
	if (key == Key.right):
		state["sound_index"] = 0 if (state["sound_index"]+1 == l) else (state["sound_index"]+1)
		playsound('./beeps/'+state["sound_list"][state["sound_index"]])
	elif (key == Key.left):
		state["sound_index"] = (l-1) if (state["sound_index"]-1 < 0) else (state["sound_index"]-1)
		playsound('./beeps/'+state["sound_list"][state["sound_index"]])
	elif (key == Key.space):
		return False

def choose_beep():
	message="""<<<<<<<<<< INSTRUCTIONS >>>>>>>>>>
- Use Left and Right arrow keys to navigate.
- Press Escape to select the current sound."""
	print(message)
	print('./beeps/'+state["sound_list"][state["sound_index"]])
	with Listener(
        on_press=on_press,
        on_release=None) as listener:
		listener.join()
start()
