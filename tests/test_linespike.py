import json
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
        l1_norms = {
            'astro_115_120': '',
            'astro_115_123': '',
            'astro_115_128': '',
            'astro_116_124': '',
            'astro_116_134': ''
        }

        asae_values = {
            'astro_115_120': 0,
            'astro_115_123': 0,
            'astro_115_128': 0,
            'astro_116_124': 0,
            'astro_116_134': 0
        }

        asae_data = self.get_asae('astro')

        c = 0
        for value in asae_values:
            asae_values[value] = asae_data[c]
            c += 1

        print(asae_values)
