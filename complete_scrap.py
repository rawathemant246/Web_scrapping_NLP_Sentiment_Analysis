from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from dataclasses import dataclass

@dataclass
class MyData:
    Heading: str
    Content: str

class Scraper:
    def to_scrape(self):

        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        rows = pd.read_csv('Scraping.csv')  # assuming this returns a list of rows
        data = []
        for _,row in rows.iterrows():
            try:
                url = row['URL']
                driver.get(url)
                get_title = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='entry-title']")))
                title = get_title.text

                get_content = wait.until(EC.presence_of_element_located((By.XPATH,"//*[@class='td-post-content tagdiv-type']/p")))
                content = get_content.text

                my_data = MyData(title, content)
                data.append(my_data)

            except Exception as e:
                print(e)

        driver.quit()
        return data


scraper = Scraper()
data = scraper.to_scrape()
df = pd.DataFrame([{k: v if not isinstance(v, tuple) else str(v) for k, v in vars(d).items()} for d in data])
df.to_csv('Raw.csv')



