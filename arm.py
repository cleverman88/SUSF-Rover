from roverVar import *

class arm():
    def __init__(self):
        self.grabberPower = roverVar(0,"gp")
        self.armX = roverVar(0,"ax")
        self.armY = roverVar(0,"ay")
        self.armZ = roverVar(0,"az")