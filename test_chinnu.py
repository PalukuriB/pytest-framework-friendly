import math 
import pytest

def test_first_case():
    n = int(input("Enter number: "))
    assert math.sqrt(n) == n**(1/2) 

@pytest.fixture
def user_inputs():
    string_1 = input("Enter string_1: ")
    string_2 = input("Enter string_2: ")
    return string_1, string_2

def test_string_concatination(user_inputs):
    string_1, string_2 = user_inputs
    d = string_1 + string_2
    assert len(d) == len(string_1 + string_2)

def test_sqrt():
    num = 6 
    assert num*6 == 36 

@pytest.mark.parametrize("num1, num2, expected", [
    (10, 20, 20),  # Case where second number is larger
    (50, 30, 50),  # Case where first number is larger
    (15, 15, 15)   # Case where both numbers are equal
])
def test_largest_number(num1, num2, expected):
    assert max(num1, num2) == expected, f"Expected {expected}, but got {max(num1, num2)}"


def test_compare_dynamic_inputs():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    smallest = min(num1, num2)
    print(f"The largest number is {smallest}")
    assert smallest == min(num1, num2), "The assertion failed!"











