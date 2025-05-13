import fileInOut
import userInterface
import gasCalculator
runner= userInterface.userInterface()

files=fileInOut.fileInOut()



#data=runner.userInputData() 

#files.giveData(data)

calculator= gasCalculator.gasCalculator(files.getData())


print(files.getData()) 
 
print(round(calculator.getEfficiency(),2), 'miles/dollar') 