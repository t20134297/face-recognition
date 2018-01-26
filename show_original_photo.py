from tkinter import *
from PIL import Image, ImageTk
import sys
original_photo = sys.argv[2]
name = sys.argv[3]
def A():
    root=Tk()
    root.title("原始图片显示窗口")
    inf='系统检测到您待检测图片中的人物为：'+name
    textLabel=Label(root,text=inf)
    textLabel.pack()
    im=Image.open(original_photo)
    tkimg=ImageTk.PhotoImage(im)
    imgLabel=Label(root,imag=tkimg)
    imgLabel.pack()
    mainloop()
A()
