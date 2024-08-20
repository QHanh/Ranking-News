from crawl_data.scraper import scrape_data
import pandas as pd
from datetime import datetime
from math import pow

def ranking_news():
    G = 1.8
    list_news = scrape_data()
    for news in list_news:
        time_obj = datetime.strptime(news['Time'], '%d/%m/%Y %H:%M:%S')
        t = (datetime.now() - time_obj).total_seconds() / 3600  
        score = news['Like'] / pow((t + 2), G)  
        news['Score'] = score
        
    df = pd.DataFrame(list_news)
    df_sorted = df.sort_values(by='Score', ascending=False)
    return df_sorted  
