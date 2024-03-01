"""This file contains the velocity.py tests."""

import pytest
from numpy import array
from numpy.testing import assert_allclose, assert_array_equal

from autonav.velocity import _velocity


@pytest.mark.critical()
def test_velocity_higher_distance():
    """Test velocity function in normal conditions when the error_norm is higher than 1."""
    current_position = array([0, 0, 5])
    destination_position = array([10, 10, 5])
    param_max_velocity: int = 2
    param_reach_distance: int = 4
    param_smooth_factor: int = 2
    estimated_velocity = _velocity(
        current_position, destination_position, param_max_velocity, param_reach_distance, param_smooth_factor
    )
    assert_allclose(estimated_velocity, array([1.41421356, 1.41421356, 0]))


@pytest.mark.critical()
def test_velocity_lower_distance():
    """Test velocity function in normal conditions when the error_norm is lower than the param_reach_distance."""
    current_position = array([8, 10, 5])
    destination_position = array([10, 10, 5])
    param_max_velocity: int = 2
    param_reach_distance: int = 4
    param_smooth_factor: int = 2
    estimated_velocity = _velocity(
        current_position, destination_position, param_max_velocity, param_reach_distance, param_smooth_factor
    )
    assert_allclose(estimated_velocity, array([0.5, 0, 0]))


@pytest.mark.critical()
def test_velocity_reached_destination():
    """Test velocity function when reaching the destination."""
    current_position = array([10, 10, 5])
    destination_position = array([10, 10, 5])
    param_max_velocity: int = 2
    param_reach_distance: int = 4
    param_smooth_factor: int = 2
    estimated_velocity = _velocity(
        current_position, destination_position, param_max_velocity, param_reach_distance, param_smooth_factor
    )
    assert_array_equal(estimated_velocity, array([0, 0, 0]))


@pytest.mark.parametrize(
    (
        "current_position",
        "destination_position",
        "param_max_velocity",
        "param_reach_distance",
        "param_smooth_factor",
        "expected_error",
    ),
    [
        (array(["a", "a", "a"]), array([10, 10, 5]), "a", "a", "a", TypeError),
        (array([10, 10, 5]), array(["a", "a", "a"]), "a", "a", "a", TypeError),
    ],
)
def test_velocity_invalid_parameters(
    current_position,
    destination_position,
    param_max_velocity,
    param_reach_distance,
    param_smooth_factor,
    expected_error,
):
    """Test velocity function when the parameters are incorrect."""
    with pytest.raises(expected_error):
        _velocity(current_position, destination_position, param_max_velocity, param_reach_distance, param_smooth_factor)
