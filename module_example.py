import triangulator

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

triangulator.setAngularCoordinateSystem('cardinal_0to36')




"""

    Takes in raw minecraft X,Z coordinates and angles (in a previously configured angular coordinate system) and then returns triangulated coordinates.

    Can be configured to either return accuracy or not by changing the last argument to True/False

"""
x = triangulator.triangulateRaw(0.5, -40.5, 180, 
                                18.5, -30.5, 212.6, 
                                True) # X1, Z1, A1, X2, Z2, A2, False/True (decides whether to return accuracy)


"""

    Takes in commands exported from minecraft via the F3+C keybind and then returns triangulated coordinates.

    Can be configured to either return accuracy or not by changing the last argument to True/False

"""

y = triangulator.parseAndTriangulate("/execute in minecraft:overworld run tp @s 2725.51 69.00 5195.53 -854.19 -32.02",
                                     "/execute in minecraft:overworld run tp @s 2818.45 64.00 5254.47 -857.89 -32.05" , False)

print(x)
