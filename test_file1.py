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

<<<<<<< HEAD
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
=======
class Test_1 :
  def test_sum(self):
    a=10
    b=20
    c=a+b
    if c==30:
        print("test cases passed")
        assert True
    else:
        print("test cases failed")
  def test_mul(self):
    a=10
    b=20
    c=a*b
    if c==200:
     print("test cases passed")
     assert True
    else:
     print("test cases passed")
     assert False
  def test_sub(self):
      a = 10
      b = 5
      c = a - b
      if c == 5:
          print("test case passed")
          assert True
      else:
          print("test case failed")
          assert False
>>>>>>> bd3319a7f11429579df1008f9e394aba2a8e49cd

    def test_sub(self):
        a = 10
        b = 5
        c = a - b
        if c == 5:
            print("test cases passed")
            assert True
        else:
            print("test cases failed")
            assert False

    def test_sub1(self):
        a = 10
        b = 5
        c = a - b
        if c == 5:
            print("test cases passed")
            assert True
        else:
            print("test cases failed")
            assert False
