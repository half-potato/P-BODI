import numpy
import cv2
import math
import util

class DyHeatmap:
    # Store vectors in chunks
    def __init__(self, chunkSize):
        self.chunkSize = chunkSize
        self.chunks = [[[]]]

    def getChunksCoordsAt(self, x, y, z, radius):
        cx = x / chunkSize
        cy = y / chunkSize

        rx = (x + radius) / chunkSize
        lx = (x - radius) / chunkSize
        ty = (y + radius) / chunkSize
        by = (y - radius) / chunkSize

        trc = [math.ceil(rx), math.ceil(ty)]
        tlc = [math.floor(lx), math.ceil(ty)]
        brc = [math.ceil(rx), math.floor(by)]
        blc = [math.floor(lx), math.floor(by)]

        #check for dups
        chunks = filter(lambda x, y : x[0]!=y[0] and x[1]!=y[1], [trc, tlc, brc, blc])
        if chunks[0] == chunks[len(chunks) - 1]:
            chunks = chunks[0:(len(chunks)-1)]

        return chunks

    def getChunksAt(x, y, z, radius):
        cc = self.getChunksCoordsAt(x, y, z, radius)
        return map(lambda x:self.chunks[x[0]][x[1]], cc)

    def getVecsAt(self, x, y, z, radius):
        chunks = self.getChunksAt(x, y, z, radius)
        vecs = []
        for c in chunks:
            for i in c:
                if util.vlen(numpy.subtract(i[0:3], [x, y, z])) > radius:
                    vecs[len(vecs)] = i
        
        return vecs

    def getClosestVec(self, x, y, z, maxSearchRadius):
        vecs = self.getVecsAt(x, y, z, maxSearchRadius)
        curClosestLen = 0.0
        curClosestVec = None
        for v in vecs:
            if util.vlen(numpy.subtract(i, [x, y, z])) < curClosestLen:
                curClosestLen = util.vlen(numpy.subtract(i, [x, y, z]))
                curClosestVec = v

        return curClosestVec

    def getConvergedVec(self, x, y, z, maxSearchRadius):
        vecs = getVecsAt(x, y, z, maxSearchRadius)
        m = [0, 0, 0]
        diffs = []
        for v in vecs:
            diff = numpy.subtract([x, y, z], v[0:3])
            corrected = numpy.add(diff, v[4:6])
            m = numpy.add(m, corrected)
            diffs.append(diff)
        return (util.normalize(m), diffs)

    def addVec(self, x, y, z, vec):
        chunk = self.getChunksAt(x, y, z, 0)
        self.chunks[chunk[0]][chunk[1]].append(vec)
