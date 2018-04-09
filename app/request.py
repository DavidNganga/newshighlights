import urllib.request,json
from .models import Newssource


# Newssource = Newssource.Newssource
# Newsarticle =Newsarticle.Newsarticle

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


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
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        if url:
            source_object = Newssource(name,description,url)
            source_results.append(source_object)
    print(source_results)
    return source_results





