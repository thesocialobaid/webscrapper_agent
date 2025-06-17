# 🌐 AI-Powered Web Scraping Agent

This project is a full-stack AI agent that scrapes any website URL, processes its content using Google Gemini AI, and provides a downloadable summary in JSON or PDF format.

## 🔍 Overview

The tool combines a Playwright-based web scraper, a FastAPI backend, and a clean HTML/JS frontend to create an intelligent web agent. Given a URL and optional extraction instructions, it:

- Navigates to the page
- Extracts readable HTML content
- Sends it to Gemini AI for intelligent summarization or transformation
- Returns the processed result and offers it for download (as JSON or PDF)

This is ideal for:
- Summarizing long webpages
- Extracting structured data
- Automating manual browsing tasks

---

## ⚙️ Features

✅ Scrape any publicly accessible webpage  
✅ Optionally guide the AI using custom instructions  
✅ Returns AI-enhanced structured or summarized content  
✅ PDF + JSON downloads supported  
✅ Works fully in-browser with no need for code knowledge  
✅ Screenshot support (internal API)

---

## 🧠 What I Learned

This was my **first-ever full AI agent build**, and I gained practical experience in:

- Asynchronous Python with `async/await`
- FastAPI for building REST APIs
- Headless web scraping using Playwright
- Prompt engineering for Gemini AI
- Frontend-backend integration using fetch APIs
- File download functionality (PDF/JSON)
- Debugging async errors and deployment issues
- Accessibility improvements in web apps
- GitHub Codespaces and Git workflows

It taught me how AI can be wrapped into usable tools for the public.

---

## 💡 How It Works

1. **Frontend**  
   - Simple HTML interface for URL + instructions  
   - Sends request to FastAPI backend via JavaScript `fetch`  
   - Shows live scraping status  
   - Displays results + download options

2. **Backend (FastAPI)**  
   - Receives URL + prompt  
   - Uses Playwright to open the page, extract HTML and screenshot  
   - Sends HTML and prompt to Gemini for processing  
   - Returns structured AI response

3. **PDF/JSON Export**  
   - Processed result can be downloaded with one click

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Playwright (headless browser automation)
- Google Gemini AI API
- HTML + JavaScript (vanilla)
- GitHub Codespaces

---

## 🚀 Run Locally

Clone and run:

```bash
git clone https://github.com/your-username/ai-scraper-agent.git
cd ai-scraper-agent
pip install -r requirements.txt
uvicorn main:app --reload
