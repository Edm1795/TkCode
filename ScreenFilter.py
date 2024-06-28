# This overlays block lines on the screen so as to block out unwanted parts of the screen and allow you to focus your attention.
from tkinter import *

# Create object
root = Tk()

# Adjust size
# root.geometry("600x500")
root.attributes('-fullscreen', True)
# Create transparent window
# root.attributes('-alpha',0.5)

root.wm_attributes('-transparentcolor','white') # make viewable window transp, not the top bar

# highlibackgrnd--just like a border, make white so it goes transparent. This makes the canvas completely transparent but not anything on it which is other than white



leftx1,leftx2=0,0
lefty1=0
lefty2=1080

rightx1,rightx2=583,583
righty1=0
righty2=1080

# canvas=Canvas(root)
canvas = Canvas(root, bg="white",highlightbackground="white")
canvas.pack(pady=0,padx=0,fill=BOTH, expand=True)

canvas.create_line(leftx1,lefty1,leftx2,lefty2,width=1046,fill='#103D2D') # Screen units are inputed as strings; pixels are inputed an numbers. Screen units are absolute distances such as mm or cm eg:10m
canvas.create_line(rightx1,righty1,rightx2,righty2,width=497,fill='#103D2D') # Screen units are inputed as strings; pixels are inputed an numbers. Screen units are absolute distances such as mm or cm eg:10m

# Execute tkinter
root.mainloop() # do not run this line if running this in a console realtime mode
