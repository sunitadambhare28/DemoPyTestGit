import pytest
from selenium import webdriver
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Test1:

 def test_sum(self):
        a = 10
        b = 20
        sum = a+b
        if(sum == 30):
            print("test case is passed")
            assert True
        else:
            print("test case is failed")
            assert False

 def test_sub(self):
      a = 20
      b = 10
      sub = a-b
      if(sub == 10):
          print("test case is passe")
          assert True
      else:
          print("Test case is failed")
          assert False

 def test_mul(self):
      a = 10
      b = 20
      mul = a*b
      if(mul == 200):
          print("Test passed")
          assert True
      else:
          print("Test case failed")
          assert False
 def test_mul1(self):
      a = 10
      b = 20
      mul = a*b
      if(mul == 200):
          print("Test passed")
          assert True
      else:
          print("Test case failed")
          assert False

 def test_square(self):
     a =4
     result = a*a
     if(result == 16):
         assert True
     else:
         assert False


