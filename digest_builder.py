from config import FEEDS
from scraper import fetch_articles, get_all_full_text
from summarizer import summarize_all_text



def build_digest_entries(articles, summaries):
    digest_entries = []
    for article, summary in zip(articles, summaries):
        entry = {
           "title": article.title,
           "link": article.link,
            "summary": summary
        }
        digest_entries.append(entry)
    return digest_entries




if __name__ == "__main__":
    print("Starting...")
    articles = fetch_articles(FEEDS)
    texts = get_all_full_text(articles)
    summaries = summarize_all_text(texts)
    digest_entries = build_digest_entries(articles, summaries)

    print(len(digest_entries))
    print(digest_entries[0])
