
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry("600x500")

# Create transparent window
root.attributes('-alpha',0.5)

x1,x2=400,400
y1=100
y2=200

canvas=Canvas(root)
canvas.pack(pady=0,padx=0,fill=BOTH, expand=True)
canvas.create_line(x1,y1,x2,y2,width='10',fill='green')

# Execute tkinter
root.mainloop() # do not run this line if running this in a console realtime mode
