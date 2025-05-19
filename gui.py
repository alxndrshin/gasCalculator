import tkinter as tk
from tkinter import ttk
import fileInOut
import datetime
#gui for display for the input form window
# def inputForm():
#    fileHandler=fileInOut.fileInOut()
#    inputMiles=float
#    inputCost=float
   
#    root=Tk()
#    root.title('User Input')
   
#    root.minsize(width=500,height=250)
   
#    frame= ttk.Frame(root, padding="3 3 12 12")
   
#    frame.grid(column=0, row=0, sticky=(N, W, E, S))


#    root.columnconfigure(0, weight=1)
#    root.rowconfigure(0, weight=1)

#    milesInput=ttk.Entry(frame,width=10,textvariable='feet')
#    costInput=ttk.Entry(frame,width=10,textvariable='Cost')
   
#    def input():
#       try:
#          data=[]
#          newMiles=milesInput.get()
#          newCost=costInput.get()
#          data=[datetime.date.today(),newMiles,newCost]
#          fileHandler.giveData(data)
#       except ValueError:
#          pass
      

#    ttk.Label(frame,text='Miles:').grid(column=1,row=1)
#    milesInput.grid(column=2, row=1, sticky=(W, E))
#    ttk.Label(frame,text='Cost:').grid(column=1,row=3)
#    costInput.grid(column=2, row=3, sticky=(W, E))

#    ttk.Button(frame,text='Input',command=input).grid(column=6,row=3,sticky=(W,E))

#    root.bind("<Return>", input)

#    root.mainloop()


class gui(tk.Tk):
   def __init__(self,*args,**kwargs):
      tk.Tk.__init__(self, *args, **kwargs)
      
      container=tk.Frame(self)
      container.pack(side = "top", fill = "both", expand = True)
      container.grid_rowconfigure(0, weight = 1)
      container.grid_columnconfigure(0, weight = 1)
      
      self.frames={}

      for F in (welcomePage,dataPage,calcPage):
         frame=F(container,self)
         self.frames[F]=frame

         frame.grid(row = 0, column = 0, sticky ="nsew")

      self.showFrame=(welcomePage)
   
   def showFrame(self, pageName):
      frame = self.frames[pageName]
      frame.tkraise()

  


class welcomePage(tk.Frame):
   def __init__(self,parent,controller):
      tk.Frame.__init__(self, parent)
        
      label = ttk.Label(self, text ="Welcome Page")
      label.grid(row = 0, column = 4, padx = 10, pady = 10) 

      dataButton=ttk.Button(self, text ="Data Input",command = lambda : controller.showFrame(dataPage))
      dataButton.grid(row = 1, column = 1, padx = 10, pady = 10)

      calcButton = ttk.Button(self, text ="Gas Calculator",command = lambda : controller.showFrame(calcPage))
      calcButton.grid(row = 2, column = 1, padx = 10, pady = 10)

class dataPage(tk.Frame):
   def __init__(self,parent,controller):
      tk.Frame.__init__(self, parent)
      label = ttk.Label(self, text ="Data Input")
      label.grid(row = 0, column = 4, padx = 10, pady = 10)

      backButton = ttk.Button(self, text ="Back",command = lambda : controller.showFrame(welcomePage))
      backButton.grid(row = 1, column = 4, padx = 10, pady = 10)

      
   
   

   def input(self):
      fileHandler=fileInOut()
      try:
         data=[]
         newMiles=self.milesInput.get()
         newCost=self.costInput.get()
         newMileage=self.mileageInput.get()
         data=[datetime.date.today(),newMiles,newCost,newMileage]
         fileHandler.giveData(data)
      except ValueError:
         pass


class calcPage(tk.Frame):
   def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Gas Calculator")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        backButton = ttk.Button(self, text ="Back",command = lambda : controller.showFrame(welcomePage))
        backButton.grid(row = 1, column = 4, padx = 10, pady = 10)

guiTester=gui()
guiTester.mainloop()
