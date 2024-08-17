from flask import render_template
from scraping.scraper import scrape_data

def init_routes(app):
    @app.route('/')
    def home():
        news = scrape_data()
        if news.empty:
            return "No news articles were found or could be ranked."
        return render_template('news.html', news=news)
