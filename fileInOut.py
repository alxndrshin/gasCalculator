import csv

class fileInOut:

    #def __init__():
      
    #opens and reads in file
    #file in format date-miles-price 
    #date in format yyyy-mm-dd miles to tenths prices to hundredths
    #return is a list of lists 
    def fileRead():
        dataList=[]
        with open('gasData.csv',newline='' ) as fileData:
            fileReader= csv.reader(fileData)
            for row in fileReader:
                dataList.append(row)
        print(dataList)
        return dataList

    #writes to the file
    def fileWrite(data):
        with open('gasData.csv','a',newline='\n') as fileData:
            fileWriter=csv.writer(fileData)
            fileWriter.writerow(data)