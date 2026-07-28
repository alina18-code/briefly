
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
    return text


def get_all_full_text (articles):
   all_text = []
   for article in articles:
      text = get_full_text (article)
      all_text.append(text)

   return all_text
      
   

if __name__ == "__main__":
    articles = fetch_articles(FEEDS)
    print(len(articles))
    #articles_url = get_full_text("https://techcrunch.com/2026/07/27/openais-hugging-face-breach-has-reignited-the-debate-over-alignment-and-control/")
   # print(articles_url)
    articles_text = get_all_full_text(articles)
    print(len(articles_text))
        


