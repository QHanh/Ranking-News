from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

def get_news_info(news_elm, driver1):
    title = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').text
    url = news_elm.find_element(By.CLASS_NAME, 'cfbiznews_title').get_attribute('href')
    driver1.get(url)
    sleep(2)
    time_str = driver1.find_element(By.ID, 'hidLastModifiedDate').get_attribute('value')
    try:
        iframe = driver1.find_elements(By.TAG_NAME, 'iframe')[1]
        driver1.switch_to.frame(iframe)
        sleep(2)
        count_like = driver1.find_element(By.CLASS_NAME, '_5n6h').text
    except (IndexError, NoSuchElementException):
        driver1.switch_to.default_content()
        iframe = driver1.find_elements(By.TAG_NAME, 'iframe')[2]
        driver1.switch_to.frame(iframe)
        sleep(2)
        count_like = driver1.find_element(By.CLASS_NAME, '_5n6h').text

    result = {
        'Title': title,
        'Url': url,
        'Like': int(count_like),
        'Time': time_str
    }
    return result

def scrape_data():
    url = 'https://cafebiz.vn'
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

    return all_product_list