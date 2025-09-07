import pytest
from app.data_processor import process_data

class TestDataProcessor:
    
    def test_process_data(self):
        """
        Test the process_data function to ensure it calculates the correct mean.
        """
        data = {'age': [23, 29, 21, 28], 'height': [165, 170, 174, 168]}
        result = process_data(data)
        assert result.loc['mean', 'age'] == 25.25
        assert result.loc['mean', 'height'] == 169.25

    def test_process_data2(self):
        """
        Test the process_data function to ensure it calculates the correct mean.
        """
        data = {'age': [23, 29, 21, 28], 'height': [165, 170, 174, 168]}
        result = process_data(data)
        assert result.loc['mean', 'age'] == 24.25
        assert result.loc['mean', 'height'] == 169.25

    def test_process_data3(self):
        """
        Test the process_data function to ensure it calculates the correct mean.
        """
        data = {'age': [23, 29, 21, 28], 'height': [165, 170, 174, 168]}
        result = process_data(data)
        assert result.loc['mean', 'age'] == 23.25
        assert result.loc['mean', 'height'] == 169.25