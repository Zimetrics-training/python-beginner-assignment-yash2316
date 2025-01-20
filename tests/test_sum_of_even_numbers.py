# test_sum_of_even_numbers.py
import sys
sys.path.insert(0, './src')  # Add the 'src' directory to the path

from sum_of_even_numbers import sum_of_even_numbers

def test_sum_of_even_numbers():
    assert sum_of_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_of_even_numbers([10, 15, 20]) == 30
    assert sum_of_even_numbers([1, 3, 5]) == 0
    assert sum_of_even_numbers([2, 4, 6, 8]) == 20
    assert sum_of_even_numbers([0, 2, -4]) == -2
