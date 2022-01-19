import json
import os


class LineSpike:
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

    def setup(self, location, file_name):
        # Load data
        self.get_data(location, file_name)

        # Isolate extrema
        self.find_extrema()
        print('\nLoaded extrema -------------------')
        print(self.extrema)

        # Sort extrema
        self.quicksort(self.extrema, 0, len(self.extrema) - 1)
        print('\nSorted extrema -------------------')
        print(self.extrema)

        # Check sort
        failed = False
        for i in range(0, len(self.extrema) - 2):
            if self.extrema[i][0] > self.extrema[i + 1][0]:
                print('FAIL: ' + str(self.extrema[i][0]) + ' is > ' + str(self.extrema[i + 1][0]))
                failed = True
                break

        if not failed:
            print('SUCCESS')

        # self.lower_star_filtration()
        # self.generate_persistence_diagram()

    def get_data(self, location, file_name):
        """
        Loads a specified data set.

        Parameters
        ----------
        location : string
            The folder name of the data set under tests/data.
        """

        location = os.getcwd() + '\\data\\' + location
        # for file in os.listdir(location):
        #     try:
        #         if file.endswith(".json"):
        #             print(file)
        #             with open(location + '\\' + file) as f:
        #                 self.data.append(json.load(f))
        #     except Exception as e:
        #         raise e

        for file in os.listdir(location):
            try:
                if file.endswith(file_name + ".json"):
                    print(file)
                    with open(location + '\\' + file) as f:
                        self.data.append(json.load(f))
            except Exception as e:
                raise e

        self.data = self.data[0]

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
    ls.setup('chi_homicide', 'weekly')


if __name__ == '__main__':
    main()
