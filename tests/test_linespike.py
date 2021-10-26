import json
import matplotlib.pyplot as plt
import numpy as np
import os
from unittest import TestCase

from linespike.linespike import LineSpike


class TestLineSpike(TestCase):
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.ls = LineSpike()
        self.titles = 'ASAE\n-------------------------------------------------------'

    def test_average_slopes_around_extrema(self):
        self.assertEqual(self.ls.asae([0, 1, 0], 2), 1.7320508075688772)

    def test_average_slopes_around_extrema_astro_data(self):
        print('\nASTRO DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\astro'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 5)

    def test_average_slopes_around_extrema_chi_homicide_data(self):
        print('\nCHI HOMICIDE DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\chi_homicide'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 2)

    def test_average_slopes_around_extrema_climate_awnd_data(self):
        print('\nCLIMATE AWND DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\climate_awnd'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_climate_prcp_data(self):
        print('\nCLIMATE PRCP DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\climate_prcp'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_climate_tmax_data(self):
        print('\nCLIMATE TMAX DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\climate_tmax'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_eeg_500_data(self):
        print('\nEEG 500 DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\eeg_500'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_eeg_2500_data(self):
        print('\nEEG 2500 DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\eeg_2500'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_eeg_10000_data(self):
        print('\nEEG 10000 DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\eeg_10000'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 6)

    def test_average_slopes_around_extrema_flights_data(self):
        print('\nFLIGHTS DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\flights'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 3)

    def test_average_slopes_around_extrema_nz_tourist_data(self):
        print('\nNZ TOURIST DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\nz_tourist'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 2)

    def test_average_slopes_around_extrema_stock_price_data(self):
        print('\nSTOCK PRICE DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\stock_price'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 9)

    def test_average_slopes_around_extrema_stock_volume_data(self):
        print('\nSTOCK VOLUME DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\stock_volume'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 9)

    def test_average_slopes_around_extrema_unemployment_data(self):
        print('\nUNEMPLOYMENT DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\unemployment'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 14)

    def test_average_slopes_around_extrema_line_data(self):
        print('\nLINE DATA'.ljust(52) + self.titles)

        location = os.getcwd() + '\\data\\lines'
        c = 0
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    c += 1
                    with open(location + '\\' + file) as f:
                        data = json.load(f)
                        print(file.ljust(35)
                              + '{:>7.10f}'.format(self.ls.asae(data)).rjust(20))
            except Exception as e:
                raise e

        self.assertEqual(c, 4)

    def test_average_slopes_around_extrema_all_data(self):
        self.test_average_slopes_around_extrema_astro_data()
        self.test_average_slopes_around_extrema_chi_homicide_data()
        self.test_average_slopes_around_extrema_climate_awnd_data()
        self.test_average_slopes_around_extrema_climate_prcp_data()
        self.test_average_slopes_around_extrema_climate_tmax_data()
        self.test_average_slopes_around_extrema_eeg_500_data()
        self.test_average_slopes_around_extrema_eeg_2500_data()
        self.test_average_slopes_around_extrema_eeg_10000_data()
        self.test_average_slopes_around_extrema_flights_data()
        self.test_average_slopes_around_extrema_nz_tourist_data()
        self.test_average_slopes_around_extrema_stock_price_data()
        self.test_average_slopes_around_extrema_stock_volume_data()
        self.test_average_slopes_around_extrema_unemployment_data()
        self.test_average_slopes_around_extrema_line_data()

    def get_asae(self, location):
        location = os.getcwd() + '\\data\\' + location
        asae_data = []
        for file in os.listdir(location):
            try:
                if file.endswith(".json"):
                    with open(location + '\\' + file) as f:
                        asae_data.append(self.ls.asae(json.load(f)))
            except Exception as e:
                raise e
        return asae_data

    def asae_vs_l1_norm(self, data_folders, l1_norms, ln_y=False, show_graph=False, debug=False):
        asae_scores = []
        file_names = []

        c = 0
        for folder in data_folders:
            location = os.getcwd() + '\\data\\' + folder
            for file in os.listdir(location):
                try:
                    if file.endswith(".json"):
                        c += 1
                        with open(location + '\\' + file) as f:
                            asae_scores.append(self.ls.asae_scaled(json.load(f), 10))
                            file_names.append(file[0:len(file) - 5])
                except Exception as e:
                    raise e

        if debug:
            print('FILES OPENED')
            print(c)

        # Sort data from low to high ASAE scores
        asae_scores_sorted = np.sort(asae_scores)
        file_names_sorted = [x for y, x in sorted(zip(asae_scores, file_names))]
        l1_norms_sorted = [x for y, x in sorted(zip(asae_scores, l1_norms))]

        # Debug output
        if debug:
            print('\nSORTED ASAE SCORES')
            print(asae_scores_sorted)
            print('\nSORTED L1-NORMS')
            print(l1_norms_sorted)

            print('\nL1-NORM MAX')
            print(max(l1_norms))

            print('\nL1-NORM MIN')
            print(min(l1_norms))

            print('\nSORTED FILE NAMES')
            print(file_names_sorted)

        # Correct data
        if ln_y:
            for x in range(0, len(l1_norms_sorted)):
                l1_norms_sorted[x] = np.log(l1_norms_sorted[x])

        # Find correlation
        r = np.corrcoef(asae_scores_sorted, l1_norms_sorted)[0, 1]
        if debug:
            print('\nCORRELATION COEFFICIENT')
            print(str(r) + '/1')

        # Graph results
        if show_graph:
            # Plot data
            plt.scatter(asae_scores_sorted, l1_norms_sorted, color='black', marker='x')

            # Graph line of best fit
            m, b = np.polyfit(asae_scores_sorted, l1_norms_sorted, 1)
            plt.plot(asae_scores_sorted, m * asae_scores_sorted + b, color='black')

            # Set plot metadata
            plt.xlabel('Scaled ASAE Score')
            plt.ylabel('Scaled l1-norm')
            plt.title('Scaled l1-norm vs. Scaled ASAE Score')
            plt.show()

        return r

    def test(self):
        data_folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp', 'climate_tmax',
                        'eeg_10000', 'eeg_2500', 'eeg_500', 'flights', 'nz_tourist',
                        'stock_price', 'stock_volume', 'unemployment']

        astro_l1_norms = [1.9158925156542754, 10.709392862216555, 7.083471311033708, 9.539825772632787,
                          7.97478401168521]
        chi_homicide_l1_norms = [16.798060899863657, 65.32799883235988]
        climate_awnd_l1_norms = [240.7681434227337, 221.39061244411116, 137.1714200430733, 261.2524456347594,
                                 250.74215272372595, 210.5785436875467]
        climate_prcp_l1_norms = [83.98324580659943, 43.21239758207963, 3.8809959751042933, 41.18297813945712,
                                 69.71289466723691, 46.476533942544364]
        climate_tmax_l1_norms = [125.04340948478057, 120.01770802869397, 131.0929161491176, 119.57920997041604,
                                 116.70942167884144, 127.2255776493832]
        eeg_10000_l1_norms = [170.37358274593453, 158.4524682534131, 193.16735517054713, 277.61963652249955,
                              294.99744706305097, 287.8024404484703]
        eeg_2500_l1_norms = [60.56470937311094, 52.299649590146295, 52.72095445920049, 77.01853635323752,
                             92.30978529521859, 84.92483222932505]
        eeg_500_l1_norms = [17.010259794013812, 13.951822808553429, 14.882715316880697, 14.91979131937692,
                            21.998172164626574, 18.839279926945096]
        flights_l1_norms = [163.04124292157934, 7.733752157476401, 8.5556976611674]
        nz_tourist_l1_norms = [0.053053372032573716, 9.456221283142524]
        stock_price_l1_norms = [3.9242005391209847, 3.4430156284057825, 5.099387255476029, 6.157296262911882,
                                6.8747697934976095, 4.709819193418061, 6.210223553765106, 11.142999426992098,
                                9.168838230557512]
        stock_volume_l1_norms = [36.72157160960148, 27.37454933077529, 37.10724346542393, 23.286247422965328,
                                 36.77584427290205, 41.661420475544254, 36.917166335244275, 27.26545194183638,
                                 37.98347470060832]
        unemployment_l1_norms = [8.08902151261961, 2.5394244105409154, 7.243758106355382, 2.937273443656422,
                                 3.4544483824063974, 7.60028063022249, 3.7024161626045187, 3.6764142389142394,
                                 1.9683690307806292, 3.883894696089818, 3.7632527690563404, 2.8120933372077537,
                                 2.7753711532789302, 3.332012085137085]

        correlations = [self.asae_vs_l1_norm(['astro'], astro_l1_norms),
                        self.asae_vs_l1_norm(['chi_homicide'], chi_homicide_l1_norms),
                        self.asae_vs_l1_norm(['climate_awnd'], climate_awnd_l1_norms),
                        self.asae_vs_l1_norm(['climate_prcp'], climate_prcp_l1_norms),
                        self.asae_vs_l1_norm(['climate_tmax'], climate_tmax_l1_norms),
                        self.asae_vs_l1_norm(['eeg_10000'], eeg_10000_l1_norms),
                        self.asae_vs_l1_norm(['eeg_2500'], eeg_2500_l1_norms),
                        self.asae_vs_l1_norm(['eeg_500'], eeg_500_l1_norms),
                        self.asae_vs_l1_norm(['flights'], flights_l1_norms),
                        self.asae_vs_l1_norm(['nz_tourist'], nz_tourist_l1_norms),
                        self.asae_vs_l1_norm(['stock_price'], stock_price_l1_norms),
                        self.asae_vs_l1_norm(['stock_volume'], stock_volume_l1_norms),
                        self.asae_vs_l1_norm(['unemployment'], unemployment_l1_norms)]

        print(data_folders)
        print(correlations)

        # print(self.asae_vs_l1_norm(['stock_price'], stock_price_l1_norms, show_graph=True))

    def test_scaled_asae_vs_scaled_l1_norm_outliers_removed(self):
        # data_folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp', 'climate_tmax',
        #                 'eeg_10000', 'eeg_2500', 'eeg_500', 'flights', 'nz_tourist',
        #                 'stock_price', 'stock_volume', 'unemployment']

        data_folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp',
                        'flights', 'nz_tourist', 'stock_price', 'stock_volume']

        asae_scores = []
        file_names = []

        c = 0
        for folder in data_folders:
            location = os.getcwd() + '\\data\\' + folder
            for file in os.listdir(location):
                try:
                    if file.endswith(".json"):
                        c += 1
                        with open(location + '\\' + file) as f:
                            asae_scores.append(self.ls.asae_scaled(json.load(f), 10))
                            file_names.append(file[0:len(file) - 5])
                except Exception as e:
                    raise e

        print('FILES OPENED')
        print(str(c) + '/80')

        print('\nOUTLIER DATA SETS: climate_tmax, eeg_10000, eeg_2500, eeg_500, unemployment')

        self.assertEqual(c, 42)
        self.assertEqual(len(asae_scores), 42)
        self.assertEqual(len(file_names), 42)

        # Scaled l1-norms (no outliers)
        l1_norms = [1.9158925156542754, 10.709392862216555, 7.083471311033708, 9.539825772632787, 7.97478401168521, 16.798060899863657, 65.30730917718746, 241.63303507050313, 220.57199235802574, 136.0268919464709, 260.8967317550046, 251.65945600867627, 211.45651346205494, 82.72533719899108, 43.5581888325545, 3.9625325167575287, 41.88209087709921, 68.41816245723147, 46.4530416488198, 163.04124292157934, 7.733752157476401, 8.5556976611674, 0.053053372032573716, 9.456221283142524, 3.9242005391209847, 3.4430156284057825, 5.099387255476029, 6.157296262911882, 6.8747697934976095, 4.709819193418061, 6.337140450491266, 11.142999426992098, 9.168838230557512, 36.72157160960148, 27.37454933077529, 37.10724346542393, 23.286247422965328, 36.77584427290205, 41.661420475544254, 36.917166335244275, 27.26545194183638, 37.98347470060832]

        asae_scores_sorted = np.sort(asae_scores)
        file_names_sorted = [x for y, x in sorted(zip(asae_scores, file_names))]
        l1_norms_sorted = [x for y, x in sorted(zip(asae_scores, l1_norms))]

        print('\nSORTED ASAE SCORES')
        print(asae_scores_sorted)
        print('\nSORTED L1-NORMS')
        print(l1_norms_sorted)

        print('\nL1-NORM MAX')
        print(max(l1_norms))

        print('\nL1-NORM MIN')
        print(min(l1_norms))

        print('\nSORTED FILE NAMES')
        print(file_names_sorted)

        for x in range(0, len(l1_norms_sorted)):
            l1_norms_sorted[x] = np.log(l1_norms_sorted[x])

        # Find correlation
        print('\nCORRELATION COEFFICIENT')
        print(str(np.corrcoef(asae_scores_sorted, l1_norms_sorted)[0, 1]) + '/1')

        # plotting the points
        plt.scatter(asae_scores_sorted, l1_norms_sorted, color='black', marker='x')
        m, b = np.polyfit(asae_scores_sorted, l1_norms_sorted, 1)
        plt.plot(asae_scores_sorted, m * asae_scores_sorted + b, color='black')

        # naming the x axis
        plt.xlabel('Scaled ASAE Score')
        # naming the y axis
        plt.ylabel('$ln($Scaled l1-norm$)$')

        # giving a title to my graph
        plt.title('$ln($Scaled l1-norm$)$ vs. Scaled ASAE Score (Outliers Removed)')

        # function to show the plot
        plt.show()

    def test_scaled_asae_vs_scaled_l1_norm_all_outliers_only(self):
        data_folders = ['climate_tmax', 'eeg_10000', 'eeg_2500', 'eeg_500', 'unemployment']

        asae_scores = []
        file_names = []

        c = 0
        for folder in data_folders:
            location = os.getcwd() + '\\data\\' + folder
            for file in os.listdir(location):
                try:
                    if file.endswith(".json"):
                        c += 1
                        with open(location + '\\' + file) as f:
                            asae_scores.append(self.ls.asae_scaled(json.load(f), 10))
                            file_names.append(file[0:len(file) - 5])
                except Exception as e:
                    raise e

        print('FILES OPENED')
        print(str(c) + '/80')

        print('\nOUTLIER DATA SETS: climate_tmax, eeg_10000, eeg_2500, eeg_500, unemployment')

        self.assertEqual(c, 38)
        self.assertEqual(len(asae_scores), 38)
        self.assertEqual(len(file_names), 38)

        # Scaled l1-norms (outliers only)
        l1_norms = [124.65735632547853, 120.49734435036598, 131.18465737576452, 120.80043192261343, 116.08861956601363, 127.98242080622637, 170.37358274593453, 158.4524682534131, 193.16735517054713, 277.61963652249955, 294.99744706305097, 287.8024404484703, 60.56470937311094, 52.299649590146295, 52.72095445920049, 77.01853635323752, 92.30978529521859, 84.92483222932505, 17.010259794013812, 13.951822808553429, 14.882715316880697, 14.91979131937692, 21.998172164626574, 18.839279926945096, 8.08902151261961, 2.5394244105409154, 7.243758106355382, 2.937273443656422, 3.4544483824063974, 7.60028063022249, 3.7024161626045187, 3.6764142389142394, 1.9683690307806292, 3.883894696089818, 3.7632527690563404, 2.8120933372077537, 2.7753711532789302, 3.337693903318903]

        asae_scores_sorted = np.sort(asae_scores)
        file_names_sorted = [x for y, x in sorted(zip(asae_scores, file_names))]
        l1_norms_sorted = [x for y, x in sorted(zip(asae_scores, l1_norms))]

        print('\nSORTED ASAE SCORES')
        print(asae_scores_sorted)
        print('\nSORTED L1-NORMS')
        print(l1_norms_sorted)

        print('\nL1-NORM MAX')
        print(max(l1_norms))

        print('\nL1-NORM MIN')
        print(min(l1_norms))

        print('\nSORTED FILE NAMES')
        print(file_names_sorted)

        # Find correlation
        print('\nCORRELATION COEFFICIENT')
        print(str(np.corrcoef(asae_scores_sorted, l1_norms_sorted)[0, 1]) + '/1')

        # plotting the points
        plt.scatter(asae_scores_sorted, l1_norms_sorted, color='black', marker='x')
        m, b = np.polyfit(asae_scores_sorted, l1_norms_sorted, 1)
        plt.plot(asae_scores_sorted, m * asae_scores_sorted + b, color='black')

        # naming the x axis
        plt.xlabel('Scaled ASAE Score')
        # naming the y axis
        plt.ylabel('Scaled l1-norm')

        # giving a title to my graph
        plt.title('Scaled l1-norm vs. Scaled ASAE Score (Outliers Only)')

        # function to show the plot
        plt.show()