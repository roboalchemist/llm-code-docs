# Source: https://playwright.dev/python/docs/pages

Title: Pages | Playwright Python

URL Source: https://playwright.dev/python/docs/pages

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
## Pages[​](https://playwright.dev/python/docs/pages#pages "Direct link to Pages")

Each [BrowserContext](https://playwright.dev/python/docs/api/class-browsercontext "BrowserContext") can have multiple pages. A [Page](https://playwright.dev/python/docs/api/class-page "Page") refers to a single tab or a popup window within a browser context. It should be used to navigate to URLs and interact with the page content.

*   Sync
*   Async

`page = context.new_page()# Navigate explicitly, similar to entering a URL in the browser.page.goto('http://example.com')# Fill an input.page.locator('#search').fill('query')# Navigate implicitly by clicking a link.page.locator('#submit').click()# Expect a new url.print(page.url)`

## Multiple pages[​](https://playwright.dev/python/docs/pages#multiple-pages "Direct link to Multiple pages")

Each browser context can host multiple pages (tabs).

*   Each page behaves like a focused, active page. Bringing the page to front is not required.
*   Pages inside a context respect context-level emulation, like viewport sizes, custom network routes or browser locale.

*   Sync
*   Async

`# create two pagespage_one = context.new_page()page_two = context.new_page()# get pages of a browser contextall_pages = context.pages`

## Handling new pages[​](https://playwright.dev/python/docs/pages#handling-new-pages "Direct link to Handling new pages")

The `page` event on browser contexts can be used to get new pages that are created in the context. This can be used to handle new pages opened by `target="_blank"` links.

*   Sync
*   Async

`# Get page after a specific action (e.g. clicking a link)with context.expect_page() as new_page_info:    page.get_by_text("open new tab").click() # Opens a new tabnew_page = new_page_info.value# Interact with the new page normallynew_page.get_by_role("button").click()print(new_page.title())`

If the action that triggers the new page is unknown, the following pattern can be used.

*   Sync
*   Async

`# Get all new pages (including popups) in the contextdef handle_page(page):    page.wait_for_load_state()    print(page.title())context.on("page", handle_page)`

## Handling popups[​](https://playwright.dev/python/docs/pages#handling-popups "Direct link to Handling popups")

If the page opens a pop-up (e.g. pages opened by `target="_blank"` links), you can get a reference to it by listening to the `popup` event on the page.

This event is emitted in addition to the `browserContext.on('page')` event, but only for popups relevant to this page.

*   Sync
*   Async

`# Get popup after a specific action (e.g., click)with page.expect_popup() as popup_info:    page.get_by_text("open the popup").click()popup = popup_info.value# Interact with the popup normallypopup.get_by_role("button").click()print(popup.title())`

If the action that triggers the popup is unknown, the following pattern can be used.

*   Sync
*   Async

`# Get all popups when they opendef handle_popup(popup):    popup.wait_for_load_state()    print(popup.title())page.on("popup", handle_popup)`
