
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
   try:
      downloaded = trafilatura.fetch_url(url)
      text = trafilatura.extract(downloaded) 

   except Exception as e:
        print("Failed to fetch:", url, e)
        return None


   if text is None or len(text) < 200:   
     return None
   
   return text
 


def get_all_full_text (articles):
   all_text = []

   for article in articles:
      text = get_full_text (article.link)
      if text is None or len(text) < 200: 
         print("SKIPPED:", article.link)
         continue

      print("KEPT:", article.link)


      
      all_text.append(text)
   return all_text
   


if __name__ == "__main__":
    articles = fetch_articles(FEEDS)
    articles_text = get_all_full_text(articles)
   

        


