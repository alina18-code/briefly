from config import FEEDS
from scraper import fetch_articles, get_all_full_text
from summarizer import summarize_all_text
from mailer import send_email
from datetime import date, datetime
import time 
from database import init_db, is_duplicate, save_sent_articles, get_last_sent_time

def filter_new_articles(articles):
    new_articles = []

    last_sent = get_last_sent_time()
    if last_sent:
        cutoff = datetime.fromisoformat(last_sent)
    else:
        cutoff = datetime.combine(date.today(), datetime.min.time())

    print("Cutoff being used:", cutoff)

    for article in articles:
        struct_date = article.get('published_parsed')
        if not struct_date:
            continue

        article_datetime = datetime.fromtimestamp(time.mktime(struct_date))

        if article_datetime > cutoff:
            new_articles.append(article)

    return new_articles
  


def build_digest_entries(new_articles, texts , summaries):
    digest_entries = []
    for article, text, summary in zip(new_articles, texts, summaries):
        word_counts = text.split()
        word_count = len(word_counts)
        read_time = word_count / 200 
        round_read_time = round(read_time)
        entry = {
           "title": article.title,
           "link": article.link,
            "summary": summary,
            "word_counts": word_count,
            "read_time": round_read_time
        }
        digest_entries.append(entry)
    return digest_entries


def build_email_body(digest_entries):
    today_str = date.today().strftime("%Y-%m-%d")

    body = f"""
    <h1 style="color: #2563eb; font-size: 28px; font-family: Arial, sans-serif;">
        AI News Digest - {today_str}
    </h1>
    <hr style="border: none; border-top: 3px solid #2563eb; margin-bottom: 25px;">
    """

    for entry in digest_entries:
        card = f"""
        <div style="border-left: 4px solid #2563eb; padding-left: 15px; margin-bottom: 30px;">
            <h3 style="font-family: Arial, sans-serif; color: #1e293b; margin-bottom: 5px;">
                {entry['title']}
            </h3>
            <p style="font-family: Arial, sans-serif; color: #475569; font-size: 13px; margin-top: 0;">
                ⏱️ {entry['read_time']} min read &nbsp;|&nbsp; 📝 {entry['word_counts']} words
            </p>
            <p style="font-family: Arial, sans-serif; color: #334155; font-size: 15px; line-height: 1.5;">
                {entry['summary']}
            </p>
            <p style="font-family: Arial, sans-serif; font-size: 14px;">
                🔗 <a href="{entry['link']}" style="color: #2563eb; text-decoration: none;">Read full article</a>
            </p>
        </div>
        """
        body += card

    return body



if __name__ == "__main__":
    init_db()

    articles = fetch_articles(FEEDS)
    print("Fetched:", len(articles))

    todays_articles = filter_new_articles(articles)
    print("After date filter:", len(todays_articles))


    new_articles = []
    for article in todays_articles:
        if not is_duplicate(article.link):
            new_articles.append(article)
    print("After duplicate filter:", len(new_articles))

    texts = get_all_full_text(new_articles)
    summaries = summarize_all_text(texts)
    digest_entries = build_digest_entries(new_articles, texts, summaries)
    email_body = build_email_body(digest_entries)
    send_email("Your Daily AI News Digest", email_body)

    today_str = date.today().strftime("%Y-%m-%d")
    for article in new_articles:
        struct_date = article.get('published_parsed')
        published_dt = datetime.fromtimestamp(time.mktime(struct_date))
        save_sent_articles(article.link, article.title, today_str, published_dt.isoformat())
  

