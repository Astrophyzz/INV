#!/opt/anaconda/bin/python
'''
from Tkinter import *
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.backend_bases import key_press_handler
#from matplotlib.figure import Figure
#read the data file to a list of dictionaries, night
#each dictionary holds the line in the *cal.tab file
#this is a more structured way to hold the data in the file
def dude(target,flt):
	night=[]
	filename=target+'.'+flt+'cal.tab'
	with open(filename,'r') as f:
		for line in f:
			s=line.strip()			#the .tab file has funny formatting and whitespaces
			s=s.split(' ')			#and \n. clean it up so the list s contains only real data 
			s=[eval(i) for i in s if i!='']
			night.append(dict(date=s[0], jdate=s[1], mag=s[2], magerr=s[3]))

#now using the list night, lets make two seperate lists. one to hold the data for the jdate keyword
#and one to hold data for the mag keyword. Then we will make an array that holds these lists.
	maglist=[]
	jdatelist=[]
	for i in night:
		jdatelist.append(i['jdate'])
		maglist.append(i['mag'])

	jdateVmag=[jdatelist,maglist]
	return jdateVmag

#this is a little user interface to allow a user to
#enter an object name and a list of filters
#a dictionary with the object name and filter list is returned
def gatherdude():
	n=raw_input("Enter the object name \n")
	m=[]
	while True:
		s=(raw_input("Enter the filter you want data for \n"))
#the try/except block below is to handle if the user enters a filter 
#for which there is no data
		try:
			fname=n+'.'+s+'cal.tab'
			fcheck=open(fname, 'rb', 0)
			try:
				fdata=fcheck.read()
			finally:
				fcheck.close()
			m.append(s)
			q=(raw_input("Do you wish to add another filter? \nPress enter to continue or type 'no' when finished \n"))
			if q.lower() == 'no':
				break
		except IOError:
			print "there is no data for that filter. try again"

	blazar=dict(name=n, filters=m)
	return blazar

#this uses dude and gather dude. gather dude is called first
#to prompt user for target name and filters
#dude is used to collet the data of the named object for each 
#filter to a list which has a dictionary for each element.
#each dictionary has a key 'filters' which has values of 
#filters the user provided, and a key 'data' that contains
#a list of the jdate list and mag list.
def returndude():
	a=[]
	target=gatherdude()
	for i in range(0,len(target['filters'])):
		a.append(dict(flt=target['filters'][i],name=target['name'],data=dude(target['name'],target['filters'][i])))
	return a

#does what the name implies. makes a multiplot of the data
#one column and one row per filter selected.
#doesnt return anything, or take any inputs. It runs returndude()
#returndude() calls gatherdude() and dude() which prompt user for input
#see above for more about *dude
def makeplot():
	import matplotlib.pyplot as plt
	targetdata=returndude()
	for i in range(0,len(targetdata)):
		targetdata[i]['data'][0]=[(j-2400000) for j in targetdata[i]['data'][0]]
	#the for loop above subtracts 2400000 days from the dates so we can plot in MJD
	numplots=len(targetdata) #tells us how many filters there are
	plt.figure(1)
	for i in range(0,numplots):			#make a subplot for each filter
		plt.subplot(numplots,1,i+1)
		plt.plot(targetdata[i]['data'][0],targetdata[i]['data'][1], 'ro')
		plt.legend(targetdata[i]['flt'])
		plt.ylim(plt.ylim()[::-1])		#reverses the y axis since magnitudes are backwards
	plt.show()
	return

#makes a plot but now using the tk gui widgety thing
def makeplotintk():
	from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
	from matplotlib.backend_bases import key_press_handler
	from matplotlib.figure import Figure
	import Tkinter as Tk
	targetdata=returndude()
	for i in range(0,len(targetdata)):
		targetdata[i]['data'][0]=[(j-2400000) for j in targetdata[i]['data'][0]]
	numplots=len(targetdata)
#this is where its different thatn makeplot, we need to set up the tk enviornment etc
	root=Tk.Tk()
	root.wm_title(targetdata[0]['name'])
	f=Figure(figsize=(10,8))
	for i in range(0,numplots):
		a=f.add_subplot(3,1,i+1)
		a.plot(targetdata[i]['data'][0],targetdata[i]['data'][1], 'ro')
		a.axes.invert_yaxis()
		a.legend(targetdata[i]['flt'])
	canvas=FigureCanvasTkAgg(f, master=root)
	canvas.show()
	canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#now to add the cool widget bar
	toolbar = NavigationToolbar2TkAgg( canvas, root )
	toolbar.update()
	canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
	Tk.mainloop()
	return
'''

