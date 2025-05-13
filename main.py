import fileInOut
import userInterface
import gasCalculator


runner= userInterface.userInterface()

files=fileInOut.fileInOut()

calculator= gasCalculator.gasCalculator(files.getData())
