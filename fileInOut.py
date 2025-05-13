import csv

class fileInOut:


    def __init__(self):
        self.dataList=[]

    #opens and reads in file
    #file in format date-miles-price 
    #date in format yyyy-mm-dd miles to tenths prices to hundredths
    #return is a list of lists 
    def __fileRead(self):
        with open('gasData.csv',newline='' ) as fileData:
            fileReader= csv.reader(fileData)
            for row in fileReader:
                self.dataList.append(row) 

    #writes to the file
    def __fileWrite(self,data):
        with open('gasData.csv','a',newline='\n') as fileData:
            fileWriter=csv.writer(fileData)
            fileWriter.writerow(data)
    
    def giveData(self,inputData):
        self.__fileWrite(inputData)

    def getData(self):
        self.__fileRead()
        return self.dataList
