from flask import render_template
from model.ranking import ranking_news

def init_routes(app):
    @app.route('/')
    def home():
        news = ranking_news()
        if news.empty:
            return "No news articles were found."
        return render_template('news.html', news=news)
