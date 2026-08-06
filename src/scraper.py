
from config import FEEDS
import feedparser
import trafilatura

def fetch_articles(feeds):
    all_articles = []

    for feed in feeds:
        parsed = feedparser.parse(feed["url"])

        for entry in parsed.entries:
            all_articles.append(entry)

    return all_articles



def get_full_text (url):
   downloaded = trafilatura.fetch_url(url)
   text = trafilatura.extract(downloaded) 

   if text is None or len(text) < 200:   
      return None 
   
   return text
 


def get_all_full_text (articles):
   all_text = []

   for article in articles:
      text = get_full_text (article.link)
      if text is None or len(text) < 200: 
         continue
      
      all_text.append(text)
   return all_text
   


if __name__ == "__main__":
    articles = fetch_articles(FEEDS)
    articles_text = get_all_full_text(articles)
   

        


