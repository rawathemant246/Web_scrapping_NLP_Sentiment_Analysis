from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from dataclasses import dataclass

driver  = webdriver.Chrome()

driver.get('https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator')
driver.implicitly_wait(10)

get_title = driver.find_element(By.XPATH, "//*[@class ='tdb-title-text']")
title = get_title.text
content = driver.find_elements(By.XPATH, "//*[@class ='tdb-block-inner td-fix-index']/p")

content_list = [content.text]

@dataclass
class MyData:
    Heading: str
    Content: str

my_data = MyData(title[0],content_list[0])
df = pd.DataFrame(my_data.__dict__, index=[1])
print(df.shape)
print(df)