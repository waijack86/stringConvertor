import unittest
import stringConvertor
import os
import csv

class TestStringMethods(unittest.TestCase):

    # test to convert upper 
    def test_upper(self):
        self.assertEqual(stringConvertor.convertUpper('hello world'), 'HELLO WORLD')

    # test to convert alternate upper and lower
    def test_alternate(self):
        self.assertEqual(stringConvertor.convertAlternate('hello world'), 'hElLo wOrLd')

    # test is the csv file being created and content matching input
    def test_csvExist(self):
        data = "hello world"
        stringConvertor.createCSV(data)
        assert os.path.exists('csvFile.csv') == 1

        # test is the content in the csv file matching with input
        if os.path.exists('csvFile.csv'):
            with open('csvFile.csv', 'r') as csv_file:	
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    if any(row):
                        # print("==========")
                        string = (f'{"".join(row)}')
                        self.assertEqual(string, data)

if __name__ == '__main__':
    unittest.main()