from tkinter import *

# Scrollbar works indirectly on labels by way of canvas
# Frame1 has Canvas and Scrollbar,Canvas in turn holds the labels

text1='''Earth has not anything to show more fair:
Dull would he be of soul who could pass by
A sight so touching in its majesty:   '''

text2='''This City now doth, like a garment, wear
The beauty of the morning: silent, bare,
Ships, towers, domes, theatres, and temples lie
Open unto the fields, and to the sky …       '''

text3='''
Wisdom and Spirit of the universe!
Thou Soul that art the eternity of thought!
That giv’st to forms and images a breath
And everlasting motion! not in vain,
By day or star-light thus from my first dawn
Of Childhood didst Thou intertwine for me
The passions that build up our human Soul,
Not with the mean and vulgar works of Man,
But with high objects, with enduring things,
With life and nature, purifying thus
The elements of feeling and of thought,
And sanctifying, by such discipline,
Both pain and fear, until we recognize
A grandeur in the beatings of the heart …

With life and nature, purifying thus
The elements of feeling and of thought,
And sanctifying, by such discipline,
Both pain and fear, until we recognize
A grandeur in the beatings of the heart'''

w=400
h=200

root = Tk()

root.title("Columns")

f0=Frame(root)
f1=Frame(root,width=w,height=h,bg='purple')
f2=Frame(root,width=w,height=h,bg='grey')

f0.grid(row=0,column=0)  # Top row
f1.grid(row=1,column=0)  # Column with text
f2.grid(row=1,column=1)  # Empty column

root.rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=2)
root.grid_columnconfigure(0,weight=1)

c = Canvas(f1) # canvas in f1, text column
sb = Scrollbar(f1, orient='vertical', command=c.yview) # scrollbar in f1

# Labels inserted on canvas
l0 = Label(c, text=text1,wraplength=w)
c.create_window(0, 0, window=l0, anchor=NW)

l1 = Label(c, text=text3,wraplength=w)
c.create_window(0, 30, window=l1, anchor=NW)

c.configure(scrollregion=c.bbox('all'), yscrollcommand=sb.set)

c.pack(fill='both', expand=True, side='left')
sb.pack(fill='y', side='right')

# l1 = Label(f1, text=text2,wraplength=w)
#
# l1.pack()
#
# l3 = Label(f1, text=text3,wraplength=w)
#
# l3.pack()

root.mainloop()
