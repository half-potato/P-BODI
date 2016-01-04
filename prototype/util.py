import math
import numpy

def vlen( a ):
    return math.sqrt(reduce(lambda x,y:x+y, map(lambda x,y:x*y, a, a)))

#radians
def normalizeAngle(radians):
    fullRevos = math.floor(radians / (2.0 * math.pi))
    return radians - (2.0 * math.pi * fullRevos)

def normalize(vec):
    return numpy.divide(vec, vlen(vec))

def acos(a, b):
    return math.acos(numpy.dot(a, b) / (vlen(a) * vlen(b)))
