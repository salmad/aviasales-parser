#!/usr/bin/env python3
"""
Flight Price Monitor for Aviasales
Monitors prices for a specific flight search and displays results
"""

import asyncio
from playwright.async_api import async_playwright
import json
from datetime import datetime


async def monitor_flight_prices(url: str, wait_time: int = 30):
    """
    Monitor flight prices from Aviasales search page

    Args:
        url: The Aviasales search URL
        wait_time: How long to wait for prices to load (seconds)
    """
    flight_data = []
    api_responses = []

    async with async_playwright() as p:
        print(f"🚀 Launching browser...")
        browser = await p.chromium.launch(headless=False)  # Show browser for debugging
        page = await browser.new_page()

        # Intercept API responses
        async def handle_response(response):
            # Look for API calls that contain flight data
            if 'search' in response.url or 'ticket' in response.url or 'price' in response.url:
                try:
                    if response.status == 200:
                        content_type = response.headers.get('content-type', '')
                        if 'json' in content_type:
                            data = await response.json()
                            api_responses.append({
                                'url': response.url,
                                'data': data
                            })
                            print(f"\n📡 Captured API response from: {response.url[:80]}...")
                except Exception as e:
                    pass

        page.on('response', handle_response)

        print(f"📄 Loading page: {url}")
        await page.goto(url, wait_until='networkidle')

        print(f"⏳ Waiting {wait_time} seconds for prices to load...")
        await asyncio.sleep(wait_time)

        # Try to extract flight data from the page
        print("\n🔍 Extracting flight prices from page...")

        # Look for flight card elements
        try:
            # Try multiple selectors
            selectors = [
                '[data-test-id*="ticket"]',
                '[class*="ticket"]',
                '[class*="flight"]',
                '[class*="price"]',
            ]

            for selector in selectors:
                elements = await page.locator(selector).all()
                if elements:
                    print(f"\n✅ Found {len(elements)} elements with selector: {selector}")
                    for i, elem in enumerate(elements[:5], 1):
                        text = await elem.text_content()
                        if text and len(text.strip()) > 5:
                            print(f"  {i}. {text.strip()[:200]}")
                    break

        except Exception as e:
            print(f"⚠️  Error: {e}")

        # Save API responses
        if api_responses:
            print(f"\n💾 Captured {len(api_responses)} API responses")
            api_file = f"/home/salim/projects/temp_pa/api_responses_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            with open(api_file, 'w', encoding='utf-8') as f:
                json.dump(api_responses, f, ensure_ascii=False, indent=2)
            print(f"💾 API responses saved to: {api_file}")

            # Try to extract prices from API responses
            print("\n💰 Extracting prices from API responses...")
            for i, resp in enumerate(api_responses, 1):
                print(f"\n--- Response {i}: {resp['url'][:60]}... ---")
                try:
                    data_str = json.dumps(resp['data'], ensure_ascii=False)
                    # Look for price-like numbers
                    if 'price' in data_str.lower():
                        print("  Contains price data!")
                except:
                    pass

        # Take screenshot
        screenshot_path = f"/home/salim/projects/temp_pa/aviasales_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        await page.screenshot(path=screenshot_path, full_page=True)
        print(f"\n📸 Screenshot saved to: {screenshot_path}")

        await browser.close()

        print("\n✅ Done!")


if __name__ == "__main__":
    # The URL for Moscow (MOW) to Colombo (CMB) on Jan 14
    url = "https://www.aviasales.ru/search/MOW1401CMB1"

    print("=" * 60)
    print("Flight Price Monitor - Aviasales")
    print("=" * 60)

    asyncio.run(monitor_flight_prices(url, wait_time=30))
