from google import genai
from dotenv import load_dotenv
import os

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


if __name__ == "__main__":
    result = summarize("Apple announced a new iPhone today with improved cameras and battery life.")
    print(result)