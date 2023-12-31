# run: 
#   $ python3 checkboxes.py
#   $ playwright show-trace logs/trace.zip

import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    await context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = await context.new_page()
    await page.goto("https://demoqa.com/checkbox")

    await page.locator("#tree-node svg").nth(3).click()
    await page.screenshot(path="screenshots/checkboxes.png")

    await expect(page.locator("#result")).to_have_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
    await context.tracing.stop(path="logs/trace.zip")

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
