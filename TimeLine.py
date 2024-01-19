# colour picker crtl shift a, Type in colour

import time
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
        # self.master.attributes('-fullscreen', True)
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        self.master.config(bg='white') # use this in conj with wm_atts below bg="#add123"

        self.master.attributes("-topmost", True)
        # self.master.attributes('-alpha', 0.2) # make window transparent 1.0=totally solid
        self.master.wm_attributes('-transparentcolor','white') # make viewable window transp, not the top bar

        canvas = Canvas(self.master,width=screenWidth,height=screenHeight, bg="white",highlightbackground="white") #highlibackgrnd--just like a border, make white so it goes transparent
        #canvas.create_line(15, 0, 15, 500, width=5) # x,y x,y, dash=(10)
        canvas.pack(pady=0,padx=0,fill=BOTH, expand=True)

        self.timeLine(canvas)





    def timeLine(self,canvas):
        '''
        Draws a line at the correct time on the x axis
        inputs: the canvas
        '''

        # 9am top point on the browser: 795,431
        x1, y1, x2, y2 = 795,400,795, 900 # home vals: 795, 431, 795, 900; work vals: 524,280,524,900
        canvas.create_line(x1, y1, x2, y2, width=1, fill="green")
        loop=False
        while loop:
            canvas.create_line(x1,y1,x2,y2,width=1,fill="green")
            self.master.update()
            time.sleep(0.2)
            canvas.create_line(x1, y1, x2, y2, width=2, fill="#FFFFFF")
            self.master.update()
            x1+=1
            x2+=1







        windll.shcore.SetProcessDpiAwareness(1)  # used for fixing blurry fonts on win 10 and 11

root=Tk()
mainWin=MainWindow(root)

root.mainloop()

