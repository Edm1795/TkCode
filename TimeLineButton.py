# Timeline overlay with an extra button as well

# colour picker crtl shift a, Type in colour

import time
from datetime import datetime
from tkinter import *
from ctypes import windll  # used for fixing blurry fonts on win 10 and 11 (also  windll.shcore.SetProcessDpiAwareness(1))
#from tkinter import ttk



class MainWindow:

    def __init__(self, master):

        # Master Window
        self.master = master
        self.master.title('AutoGui Ver. 0.0')
        self.master.geometry("+150+500")  # position of the window in the screen (200x300)
        self.master.geometry("1000x400")  # set initial size of the root window (master) (1500x700);
        # if not set, the frames will fill the master window
        self.master.attributes('-fullscreen', True)
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        self.master.config(bg='white') # use this in conj with wm_atts below bg="#add123"

        self.master.attributes("-topmost", True)
        # self.master.attributes('-alpha', 0.2) # make window transparent 1.0=totally solid
        self.master.wm_attributes('-transparentcolor','white') # make viewable window transp, not the top bar

        # highlibackgrnd--just like a border, make white so it goes transparent. This makes the canvas completely transparent but not anything on it which is other than white
        canvas = Canvas(self.master,width=screenWidth,height=screenHeight, bg="white",highlightbackground="white")
        #canvas.create_line(15, 0, 15, 500, width=5) # x,y x,y, dash=(10)
        canvas.pack(pady=0,padx=0,fill=BOTH, expand=True)

        self.timeLine(canvas)

        self.button = Button(canvas, text="Schedule", width=12,bg='blue', command=self.schedule,)
        self.button.pack()


    def schedule(self):
        pass

    def timeLine(self,canvas):
        '''
        Draws a line downwards at the correct current time on screen. This function has a helper function
        which calulates the time difference from 8 am to the current time of day
        inputs: the canvas
        '''

        def getTimeDiff():
            '''
            This function calculates the number of minutes elapsed between 8 am and the current time of day
            Ex: if it is 9 am currently, then 60 mins has elapsed since 8 am
            :return: float of num of minutes elapsed
            '''

            # t = time.localtime() # get local time
            # current_time = time.strftime("%H:%M:%S", t) # convert local time to string readable

            now = datetime.now()
            currTime = now.strftime("%H:%M:%S")

            start = datetime.strptime("8:00:00", "%H:%M:%S")
            end = datetime.strptime(currTime, "%H:%M:%S")

            difference = end - start

            seconds = difference.total_seconds()

            # hours = seconds / (60 * 60)

            return seconds / 60 # returns number of minutes elapsed


        # 30 mins = how many pixels? --> 831-794 = 37
        # 37 pixels / 30 = 1.2333 pixels per minute

        # 1.2333.. number of pixels horizontally per minute of time, move timeline 1.23 pixels every minute
        x1,x2 = (getTimeDiff() * 1.24) + 718, (getTimeDiff() * 1.24) + 718 # x coords = num of minutes elapsed since 8 am * num of pixels per minute (1.23)
        y1=380
        y2=900
        # x1, y1, x2, y2 = 718,423,718, 900 # 8:00am top point: 718,423. # 9am top point: 795,431   795, 431, 795, 900
        # 9 am ? home vals: 795, 431, 795, 900; work vals: 524,280,524,900
        canvas.create_line(x1, y1, x2, y2, width=1, fill="green") # draw a line at coordinates needed to display at correct time on schedule

        # this loop can be used to draw a line, then erase that original line and draw a new line.
        # loop=False
        # while loop:
        #     canvas.create_line(x1,y1,x2,y2,width=1,fill="green")
        #     self.master.update()
        #     time.sleep(0.2)
        #     canvas.create_line(x1, y1, x2, y2, width=2, fill="#FFFFFF")
        #     self.master.update()
        #     x1+=1
        #     x2+=1







        windll.shcore.SetProcessDpiAwareness(1)  # used for fixing blurry fonts on win 10 and 11

def main():

    root=Tk()
    mainWin=MainWindow(root)

    root.mainloop()

main()
