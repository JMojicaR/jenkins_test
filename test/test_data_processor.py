import unittest
from app.data_processor import process_data

class TestDataProcessor(unittest.TestCase):

    def test_process_data(self):
        data = {'age': [23,29,21,28], 'height': [165,170,174,168]}
        result = process_data(data)
        self.assertEqual(result.loc['mean', 'age'], 25.25)

    if __name__=='__main__':
        unittest.main()