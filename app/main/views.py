from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_article
from flask import render_template
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    category_news = get_sources('source')
    print(category_news)



    title = 'Home'
    
    return render_template('index.html',title = title,  sources=category_news)

# @main.route('/news/<int:news_id>')
# def news(news_id):

   
#     return render_template('news.html',id = news_id, )

@main.route('/article/<id>')
def article(id):

    '''
    View root page function that returns the index page and its data
    '''
    article = get_article(id)
    
    


    
    return render_template('article.html', articles= article)