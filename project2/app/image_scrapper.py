# import requests
# from bs4 import BeautifulSoup, Tag
# import urllib2
# import sys



# #first_arg = sys.argv[1]

# def scrape(url):
#     page = urllib2.urlopen(url).read()
#     soup = BeautifulSoup(page, 'html.parser')
#     soup.prettify()
#     images = []
#     image = {}
    
#     img_list = soup.findAll('meta', {"property":'og:image'})
#     for og_image in img_list:
#         if not og_image.get('content'):
#             continue
    
#         image = {'url': og_image['content']}
#         next = og_image.nextSibling.nextSibling # calling once returns end of line char '\n'
    
#         if next and isinstance(next, Tag) and next.get('property', '').startswith('og:image:'):
#             dimension = next['content']
#             prop = next.get('property').rsplit(':')[-1]
#             image[prop] = dimension
    
#             next = next.nextSibling.nextSibling
#             if next and isinstance(next, Tag) and next.get('property', '').startswith('og:image:'):
#                 dimension = next['content']
#                 prop = next.get('property').rsplit(':')[-1]
#                 image[prop] = dimension
    
#         images.append(image)
#     return images

import requests
from bs4 import BeautifulSoup
import urlparse

def scrape(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    image = """<img src="%s"><br />"""
    imagelst = []
    for img in soup.findAll("img", src=True):
        if "sprite" not in img["src"]:
            imagelst.append(urlparse.urljoin(url, img["src"]))
    return imagelst