import datetime 

class userInterface:

    def __init__(self):
        self.data=[]
        self.miles=0
        self.cost=0
        self.gallons=0

    #takes in user data plan to adjust in the future 
    def userInputData(self):

        self.miles=input('how many miles did you drive')

        self.cost=input('how much did you pay?')

        self.gallons=input('How many gallons did you burn?')

        self.date=datetime.date.today()

        self.data=[self.date,self.miles,self.cost,self.gallons]

        return self.data


