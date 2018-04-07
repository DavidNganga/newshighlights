from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home'
    message = 'On the news today!!'
    return render_template('index.html',title = title, message = message)

@app.route('/news/<int:news_id>')
def news(news_id):

   
    return render_template('news.html',id = news_id)