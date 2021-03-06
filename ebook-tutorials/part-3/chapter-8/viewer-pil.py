import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = "pics"
imgfile = "one.jpg"

if len(sys.argv) > 1:
	imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath)
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height())
win.mainloop()