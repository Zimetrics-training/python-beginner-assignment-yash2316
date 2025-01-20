import pytest
import sys
from cart_total import calculate_total_cost, apply_discount, apply_tax, calculate_final_price

sys.path.insert(0, './src')  # Add the 'src' directory to the path

def test_calculate_total_cost():
    # Test case 1: Simple cart with two items
    cart = [{"name": "item1", "price": 20.0, "quantity": 2}, {"name": "item2", "price": 50.0, "quantity": 1}]
    assert calculate_total_cost(cart) == 90.0

    # Test case 2: Cart with one item
    cart = [{"name": "item1", "price": 30.0, "quantity": 1}]
    assert calculate_total_cost(cart) == 30.0

    # Test case 3: Empty cart
    cart = []
    assert calculate_total_cost(cart) == 0.0


def test_apply_discount():
    # Test case 1: Total cost below 100 (no discount)
    assert apply_discount(90.0) == 90.0

    # Test case 2: Total cost above 100 (discount applied)
    assert apply_discount(130.0) == 117.0


def test_apply_tax():
    # Test case 1: Applying tax on a cost of 90.0
    assert apply_tax(90.0) == 97.2

    # Test case 2: Applying tax on a cost of 117.0
    assert apply_tax(117.0) == 126.36


def test_calculate_final_price():
    # Test case 1: Cart with two items, total < 100, no discount
    cart = [{"name": "item1", "price": 20.0, "quantity": 2}, {"name": "item2", "price": 50.0, "quantity": 1}]
    assert calculate_final_price(cart) == 97.2  # No discount, tax applied

    # Test case 2: Cart with three items, total > 100, discount and tax applied
    cart = [{"name": "item1", "price": 50.0, "quantity": 2}, {"name": "item2", "price": 30.0, "quantity": 1}]
    assert calculate_final_price(cart) == 126.36  # Discount applied, tax added

    # Test case 3: Cart with one item, total < 100, no discount
    cart = [{"name": "item1", "price": 10.0, "quantity": 5}]
    assert calculate_final_price(cart) == 54.0  # No discount, tax applied


# Run all the tests
if __name__ == "__main__":
    pytest.main()
