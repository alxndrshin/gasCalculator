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
   
   root.minsize(width=500,height=250)
   
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

def startUp():
   root=Tk()
   root.title('Welcome')

   root.minsize(width=500,height=250)
   root.columnconfigure(0, weight=1)
   root.rowconfigure(0, weight=1)

   def input():
      inputForm()


   frame=ttk.Frame(root,padding="3 3 12 12")
   frame.grid(column=0, row=0, sticky=(N, W, E, S))
   ttk.Label(frame,text='Welcome').grid(column=4,row=1,sticky=(W,E))
   ttk.Button(frame,text='Input',command=input).grid(column=2,row=3,sticky=(W,E))
   
   
   root.mainloop()

class gui():
   def __init__(self):
      root=Tk()
      root.title=('Gas Calculator')
      root.minsize(width=500,height=250)

      self.frames={}

      for page in (welcomePage,calcPage,dataPage):
         pageName=page.__name__
         frame=page(parent=root,controller=self)
         self.frames[pageName]=frame

         frame.grid(row=0, column=0, sticky="nsew")

      self.showFrame=("welcomePage")
   
   def showFrame(self, pageName):
      frame = self.frames[pageName]
      frame.tkraise()

class welcomePage(ttk.Frame):
   def __init__(self,parent,controller):
      ttk.Frame.__init__(self,parent)
      self.controller=controller
      ttk.Lable(text='Welcome').grid(column=2,row=3,sticky=(W,E))
      ttk.Button(text='Data Entry',command=lambda: controller.show_frame("dataPage"))

class dataPage(ttk.frame):
   def __init__(self,parent,controller):
      ttk.Frame.__init__(self,parent)
      self.controller=controller
      ttk.Lable(text='Welcome').grid(column=2,row=3,sticky=(W,E))
      ttk.Button(text='Back',command=lambda: controller.show_frame("welcomePage"))
      ttk.button(text='Input Data',command=input)
   
   def input():
      fileHandler=fileInOut()
      try:
         data=[]
         newMiles=milesInput.get()
         newCost=costInput.get()
         data=[datetime.date.today(),newMiles,newCost]
         fileHandler.giveData(data)
      except ValueError:
         pass


