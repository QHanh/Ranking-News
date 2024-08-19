from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
from datetime import datetime
from math import pow

def get_news_info(news_elm, driver1):
    G = 1.8
    title = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').text
    url = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').get_attribute('href')

    try:
        driver1.get(url)
        sleep(2)
        time_str = driver1.find_element(By.ID, 'hidLastModifiedDate').get_attribute('value')
        iframe = driver1.find_elements(By.TAG_NAME,'iframe')[1]
        driver1.switch_to.frame(iframe)
        sleep(2)
        count_like = driver1.find_element(By.CLASS_NAME, '_5n6h').text
    except Exception as e:
        count_like = 0
        time_str = None

    time_format = '%d/%m/%Y %H:%M:%S'
    time_obj = datetime.strptime(time_str, time_format)
    
    t = (datetime.now() - time_obj).total_seconds() / 3600
    
    score = int(count_like) / pow((t + 2), G)

    result = {
        'Title': title,
        'Url': url,
        'Like': int(count_like),
        'Time': time_str,
        'Score': score
    }
    return result

def scrape_data():
    url = 'https://cafebiz.vn/cong-nghe.chn'
    driver = webdriver.Chrome()

    driver.get(url)
    listnews_elm = driver.find_element(By.CLASS_NAME, 'cfbiz_home20-wrapper')
    news_list = listnews_elm.find_elements(By.CLASS_NAME, 'cfbiznews_box')
    driver1 = webdriver.Chrome()

    all_product_list = []

    for new_elm in news_list[:6]:
        news_info = get_news_info(news_elm=new_elm, driver1=driver1)
        all_product_list.append(news_info)

    driver.quit()
    driver1.quit()

    df = pd.DataFrame(all_product_list)
    sorted_df = df.sort_values(by='Score', ascending=False)
    return sorted_df
