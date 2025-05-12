import fileInOut
import userInterface

runner= userInterface.userInterface()

files=fileInOut.fileInOut()

data=runner.userInputData()

files.giveData(data)
print(files.getData())
