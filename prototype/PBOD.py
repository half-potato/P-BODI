import math
import numpy
import cv2
import util

class PBOD:
    # angle refers to the view
    def __init__( self, heightFromGround, pixelWidth, pixelHeight, widthAngle, heightAngle, cameraDirection = [1.0, 0.0, 0.0]):
        self.h = heightFromGround
        self.widthAngle = widthAngle
        self.heightAngle = heightAngle
        self.pwidth = pixelWidth
        self.pheight = pixelHeight
        self.cameraDirection = cameraDirection

    def getXYAngle( self ):
        unitx = [1.0, 0.0, 0.0]
        xcomp = numpy.dot( unitx, self.cameraDirection ) / numpy.dot( unitx, unitx )
        unity = [0.0, 1.0, 0.0]
        ycomp = numpy.dot( unity, self.cameraDirection ) / numpy.dot( unity, unity )
        return math.atan( ycomp / xcomp )

    def getXZAngle( self ):
        unitx = [1.0, 0.0, 0.0]
        xcomp = numpy.dot( unitx, self.cameraDirection ) / numpy.dot( unitx, unitx )
        unitz = [0.0, 0.0, 1.0]
        zcomp = numpy.dot( unitz, self.cameraDirection ) / numpy.dot( unitz, unitz )
        return math.atan( zcomp / xcomp )

    def getYZAngle( self ):
        unity = [0.0, 1.0, 0.0]
        ycomp = numpy.dot( unity, self.cameraDirection ) / numpy.dot( unity, unity )
        unitz = [0.0, 0.0, 1.0]
        zcomp = numpy.dot( unitz, self.cameraDirection ) / numpy.dot( unitz, unitz )
        return math.atan( zcomp / ycomp )
    
    #check
    def yAngleInView( self, height ):
        a = ( ( float(self.pheight) - float(height) ) / float(self.pheight) ) * self.heightAngle
        return a

    #checked
    def getAngleFromGround( self ):
        b = [self.cameraDirection[0], 0.0, self.cameraDirection[2]]
        a = self.cameraDirection
        cos = numpy.dot(a, b) / (util.vlen(a) * util.vlen(b))
        angleToLevel = math.acos(cos)
        return math.pi/2 - angleToLevel

    #good
    def getAngleFromCamera( self, pheight ):
        return self.getAngleFromGround() - (self.heightAngle / 2.0) + self.yAngleInView( pheight )

    #good
    def getDistanceAtHeight( self, pheight, incline = 0 ):
        A = self.getAngleFromCamera( pheight )
        print("A:", A)
        if A >=math.pi/2:
            return float('nan')
        X = math.pi / 2.0 - incline
        H = math.pi - ( X + A )
        # Law of sines
        x = self.h * math.sin( X ) / math.sin( H )
        print(x)
        return x

    def getAngularSize( self, x, y, objectSize, incline = 0 ):
        A = self.getAngleFromCamera( y )
        d = self.getDistanceAtHeight( y )
        dist = 1.0 if math.isnan(d) else d
        X = math.pi / 2.0 - incline
        farend = dist + objectSize[2]
        # determine distance to end point, calculate AE
        #determine angle to far end's tip from the tip of the close end

        #find angle opposite to dist_to_bot_end
        dist_to_bot_end = math.sqrt(farend ** 2 + self.h ** 2)
        dist_to_top_end = math.sqrt((self.h - objectSize[1]) ** 2 + farend ** 2)
        dist_to_top_close = math.sqrt((self.h - objectSize[1]) ** 2 + dist ** 2)
        dist_to_bot_close = math.sqrt(self.h ** 2 + dist ** 2)
        print("Top:", dist_to_top_close)
        #law of cosines
        #calculate angular size of end bit (why tho?)
        AB = math.acos((dist_to_top_end**2 + dist_to_bot_end**2 - objectSize[1]**2) / (2 * dist_to_bot_end * dist_to_top_end))
        #determine anglular size of the up front bit
        AF = math.acos((dist_to_top_close**2 + dist_to_bot_close**2 - objectSize[1]**2) / (2 * dist_to_top_close * dist_to_bot_close))
        #determine the size of the top
        AT = math.acos((dist_to_top_close**2 + dist_to_top_end**2 - objectSize[2]**2) / (2 * dist_to_top_close * dist_to_top_end))
        print("AT:", AF)

        AH = AF + AT

        #width at top
        '''left_edge_dist = 
        close_edge_dist
        right_edge_dist = 
        AFTW = 
        ASTW = 
        #width at bot
        AFBW = 
        ASBW = '''

        #lazy method
        ratio = AF / objectSize[1]
        w = ratio * objectSize[0]

        return (AT, AF, w, w)

    def getPixelAngSize( self ):
        return self.pheight / self.heightAngle

    # Object dimensions must be in the same dimensions as everything else
    '''def getWindow( self, x, y, objectW, objectH, image, incline = 0 ):
        dist = self.getDistanceAtHeight( y, incline )
        angleWidth = 2.0 * math.asin( (0.5 * objectW / dist) / self.h )# * (1.0/dist)
        angleHeight = 2.0 * math.asin( (0.5 * objectH / dist) / self.h )# * (1.0/dist)
        w = angleWidth * self.pwidth
        pheight = angleHeight * self.pheight
        return image[y:(y + pheight), x:(x + w)]'''
    def getWindow( self, x, y, objectSize, image, incline = 0):
        (topSize, frontSize, width, _)  = self.getAngularSize( x, y, objectSize, incline )
        windW = width * self.getPixelAngSize()
        print("Height:", topSize + frontSize)
        windH = (frontSize + topSize) * self.getPixelAngSize()
        return image[y:(y + windH), x:(x + windW)]

    def getWindows( self, objectSize, image, stepSize, incline = 0 ):
        for y in xrange( 0, image.shape[0], stepSize ):
            for x in xrange( 0, image.shape[1], stepSize ):
                yield ( x, y, self.getWindow( x, y, objectSize, image, incline ) )

    # Constantly update
    def setCameraDirection( self, cameraDirection ):
        self.cameraDirection = cameraDirection
