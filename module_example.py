import triangulator

triangulator.setAngularCoordinateSystem('woowee')

x = triangulator.triangulateRaw(0.5, -40.5, 180, 18.5, -30.5, 212.6)


print(x)
