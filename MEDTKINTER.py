#import tkinter module 
from tkinter import*

#import other necessary modules 
import random
import time
import datetime

#cracking root object
root = Tk()

#defining size of window
root.geometry("1200x6000")

#setting up the title of the window 
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)

f1.pack(side=LEFT)

#========================================================
#                       TIME                             
#========================================================
locltime=time.sctime(time.locltime(time.time()))

lblInfo = Label(Tops, font=('helvatica, 50,'bold), text="SECRET MESSAGING \n Vigenere cipher", fg="Black, bd=10, anchor="w)

lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10. anchor='w')

lblInfo.grid(row=1, column=0)

rand=StringVar()
Msg=StringVar()
key=StringVar()
mode=StringVar()
Result=StringVar()

#exit function
def qExit():
    root.destroy()

#Function to reset the windows
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")


#reference
lblReference = Label(f1, font=('arial', 16, 'bold'), text="Name:", bd=16, anchor='w')
