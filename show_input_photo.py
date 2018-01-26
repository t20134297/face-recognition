from tkinter import *
from PIL import Image, ImageTk
import sys
input_photo = sys.argv[1]
def A():
    root=Tk()
    root.title("输入图片显示窗口")
    textLabel=Label(root,text='您输入的图片为:')
    textLabel.pack()
    im=Image.open(input_photo)
    tkimg=ImageTk.PhotoImage(im)
    imgLabel=Label(root,imag=tkimg)
    imgLabel.pack()
    mainloop()
A()
