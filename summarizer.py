from google import genai
from dotenv import load_dotenv
import os

load_dotenv
api_key = os.getenv("GEMINI_API_KEY")
print("Key loaded:", api_key)

client = genai.Client(api_key=api_key)

def summarize (text):
    prompt = f"""Summarize the following article in 8 to 10 sentences. Preserve all specific 
numbers, financial figures, statistics, dates, and key facts exactly as stated 
in the article. Use a neutral, formal tone, but keep the language simple and 
easy to understand. Do not add opinions or information not present in the article.

Article:
{text}"""
    
    response = client.model.generate_content(   
             model = "gemini-2.5-flash",
            contents = "prompt"
    
    )

if __name__ == "__main__":
    result = summarize("Apple announced a new iPhone today with improved cameras and battery life.")
    print(result)