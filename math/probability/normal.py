#!/usr/bin/env python3
"""Module that defines the Normal distribution class"""


class Normal:
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """Initializes the Normal distribution

        Args:
            data (list): data to be used to estimate the distribution
            mean (float): the mean of the distribution
            stddev (float): the standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            total = 0
            for value in data:
                total += value
            self.mean = float(total / len(data))
            variance = 0
            for value in data:
                variance += (value - self.mean) ** 2
            variance /= len(data)
            self.stddev = float(variance ** 0.5)
