# This file contains a Webscraper agent that:
# 1. Initializes a Playwright browser (headless, no UI)
# 2. Navigates to any URL
# 3. Returns the main readable HTML text of the page (cleaned)
# 4. Captures a screenshot (optional)
# 5. Cleans up and closes the browser properly

from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

class WebScraperAgent:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def init_browser(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--disable-web-security",
                "--disable-extensions"
            ]
        )
        self.page = await self.browser.new_page()

    async def scrape_content(self, url):
        if not self.page or self.page.is_closed():
            await self.init_browser()

        await self.page.goto(url, wait_until="networkidle")
        await self.page.wait_for_timeout(2000)

        full_html = await self.page.content()

        # Extract <body> content only and clean it
        soup = BeautifulSoup(full_html, 'html.parser')

        # Remove unnecessary tags
        for tag in soup(['script', 'style', 'noscript', 'meta', 'link']):
            tag.decompose()

        body = soup.body
        if body:
            return body.get_text(separator="\n", strip=True)
        else:
            return soup.get_text(separator="\n", strip=True)

    async def screenshot_buffer(self):
        return await self.page.screenshot(type="png", full_page=True)

    async def take_screenshot(self, path="screenshot.png"):
        await self.page.screenshot(path=path, full_page=True)
        return path

    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
        self.playwright = None
        self.browser = None
        self.page = None
