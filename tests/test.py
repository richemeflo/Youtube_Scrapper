import scrapper as sc

class TestClass:
    def test_load_json(self):
        with pytest.raises(JsonError):
            sc.load_json("input.txt")