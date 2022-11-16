import scrapper as sc
import pytest

class TestClass:
    def test_load_json(self):
        with pytest.raises(sc.JsonError):
            sc.load_json("input.txt")