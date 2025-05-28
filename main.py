import fileInOut
import userInterface
import gasCalculator

class main():
    def __init__(self):
        #user input class
        self.userInput= userInterface.userInterface()
        #files class
        self.files=fileInOut.fileInOut()
        #working data
        self.data=self.files.getData()
        #calculator class
        self.calculator=gasCalculator.gasCalculator(self.data)
       


    def driver(self):
        choice=1000000000000
        keepGoing= True
        while keepGoing:
            print('What would you like to do today?')
            choice=int(input('0 for quit, 1 for add data, 2 for calculate efficiency, 3 for dates filled'))
            if choice == 0:
                keepGoing= False
            elif choice == 1:
                choice=int(input('how many data points would you like to add? '))
                for x in range(choice):
                    newData=self.userInput.userInputData()
                    #update CSV file with new data
                    self.files.giveData(newData)
                    #retrieve new data and store
                    self.data=self.files.getData()
            elif choice == 2:
                print('what efficiency would you like to calculate?')
                choice=int(input('1 for MPG, 2 for MPD'))
                #run with newest data
                self.calculator.updateData(self.data)
                self.calculator.runner(choice)
            elif choice == 3:
                self.calculator.runner(choice)
            else:
                print(choice,' That is not an available option')
        print('Thank you') 

mainCode=main()
mainCode.driver()

               