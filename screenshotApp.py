
import pyautogui
import time
import tkinter as tk


def screenshot():
	time.sleep(3) #Delay for 3 seconds
	name = time.time()
	name = "D:/UBCD/Cyber sec_Python scripts/ScreenShots/{}.png".format(name)
	img = pyautogui.screenshot() # grabs a screenshot using the pythonautogui
	img.save(name)#saves the captured image
	img.show() #displays the captured screenshot

#print("ScreenShot Successful")

#screenshot()
#USING TKINTER GUI TO DEVELOP AN APP THAT TAKE A SCREENSHOT

root = tk.Tk()# initalize a variable root and call the tinker function
frame = tk.Frame(root)# gives frame to our GUI app with the argument root
frame.pack()# displays the frame


button = tk.Button(frame,text="Click 2 ScreenShot", command=screenshot)#Displays the Take screenshot button.
button.pack(side=tk.LEFT)# Displays the button to the left side

close = tk.Button(frame,text="Quit", command=quit)
close.pack(side=tk.RIGHT)

root.mainloop()
