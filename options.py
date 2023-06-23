import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    
    await page.set_viewport_size({"width": 1000, "height": 1200 })
    await page.goto("https://demoqa.com/select-menu")
    await page.locator("#cars").select_option(["volvo", "saab", "opel"])

    await page.screenshot(path="screenshots/options.png")
    await context.tracing.stop(path="logs/options.zip") 

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
