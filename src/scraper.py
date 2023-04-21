from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dataclasses import dataclass
from src.logger import logger
from src.exception import CustomException
import os
import sys


@dataclass
class MyData:
    Heading: str
    Content: str
    logger.info("Naming the Columns of the new scrapped dataframe")

class Scraper:
    def to_scrape(self):
        try:
            driver = webdriver.Chrome()
            wait = WebDriverWait(driver, 10)
            rows = pd.read_csv('Scraping.csv')  # assuming this returns a list of rows
            data = []

            logger.info("Calling Selenium Web Driver and reading the Scraping csv file and lastly to store the results we take empty list name data")
            for _,row in rows.iterrows():

                url = row['URL']
                driver.get(url)
                get_title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='entry-title']")))
                title = get_title.text

                get_content = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='td-post-content tagdiv-type']/p")))
                content = get_content.text

                my_data = MyData(title, content)
                data.append(my_data)

        except Exception as e:
            raise CustomException(e,sys)

        driver.quit()
        return data
    logger.info("Now this code will scrape the data from the Scrapper csv file and save it into list")


scraper = Scraper()
data = scraper.to_scrape()
df = pd.DataFrame([{k: v if not isinstance(v, tuple) else str(v) for k, v in vars(d).items()} for d in data])
df.to_csv('Raw.csv')