'''
----------------------------------------------------------------------------------------------------------------------
'''

from Tkinter import *

def dude(target,flt):
	night=[]
	filename=target+'.'+flt+'cal.tab'
	with open(filename,'r') as f:
		for line in f:
			s=line.strip()			#the .tab file has funny formatting and whitespaces
			s=s.split(' ')			#and \n. clean it up so the list s contains only real data 
			s=[eval(i) for i in s if i!='']
			night.append(dict(date=s[0], jdate=s[1], mag=s[2], magerr=s[3]))

#now using the list night, lets make two seperate lists. one to hold the data for the jdate keyword
#and one to hold data for the mag keyword. Then we will make an array that holds these lists.
	maglist=[]
	jdatelist=[]
	for i in night:
		jdatelist.append(i['jdate'])
		maglist.append(i['mag'])

	jdateVmag=[jdatelist,maglist]
	return jdateVmag

def returndudetk(blazar, fltlist):
	a=[]
	target=dict(name=blazar, filters=fltlist)
	for i in range(0,len(target['filters'])):
		a.append(dict(flt=target['filters'][i],name=target['name'],data=dude(target['name'],target['filters'][i])))
	return a

def makeplottk(targetdata):
	from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
	from matplotlib.backend_bases import key_press_handler
	from matplotlib.figure import Figure
	for i in range(0,len(targetdata)):
		targetdata[i]['data'][0]=[(j-2400000) for j in targetdata[i]['data'][0]]
	numplots=len(targetdata)
#this is where its different thatn makeplot, we need to set up the tk enviornment etc
	root=Tk()
	root.wm_title(targetdata[0]['name'])
	f=Figure(figsize=(10,8))
	for i in range(0,numplots):
		a=f.add_subplot(numplots,1,i+1)
		a.plot(targetdata[i]['data'][0],targetdata[i]['data'][1], 'ro')
		a.axes.invert_yaxis()
		a.legend(targetdata[i]['flt'])
	canvas=FigureCanvasTkAgg(f, master=root)
	canvas.show()
	canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
#now to add the cool widget bar
	toolbar = NavigationToolbar2TkAgg( canvas, root )
	toolbar.update()
	canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
	mainloop()
	return

def userbox():
	fieldnames = ('Target name', 'Filters')
	global entries
	window=Tk()
	window.title('Blazar data querry')
	#this form bit is so that all the other crap below knows
	#they all operate under the variable 'window'
	form = Frame(window)
	labels = Frame(form)	#text on side of window
	values = Frame(form)	#text box for user input
	labels.pack(side=LEFT)
	values.pack(side=RIGHT)
	form.pack()
	entries={}
	for label in fieldnames:
		Label(labels, text=label).pack(expand=YES, fill=BOTH)
		ent = Entry(values)
		ent.pack(expand=YES, fill=BOTH)
		entries[label] = ent
	#Button(window, text="echo", command=(lambda: reply(entries['Target name'].get(),entries['Filters'].get()))).pack(side=LEFT)
	Button(window, text='get plots', command=(lambda: showplot(entries['Target name'].get(),entries['Filters'].get()))).pack(side=BOTTOM)
	Label(window, text="for multiple filters, seperate by comma and space. i.e. B, V, R").pack()
	mainloop()
	return window

def reply(firstbro,secondbro):
	#from Tkinter import *
	replyspace=Tk()
	replyspace.title('Replies from Blazar data querry')
	Label(replyspace, text='Target name :'+ firstbro).pack()
	Label(replyspace, text='Filters selected :'+ secondbro).pack()
	
def showplot(blazar, inlist):
	fltlist=inlist.split(', ')
	targetdata=returndudetk(blazar, fltlist) 
	makeplottk(targetdata)
