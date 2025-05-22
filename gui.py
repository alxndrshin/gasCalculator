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

   # milesInput=ttk.Entry(frame,width=10,textvariable='feet')
   # costInput=ttk.Entry(frame,width=10,textvariable='Cost')
   
#    def input():
#       try:
#          data=[]
#          newMiles=milesInput.get()
#          newCost=costInput.get()
#          data=[datetime.date.today(),newMiles,newCost]
#          fileHandler.giveData(data)
#       except ValueError:
#          pass
      

   # ttk.Label(frame,text='Miles:').grid(column=1,row=1)
   # milesInput.grid(column=2, row=1, sticky=(W, E))
   # ttk.Label(frame,text='Cost:').grid(column=1,row=3)
   # costInput.grid(column=2, row=3, sticky=(W, E))

#    ttk.Button(frame,text='Input',command=input).grid(column=6,row=3,sticky=(W,E))

#    root.bind("<Return>", input)

#    root.mainloop()


LARGEFONT =("Verdana", 35)
 
class gui(tk.Tk):
    
    # __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        # initializing frames to an empty array
        self.frames = {}  
 
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (welcomePage, inputPage, calcPage):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            # welcomePage, inputPage, calcPage respectively with 
            # for loop
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(welcomePage)
 
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
 
# first window frame welcomePage
 
class welcomePage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        # label of frame Layout 2
        label = ttk.Label(self, text ="welcomePage", font = LARGEFONT)
        
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 4, padx = 10, pady = 10) 
 
        inputButton = ttk.Button(self, text ="Input",
        command = lambda : controller.show_frame(inputPage))
    
        # putting the button in its place by
        # using grid
        inputButton.grid(row = 1, column = 1, padx = 10, pady = 10)
 
        ## button to show frame 2 with text layout2
        calcButton = ttk.Button(self, text ="Calculator",
        command = lambda : controller.show_frame(calcPage))
    
        # putting the button in its place by
        # using grid
        calcButton.grid(row = 2, column = 1, padx = 10, pady = 10)

        
 
         
 
 
# second window frame inputPage 
class inputPage(tk.Frame):
   fileHandler=fileInOut.fileInOut()
   inputMiles=float
   inputCost=float

   def input(self):
      try:
         data=[]
         newMiles=self.milesInput.get()
         newCost=self.costInput.get()
         data=[datetime.date.today(),newMiles,newCost]
         self.fileHandler.giveData(data)
      except ValueError:
         pass

   def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)

      self.milesInput=ttk.Entry(parent,width=10,textvariable='feet')
      self.costInput=ttk.Entry(parent,width=10,textvariable='Cost')

      label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
      label.grid(row = 0, column = 4, padx = 10, pady = 10)
 
        # button to show frame 2 with text
        # layout2
      backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(welcomePage))
    
        # putting the button in its place 
        # by using grid
      backButton.grid(row = 1, column = 1, padx = 10, pady = 10)
 
        # button to show frame 2 with text
        # layout2
      enter = ttk.Button(self, text ="Enter",
                            command = input)
      
   

    
        # putting the button in its place by 
        # using grid
      enter.grid(row = 2, column = 1, padx = 10, pady = 10)

     
 
 
 
 
# third window frame calcPage
class calcPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)
 
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(inputPage))
    
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
 
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="welcomePage",
                            command = lambda : controller.show_frame(welcomePage))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

app = gui()
app.mainloop()