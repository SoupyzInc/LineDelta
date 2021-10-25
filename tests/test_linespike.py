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

    def test_asae_vs_l1_norm(self):
        data_folders = ['astro', 'chi_homicide', 'climate_awnd', 'climate_prcp', 'climate_tmax',
                        'eeg_10000', 'eeg_2500', 'eeg_500', 'flights', 'nz_tourist',
                        'stock_price', 'stock_volume', 'unemployment']

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
                            asae_scores.append(self.ls.asae(json.load(f)))
                            file_names.append(file[0:len(file) - 5])
                except Exception as e:
                    raise e

        print('FILES OPENED')
        print(str(c) + '/80')

        self.assertEqual(c, 80)
        self.assertEqual(len(asae_scores), 80)
        self.assertEqual(len(file_names), 80)

        l1_norms = [2.2368205288877974, 2.267231823126484, 2.2864159033626725, 2.309500523421754, 2.267861501198229, 1377.44099378882, 1889.852875229346, 5606.180193333201, 7553.169248618906, 2585.2628563434278, 6598.200580087601, 5152.525807583787, 5467.712731856811, 355.88654715598216, 344.47627096577855, 10.808528422557393, 284.5694560787323, 227.75568054255587, 92.28566309826914, 9915.091319891097, 10670.837811090561, 6950.093853272531, 13532.689089944914, 8238.951512996493, 11641.3002933666, 45716.34345821661, 30601.291383908658, 27171.49968035467, 38701.565429419046, 47337.945332760726, 43822.66691195881, 11118.105958459468, 6608.060725714984, 5539.496126937114, 9150.264229982737, 12487.390825381284, 11352.326948255028, 2441.992896028623, 1503.839076888357, 1223.1657237484737, 1772.5607274898944, 2422.9226785563, 2251.0867191907428, 3512190.4962595836, 2095514.2833333332, 778063.7010042245, 198014.97333333327, 4853963.490628606, 789.470636990956, 6034.091462832806, 120.84824836390892, 5356.6545820349775, 235.18588151032304, 405.8607992676733, 235.8683612301445, 524.5715744699726, 2633.9321951676093, 5539239764.350209, 628924795.9646962, 13406227373.091793, 251896652.87318516, 4066864094.087728, 2202555977.7010736, 1743379954.7322092, 55209813.637024485, 1251240228.5450292, 2289.1930880713494, 3138.7285714285713, 14893.166666666666, 2899.0888888888885, 1810.1309523809523, 6536.241341991341, 4324.422077922078, 1088.2186147186148, 2783.2738095238096, 477.7190476190476, 1685.9372405372405, 1552.2755221386801, 4032.614285714286, 1762.3023809523809]

        # Scaled l1-norms (l1-norm / range of data)
        # l1_norms = [1.9158925156542754, 10.709392862216555, 7.083471311033708, 9.539825772632787, 7.97478401168521, 16.798060899863657, 66.15883925630376, 240.9329038411422, 221.07439267995267, 137.19938822359788, 260.875243016972, 251.8302484233475, 210.10877768905604, 82.71583701479973, 43.83981893595221, 3.9175142843886857, 41.57595374741209, 68.450726650004, 46.411678561666214, 123.03557844327304, 119.77244642388182, 129.96276873664863, 119.99640966605567, 117.39636735299035, 127.58951763097026, 170.37358274593453, 158.4524682534131, 193.16735517054713, 277.61963652249955, 294.99744706305097, 287.803363271898, 60.56470937311094, 52.299649590146295, 52.72095445920049, 77.01853635323752, 92.30978529521859, 84.92483222932505, 17.010259794013812, 13.951822808553429, 14.882715316880697, 14.91979131937692, 21.998172164626574, 18.839279926945096, 163.0316342319818, 7.733752157476401, 8.5556976611674, 0.053053372032573716, 9.456221283142524, 3.9242005391209847, 3.4430156284057825, 4.960929735792648, 6.157296262911882, 6.8747697934976095, 4.715473498119517, 6.337140450491266, 11.142999426992098, 9.168838230557512, 36.72157160960148, 27.37454933077529, 37.10724346542393, 23.286247422965328, 36.77584427290205, 41.661420475544254, 36.917166335244275, 27.26545194183638, 37.98347470060832, 8.08902151261961, 2.5394244105409154, 7.243758106355382, 2.937273443656422, 3.4544483824063974, 7.60028063022249, 3.7024161626045187, 3.6764142389142394, 1.9683690307806292, 3.920550758302614, 3.7632527690563404, 2.8120933372077537, 2.7753711532789302, 3.337693903318903]

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
        r = np.corrcoef(asae_scores_sorted, l1_norms_sorted)
        print('\nCORR COEF')
        print(r[0, 1])

        # plotting the points
        plt.scatter(asae_scores_sorted, l1_norms_sorted)
        # plt.ylim(0, 10000)

        # naming the x axis
        plt.xlabel('ASAE Score')
        # naming the y axis
        plt.ylabel('L1-Norm')

        # giving a title to my graph
        plt.title('L1-norm vs. ASAE Score')

        # function to show the plot
        plt.show()
