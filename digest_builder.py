from config import FEEDS
from scraper import fetch_articles, get_all_full_text
from summarizer import summarize_all_text
from mailer import send_email



def build_digest_entries(articles, texts , summaries):
    digest_entries = []
    for article, text, summary in zip(articles, texts, summaries):
        word_counts = text.split()
        word_count = len(word_counts)
        read_time = word_count / 200 
        round_read_time = round(read_time)
        entry = {
           "title": article.title,
           "link": article.link,
            "summary": summary,
            "word_count": word_count,
            "read_time": round_read_time
        }
        digest_entries.append(entry)
    return digest_entries


def build_email_body(digest_entries):
    body = ""
    for entry in digest_entries:
        chunk = f"""
     📰 {entry['title']}
     ⏱️ {entry['read_time']} min read | 📝 {entry['word_count']} words
     {entry['summary']}
     🔗 Read full article: {entry['link']}
     -------------------------------------------------
                                                        """
        body += chunk

    return body


if __name__ == "__main__":
    print("Starting...")
    articles = fetch_articles(FEEDS)
    texts = get_all_full_text(articles)
    summaries = summarize_all_text(texts)
    digest_entries = build_digest_entries(articles, texts, summaries)
    print(len(digest_entries))
    email_body = build_email_body(digest_entries)
    send_email("Your Daily AI News Digest", email_body)

