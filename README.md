# Briefly

**Briefly** is an automated AI news digest that scrapes the latest tech news, summarizes each article with AI, and delivers a clean, readable digest straight to your inbox — every day.

No more scrolling through a dozen tabs to keep up with tech news. Briefly does the reading for you.

## What It Does

Briefly pulls the latest articles from trusted tech news sources, extracts the full article text, and uses Google's Gemini API to generate a concise, fact-preserving summary of each one. Every summary includes an estimated read time and a direct link to the original article, so you can decide what's worth a deeper read — all delivered as a single, well-formatted email.

## How It Works

Briefly runs as a simple pipeline:

1. **Fetch** — Pulls the latest articles from configured RSS feeds (TechCrunch, Engadget)
2. **Extract** — Downloads each article's full text and filters out broken or paywalled pages
3. **Summarize** — Sends each article to Gemini with a tuned prompt, generating a clear, neutral summary that preserves key facts, figures, and dates
4. **Compile** — Combines everything into a structured, emoji-friendly digest with read time and word count per article
5. **Deliver** — Sends the finished digest via email

## Tech Stack

| Tool | Role |
|---|---|
| `feedparser` | Parses RSS feeds |
| `trafilatura` | Extracts clean article text from raw HTML |
| `google-genai` | Gemini API SDK for AI summarization |
| `smtplib` / `email` | Sends the digest via SMTP |
| `python-dotenv` | Manages secrets via environment variables |
| GitHub Actions | Runs the pipeline automatically, on a schedule, in the cloud |

## Project Status

**Phase 1 — Complete**
Single-user, tech-only digest, fully automated via GitHub Actions. No database, no UI — a clean, working script.

**Planned**
- **Phase 2:** SQLite storage, multiple topics (finance, sports, etc.), and a Flask viewer UI
- **Phase 3:** Multi-user support with per-user topic and delivery preferences, full deployment

## Setup

1. Clone the repo and install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Create a `.env` file with the following:
   ```
   GEMINI_API_KEY=your_key_here
   GMAIL_ADDRESS=your_email_here
   GMAIL_APP_PASSWORD=your_app_password_here
   ```
3. Run the digest:
   ```
   python digest_builder.py
   ```
