import pytest
import sys
sys.path.insert(0, '../src')  # Add the 'src' directory to the path
from rectangle import Rectangle

def test_rectangle():
    # Create test rectangles
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 3)

    # Test area method
    assert rect1.area() == 50
    assert rect2.area() == 9

    # Test perimeter method
    assert rect1.perimeter() == 30
    assert rect2.perimeter() == 12

    # Test is_square method
    assert rect1.is_square() == False
    assert rect2.is_square() == True
