
from config import FEEDS
import feedparser

def fetch_articles(feeds):
    all_articles = []
    for feed in feeds:
        parsed = feedparser.parse(feed["url"])
        for entry in parsed.entries:
            all_articles.append(entry)

    return all_articles


if __name__ == "__main__":
    articles = fetch_articles(FEEDS)
    print(len(articles))
        


