from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep

def get_news_info(news_elm, driver1, driver2):
    title = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').text
    url = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').get_attribute('href')

    try:
        driver1.get(url)
        like_pos = driver1.find_element(By.CLASS_NAME, 'fbLikeWrap')
        like_base = like_pos.find_element(By.CLASS_NAME, 'fb-like').get_attribute('fb-iframe-plugin-query')
        url_like = 'https://www.facebook.com/v2.8/plugins/like.php?' + like_base
        driver2.get(url_like)
        count_like = driver2.find_element(By.CLASS_NAME, '_5n6h').text
    except Exception as e:
        count_like = None
    
    sleep(2)

    result = {
        'Title': title,
        'Url': url,
        'Like': int(count_like)
    }
    return result

def scrape_data():
    url = 'https://cafebiz.vn/cong-nghe.chn'
    driver = webdriver.Chrome()

    driver.get(url)
    listnews_elm = driver.find_element(By.CLASS_NAME, 'cfbiz_home20-wrapper')
    news_list = listnews_elm.find_elements(By.CLASS_NAME, 'cfbiznews_box')
    driver1 = webdriver.Chrome()
    driver2 = webdriver.Chrome()

    all_product_list = []

    for new_elm in news_list:
        news_info = get_news_info(news_elm=new_elm, driver1=driver1, driver2=driver2)
        all_product_list.append(news_info)

    driver.quit()
    driver1.quit()
    driver2.quit()

    df = pd.DataFrame(all_product_list)
    sorted_df = df.sort_values(by='Like', ascending=False)
    return sorted_df
