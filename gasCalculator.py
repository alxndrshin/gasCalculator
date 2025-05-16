import datetime

class gasCalculator:
     #data in format date-miles-price or miles-price
    def __init__(self):
        self.data=[]
        self.workingData=[]

    #instance variables: rawData, workingData
    def __init__(self,data):
        self.rawData=data
        self.workingData=[]
        self.__calcWorkingData(self.rawData)
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
            self.workingData.append(newData)

    def __calcTotalEfficiency(self):
        miles=0
        price=0
        efficiency=0
        #print(self.workingData)
        for row in self.workingData:
            miles+=int(row[0])
            price+=int(row[1])
        efficiency= float(miles/price)
        return efficiency

    def updateData(self, newData):
        self.rawData=newData
        self.__calcWorkingData(newData)

    def getEfficiency(self):
        return(self.__calcTotalEfficiency())    
    
    def runner(self,choice):
        if choice==1:
            return self.getEfficiency()
