import json
import os
import statistics


class LineSpike:
    """
    A class to hold all methods to perform an analysis of a line chart's 'spikiness,' using the LineSpike framework.

    Methods
    -------
    asae(self, data, w)
        Finds the average slopes around all relative extrema of a data set.
    asae_scaled(self, data, w)
        Finds the average slopes around all relative extrema of a data set converted to z-scores.
    """

    data = []
    C = []
    E = []

    def setup(self, location):
        self.get_data(location)
        self.find_extrema()
        print(self.E)
        self.sort_extrema(0, int(len(self.data) / 2))
        print(self.E)
        # self.lower_star_filtration()
        # self.generate_persistence_diagram()

    def get_data(self, location):
        """
        Loads a specified data set.

        Parameters
        ----------
        location : string
            The folder name of the data set under tests/data.
        """

        location = os.getcwd() + '\\data\\' + location
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    with open(location + '\\' + file) as f:
                        self.data.append(json.load(f))
            except Exception as e:
                raise e

    def find_extrema(self):
        """
        Finds all local extrema in the data set, including boundaries.
        """

        self.E.append([self.data[0], 0])

        for i in range(1, len(self.data) - 2):
            if self.data[i-1] < self.data[i] and self.data[i+1] < self.data[i]:  # local max
                self.E.append([self.data[i], i])
            elif self.data[i-1] > self.data[i] and self.data[i+1] > self.data[i]:  # local min
                self.E.append([self.data[i], i])

        self.E.append([self.data[-1], len(self.data) - 1])

    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort_extrema(self, low, high):
        """
        Sorts extrema in a data set from low to high y-values.
        """

        if len(self.data) == 1:
            return self.data
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(self.data, low, high)

            # Separately sort elements before
            # partition and after partition
            self.sort_extrema(low, pi - 1)

    def lower_star_filtration(self):
        """
        Implements lower-star filtration on the data set to generate a merge tree and persistence diagram.
        """

    def generate_persistence_diagram(self):
        """
        Generates a persistence diagram from the lower-star filtration.
        """

def main():
    ls = LineSpike()
    ls.setup('astro')

if __name__ == '__main__':
    main()
