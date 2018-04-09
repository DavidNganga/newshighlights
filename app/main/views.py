from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources
# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    category_news = get_sources('source')
    print(category_news)



    title = 'Home'
    message = 'On the news today!!'
    return render_template('index.html',title = title, message = message, sources=category_news)

@app.route('/news/<int:news_id>')
def news(news_id):

   
    return render_template('news.html',id = news_id, )