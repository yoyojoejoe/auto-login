import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "E:\chromedriver\chromedriver.exe"		  #取得chromedriver位置
os.environ["webdriver.chrome.driver"] = chromedriver	#調用chromedriver
driver = webdriver.Chrome(chromedriver)					      #用selenium控制webdriver
driver.get("https://cu.nsysu.edu.tw/")				      	#以google開啟中山網路大學
elem_user = driver.find_element_by_name("username")
elem_user.send_keys("B085090023")						          #輸入username
elem_pwd = driver.find_element_by_name("password")
elem_pwd.send_keys("yoyojoejoe20049")				         	#輸入password
elem_pwd.send_keys(Keys.RETURN)
