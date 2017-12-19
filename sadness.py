import time
import tkinter
from tkinter import *
import datetime as dt
import tkinter.messagebox

monthly_wage = 0
days_field = 0
days_normal = 0
hours_normal = 0
fixed_expenses = 0
hourly = 0
minutely = 0
secondly = 0
real_secondly = 0
s = "0:00"
hour, minute = s.split(':')
hour = 0
minute = 0

def retrieve_input():
	global entry1
	global entry2
	global entry3
	global entry4
	global entry5
	global entry6
	global monthyly_wage
	global days_field
	global days_normal
	global hours_normal
	global fixed_expenses
	global hourly
	global minutely
	global secondly
	global real_secondly
	global real_minutely
	global real_hourly
	global real_seconds
	global hour
	global minute
	monthly_wage = entry1.get()
	days_field = entry2.get()
	days_normal = entry3.get()
	hours_normal = entry4.get()
	fixed_expenses = entry5.get()
	s = entry6.get()
	hour, minute = s.split(':')
	hour = int(hour)
	minute = int(minute)
	normal_hours = int(days_normal) * int(hours_normal)
	field_hours = int(days_field) * 24
	total_hours = int(field_hours) + int(normal_hours)
	hourly = int(monthly_wage) / total_hours
	minutely = hourly / 60
	secondly = minutely / 60
	micro_secondly = secondly / 60 # This is to make it go faster
	leftover = int(monthly_wage) - int(fixed_expenses)
	real_hourly = leftover / total_hours
	real_minutely = real_hourly / 60
	real_secondly = real_minutely / 60
	real_micro_secondly = real_secondly /60 # This is to make it go faster


def main_window():
	global root
	root = Tk()
	root.wm_title("What you actually make.")
	frame = Frame(root)
	frame.pack()


def set_frames():
	global topframe
	global bottomframe
	topframe = Frame(root, width=500, height=300)
	topframe.pack()
	bottomframe= Frame(root, width=500, height=300)
	bottomframe.pack()


def quit_window():
	global root
	avghour.grid_forget()
	avgminute.grid_forget()
	root.destroy()
	exit()


def set_top_frame():
	global entry1
	global entry2
	global entry3
	global entry4
	global entry5
	global entry6
	mainlabel = Label(topframe, text="This is the sadness of your job...", font="Times 20")
	mainlabel.grid(row=0, columnspan=2)
	space = Label(topframe, text=" ")
	space.grid(row=1)
	monthwage = Label(topframe, text="What is your monthly wage from LES?")
	monthwage.grid(row=2, column=0, sticky=E)
	entry1 = Entry(topframe)
	entry1.grid(row=2, column= 1)
	fielddays = Label(topframe, text="How many days are you in the field this month?")
	fielddays.grid(row=3, column=0, sticky=E)
	entry2 = Entry(topframe)
	entry2.grid(row=3, column=1)
	officedays = Label(topframe, text="How many days are you in the office this month?")
	officedays.grid(row=4, column=0, sticky=E)
	entry3 = Entry(topframe)
	entry3.grid(row=4, column=1)
	hoursnormal = Label(topframe, text="How many hours do you work on a normal day?")
	hoursnormal.grid(row=5, column=0, sticky=E)
	entry4 = Entry(topframe)
	entry4.grid(row=5, column=1)
	fixedexpenses = Label(topframe, text="What are your monthly fixed expenses?")
	fixedexpenses.grid(row=6, column=0, sticky=E)
	entry5 = Entry(topframe)
	entry5.grid(row=6, column=1)
	worktime = Label(topframe, text="What time did you start work today (H:MM)?")
	worktime.grid(row=7, column=0, sticky=E)
	entry6 = Entry(topframe)
	entry6.grid(row=7, column=1)
	button1 = Button(topframe, text="Update my Values", command=retrieve_input)
	button1.grid(row=9, columnspan=2)
	button2 = Button(topframe, text="Run", command=set_bottom_frame)
	button2.grid(row=10, columnspan=2)
	button3= Button(topframe, text="Quit", command=quit_window)
	button3.grid(row=11, columnspan=2)


def delete_live():
	global totalmoney
	global realmoney
	global avghour
	global avgminute
	global avgsec
	avghour.destroy()
	avgminute.destroy()
	avgsec.destroy()
	totalmoney.destroy()
	realmoney.destroy()
	
	
def set_bottom_frame():
	global hourly
	global minutely
	global secondly
	global real_seconds
	global secondly
	global real_secondly
	global hour
	global minute
	global stop
	global now
	global b
	global totalmoney
	global realmoney
	global avghour
	global avgminute
	global avgsec

	stop = time.clock()
	now = dt.datetime.now()
	b = dt.datetime(now.year,now.month,now.day,hour,minute,00)
	real_seconds = (now - b).total_seconds()
	avghourtext = ("Your average hourly wage is $" + str(hourly))
	avghour = Label(bottomframe, text=avghourtext, font="Times 14")
	avghour.grid(row=1, columnspan=2)
	avgmintext = ("Your average minutely wage is $" + str(minutely))
	avgminute = Label(bottomframe, text=avgmintext, font="Times 14")
	avgminute.grid(row=2, columnspan=2)
	avgsectext = ("Your average secondly wage is $" + str(secondly))
	avgsec = Label(bottomframe, text=avgsectext, font="Times 14")
	avgsec.grid(row=3, columnspan=2)
	totalmoneytext= StringVar()
	totalmoneytext.set ("You've made $" + ("%.6f" % (((int(real_seconds)) * secondly))) + " so far today.")
	totalmoney = Label(bottomframe, textvariable=totalmoneytext, bg='light green', font="Times 16 bold")
	totalmoney.grid(row=4, columnspan=2, sticky=W+E)
	realmoneytext= StringVar()
	realmoneytext.set ("You've made $" + ("%.6f" %(((int(real_seconds)) * real_secondly))) + " to keep today.")
	realmoney = Label(bottomframe, textvariable=realmoneytext, bg='red', font="Times 16 bold")
	realmoney.grid(row=5, columnspan=2, sticky=W+E)
	bottomframe.after(90, delete_live)
	bottomframe.after(100, set_bottom_frame)


main_window()
set_frames()
set_top_frame()

root.mainloop()