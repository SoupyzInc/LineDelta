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

    @staticmethod
    def asae(data, w=2):
        """
        Finds the average slopes around all relative extrema of a data set.

        Parameters
        ----------
        data : list of int
            The data set to be analyzed.
        w : int, optional
            The amount of data points left and right of the extrema to be considered. A window
            size of X, will consider X points to the left and X points to the right of an extrema.

        Returns
        -------
        int
            The average slopes of all relative extrema of the data set.
        """

        if w < 1:
            raise ValueError('Window size, w, must be greater than 0.')

        # Find extrema
        extrema_indices = []
        for i in range(1, len(data) - 1):
            if data[i - 1] > data[i] and data[i] < data[i + 1]:
                extrema_indices.append(i)
            elif data[i - 1] < data[i] and data[i] > data[i + 1]:
                extrema_indices.append(i)

        if len(extrema_indices) == 0:
            return 0

        # Iterate through all extrema (windows).
        slope_sum = 0
        for i in range(0, len(extrema_indices)):
            # Find slope of window
            window_sum = 0

            # Set window indices
            left_bound = extrema_indices[i] - w
            if left_bound < 0:
                left_bound = 0

            right_bound = extrema_indices[i] + w
            if right_bound > len(data) - 1:
                right_bound = len(data) - 1

            # Sum slopes of window
            for x in range(left_bound, right_bound):
                window_sum += abs(data[x + 1] - data[x])

            slope_sum += window_sum / (right_bound - left_bound)

        return slope_sum / len(extrema_indices)

    @staticmethod
    def asae_scaled(data, w=2):
        """
        Finds the average slopes around all relative extrema of a data set converted to z-scores.

        Parameters
        ----------
        data : list of int
            The data set to be analyzed.
        w : int, optional
            The amount of data points left and right of the extrema to be considered. A window
            size of X, will consider X points to the left and X points to the right of an extrema.

        Returns
        -------
        int
            The average slopes of all relative extrema of the z-scores of the data set.
        """

        if w < 1:
            raise ValueError('Window size, w, must be greater than 0.')
        if len(data) == 0:
            raise ValueError('The data set, data, cannot be empty.')

        # Convert data into z-scores
        mean = statistics.mean(data)
        sx = statistics.stdev(data)

        scaled_data = []
        for x in data:
            if sx != 0:
                scaled_data.append((x - mean) / sx)
            else:
                scaled_data.append(0)

        # Find extrema
        extrema_indices = []
        for i in range(1, len(scaled_data) - 1):
            if scaled_data[i - 1] > scaled_data[i] and scaled_data[i] < scaled_data[i + 1]:
                extrema_indices.append(i)
            elif scaled_data[i - 1] < scaled_data[i] and scaled_data[i] > scaled_data[i + 1]:
                extrema_indices.append(i)

        if len(extrema_indices) == 0:
            return 0

        # Iterate through all extrema (windows).
        slope_sum = 0
        for i in range(0, len(extrema_indices)):
            # Find slope of window
            window_sum = 0

            # Set window indices
            left_bound = extrema_indices[i] - w
            if left_bound < 0:
                left_bound = 0

            right_bound = extrema_indices[i] + w
            if right_bound > len(scaled_data) - 1:
                right_bound = len(scaled_data) - 1

            # Sum slopes of window
            for x in range(left_bound, right_bound):
                window_sum += abs(scaled_data[x + 1] - scaled_data[x])

            slope_sum += window_sum / (right_bound - left_bound)

        return slope_sum / len(extrema_indices)
