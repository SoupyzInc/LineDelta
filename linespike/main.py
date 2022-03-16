import json
import math
import os
import statistics
import matplotlib.pyplot as plt


def load_data_file(folder, file_name):
    """
    Loads a specified data set.

    Parameters
    ----------
    folder : string
        The folder name of the data set under the data folder.
    file_name : string
        The ending of the specified file name(s) wanted.
    """

    location = os.getcwd() + '\\data\\' + folder
    opened_data = []
    for file in os.listdir(location):
        try:
            if file.endswith(file_name + ".json"):
                with open(location + '\\' + file) as f:
                    opened_data.append(json.load(f))
        except Exception as e:
            raise e

    return opened_data[0]


def circle_union(x1, y1, x2, y2, r):
    """
    Checks if two circles are tangent or intersect.

    Parameters
    ----------
    x1 : float
        The x coordinate of the center of the first circle.
    y1 : float
        The y coordinate of the center of the first circle.
    x2 : float
        The x coordinate of the center of the second circle.
    y2 : float
        The y coordinate of the center of the second circle.
    r : float
        The radius of the circles.
    """
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)  # Distance between centers.

    if d == 2 * r or d == 0:  # Circles tangent
        return True
    elif 0 < d < 2 * r:  # Circles intersect
        return True
    else:
        return False


class LineDelta:
    def __init__(self, graph, folder, file_name):
        self.data = load_data_file(folder, file_name)  # Load data into memory.
        self.graph = graph  # Display graph?

    def __tccc_creation(self):
        # Generate radius value.
        # Needs to be > 1 (distance b/w points next to each other) otherwise only same y-values will touch.
        y_diffs = []
        for i in range(0, len(self.data) - 2):
            y_diffs.append(abs(self.data[i + 1] - self.data[i]))

        quartiles = statistics.quantiles(y_diffs)
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

        # Perform point cloud filtration via reduction of Cech complex.
        # =============================================================
        extrema_ranges = []
        i = 0
        while i < len(extrema) - 2:  # Iterate through extrema, where the circles are.
            start_extrema = extrema[i]  # First extrema (circle) of chain.
            end_extrema = extrema[i]
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
            if start_extrema != end_extrema:
                extrema_ranges.append([start_extrema, end_extrema])
            i += 1

        # Generate circles.
        # =================
        fig, ax = plt.subplots()

        if self.graph:
            for e in extrema:
                circle = plt.Circle((e[0], e[1]), r, color='r', alpha=0.5)
                ax.add_patch(circle)

        # Generate rectangles.
        # ====================
        if self.graph:
            for extrema_pair in extrema_ranges:
                xy = (extrema_pair[0][0], extrema_pair[0][1])
                width = abs(extrema_pair[1][0] - extrema_pair[0][0])
                height = extrema_pair[1][1] - extrema_pair[0][1]
                rectangle = plt.Rectangle(xy, width, height, color='g', alpha=0.5)
                ax.add_patch(rectangle)

        # Show complex.
        # =============
        if self.graph:
            N = len(self.data)  # The number of points
            t = []
            for i in range(1, len(self.data) + 1):
                t.append(i)
            ax.plot(t, self.data)
            plt.show()
            plt.close()

        return extrema_ranges

    def __tccc_filtration(self):
        # Generate radius value.
        # Needs to be > 1 (distance b/w points next to each other) otherwise only same y-values will touch.
        y_diffs = []
        for i in range(0, len(self.data) - 2):
            y_diffs.append(abs(self.data[i + 1] - self.data[i]))

        quartiles = statistics.quantiles(y_diffs)
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

        # Perform point cloud filtration via reduction of Cech complex.
        # =============================================================
        extrema_ranges = []
        i = 0
        while i < len(extrema) - 2:  # Iterate through extrema, where the circles are.
            start_extrema = extrema[i]  # First extrema (circle) of chain.
            end_extrema = extrema[i]
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
            if start_extrema != end_extrema:
                extrema_ranges.append([start_extrema, end_extrema])
            i += 1

        fig, ax = plt.subplots()

        # Generate noise-reduced data.
        # ============================
        noise_reduced_data = self.data
        for extrema_pair in extrema_ranges:
            for i in range(extrema_pair[0][0] - 1, extrema_pair[1][0]):
                noise_reduced_data[i] = extrema_pair[0][1]

        if self.graph:
            t = []
            for i in range(1, len(noise_reduced_data) + 1):
                t.append(i)
                ax.plot(t, noise_reduced_data)
                plt.show()

        return noise_reduced_data


def main():
    # folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp', 'climate_tmax',
    #            'eeg_10000', 'eeg_2500', 'eeg_500', 'flights', 'nz_tourist',
    #            'stock_price', 'stock_volume', 'unemployment']

    ls = LineDelta(True, 'stock_price', 'aapl_price')
    ls.tccc_creation()
    ls.tccc_filtration()


if __name__ == '__main__':
    main()
