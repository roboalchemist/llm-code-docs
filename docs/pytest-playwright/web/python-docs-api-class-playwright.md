# Source: https://playwright.dev/python/docs/api/class-playwright

Title: Playwright | Playwright Python

URL Source: https://playwright.dev/python/docs/api/class-playwright

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
Playwright module provides a method to launch a browser instance. The following is a typical example of using Playwright to drive automation:

*   Sync
*   Async

`from playwright.sync_api import sync_playwright, Playwrightdef run(playwright: Playwright):    chromium = playwright.chromium # or "firefox" or "webkit".    browser = chromium.launch()    page = browser.new_page()    page.goto("http://example.com")    # other actions...    browser.close()with sync_playwright() as playwright:    run(playwright)`

* * *

## Methods[​](https://playwright.dev/python/docs/api/class-playwright#methods "Direct link to Methods")

### stop[​](https://playwright.dev/python/docs/api/class-playwright#playwright-stop "Direct link to stop")

Added before v1.9

playwright.stop
Terminates this instance of Playwright in case it was created bypassing the Python context manager. This is useful in REPL applications.

`from playwright.sync_api import sync_playwrightplaywright = sync_playwright().start()browser = playwright.chromium.launch()page = browser.new_page()page.goto("https://playwright.dev/")page.screenshot(path="example.png")browser.close()playwright.stop()`

**Usage**

`playwright.stop()`

**Returns**

*   [NoneType](https://docs.python.org/3/library/constants.html#None "None")[#](https://playwright.dev/python/docs/api/class-playwright#playwright-stop-return)

* * *

## Properties[​](https://playwright.dev/python/docs/api/class-playwright#properties "Direct link to Properties")

### chromium[​](https://playwright.dev/python/docs/api/class-playwright#playwright-chromium "Direct link to chromium")

Added before v1.9

playwright.chromium
This object can be used to launch or connect to Chromium, returning instances of [Browser](https://playwright.dev/python/docs/api/class-browser "Browser").

**Usage**

`playwright.chromium`

**Type**

*   [BrowserType](https://playwright.dev/python/docs/api/class-browsertype "BrowserType")

* * *

### devices[​](https://playwright.dev/python/docs/api/class-playwright#playwright-devices "Direct link to devices")

Added before v1.9

playwright.devices
Returns a dictionary of devices to be used with [browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context) or [browser.new_page()](https://playwright.dev/python/docs/api/class-browser#browser-new-page).

*   Sync
*   Async

`from playwright.sync_api import sync_playwright, Playwrightdef run(playwright: Playwright):    webkit = playwright.webkit    iphone = playwright.devices["iPhone 6"]    browser = webkit.launch()    context = browser.new_context(**iphone)    page = context.new_page()    page.goto("http://example.com")    # other actions...    browser.close()with sync_playwright() as playwright:    run(playwright)`

**Usage**

`playwright.devices`

**Type**

*   [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")

* * *

### firefox[​](https://playwright.dev/python/docs/api/class-playwright#playwright-firefox "Direct link to firefox")

Added before v1.9

playwright.firefox
This object can be used to launch or connect to Firefox, returning instances of [Browser](https://playwright.dev/python/docs/api/class-browser "Browser").

**Usage**

`playwright.firefox`

**Type**

*   [BrowserType](https://playwright.dev/python/docs/api/class-browsertype "BrowserType")

* * *

### request[​](https://playwright.dev/python/docs/api/class-playwright#playwright-request "Direct link to request")

Added in: v1.16

playwright.request
Exposes API that can be used for the Web API testing.

**Usage**

`playwright.request`

**Type**

*   [APIRequest](https://playwright.dev/python/docs/api/class-apirequest "APIRequest")

* * *

### selectors[​](https://playwright.dev/python/docs/api/class-playwright#playwright-selectors "Direct link to selectors")

Added before v1.9

playwright.selectors
Selectors can be used to install custom selector engines. See [extensibility](https://playwright.dev/python/docs/extensibility) for more information.

**Usage**

`playwright.selectors`

**Type**

*   [Selectors](https://playwright.dev/python/docs/api/class-selectors "Selectors")

* * *

### webkit[​](https://playwright.dev/python/docs/api/class-playwright#playwright-webkit "Direct link to webkit")

Added before v1.9

playwright.webkit
This object can be used to launch or connect to WebKit, returning instances of [Browser](https://playwright.dev/python/docs/api/class-browser "Browser").

**Usage**

`playwright.webkit`

**Type**

*   [BrowserType](https://playwright.dev/python/docs/api/class-browsertype "BrowserType")
