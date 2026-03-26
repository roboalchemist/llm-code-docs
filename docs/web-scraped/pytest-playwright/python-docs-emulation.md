# Source: https://playwright.dev/python/docs/emulation

Title: Emulation | Playwright Python

URL Source: https://playwright.dev/python/docs/emulation

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
## Introduction[​](https://playwright.dev/python/docs/emulation#introduction "Direct link to Introduction")

With Playwright you can test your app on any browser as well as emulate a real device such as a mobile phone or tablet. Simply configure the devices you would like to emulate and Playwright will simulate the browser behavior such as `"userAgent"`, `"screenSize"`, `"viewport"` and if it `"hasTouch"` enabled. You can also emulate the `"geolocation"`, `"locale"` and `"timezone"` for all tests or for a specific test as well as set the `"permissions"` to show notifications or change the `"colorScheme"`.

## Devices[​](https://playwright.dev/python/docs/emulation#devices "Direct link to Devices")

Playwright comes with a [registry of device parameters](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json) using [playwright.devices](https://playwright.dev/python/docs/api/class-playwright#playwright-devices) for selected desktop, tablet and mobile devices. It can be used to simulate browser behavior for a specific device such as user agent, screen size, viewport and if it has touch enabled. All tests will run with the specified device parameters.

*   Sync
*   Async

`from playwright.sync_api import sync_playwright, Playwrightdef run(playwright: Playwright):    iphone_13 = playwright.devices['iPhone 13']    browser = playwright.webkit.launch(headless=False)    context = browser.new_context(        **iphone_13,    )with sync_playwright() as playwright:    run(playwright)`

![Image 1: playwright.dev website emulated for iPhone 13](https://user-images.githubusercontent.com/13063165/220411073-76fe59f9-9a2d-463d-8e30-c19a7deca133.png)

## Viewport[​](https://playwright.dev/python/docs/emulation#viewport "Direct link to Viewport")

The viewport is included in the device but you can override it for some tests with [page.set_viewport_size()](https://playwright.dev/python/docs/api/class-page#page-set-viewport-size).

Test file:

The same works inside a test file.

*   Sync
*   Async

`# Create context with given viewportcontext = browser.new_context(  viewport={ 'width': 1280, 'height': 1024 })# Resize viewport for individual pagepage.set_viewport_size({"width": 1600, "height": 1200})# Emulate high-DPIcontext = browser.new_context(  viewport={ 'width': 2560, 'height': 1440 },  device_scale_factor=2,)`

## isMobile[​](https://playwright.dev/python/docs/emulation#ismobile "Direct link to isMobile")

Whether the meta viewport tag is taken into account and touch events are enabled.

*   Sync
*   Async

`context = browser.new_context(  is_mobile=False)`

## Locale & Timezone[​](https://playwright.dev/python/docs/emulation#locale--timezone "Direct link to Locale & Timezone")

Emulate the browser Locale and Timezone which can be set globally for all tests in the config and then overridden for particular tests.

*   Sync
*   Async

`context = browser.new_context(  locale='de-DE',  timezone_id='Europe/Berlin',)`

![Image 2: Bing in german lang and timezone](https://user-images.githubusercontent.com/13063165/220416571-ccc96ab1-44bb-4579-8430-64502fc24a15.png)

## Permissions[​](https://playwright.dev/python/docs/emulation#permissions "Direct link to Permissions")

Allow app to show system notifications.

*   Sync
*   Async

`context = browser.new_context(  permissions=['notifications'],)`

Allow notifications for a specific domain.

*   Sync
*   Async

`context.grant_permissions(['notifications'], origin='https://skype.com')`

Revoke all permissions with [browser_context.clear_permissions()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-clear-permissions).

*   Sync
*   Async

`context.clear_permissions()`

## Geolocation[​](https://playwright.dev/python/docs/emulation#geolocation "Direct link to Geolocation")

Grant `"geolocation"` permissions and set geolocation to a specific area.

*   Sync
*   Async

`context = browser.new_context(  geolocation={"longitude": 41.890221, "latitude": 12.492348},  permissions=["geolocation"])`

![Image 3: geolocation for italy on bing maps](https://user-images.githubusercontent.com/13063165/220417670-bb22d815-f5cd-47c4-8562-0b88165eac27.png)

Change the location later:

*   Sync
*   Async

`context.set_geolocation({"longitude": 48.858455, "latitude": 2.294474})`

**Note** you can only change geolocation for all pages in the context.

Emulate the users `"colorScheme"`. Supported values are 'light' and 'dark'. You can also emulate the media type with [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media).

*   Sync
*   Async

`# Create context with dark modecontext = browser.new_context(  color_scheme='dark' # or 'light')# Create page with dark modepage = browser.new_page(  color_scheme='dark' # or 'light')# Change color scheme for the pagepage.emulate_media(color_scheme='dark')# Change media for pagepage.emulate_media(media='print')`

![Image 4: playwright web in dark mode](https://user-images.githubusercontent.com/13063165/220411638-55d2b051-4678-4da7-9f0b-ed22f5a3c47c.png)

## User Agent[​](https://playwright.dev/python/docs/emulation#user-agent "Direct link to User Agent")

The User Agent is included in the device and therefore you will rarely need to change it however if you do need to test a different user agent you can override it with the `userAgent` property.

*   Sync
*   Async

`context = browser.new_context(  user_agent='My user agent')`

## Offline[​](https://playwright.dev/python/docs/emulation#offline "Direct link to Offline")

Emulate the network being offline.

*   Sync
*   Async

`context = browser.new_context(  offline=True)`

## JavaScript Enabled[​](https://playwright.dev/python/docs/emulation#javascript-enabled "Direct link to JavaScript Enabled")

Emulate a user scenario where JavaScript is disabled.

*   Sync
*   Async

`context = browser.new_context(  java_script_enabled=False)`
