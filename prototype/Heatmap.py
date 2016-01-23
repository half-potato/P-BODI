import numpy
import math
import util
import cv2

#The heatmap can be visualized as a furry ball. There is a single point that represents camera and the vectors point at positions where objects have been seen
class Heatmap:
    def __init__(self, amtOfVecs, spiralCount, learningRate):
        self.hmap = [[1,0,0] for i in range(amtOfVecs)]
        self.spiralCount = spiralCount
        self.reset()
        self.learningRate = learningRate

    #Imagine these are like right ascention declination
    def getIndex(self, degX, degY):
        #spiral around the sphere, radius = 1
        #resolution = distance between points
        #imagine a giant triangle spun around a sphere. That's what we're going to do
        c = 2.0 * math.pi
        #the points would be evenly distributed along the height
        dia = 2.0 #diameter = 2
        #Imagine fanning out the verticies
        degSep = (c / len(self.hmap)) * self.spiralCount
        #get an array of the points within that degree, get the closest one along the y axis
        indicies = []
        for i in xrange(0.0, 360.0, degSep):
            indicies.append(int(360.*self.spiralCount / i))

        #Getting the y axis
        #imagine a line from the center of the sphere to the point on the outside
        #the radius is 1, the adj is the dist from the point along the height
        for i in indicies:
            h = i * res
            ang = math.acos(h / 1.0)
            if math.abs(ang - degY) < res:
                return i

        return 0

    def getDegrees(self, index):
        #reverse of getIndex
        i = float(index)
        c = 2.0 * math.pi
        dia = 2.0
        res = dia / len(self.hmap)
        degSep = (c / len(self.hmap)) * self.spiralCount
        h = (i * res) - (dia / 2.)
        vAng = math.acos(h / 1.0)
        hAng = i * degSep
        #print(util.normalizeAngle(hAng),vAng)
        return (util.normalizeAngle(hAng), vAng)

    def resetVector(self, index):
        (ax, ay) = self.getDegrees(index)
        #translate the degrees to a vector
        v = [math.cos(ax), math.sin(ay)]
        #normalize vector
        v = util.normalize(v)
        #set vector to index
        self.hmap[index] = v

    def reset(self):
        for i in range(len(self.hmap)):
            self.resetVector(i)
    
    def vecToDegrees(self, vec):
        v = util.normalize(vec)
        horV = [v[0], 0, v[2]]
        vertAng = util.acos(v, horV)
        startVec = [1,0,0]
        horzAng = util.acos(horv, startVec)
        return (horzAng, vertAng)

    def singleTrain(self, vec):
        i = self.getIndex(self.vecToDegrees(vec))
        self.hmap[i] *= self.learningRate

    def visualize(self, image, scale):
        r = image
        offsetX = int(image.shape[1] / 2)
        offsetY = int(image.shape[0] / 2)
        for i in self.hmap:
            cv2.arrowedLine(r, (offsetY,offsetX), (int(i[1] * scale + offsetY), int(i[0] * scale + offsetX)), (255, 0, 0))
        return r
