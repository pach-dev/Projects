# Automate WebBrowsers to open Automatically

import webbrowser
#import os # inbuil function in python used to open a particular file 

def workauto():
	#app_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
	#os.startfile(app_path)# an os function that opens the file assigned
	#ChromePath = 'C:/Users/Pach/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/chrome.exe %s'
	urls_to_open = ("https://op.stariboss.com/portal-ui/index?co=ke&lang=en","https://web.whatsapp.com/","geeksforgeeks.org ")

	#for url in urls_to_open: # for loop loops through the urls to open
	webbrowser.open(urls_to_open) # gets the Chrome's path and opens the urls
#print ('Your Daily Working browsers and textfile opened, Sir!: ')
workauto()

