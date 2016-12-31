__author__ = 'john'

import unittest
import datetime

import fetcher


class MyTestCase(unittest.TestCase):

    def test_fetchaverage(self):
        now=datetime.datetime.now()
        f=fetcher.Fetcher()
        average= f.get_average_speed(60,now)
        print("Average Speed: %s" % average)

    def test_fetchmax(self):
            now=datetime.datetime.now()
            f=fetcher.Fetcher()
            max= f.get_max_speed(60,now)
            print("Max Speed: %s" % max)

if __name__ == '__main__':
    unittest.main()
