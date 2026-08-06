from google import genai
from dotenv import load_dotenv
import os
from scraper import fetch_articles, get_all_full_text
from config import FEEDS
import time

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def summarize (text):
    prompt = f"""Summarize the following article in approximately 130 to 170 words covering all the major points from the article,
        covering all major points, events, and developments described — not just the opening details.
        Preserve all specific numbers, financial figures, statistics, dates, and names exactly as stated in the article.
        Only mention such details if they actually appear in the article — do not comment on missing information or note that something wasn't provided.
        Use a neutral, formal tone, but keep the language simple and easy to understand. 
        Do not add opinions, speculation, or information not present in the article.

        Article:
        {text}"""

    
    response = client.models.generate_content(   
             model = "gemini-3.5-flash-lite",
            contents = prompt
    
    )
 
    return response.text


def summarize_all_text(texts):
    all_summaries = []
    for text in texts:
        summary = summarize(text)
        time.sleep(6)

        all_summaries.append(summary)

    return all_summaries


if __name__ == "__main__":
   articles = fetch_articles(FEEDS)
   texts = get_all_full_text(articles)
   summaries = summarize_all_text(texts)


