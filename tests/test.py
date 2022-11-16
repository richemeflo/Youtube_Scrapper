def setup_module(module):
    print("\n--> Setup module")

def teardown_module(module):
    print("--> Teardown module")

class TestClass:
    @classmethod
    def setup_class(cls):
        print("--> Setup class")

    @classmethod
    def teardown_class(cls):
        print("--> Teardown class")