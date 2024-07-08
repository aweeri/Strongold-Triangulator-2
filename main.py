import numpy as np
import math

"""

# Distance and midpoint
def getDistance(pos0, pos1):
    return math.sqrt((pos0[0]-pos1[0])**2 + (pos0[1]-pos1[1])**2)
def midpoint(pos0, pos1):
    return (pos0[0]+pos1[0])/2, (pos0[1]+pos1[1])/2
def calculateTriHeight(base, theta):
  theta_radians = math.radians(theta)
  height = base * math.tan(theta_radians)
  return round(height,2)

"""

def parseCmd(cmd: str):
    data = cmd[42:].split(" ")
    data = [float(i) for i in data]
    data[3] = round((data[3] + 180) % 360, 2)
    del data[4]
    return data

# Main triangulation
def parallax(pos0, pos1, angle1, angle2):
    a1 = weirdToCardinal(angle1)
    a2 = weirdToCardinal(angle2)
    mid = midpoint(pos0, pos1)
    dist = getDistance(pos0[0], pos0[1], pos1[0], pos1[1])
    height = calculateTriHeight(dist, )


"""

TEST VALUES:
/execute in minecraft:overworld run tp @s 2725.51 69.00 5195.53 -854.19 -32.02
/execute in minecraft:overworld run tp @s 2818.45 64.00 5254.47 -857.89 -32.05

ESTIMATION SHOULD BE CLOSE TO:
3930 ~ 4023

"""


def main():
    cmd = input("Enter the command generated by MC: ")
    data = parseCmd(cmd)
    print(data)


main()

