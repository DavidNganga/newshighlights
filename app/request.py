import urllib.request,json
from .models import Newssource, Newsarticle


# Newssource = Newssource.Newssource
# Newsarticle =Newsarticle.Newsarticle

# Getting api key
api_key = None
# Getting the movie base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_SOURCES_URL']

def get_sources(source):
    '''
    Function gets json response
    '''
    get_source_url = 'https://newsapi.org/v1/sources'.format(api_key)


    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data  = url.read()
        get_source_dict = json.loads(get_sources_data)
        
        source_results = None
        if get_source_dict['sources']:
            source_results_list = get_source_dict['sources']
            source_results = process_results(source_results_list)
    return source_results
    

 
def process_results(source_list):
   
    
    source_results = []

    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        if url:
            source_object = Newssource(id,name,description,url)
            source_results.append(source_object)
    print(source_results)
    return source_results

def get_article(id):
    '''
    Function gets json response
    '''
    get_article_url ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)


    with urllib.request.urlopen(get_article_url) as url:
        get_article_data  = url.read()
        get_article_response = json.loads(get_article_data)
        
        article_results = None
        if get_article_response['articles']:
            
            article_results_list = get_article_response['articles']
            article_results = process_article(article_results_list)
    return article_results
    

 
def process_article(article_list):
   
    
    article_results = []

    for article_item in article_list:
        id = article_item["source"]["id"]
        name = article_item["source"]["name"]
        title = article_item["title"]
        description = article_item["description"]
        author = article_item["author"]
        url = article_item["url"]
        urlToImage = article_item["urlToImage"]
        publishedAt = article_item["publishedAt"]
       
        
        if url:
            article_object = Newsarticle(id,name,title,description,author,url,urlToImage,publishedAt)
            article_results.append(article_object)
   
    return article_results

    





