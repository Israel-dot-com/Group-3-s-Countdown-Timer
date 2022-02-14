
#import time module, tkinter, tkinter.ttk, and message box

import time
from tkinter import *
import tkinter
from tkinter.ttk import * 
from tkinter import messagebox


 
#The root tkinter window
root = Tk()

icon=PhotoImage(file="timer.png")
root.iconphoto(False, icon)
  
#setting the geometry of tk window to 800*700
root.geometry("800x700")
  

root.title("Group's 3-Countdown Timer")
# Creating the time windows in the GUI
hour=StringVar()
minute=StringVar()
second=StringVar()




class Countdown:
    #Setting All The global time variables to zero
    hour.set("0")
    minute.set("0")
    second.set("0")
    
    # Use of Entry class to take input from the user
    hourEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=hour)
    hourEntry.place(x=300,y=20)

    minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=minute)
    minuteEntry.place(x=350,y=20)

    secondEntry= Entry(root, width=3, font=("Arial",18,""),
                    textvariable=second)
    secondEntry.place(x=400,y=20)
  
    def submit(self):
        try:
            
            timeCalc = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        except:
            print("Please input the right value")
        while timeCalc >-1:
            
            # divmod(firstvalue = timeCalc//60, secondvalue = timeCalc%60)
            mins,secs = divmod(timeCalc,60)
    
            # Converting the input entered in mins or secs to hours,
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
            # 50min: 0sec)
            hours=0
            if mins >60:
                
                # divmod(firstvalue = timeCalc//60, secondvalue
                # = timeCalc%60)
                hours, mins = divmod(mins, 60)
            
            # using format () method to store the value up to
            # two decimal places
            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))
    
            # updating the GUI window after decrementing the
            # timeCalc value every time
            root.update()
            time.sleep(1)
    
            # when timeCalc value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (timeCalc == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            
            # after every one sec the value of timeCalc will be decremented
            # by one
            timeCalc -= 1
count=Countdown()
# button widget
btn = Button(root, text='Set Time Countdown',
             command= count.submit)
btn.place(x = 307,y = 80)
  
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()