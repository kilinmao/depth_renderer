import math
import numpy as np


if __name__ == '__main__':
    randius = 2
    azimuth = [*np.arange(math.radians(-180),math.radians(180),math.radians(15))]
    elevation = [math.radians(-15), math.radians(-30), math.radians(-45)]
    distance = [randius/math.cos(x) for x in elevation ]

    # get Azimuth, Elevation angles
    # Azimuth varies from -pi to pi
    # Elevation from 0 to pi/2
    with open('./view_points.txt', 'w+') as f:
        for i, _ in enumerate(elevation):
            for a in azimuth:
                f.writelines(f'{a} {elevation[i]} 0. {distance[i]}\n')


