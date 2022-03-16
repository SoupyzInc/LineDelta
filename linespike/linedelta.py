import math
import statistics


def circle_union(x1, y1, x2, y2, r):
    """
    Checks if two circles are tangent or intersect.

    Parameters
    ----------
    x1 : float
        The x-coordinate of the center of the first circle.
    y1 : float
        The y-coordinate of the center of the first circle.
    x2 : float
        The x-coordinate of the center of the second circle.
    y2 : float
        The y-coordinate of the center of the second circle.
    r : float
        The radius of the circles.

    Returns
    -------
    Boolean True if the circles are tangent or intersect, False otherwise.
    """
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Distance between centers.

    if d == 2 * r or d == 0:  # Circles tangent
        return True
    elif 0 < d < 2 * r:  # Circles intersect
        return True
    else:
        return False


class LineDelta:
    def __init__(self, data):
        self.data = data

    def tcccf(self):
        """
        Performs time conscious cech complex filtration on a time series to remove noisy, non-spiky features.

        Returns
        -------
        The data with noise removed.
        """

        # Generate radius value.
        # Needs to be > 1 (distance b/w points next to each other) otherwise only same y-values will touch.
        y_diffs = []
        for i in range(0, len(self.data) - 2):  # Get all y differences of adjacent points.
            y_diffs.append(abs(self.data[i + 1] - self.data[i]))

        quartiles = statistics.quantiles(y_diffs)  # Find median value.
        r = quartiles[1]  # Median of y_diffs

        # Get extrema of data.
        # ====================
        extrema = [[1, self.data[0]]]  # [index of extrema (x), value of extrema (y)]

        for i in range(1, len(self.data) - 2):
            if self.data[i - 1] < self.data[i] and self.data[i + 1] < self.data[i]:  # local max
                extrema.append([i + 1, self.data[i]])
            elif self.data[i - 1] > self.data[i] and self.data[i + 1] > self.data[i]:  # local min
                extrema.append([i + 1, self.data[i]])

        extrema.append([len(self.data), self.data[-1]])

        # Perform filtration.
        # ===================
        extrema_ranges = []
        i = 0
        while i < len(extrema) - 2:  # Iterate through extrema, where the circles are.
            start_extrema = extrema[i]  # First extrema (circle) of chain.
            end_extrema = extrema[i]  # Default pair is none
            for k in range(i, len(extrema) - 2):  # Iterate until complex chain is broken.
                c = 0  # Offset.
                d = 1  # Length of chain.
                if circle_union(extrema[k + c][0], extrema[k + c][1], extrema[k + d][0], extrema[k + d][1], r):
                    # Adjacent extrema has union, continue search with next extrema.
                    end_extrema = extrema[k + d]
                    c += 1
                    d += 1
                else:
                    # Adjacent extrema has no union, chain has ended.
                    break

                i = k + c  # Continue to search at extrema after found chain.
            if start_extrema != end_extrema:  # Do not add to list if the chain is just one point.
                extrema_ranges.append([start_extrema, end_extrema])
            i += 1

        # Generate noise-reduced data.
        # ============================
        noise_reduced_data = self.data
        for extrema_pair in extrema_ranges:
            for i in range(extrema_pair[0][0] - 1, extrema_pair[1][0]):
                noise_reduced_data[i] = extrema_pair[0][1]

        return noise_reduced_data
