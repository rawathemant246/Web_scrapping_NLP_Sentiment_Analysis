from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from dataclasses import dataclass




driver  = webdriver.Chrome()

driver.get('https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/')
driver.implicitly_wait(10)

get_title = driver.find_element(By.XPATH, '//*[@class="tdb-title-text"]')
title = get_title.text
content = driver.find_element(By.XPATH, '//*[@id="tdi_113"]/div/div[1]/div/div[10]/div')

content_list = [content.text]
print(content_list)

#@dataclass
#class MyData:
 #   Heading: str
#    Content: str

#my_data = MyData(title[0],content_list[0])
#df = pd.DataFrame(my_data.__dict__, index=[0])
#print(df)

