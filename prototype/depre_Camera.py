import math
import numpy
import cv2

class PBOD:
    # angle refers to the view
    def __init__( self, heightFromGround, pixelWidth, pixelHeight, widthAngle, heightAngle, cameraDirection = [1, 0, 0]):
        self.h = heightFromGround
        self.widthAngle = widthAngle
        self.heightAngle = heightAngle
        self.pwidth = pixelWidth
        self.pheight = pixelHeight
        self.cameraDirection = cameraDirection

    def getXYAngle( self ):
        unitx = [1, 0, 0]
        xcomp = numpy.dot( unitx, self.cameraDirection ) / numpy.dot( unitx, unitx )
        unity = [0, 1, 0]
        ycomp = numpy.dot( unity, self.cameraDirection ) / numpy.dot( unity, unity )
        return math.atan( ycomp / xcomp )

    def getXZAngle( self ):
        unitx = [1, 0, 0]
        xcomp = numpy.dot( unitx, self.cameraDirection ) / numpy.dot( unitx, unitx )
        unitz = [0, 0, 1]
        zcomp = numpy.dot( unitz, self.cameraDirection ) / numpy.dot( unitz, unitz )
        return math.atan( zcomp / xcomp )

    def getYZAngle( self ):
        unity = [0, 1, 0]
        ycomp = numpy.dot( unity, self.cameraDirection ) / numpy.dot( unity, unity )
        unitz = [0, 0, 1]
        zcomp = numpy.dot( unitz, self.cameraDirection ) / numpy.dot( unitz, unitz )
        return math.atan( zcomp / ycomp )

    def yAngleInView( self, height ):
        return ( height / self.pheight ) * self.heightAngle

    def getAngleFromGround( self ):
        b = [self.cameraDirection[0], 0, self.cameraDirection[2]]
        a = self.cameraDirection
        return math.acos( b / a )
    
    # Negative incline for looking up
    def getDistanceAtHeight( self, pheight ):
        angleInView = self.getAngleFromGround( self.cameraDirection ) - self.heightAngle / 2 + self.yAngleInView( pheight )
        X = 90
        H = 180 - ( X + angleInView )
        # Law of sines
        x = self.h * math.sin( X ) / math.sin( H )
        return x

    # Object dimensions must be in the same dimensions as everything else
    def getWindow( self, x, y, objectW, objectH, image ):
        dist = getDistanceAtHeight( self, self.cameraDirection, y )
        angleWidth = 2 * math.asin( (0.5 * objectW) / h ) * (1/dist)
        angleHeight = 2 * math.asin( (0.5 * objectH) / h ) * (1/dist)
        pwidth = angleWidth * self.pwidth
        pheight = angleHeight * self.pheight
        return image[y:(y + pheight), x:(x + pwidth)]

    def getWindows( self, objectW, objectH, image, stepSize ):
        for y in xrange( 0, image.shape[0], stepSize ):
            for x in xrange( 0, image.shape[1], stepSize ):
                yield ( x, y, self.getWindow( x, y, objectW, objectH, image )

    # Constantly update
    #def setCameraDirection( self, cameraDirection ):
        #self.cameraDirection = cameraDirection

def calcFOV( focalLengthMultiplier, sensorSizeX, sensorSizeY ):
    w = 2 * math.atan( sensorSizeX / ( 2 * focalLengthMultiplier ))
    h = 2 * math.atan( sensorSizeY / ( 2 * focalLengthMultiplier ))
    return w, h

def calcNormFOV( sensorSizeX, sensorSizeY ):
    normal = math.sqrt( sensorSizeX ** 2 + sensorSizeY ** 2 )
    return calcFOV( normal, sensorSizeX, sensorSizeY )
