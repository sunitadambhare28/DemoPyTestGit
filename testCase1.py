import time
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class TestCase:
    def test_sum(self,):
        driver = webdriver.Chrome()
        url = "https://credence.in"
        driver.get(url)
        time.sleep(5)
        driver.find_element(By.XPATH, "//img[@src='/website/images/enquiry.png']").click()
        time.sleep(2)
        size = len(driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(size)
        actual_no = "+91 7385318590"
        flag =0;

        contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//a["+str(1)+"]")
        print(contact)
        a =10
        b = 20
        c = a + b
        if c == 30:
            print("test cases passed")
            assert True
        else:
            print("test cases failed")



