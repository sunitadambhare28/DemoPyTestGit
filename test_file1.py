class Test_1:
    def test_sum(self):
        a = 10
        b = 20
        c = a + b
        if c == 30:
            print("test cases passed")
            assert True
        else:
            print("test cases failed")

    def test_mul(self):
        a = 10
        b = 20
        c = a * b
        if c == 200:
            print("test cases passed")
            assert True
        else:
            print("test cases passed")
            assert False

    def test_mul1(self):
        assert True