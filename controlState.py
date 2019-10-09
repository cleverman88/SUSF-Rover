from arm import *
from driveTrain import *

class controlState():
    def __init__(self):
        self.drivetrain = drivetrain()
        self.arm = arm()



    def formatForSending(self):
        networkData = ""
        attributes = list(vars(self).keys())
        for attributeNum in range(len(attributes)):
            self.networkData = ""
            exec("self.networkData = self."+str(attributes[attributeNum])+".getDataString()")
            networkData += self.networkData
            del(self.networkData)
        print(networkData)


def calcStateDifferential(stateA,stateB):
    attributes = list(vars(stateA).keys())
    for attributeNum in range (len(attributes)):
        attrType = type(getattr(stateA,attributes[attributeNum]))
        if attrType != int:
            calcStateDifferential(getattr(stateA,attributes[attributeNum]),getattr(stateB,attributes[attributeNum]))
        elif attrType != str:
            differential = getattr(stateA,attributes[attributeNum]) - getattr(stateB,attributes[attributeNum])
            setattr(stateA,attributes[attributeNum],differential)

stA = controlState()
stB = controlState()
stA.arm.armX = 3
stB.arm.armX = 5


calcStateDifferential(stA,stB)

stA.formatForSending()
