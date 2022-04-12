# Import Module
# Basic packages
import requests
from bs4 import BeautifulSoup
  

class Scrapper():
    def __init__(self):
        pass
    @staticmethod
    def remove_tags(html_code):
        '''
        Since the website is comming in html format, we need to remove the tags

        Parameters
        ----------
        html : str
            The html code of the article.

        Returns
        -------
        article : str
        '''
        # parse html content
        soup = BeautifulSoup(html_code, "html.parser")
    
        for data in soup(['style', 'script']):
            # Remove tags
            data.decompose()
    
        # return data by retrieving the tag content
        return ' '.join(soup.stripped_strings)
  
    def get_page_article(self, url):
        '''
        Gets the article from the page.

        Parameters
        ----------
        url : str
            The url of the article.
        
        Returns
        -------
        article : str
            The article.
        '''
        response = requests.get(url)
        html_code = response.content
        article = self.remove_tags(html_code)
        return article