import numpy as np
import math
# Cardinal conversions
def weirdToCardinal(angle: float):
    return 180+angle
def cardinalToWeird(angle: float):
    return 180-angle

# Distance and midpoint
def getDistance(pos0, pos1):
    return math.sqrt((pos0[0]-pos1[0])**2 + (pos0[1]-pos1[1])**2)
def midpoint(pos0, pos1):
    return (pos0[0]+pos1[0])/2, (pos0[1]+pos1[1])/2

# Main triangulation
def parallax(pos0, pos1, angle1, angle2):
    a1 = weirdToCardinal(angle1)
    a2 = weirdToCardinal(angle2)
    mid = midpoint(pos0, pos1)
    dist = getDistance(pos0[0], pos0[1], pos1[0], pos1[1])
    height = calculateTriHeight(dist, )

import math

def calculateTriHeight(base, theta):
  theta_radians = math.radians(theta)
  height = base * math.tan(theta_radians)
  return round(height,2)


print(parallax((0, -40), (20, -30), 0, 33))

"""