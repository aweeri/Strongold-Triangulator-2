import math
angSys = 'f3Facing_Offset180'


"""

USE EXAMPLES

print(setAngularCoordinateSystem('cardinal_0to360'))
print(triangulateRaw(0.5, -40.5, 180, 18.5, -30.5, 212.6))


print(setAngularCoordinateSystem('f3Facing_Offset180'))
print(triangulateRaw(0.5, -40.5, 0, 18.5, -30.5, 32.6))


print(setAngularCoordinateSystem('relativeFacing_SouthCentered'))
print(triangulateRaw(0.5, -40.5, -360, 18.5, -30.5, -327.45 ))


print(parseAndTriangulate("/execute in minecraft:overworld run tp @s 18.77 -59.00 -30.27 -687.14 3.15",
                          "/execute in minecraft:overworld run tp @s -0.52 -59.00 -40.64 -719.96 2.86"))

"""


# use previously calculated Magic Ratios™ to increment given values in the Minecraft coordinate system
def __trigIterate__(x, z, theta, cosinemagic, sinemagic):
    x = x + sinemagic
    z = z - cosinemagic
    return(x, z)

# calculate distance from point A to point B
def __distance__(x_A, z_A, x_B, z_B):
    return math.sqrt((x_A-x_B)**2 + (z_A-z_B)**2)

# parse generated F3+C game output 
def __parseCmd__(cmd: str):
    data = cmd[42:].split(" ")
    data = [float(i) for i in data]
    data[3] = round((data[3] + 180) % 360, 2)
    del data[4], data[1]
    return data


def setAngularCoordinateSystem(sel: str):
    global angSys
    """
    Accepted Selections:
        f3Facing_Offset180
        cardinal_0to360
        relativeFacing_SouthCentered


    f3Facing_Offset180: This reflects the method used by the F3 screen, 
        indicating cardinal directions (north, south, east, west) but offset by -180 degrees.

    cardinal_0to360: This represents the standard cardinal direction system (0-360 degrees) with north at 0 degrees.

    relativeFacing_SouthCentered: This captures the method used by F3+C, where directions are relative to the south 
        and rotations are additive, leading to values outside the typical 0-360 degree range.

    """
    if sel == 'f3Facing_Offset180':
        angSys = 'f3Facing_Offset180'
        return f"Set to {angSys}"
    
    elif sel == 'cardinal_0to360':
        angSys = 'cardinal_0to360'
        return f"Set to {angSys}"
    
    elif sel == 'relativeFacing_SouthCentered':
        angSys = 'relativeFacing_SouthCentered'
        return f"Set to {angSys}"
    
    else:
        angSys = 'f3Facing_Offset180'
        print(f"Invalid selection: \"{sel}\". try one of below:\nf3Facing_Offset180 [default] \ncardinal_0to360\nrelativeFacing_SouthCentered")
        return (f"Invalid selection: \"{sel}\". try one of below:\nf3Facing_Offset180\ncardinal_0to360\nrelativeFacing_SouthCentered")


def triangulateRaw(x_A, z_A, theta_A, x_B, z_B, theta_B, doShowAccuracy: bool = False):
    global angSys

    if angSys == 'relativeFacing_SouthCentered' or angSys == 'f3Facing_Offset180':
        theta_A, theta_B = theta_A - 180, theta_B - 180

    elif angSys == 'cardinal_0to360':
        pass

    theta_A, theta_B = math.radians(theta_A), math.radians(theta_B)
    cos_A, sin_A = math.cos(theta_A), math.sin(theta_A)
    cos_B, sin_B = math.cos(theta_B), math.sin(theta_B)
    prev_dist = dist = 60000000
    while True:
        incr = dist > prev_dist
        #print(f"{round(x_A)}\t{round(z_A)}\t{round(x_B)}\t{round(z_B)}\t{round(dist)}\t{incr}")

        x_A, z_A = __trigIterate__(x_A, z_A, theta_A, cos_A, sin_A)
        x_B, z_B = __trigIterate__(x_B, z_B, theta_B, cos_B, sin_B)
        
        prev_dist = dist
        dist = __distance__(x_A, z_A, x_B, z_B)

        if incr and doShowAccuracy:
            return round(x_A), round(z_A), round(dist)
        if incr and not doShowAccuracy:
            return round(x_A), round(z_A)


def parseAndTriangulate(str1: str, str2: str, doShowAccuracy: bool = False):
    data1 = __parseCmd__(str1)
    data2 = __parseCmd__(str2)
    x_A, z_A = data1[0], data1[1]
    theta_A = data1[2]
    x_B, z_B = data2[0], data2[1]
    theta_B = data2[2]

    theta_A, theta_B = math.radians(theta_A), math.radians(theta_B)
    cos_A, sin_A = math.cos(theta_A), math.sin(theta_A)
    cos_B, sin_B = math.cos(theta_B), math.sin(theta_B)
    prev_dist = dist = 60000000
    while True:
        incr = dist > prev_dist
        #print(f"{round(x_A)}\t{round(z_A)}\t{round(x_B)}\t{round(z_B)}\t{round(dist)}\t{incr}")

        x_A, z_A = __trigIterate__(x_A, z_A, theta_A, cos_A, sin_A)
        x_B, z_B = __trigIterate__(x_B, z_B, theta_B, cos_B, sin_B)
        
        prev_dist = dist
        dist = __distance__(x_A, z_A, x_B, z_B)

        if incr and doShowAccuracy:
            return round(x_A), round(z_A), round(dist)
        if incr and not doShowAccuracy:
            return round(x_A), round(z_A)

