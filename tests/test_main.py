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
from get_values import create_table, read_csv
from prep_graph import request_API_txn, read_df

# Tests of function of get_values.py
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

    # Valid csv
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

    # Invalid csv
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

    # Corner case
    def test_blank_table(self):
        '''
        This function check if an blank csv has a different shape
        with respect to the original csv created (CryptoTable)
        '''
        self.assertTrue(os.stat("Example2.csv").st_size != os.stat("CryptoTable.csv").st_size)

class TestCreateTable(unittest.TestCase):
    '''
    This class will test the create_table function,
    when it receives different values as inputs.
    '''
    # Valid input
    def test_valid_create_table(self):
        '''
        This test checks whether the function works correctly when it receive 
        as input a correct dataframe (with the same columns and data type)
        '''
        self.data = {'high': 42865.80, 'last': 42047.32, 'timestamp': 1642502504, 
            'bid': 42035.75, 'vwap': 42146.43, 'volume': 1077.71980924, 
            'low': 41482.63, 'ask': 42050.46, 'open': 42230.09}  
        self.df = pd.DataFrame(self.data, index=[0])
        self.assertTrue(create_table(self.df))

    # Invalid input
    def test_invalid_create_table(self):
        '''
        This test checks whether the function returns False when it receive 
        as input an invalid dataframe (with different columns or empty)
        '''
        empty_df = pd.DataFrame()
        data = {'high': 42865.80, 'last': 42047.32}
        df_2_columns = pd.DataFrame(data, index = [0])

        self.assertFalse(create_table(empty_df))
        self.assertFalse(create_table(df_2_columns))

    # Corner case
    def test_None_create_table(self):
        '''
        This test checks whether the function returns False when it receive 
        as input None (if API request is unsuccesfull, it will return None)
        '''
        self.assertFalse(create_table(None))


class TestReadCsv(unittest.TestCase):
    '''
    This class will test the read_csv function,
    when it receives different values as inputs.
    '''
    @classmethod
    def tearDownClass(cls):
        '''
        This class is used to remove csv files
        created with the setUp function after
        all tests of this class are run
        '''
        os.remove('CryptoTable.csv')

    def setUp(self):
        '''
        This function creates a mock csv with correct data
        '''
        self.data = {'high': 42865.80, 'last': 42047.32343789, 'timestamp': 1642502504, 
                'bid': 42035.75, 'vwap': 42146.43, 'volume': 1077.71980924, 
                'low': 41482.63, 'ask': 42050.46, 'open': 42230.09}  
        self.df = pd.DataFrame(self.data, index=[0])
        self.df.to_csv(r'CryptoTable.csv', index = False, header=True)

    # Valid case
    def test_valid_read_csv(self):
        '''
        This test checks whether the function returns correct values when it 
        receive valid inputs.
        '''
        self.assertEqual(read_csv('last'), round(42047.32343789, 2))
        self.assertEqual(read_csv('volume'), round(1077.71980924, 2))
        self.assertEqual(read_csv('change'), round((42047.32-42230.09)/42047.32*100, 2))

    # Invalid case
    def test_invalid_read_csv(self):
        '''
        This test checks whether the function returns None when it 
        receive invalid inputs.
        '''
        self.assertEqual(read_csv(1), None)
        self.assertEqual(read_csv(''), None)
        self.assertEqual(read_csv({}), None)
        self.assertEqual(read_csv(True), None)

    # Corner case
    def test_blank_read_csv(self):
        '''
        This test checks whether the function returns None when it 
        receive None as input
        '''
        self.assertEqual(read_csv(None), None)


# Tests of function of prep_graph.py
class TestRequestAPITxn(unittest.TestCase):
    '''
    This class will test the request_API_txn function,
    when it receives different values as inputs.
    '''
    # Valid input
    def test_valid_input(self):
        '''
        This test checks if the function returns a dataframe with 5 
        columns. Since values change every minute it makes no sense to
        check them or the number of rows.
        '''
        self.assertTrue(isinstance(request_API_txn('btceur'), pd.DataFrame))
        self.assertEqual(len(request_API_txn('btceur').columns),5)

    # Invalid input
    def test_invalid_input(self):
        '''
        This test checks the result with invalid inputs is None. Even if 
        such invalid inputs should not be allowed by argparse.
        '''
        self.assertEqual(request_API_txn(1), None)
        self.assertEqual(request_API_txn([]), None)
        self.assertEqual(request_API_txn(True), None)
        self.assertEqual(request_API_txn({}), None)

    # Corner case
    def test_corner_case(self):
        '''
        This test checks if the function returns None when None is passed.
        '''
        self.assertEqual(request_API_txn(None), None)

class TestReadDataframe(unittest.TestCase):
    '''
    This class will test the read_df function,
    when it receives different values as inputs.
    '''
    def setUp(self):
        '''
        This function creates 2 mock dataframe: one with data of 
        22/01/2022, taking only the first 2 rows and one empty to use as inputs 
        of the function.
        '''
        self.data = {'date': [1642867355,1642869224], 'tid': [218372056, 218377609], 'amount': [0.20473807,0.05000000], 
        'type': [1,0], 'price': [34611.42,35262.41]}  
        self.df = pd.DataFrame(self.data, index=[0,1])
        self.resulting_df = self.df.sort_values(by=['date'], ascending=True)

        self.empty_df = pd.DataFrame()

    # Valid input
    def test_valid_input(self):
        '''
        This test checks if the function returns the same dataframe 
        sorted in ascending order when a non-empty dataframe with 
        the right shape is passed.
        '''  
        self.assertTrue((read_df(self.df)).equals(self.resulting_df))

    # Invalid input
    def test_invalid_input(self):
        '''
        This test checks if the function returns None when it 
        receives invalid inputs. 
        '''  
        self.assertTrue(read_df(123)==False)
        self.assertTrue(read_df('')==False)
        self.assertTrue(read_df([])==False)
        self.assertTrue(read_df({})==False)

    # Corner cases     
    def test_corner_case(self):
        '''
        This test checks if the function returns the expected results 
        when None and an empty dataframe is passed. 
        '''
        self.assertEqual(read_df(None), "API request failed." )
        self.assertEqual(read_df(self.empty_df), "No data available.")

if __name__ == '__main__':
    unittest.main()
