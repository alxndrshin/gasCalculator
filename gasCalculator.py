import datetime
import fileInOut
from datetime import datetime

class gasCalculator:
     #data in format date-miles-price or miles-price
    def __init__(self):
        self.dataLoader=fileInOut.fileInOut()
        self.data=[]
        self.workingData=[]
        self.mpd=0
        self.mpg=0
        self.dates=[]

    #instance variables: rawData, workingData
    def __init__(self,data):
        self.mpd=0
        self.mpg=0
        self.dataLoader=fileInOut.fileInOut()
        self.rawData=data
        self.workingData=[]
        self.dates=[]
        self.__calcWorkingData(self.rawData)
        if len(self.workingData)!=0:
            self.calculate()
            self.fillTime()
        #print(self.workingData)

 #efficiency will be calculated using the cost 1 previous to the milage used
 #this ensures the cost of gas is associated with the correct mileage and not the mileage at the fillup

    #removes date information from data and adds it to working data
    #date data is unessesary for most calculations
    def __calcWorkingData(self,data):
        for each in data:
            newData=[]
            newData.append(each[1])
            newData.append(each[2])
            newData.append(each[3])
            self.workingData.append(newData)
            self.fillTime

    def calculate(self):
        #calculates different efficiencies to be stored for retrieval
        #mpd mpg
        # miles-price-gallons
        datapoints=0
        totalMiles=0
        totalGallons=0
        totalDollars=0

        for item in self.workingData:
            totalMiles+=float(item[0])
            totalDollars+=float(item[1])
            totalGallons+=float(item[2])
            datapoints+=1

        self.mpg=totalMiles/totalGallons
        self.mpd=totalMiles/totalDollars

    def fillTime(self):
        #determine average time between fills can recomend whether you should refill soon
        for dateVar in self.rawData:
            newDate= datetime.strptime(dateVar[0],'%Y-%m-%d')
            self.dates.append(newDate)
            
    def printDates(self):
        for date in self.dates:
            print(date) 

    def updateData(self):
        self.rawData=self.dataLoader.getData()
        self.__calcWorkingData(self.rawData)
        

    def updateData(self, newData):
        self.rawData=newData
        self.__calcWorkingData(newData)

    def getMPG(self):
        return self.mpg

    def getMPD(self):
        return self.mpd    
    
    def runner(self,choice):
        if choice==1:
            self.calculate()
            print('Your efficiency is: ',round(self.getMPG(),2),' MPG')
        if choice==2:
            self.calculate()
            print('Your efficiency is: ',round(self.getMPD(),2),' MPD')
        if choice==3:
            self.printDates()
