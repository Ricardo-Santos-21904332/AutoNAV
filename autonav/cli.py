import time
from numpy import (array, fromstring)

from .WLS import wls
from .GTRS import gtrs
from .fileHandlers import _readpathfile
from .plots import plot_trajectories

"""
    Todo: Verify user input
"""


def _main():
    print("##################")
    print("Welcome to Autonav")
    print("##################")
    print("Which algorithm you want to use (Insert the corresponding number)?")
    print("(1) GTRS")
    print("(2) WLS")
    algorithm = input()
    if algorithm == '1' or algorithm == '2':
        default = input("Do you want to use the default anchor number and positions (y/n)?\n")
        if default == 'y' or default == 'Y':
            B = 200
            N = 8
            a_i = array(
                [
                    [0, 0, 0],
                    [0, B, 0],
                    [B / 2, 0, 0],
                    [B / 2, B, 0],
                    [0, 0, B / 8],
                    [0, B, B / 8],
                    [B / 2, 0, B / 8],
                    [B / 2, B, B / 8],
                ]).T
        elif default == 'n' or default == 'N':
            N = int(input("Please insert the number of Anchors (N)\n"))
            a_i = []
            for i in range(0, N):
                aux = input(f"Please insert the positions of anchor {i + 1} in the following format: x1, y1, z1\n")
                a_i.append(fromstring(aux, dtype=int, sep=','))
            a_i = array(a_i).T
        else:
            print("Please insert a valid option!")
        K = int(input("Please insert the number of Measurement Samples (K)\n"))
        sigma = float(input("Please insert the noise level in meters (sigma)\n"))
        filename = input("Please input the path to the Waypoints file\n")
        destinations = _readpathfile(filename)
        if algorithm == '1':
            print("Running GTRS...")
            start_time = time.time()
            estimated_trajectory = gtrs(a_i, N, K, sigma, destinations, [10, 10, 5])
            exec_time = (time.time() - start_time)
            print(f"GTRS finished in {exec_time:0,.2f} seconds.")
            plot_trajectories(destinations, estimated_trajectory)
        elif algorithm == '2':
            print("Running WLS...")
            start_time = time.time()
            estimated_trajectory = wls(a_i, N, K, sigma, destinations, [10, 10, 5])
            exec_time = (time.time() - start_time)
            print(f"WLS finished in {exec_time:0,.2f} seconds.")
            plot_trajectories(destinations, estimated_trajectory)
    else:
        print("Please choose one of the available algorithms!")
