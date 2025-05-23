import datetime
import fileInOut

class gasCalculator:
     #data in format date-miles-price or miles-price
    def __init__(self):
        self.dataLoader=fileInOut.fileInOut()
        self.data=[]
        self.workingData=[]
        self.mpd=0
        self.mpg=0

    #instance variables: rawData, workingData
    def __init__(self,data):
        self.mpd=0
        self.mpg=0
        self.dataLoader=fileInOut.fileInOut()
        self.rawData=data
        self.workingData=[]
        self.__calcWorkingData(self.rawData)
        self.calculate()
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

    def calculate(self):
        #calculates different efficiencies to be stored for retrieval
        #mpd mpg
        # miles-price-gallons
        datapoints=0
        totalMiles=0
        totalGallons=0
        totalDollars=0

        for item in self.workingData:
            totalMiles+=item[0]
            totalGallons+=item[1]
            totalDollars+=item[2]
            datapoints+=1

        self.mpg=totalMiles/totalGallons
        self.mpd=totalMiles/totalDollars

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
        self.calculate()
        if choice==1:
            return self.getMPG()
        if choice==2:
            return self.getMPD()
