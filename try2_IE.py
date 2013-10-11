import unittest
import subprocess
import os, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time

class MyFirstClass(unittest.TestCase):

    def test_101(self):
        driver = webdriver.Firefox()

        driver.maximize_window()
        time.sleep(5)
        subprocess.Popen("C:/Users/CME/Desktop/New folder/exes/AuthReq.exe")

        driver.get("http://postimage.org")
        time.sleep(7)
        input_element = driver.find_element_by_class_name("uploadifive-file")
        input_element.click()
        subprocess.Popen("C:/Users/CME/Desktop/New folder/exes/BrowsePopUp.exe")
        time.sleep(7)
        driver.find_element_by_id('l_adult_no').click()
        driver.find_element_by_id('btSubmit').click()

       #         driver.close()
if __name__ == "__main__":
    unittest.main()
