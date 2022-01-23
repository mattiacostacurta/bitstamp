'''
This module collects the test made to check
wether the the program works as espected.
We created three main cases: 
- 1 smoke tesk: to check valif input
- 2nd test: to check invalid input
- 3rd test: to check corner cases
'''

import unittest
import pandas as pd
import sys
import os
sys.path.append('./')
import math
from get import create_table, read_csv

class TestCsvFile(unittest.TestCase):
    '''
    This class will test the csv file, comparing
    the original csv file with other ones which have
    invalid structure or are empty.
    '''
    @classmethod
    def tearDownClass(cls):
        '''
        This class is used to remove csv files
        created with the setUp function after
        all tests of this class are run
        '''
        os.remove('Example.csv')
        os.remove('Example1.csv')
        os.remove('Example2.csv')

    def setUp(self):
        '''
        This function creates three different csv files 
        '''
        self.table1 = pd.read_csv('CryptoTable.csv')

        #Valid csv (values of 18/01/2022)
        self.data = {'high': 42865.80, 'last': 42047.32, 'timestamp': 1642502504, 
                'bid': 42035.75, 'vwap': 42146.43, 'volume': 1077.71980924, 
                'low': 41482.63, 'ask': 42050.46, 'open': 42230.09}  
        self.df = pd.DataFrame(self.data, index=[0])
        self.df.to_csv(r'Example.csv', index = False, header=True)

        self.table2 = pd.read_csv('Example.csv')

        #Invalid csv
        self.data1 = {'high': 'wrong_format', 'last': True, 'timestamp': 0, 
                'bid': [1], 'volume': 'volume', 
                'low': 4, 'open': False }
        self.df1 = pd.DataFrame(self.data1, index=[0])
        self.df1.to_csv(r'Example1.csv', index = False, header=True)

        self.table3 = pd.read_csv('Example1.csv')

        #Corner csv: Blank
        self.data2 = None
        self.df2 = pd.DataFrame(self.data2)
        self.df2.to_csv(r'Example2.csv', index = False, header=True)

    #valid csv
    def test_valid_table(self):
        '''
        This function check if a valid csv has the same shape
        and type of the three main values used in the program
        with respect to the original csv created (CryptoTable)
        '''
        self.assertEqual(self.table1.shape, self.table2.shape)
        
        self.assertEqual(self.table1['open'].dtypes, self.table2['open'].dtypes)
        self.assertEqual(self.table1['volume'].dtypes, self.table2['volume'].dtypes)
        self.assertEqual(self.table1['last'].dtypes, self.table2['last'].dtypes)

    #invalid csv
    def test_invalid_table(self):
        '''
        This function check if an invalid csv has different shape
        and type of the three main values used in the program with 
        respect to the original csv created (CryptoTable)
        '''
        self.assertFalse(self.table1.shape == self.table3.shape)
        
        self.assertFalse(self.table1['open'].dtypes == self.table3['open'].dtypes)
        self.assertFalse(self.table1['volume'].dtypes == self.table3['volume'].dtypes)
        self.assertFalse(self.table1['last'].dtypes == self.table3['last'].dtypes)

    #corner case
    def test_blank_table(self):
        '''
        This function check if an blank csv has a different shape
        with respect to the original csv created (CryptoTable)
        '''
        self.assertTrue(os.stat("Example2.csv").st_size != os.stat("CryptoTable.csv").st_size)

class TestCreateTable(unittest.TestCase):
    #valid input
    def test_valid_create_table(self):
        self.data = {'high': 42865.80, 'last': 42047.32, 'timestamp': 1642502504, 
            'bid': 42035.75, 'vwap': 42146.43, 'volume': 1077.71980924, 
            'low': 41482.63, 'ask': 42050.46, 'open': 42230.09}  
        self.df = pd.DataFrame(self.data, index=[0])
        self.assertTrue(create_table(self.df))

    #invalid input
    def test_invalid_create_table(self):
        empty_df = pd.DataFrame()
        data = {'high': 42865.80, 'last': 42047.32}
        df_2_columns = pd.DataFrame(data, index = [0])

        self.assertFalse(create_table(empty_df))
        self.assertFalse(create_table(df_2_columns))

    #corner case
    def test_None_create_table(self):
        self.assertFalse(create_table(None))


class TestReadCsv(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        os.remove('CryptoTable.csv')

    def setUp(self):
        self.data = {'high': 42865.80, 'last': 42047.32343789, 'timestamp': 1642502504, 
                'bid': 42035.75, 'vwap': 42146.43, 'volume': 1077.71980924, 
                'low': 41482.63, 'ask': 42050.46, 'open': 42230.09}  
        self.df = pd.DataFrame(self.data, index=[0])
        self.df.to_csv(r'CryptoTable.csv', index = False, header=True)

    #valid case
    def test_valid_read_csv(self):
        self.assertEqual(read_csv('last'), round(42047.32343789, 2))
        self.assertEqual(read_csv('volume'), round(1077.71980924, 2))
        self.assertEqual(read_csv('change'), round((42047.32-42230.09)/42047.32*100, 2))

    #invalid case
    def test_invalid_read_csv(self):
        self.assertEqual(read_csv(1), None)
        self.assertEqual(read_csv(''), None)
        self.assertEqual(read_csv({}), None)
        self.assertEqual(read_csv(True), None)

    #corner case
    def test_blank_read_csv(self):
        self.assertEqual(read_csv(None), None)


if __name__ == '__main__':
    unittest.main()
