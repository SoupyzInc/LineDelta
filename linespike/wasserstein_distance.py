import json
import math
import os
import gudhi.wasserstein

from sklearn.metrics.pairwise import pairwise_distances
from scipy import sparse
from scipy.stats import wasserstein_distance

from ripser import ripser
from persim import plot_diagrams

import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse
import time

from ripser import ripser
from persim import plot_diagrams


class LineSpikeDistance:
    """
    A class to hold all methods to perform an analysis of a time series' spikiness, using the LineSpike framework.

    Methods
    -------
    setup(self, location, file_name)
        Sets up the LineSpike environment and runs the LineSpike framework.
    get_data(self, location, file_name)
        Loads the data sets specified in setup().
    find_extrema(self)
        Finds all local extrema in the data set, including boundaries.
    partition(self, arr, low, high)
        Partitions and sorts a data set for quicksort.
    quicksort(self, arr, low, high)
        An implementation of the quicksort algorithm.
    lower_star_filtration(self)
        Implements lower-star filtration on the data set to generate a merge tree and persistence diagram.
    generate_persistence_diagram(self)
        Generates a persistence diagram from the lower-star filtration.
    """

    data = []
    extrema = []
    C = []
    file_output_name = ''
    point_cloud = []

    def setup(self, location):
        # Load data
        self.get_data(location)

        # print(self.data)
        #
        # # Isolate extrema
        # self.find_extrema()
        # print('\nLoaded extrema -------------------')
        # print(self.extrema)
        #
        # # Sort extrema
        # self.quicksort(self.extrema, 0, len(self.extrema) - 1)
        # print('\nSorted extrema -------------------')
        # print(self.extrema)
        #
        # # Check sort
        # failed = False
        # for i in range(0, len(self.extrema) - 2):
        #     if self.extrema[i][0] > self.extrema[i + 1][0]:
        #         print('FAIL: ' + str(self.extrema[i][0]) + ' is > ' + str(self.extrema[i + 1][0]))
        #         failed = True
        #         break
        #
        # if not failed:
        #     print('SUCCESS')

        # self.lower_star_filtration()
        # self.generate_persistence_diagram()

    def compare(self, data_loc_a, data_file_a, data_loc_b, data_file_b):
        pd_a = self.lower_star_filtration(data_loc_a, data_file_a)
        pd_b = self.lower_star_filtration(data_loc_b, data_file_b)

        return gudhi.wasserstein.wasserstein_distance(np.array(pd_a), np.array(pd_b), order=1., internal_p=2.)
        # print(w_distance)

    def load_data(self, location, file_name):
        """
        Loads a specified data set.

        Parameters
        ----------
        location : string
            The folder name of the data set under tests/data.
        file_name : string
            The ending of the specified file name(s) wanted.
        """

        location = os.getcwd() + '\\data\\' + location
        for file in os.listdir(location):
            try:
                if file.endswith(file_name + ".json"):
                    self.data.clear()
                    # print(file)
                    with open(location + '\\' + file) as f:
                        self.data.append(json.load(f))
            except Exception as e:
                raise e

        self.data = self.data[0]

        # folder = location
        # location = os.getcwd() + '\\data\\' + location
        # for file in os.listdir(location):
        #     try:
        #         if file.endswith(".json"):
        #             print('Working on: ' + file + ' --------------------')
        #             self.file_output_name = 'imgs/' + folder + ' - ' + file[0:len(file)-5] + '.png'
        #             print(self.file_output_name)
        #             with open(location + '\\' + file) as f:
        #                 self.data.append(json.load(f))
        #
        #             self.data = self.data[0]
        #             self.lower_star_filtration()
        #             self.data.clear()
        #     except Exception as e:
        #         raise e

        # self.data = self.data[0]

    def find_extrema(self):
        """
        Finds all local extrema in the data set, including boundaries.
        """

        self.extrema.append([self.data[0], 1])

        c = 2
        for i in range(1, len(self.data) - 2):
            if self.data[i - 1] < self.data[i] and self.data[i + 1] < self.data[i]:  # local max
                self.extrema.append([self.data[i], c])
                c += 1
            elif self.data[i - 1] > self.data[i] and self.data[i + 1] > self.data[i]:  # local min
                self.extrema.append([self.data[i], c])
                c += 1

        self.extrema.append([self.data[-1], c])

    def partition(self, arr, low, high):
        """
        Partitions and sorts a data set for quicksort.
        """

        i = (low - 1)
        pivot = arr[high][0]

        for j in range(low, high):
            if arr[j][0] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort(self, arr, low, high):
        """
        An implementation of the quicksort algorithm.
        """

        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)

            self.quicksort(arr, low, pi - 1)
            self.quicksort(arr, pi + 1, high)

    def lower_star_filtration(self, data_loc, data_file):
        """
        Implements lower-star filtration on the data set to generate a merge tree and persistence diagram.
        """
        # LOAD DATA -----------------------------
        self.load_data(data_loc, data_file)

        N = len(self.data)  # The number of points
        t = np.linspace(0, N, N)
        x = self.data
        # x = np.cos(2*np.pi*t) + t
        # self.data = x
        # x = math.pow(t, 3)

        # plt.plot(t, x)
        # plt.title("$\\cos(2 pi t) + t$")
        # plt.xlabel("t")
        # plt.show()

        # Add edges between adjacent points in the time series, with the "distance"
        # along the edge equal to the max value of the points it connects
        I = np.arange(N - 1)
        J = np.arange(1, N)
        V = np.maximum(x[0:-1], x[1::])
        # Add vertex birth times along the diagonal of the distance matrix
        I = np.concatenate((I, np.arange(N)))
        J = np.concatenate((J, np.arange(N)))
        V = np.concatenate((V, x))
        # Create the sparse distance matrix
        D = sparse.coo_matrix((V, (I, J)), shape=(N, N)).tocsr()
        dgm0 = ripser(D, maxdim=0, distance_matrix=True)['dgms'][0]
        dgm0 = dgm0[dgm0[:, 1] - dgm0[:, 0] > 1e-3, :]
        allgrid = np.unique(dgm0.flatten())
        allgrid = allgrid[allgrid < np.inf]
        xs = np.unique(dgm0[:, 0])
        ys = np.unique(dgm0[:, 1])
        ys = ys[ys < np.inf]

        return dgm0

        # Plot the time series and the persistence diagram
        # plt.figure(figsize=(12, 6))
        # ylims = [min(self.data) - 1, max(self.data) + 1]
        # # ylims = [-1, 6.5]
        # plt.subplot(121)
        # plt.plot(t, x)
        # ax = plt.gca()
        # ax.set_yticks(allgrid)
        # ax.set_xticks([])
        # plt.ylim(ylims)
        # # plt.grid(linewidth=1, linestyle='--')
        # plt.title("Data")
        # plt.xlabel("t")

        # plt.subplot(122)
        # ax = plt.gca()
        # ax.set_yticks(ys)
        # ax.set_xticks(xs)
        # plt.ylim(ylims)
        # # plt.grid(linewidth=1, linestyle='--')
        # plot_diagrams(dgm0, size=50)
        # # plt.plot(dgm0, size=50)
        #
        # plt.title("Persistence Diagram")
        #
        # plt.show()
        # plt.savefig(self.file_output_name)
        # plt.close()


    def generate_persistence_diagram(self):
        """
        Generates a persistence diagram from the lower-star filtration.
        """




def main():
    ls = LineSpikeDistance()
    folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp', 'climate_tmax',
                    'eeg_10000', 'eeg_2500', 'eeg_500', 'flights', 'nz_tourist',
                    'stock_price', 'stock_volume', 'unemployment']

    # ls.compare('stock_price', 'aapl_price', 'stock_volume', 'aapl_volume')
    # print('500 vs 2500')
    # print(ls.compare('eeg_500', '05_500', 'eeg_2500', '05_2500'))
    #
    # print('500 vs 10000')
    # print(ls.compare('eeg_500', '05_500', 'eeg_10000', '05_10000'))

    print('2500 vs 10000')
    print(ls.compare('eeg_2500', '05_2500', 'eeg_10000', '05_10000'))

    # for folder in folders:
    #     ls.setup(folder)

    # ls.setup('stock_volume', 'aapl_volume')
    # ls.setup('stock_price', 'aapl_price')
    # ls.setup('lines', 'equals_1')


if __name__ == '__main__':
    main()
