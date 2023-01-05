import os
import anvil
import math

def findChunk(x0, y0, z0):
    return math.floor(x0 / 16), math.floor(z0 / 16)

def findRegion(x, z):
    x, y = (math.floor(x / 32), math.floor(z / 32))
    return f'r.{x}.{y}.mca'

def createList(s, start, end):
    blocks = dict()
    for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
        for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            for z in range(min(start[2], end[2]), max(start[2], end[2]) + 1):
                chunkX, chunkZ = findChunk(x, y, z)
                path = s + "\\region\\" + findRegion(chunkX, chunkZ)
                region = anvil.Region.from_file(path)
                chunk = anvil.Chunk.from_region(region, chunkX, chunkZ)
                block = chunk.get_block(x % 16, y, z % 16)

                block = str(block)[16:-1]
                if block not in blocks:
                    blocks[block] = 1
                else:
                    blocks[block] += 1
    return blocks