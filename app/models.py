class Newssource:
    '''
     
    '''

    def __init__(self,id, name, description, url):
       self.id = id
       self.name = name
       self.description = description
       self.url = url

class Newsarticle:
    '''
     
    '''

    def __init__(self,id, name,title, author,description,urlToImage, url,publishedAt):
       self.id = id
       self.name = name
       self.author = author
       self.title = title
       self.description = description
       self.urlToImage = urlToImage
       self.url = url
       self.publishedAt = publishedAt