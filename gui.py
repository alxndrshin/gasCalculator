from tkinter import *
from tkinter import ttk
import fileInOut
import datetime
#gui for display for the input form window
def inputForm():
   fileHandler=fileInOut.fileInOut()
   inputMiles=float
   inputCost=float
   root=Tk()
   root.title('User Input')
   frame= ttk.Frame(root, padding="3 3 12 12")

   frame.grid(column=0, row=0, sticky=(N, W, E, S))
   root.columnconfigure(0, weight=1)
   root.rowconfigure(0, weight=1)

   milesInput=ttk.Entry(frame,width=10,textvariable='feet')
   costInput=ttk.Entry(frame,width=10,textvariable='Cost')
   
   def input():
      try:
         data=[]
         newMiles=milesInput.get()
         newCost=costInput.get()
         data=[datetime.date.today(),newMiles,newCost]
         fileHandler.giveData(data)
      except ValueError:
         pass
      

   ttk.Label(frame,text='Miles:').grid(column=1,row=1)
   milesInput.grid(column=2, row=1, sticky=(W, E))
   ttk.Label(frame,text='Cost:').grid(column=1,row=3)
   costInput.grid(column=2, row=3, sticky=(W, E))

   ttk.Button(frame,text='Input',command=input).grid(column=6,row=3,sticky=(W,E))

   root.bind("<Return>", input)

   root.mainloop()

inputForm()