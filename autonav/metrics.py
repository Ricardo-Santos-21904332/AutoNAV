"""This module contains the metrics functions."""

from math import sqrt


def armse(estimated_trajectory, true_trajectory):
    """This function computes the average root mean squared error between the true and estimated trajectory of the UAV.

    Args:
        estimated_trajectory: The estimated position of the UAV.
        true_trajectory: The true position of the UAV.

    Returns:
        The average root mean squared error between the true and the estimated positions of the UAV.
    """
    rmse = []
    armse = 0
    # Trajectories must have the same length for comparison
    if len(estimated_trajectory) == len(true_trajectory):
        for i in range(len(estimated_trajectory)):
            norm = sqrt(
                (true_trajectory[i][0] - estimated_trajectory[i][0]) ** 2
                + (true_trajectory[i][1] - estimated_trajectory[i][1]) ** 2
                + (true_trajectory[i][2] - estimated_trajectory[i][2]) ** 2
            )
            rmse.append(sqrt(norm))

        armse = sum(rmse) / len(rmse)
    return armse
