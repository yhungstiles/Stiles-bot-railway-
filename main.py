import asyncio
from playwright.async_api import async_playwright
import time
import requests

# === Settings ===
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
URL = "https://quotex.com/en/trade"

async def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    try:
        requests.post(url, data=data)
        print("📩", msg)
    except Exception as e:
        print("❌ Telegram error:", e)

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(URL)
        
        # Wait and screenshot login page just to confirm it's working
        await page.screenshot(path="page.png")
        
        await send_telegram("Bot loaded Quotex site ✅")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_bot())
