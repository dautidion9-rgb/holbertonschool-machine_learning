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

    def z_score(self, x):
        """Calculates the z-score of a given x-value

        Args:
            x (float): the x-value

        Returns:
            float: the z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """Calculates the x-value of a given z-score

        Args:
            z (float): the z-score

        Returns:
            float: the x-value of z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """Calculates the value of the PDF for a given x-value

        Args:
            x (float): the x-value

        Returns:
            float: the PDF value for x
        """
        e = 2.7182818285
        pi = 3.1415926536
        exponent = -((x - self.mean) ** 2) / (2 * self.stddev ** 2)
        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)
        return coefficient * e ** exponent

    def cdf(self, x):
        """Calculates the value of the CDF for a given x-value

        Args:
            x (float): the x-value

        Returns:
            float: the CDF value for x
        """
        pi = 3.1415926536
        arg = (x - self.mean) / (self.stddev * 2 ** 0.5)
        erf = (2 / pi ** 0.5) * (arg - arg ** 3 / 3 + arg ** 5 / 10
                                 - arg ** 7 / 42 + arg ** 9 / 216)
        return (1 + erf) / 2
