import datetime 

class userInterface:

    data=[]
    miles=0
    cost=0

    def __init__(self):
        data=[]
        miles=0
        cost=0

    def userInputData(self):

        miles=input('how many miles did you drive')

        cost=input('how much did you pay?')

        date=datetime.date.today()

        data=[date,miles,cost]

        return data


