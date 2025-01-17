import unittest
import pandas as pd

class TestDataValidation(unittest.TestCase):
    def setUp(self):
        self.data = pd.read_excel('HINDALCO_1D.xlsx')

    def test_columns_exist(self):
        required_columns = {'datetime', 'close', 'high', 'low', 'open', 'volume', 'instrument'}
        self.assertTrue(required_columns.issubset(self.data.columns))

    def test_data_types(self):
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(pd.to_datetime(self.data['datetime'])))
        for col in ['close', 'high', 'low', 'open']:
            self.assertTrue(pd.api.types.is_float_dtype(self.data[col]))
        self.assertTrue(pd.api.types.is_integer_dtype(self.data['volume']))

if __name__ == "__main__":
    unittest.main()
