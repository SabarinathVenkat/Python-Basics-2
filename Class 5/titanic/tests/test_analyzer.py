import unittest
from adapters.csv_analyzer import CSVAnalyze


class TestCountCSV(unittest.TestCase):
    def setUp(self):
        self.df = CSVAnalyze('../data/test.csv')

    def test_Count(self):
        self.assertEqual(2,self.df.count())

    def test_Columns(self):
        self.assertListEqual(self.df.columns,['ID','NAME','PRICE','QTY'])

class TestNegCSV(unittest.TestCase):

    def test_Count(self):
        self.assertRaises(IOError,CSVAnalyze('../data/test1.csv'))

if __name__ == '__main__':
    unittest.main()
