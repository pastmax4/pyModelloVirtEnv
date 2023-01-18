import math

class rettangolo:
    def __init__(self, lato01, lato02):
        self.lato01 = lato01
        self.lato02 = lato02

    def setAttrLati(self,inVal01,inVal02):
        self.lato01= inVal01
        self.lato02= inVal02

    def getDiagonale(self):
        self.diagonale = math.sqrt( self.lato01* self.lato01 +  self.lato02* self.lato02 )
        #diagonale=99
        return self.diagonale

    def getPerimetro(self):
        perimetro = 2* self.lato01  + 2* self.lato02
        #diagonale=99
        return perimetro

    def getArea(self):
        area =  self.lato01 * self.lato02        
        return area


