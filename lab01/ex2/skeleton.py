
class myPoint():
    def __init__(self,xCoord,yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord

    def getX(self):
        return self.xCoord
    
    def getY(self):
        return self.yCoord
    



noOfPoints = int(raw_input())
pointList = []

for i in range (0, noOfPoints):
    s = raw_input()
    x = s.split()[0]
    y = s.split()[1]
    newPoint = myPoint(x,y)
    pointList.append(newPoint)

for number,point in reversed(list(enumerate(pointList))):
    print("Point " + str(number) + ": (" + point.getX() + ", " + point.getY() + ")")