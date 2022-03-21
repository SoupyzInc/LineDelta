import math
import statistics


class LineDelta:
    """
    The LineDelta framework.

    Methods
    -------
    __init__(self, data)
        Instantiates LineDelta class and assigns data to analyze.
    __circle_union(self, x1, y1, x2, y2, r)
        Checks if two circles are tangent or intersect.
    occ(self)
        Finds the ordered Cech complex of a data set.
    occs(self, ordered_cech_complex)
        Performs ordered Cech complex substitution on a data set.
    """

    def __init__(self, data):
        """
        Instantiates LineDelta class and assigns data to analyze.

        Parameters
        ----------
        data : float[]
            The data list to analyze.
        """

        self.data = data

    def __circle_union(self, x1, y1, x2, y2, r):
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

    # -------------
    # | FEATURE 1 |
    # -------------
    def occ(self):
        """
        Finds the ordered Cech complex of a data set.

        Returns
        -------
        The ordered Cech complex.
        """

        # Generate radius value.
        # ----------------------
        y_diffs = []
        for i in range(0, len(self.data) - 2):  # Get all y differences of adjacent points.
            y_diffs.append(abs(self.data[i + 1] - self.data[i]))

        quartiles = statistics.quantiles(y_diffs)  # Find median value.
        y_diff_mean = quartiles[1]  # Median of y_diffs
        r = quartiles[1]  # Median of y_diffs

        # Get extrema of data.
        # --------------------
        extrema = [[1, self.data[0]]]  # [index of extrema (x), value of extrema (y)]

        for i in range(1, len(self.data) - 2):
            if self.data[i - 1] < self.data[i] and self.data[i + 1] < self.data[i]:  # local max
                extrema.append([i + 1, self.data[i]])
            elif self.data[i - 1] > self.data[i] and self.data[i + 1] > self.data[i]:  # local min
                extrema.append([i + 1, self.data[i]])

        extrema.append([len(self.data), self.data[-1]])

        # Find OCC.
        # ---------
        ordered_cech_complex = []
        i = 0
        while i < len(extrema) - 2:  # Iterate through extrema, where the circles are.
            start_extrema = extrema[i]  # First extrema (circle) of chain.
            end_extrema = extrema[i]
            for k in range(i, len(extrema) - 2):  # Iterate until complex chain is broken.
                c = 0  # Offset.
                d = 1  # Length of chain.
                if self.__circle_union(extrema[k + c][0] * y_diff_mean, extrema[k + c][1],
                                       extrema[k + d][0] * y_diff_mean, extrema[k + d][1], r):
                    # Adjacent extrema has union, continue search with next extrema.
                    end_extrema = extrema[k + d]
                    c += 1
                    d += 1
                else:
                    # Adjacent extrema has no union, chain has ended.
                    break

                i = k + c  # Continue to search at extrema after found chain.
            if start_extrema != end_extrema:
                ordered_cech_complex.append([start_extrema, end_extrema])
            i += 1

        return ordered_cech_complex

    def occs(self):
        """
        Performs ordered Cech complex substitution on a data set.

        Returns
        -------
        The modified data with noise removed.
        """

        ordered_cech_complex = self.occ()

        noise_reduced_data = self.data

        for extrema_pair in ordered_cech_complex:
            x1 = extrema_pair[0][0]
            y1 = extrema_pair[0][1]
            xn = extrema_pair[1][0]
            yn = extrema_pair[1][1]
            n = xn - x1 + 1
            m = (yn - y1) / n

            if n == 2:  # 2-ordered Cech complex
                noise_reduced_data[xn - 1] = y1
            else:  # (>2)-ordered Cech complex
                # Replace intermediate values with line segment between p1 and pn
                for i in range(x1 + 1, xn + 1):
                    noise_reduced_data[i - 1] = (m * i) + (-(m * x1) + y1)

        return noise_reduced_data
