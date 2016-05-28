import pytest

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x, 'test can have output commentary'

    def test_two(self):
        x = 5
        assert x == 5

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1 / 0
