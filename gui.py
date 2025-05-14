from tkinter import *
from tkinter import ttk
import fileInOut
import datetime
#gui for display for the input form window
class inputForm():
   fileHandler=fileInOut.fileInOut()
   inputMiles=float
   inputCost=float
   root=Tk()
   root.title('User Input')
   frame= ttk.Frame()
   
   milesInput=ttk.Entry(frame,width=10,textvariable='Miles')
   costInput=ttk.Entry(frame,width=10,textvariable='Cost')
   
   def input(self,*args):
      try:
         data=[]
         newMiles=self.milesInput.get()
         newCost=self.costInput.get()
         data=[datetime.date.today(),newMiles,newCost]
         self.fileHandler.giveData(data)
      except ValueError:
         pass
      


   milesInput.grid(column=2, row=1, sticky=(W, E))
   costInput.grid(column=4, row=1, sticky=(W, E))

   ttk.Button(frame,text='Input',command=input).grid(column=6,row=2,sticky=(W,E))

   root.bind("<Return>", input)

   root.mainloop()
