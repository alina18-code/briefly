from config import FEEDS
from scraper import fetch_articles, get_all_full_text
from summarizer import summarize_all_text



def build_digest_entries(articles, texts , summaries):
    digest_entries = []
    for article, text, summary in zip(articles, texts, summaries):
        word_counts = text.split()
        word_count = len(word_counts)
        read_time = word_count / 200 
        entry = {
           "title": article.title,
           "link": article.link,
            "summary": summary,
            "word counts": word_count,
            "read time": read_time
        }
        digest_entries.append(entry)
    return digest_entries




if __name__ == "__main__":
    print("Starting...")
    articles = fetch_articles(FEEDS)
    texts = get_all_full_text(articles)
    summaries = summarize_all_text(texts)
    digest_entries = build_digest_entries(articles, summaries, texts)

    print(len(digest_entries))
    print(digest_entries[0])
