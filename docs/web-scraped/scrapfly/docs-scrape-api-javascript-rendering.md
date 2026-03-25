# Source: https://scrapfly.io/docs/scrape-api/javascript-rendering

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/javascript-rendering

Markdown Content:
Javascript Rendering
--------------------

Scrapfly's headless browser feature is the ultimate solution for web scraping needs that involve javascript-rendered content. Each Scrapfly scrape request that has [render_js option](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js) enabled runs on a dedicated cloud browser instance that is optimized for web scraping and responding quickly and reliably to web scraping actions.

Scrapfly's advanced cache resource is powered by a global private CDN for maximum efficiency, and our solution is designed to handle proxy peering with ease.

> Scraping using cloud browsers is slower and requires more proxy resources. The scraping time depends on factors such as proxy location, website hosting distance, content size, number of page resources, and javascript execution time.

When [Javascript Rendering is enabled](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js), Scrapfly also tracks web resources like:

*   Browser's HTTP queries (background requests), both request and response data
*   Local Storage
*   Session Storage
*   Screenshot (on demand)
*   Remote javascript execution result (on demand)
*   Websockets (Upgrade request and dataframes)
*   Browser downloads (file attachments)

Javascript rendering also enables advanced Scrapfly features like [Javascript Scenarios](https://scrapfly.io/docs/scrape-api/javascript-scenario) which allow issuing common browser control commands like button clicks and form inputs.

When to Use Javascript Rendering?
---------------------------------

Many modern websites require Javascript to work and load pages through javascript powered techniques like XHR (background requests). So, the most reliable way to tell is to try scraping without javascript rendering, check whether desired content exists and compare it with javascript rendering enabled. For that, use [Scrapfly's web player](https://scrapfly.io/dashboard/playground/web-scraper) to experiment with various configurations real-time!

[Wait For Your Content](https://scrapfly.io/docs/scrape-api/javascript-rendering#rendering_wait)
------------------------------------------------------------------------------------------------

Rendering delay is vital for scraping slowly loaded content as dynamic pages take time to fully load all the content.

For slower elements the Scrapfly browsers can be instructed to wait a bit longer through explicit delay or waiting for a specific element to appear:

*   [Fixed Time](https://scrapfly.io/docs/scrape-api/javascript-rendering#delay)
*   [CSS/XPATH Selector](https://scrapfly.io/docs/scrape-api/javascript-rendering#selector)
*   [XHR Pattern](https://scrapfly.io/docs/scrape-api/javascript-rendering#xhr)

In this example, Scrapfly will wait **5s** before extracting the content of the page. The `rendering_wait` parameter is expressed in **milliseconds**. The maximum allowed time to wait is **25s**.

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "render_js=true" \
--data-urlencode "rendering_wait=5000" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

> *   CSS Selector and Xpath are case sensitive
> *    Characters like `~`, `:`, `/` need to be escaped with `\\` Example: `#selector:1234` becomes `#selector\\:1234`

In this example, Scrapfly will wait until product reviews load indicated by the visible presence of `#reviews` CSS selector. The selector watcher will timeout after **15s**. Selectors are case-sensitive and need to be urlencoded.

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "render_js=true" \
--data-urlencode "wait_for_selector=#reviews" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

Alternatively, XPath selectors can be used as well which are often preferred because of more advanced querying features like selecting values based on text content. For example we can wait for reviews containing the word "delicious" to load `//div[contains(@class,"review")]/p[contains(text(),"delicious")]`

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "render_js=true" \
--data-urlencode "wait_for_selector=//div[contains(@class,\"review\")]/p[contains(text(),\"delicious\")]" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

> Related API errors : 
> *   [ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DOM_SELECTOR_NOT_FOUND)

To wait for an intermediate request to respond, you have to prefix the selector with `xhr:`

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "tags=player,project:default" \
--data-urlencode "asp=true" \
--data-urlencode "render_js=true" \
--data-urlencode "wait_for_selector=xhr:/api/graphql" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/reviews"
```

XHR pattern will match as soon it's find in the URL of the XHR requests. The pattern is case sensitive and support wildcard `*` character. E.g: `xhr:/page/*/reviews*`

[Javascript Execution](https://scrapfly.io/docs/scrape-api/javascript-rendering#javascript_executions)
------------------------------------------------------------------------------------------------------

Scrapfly provides a way to inject javascript code to Scrapfly browsers through the [js](https://scrapfly.io/docs/scrape-api/getting-started#api_param_js) parameter

**The provided javascript code has to be base64 encoded**, then it'll be executed after [rendering wait](https://scrapfly.io/docs/scrape-api/getting-started#api_param_rendering_wait) and before [wait_for_selector](https://scrapfly.io/docs/scrape-api/getting-started#api_param_wait_for_selector) (if any).

The return value of the provided javascript code is also returned by Scrapfly API (as long as it's serializable): `result.browser_data.javascript_evaluation_result`

For example, this JS script used on [new.ycombinator.com](https://news.ycombinator.com/) page will retrieve all article titles

```
return Array.from(document.querySelectorAll('.review > p')).map(
            (el) => el.textContent)
```

It should be encoded as base64 (see [our base64 web tool](https://scrapfly.io/web-scraping-tools/base64))

`cmV0dXJuIEFycmF5LmZyb20oZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLnJldmlldyA-IHAnKSkubWFwKChlbCkgPT4gZWwudGV4dENvbnRlbnQp`

and finally it can be passed to Scrapfly API as demonstrated in this example:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "render_js=true" \
--data-urlencode "js=Y21WMGRYSnVJRUZ5Y21GNUxtWnliMjBvWkc5amRXMWxiblF1Y1hWbGNubFRaV3hsWTNSdmNrRnNiQ2duTG5KbGRtbGxkeUEtSUhBbktTa3ViV0Z3S0NobGJDa2dQVDRnWld3dWRHVjRkRU52Ym5SbGJuUXA" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

`https://api.scrapfly.io/scrape?render_js=true&js=cmV0dXJuIEFycmF5LmZyb20oZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLnJldmlldyA-IHAnKSkubWFwKChlbCkgPT4gZWwudGV4dENvbnRlbnQp&key=&url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1`

The API returns the results under `result.browser_data.javascript_evaluation_result` key which contains the script's return value:

```
[
    "Absolutely delicious! The orange flavor is my favorite.",
    "I bought these as a gift, and they were well received. Will definitely purchase again.",
    "Nice variety of flavors. The chocolate is rich and smooth.",
    "The cherry flavor is amazing. Will be buying more.",
    "A bit pricey, but the quality of the chocolate is worth it."
]
```

#### [Snippets](https://scrapfly.io/docs/scrape-api/javascript-rendering#snippets)

Here are some common javascript execution snippets used in web scraping:

*   Scroll to the bottom of the page to fully render the HTML rendering on the website:

`window.scrollTo(0,document.body.scrollHeight);` 

[Screenshot](https://scrapfly.io/docs/scrape-api/javascript-rendering#screenshot)
---------------------------------------------------------------------------------

Javascript rendering also allows you to take a screenshot of the page using the [screenshot](https://scrapfly.io/docs/scrape-api/getting-started#api_param_screenshot) parameter. For more see our [in-depth docs for screenshot capture](https://scrapfly.io/docs/scrape-api/screenshot).

[Browser Downloads & File Attachments](https://scrapfly.io/docs/scrape-api/javascript-rendering#browser_downloads)
------------------------------------------------------------------------------------------------------------------

When Javascript Rendering is enabled, Scrapfly browsers automatically capture files that are downloaded during browser interactions. This powerful feature allows you to retrieve documents, PDFs, spreadsheets, and other file attachments that are triggered by button clicks, form submissions, or other browser interactions.

Downloaded files are automatically captured and stored on Scrapfly's servers. The file metadata and download URLs are available in the API response under `result.browser_data.attachments` as well as in the monitoring logs **Attachments** tab.

> When triggering a download using [JavaScript Scenarios](https://scrapfly.io/docs/scrape-api/javascript-scenario), placing the download action as the last step may prevent the download from being initiated before the scenario ends. To ensure the download begins successfully, always add a wait action after the download trigger (e.g., wait for 2-3 seconds). Once initiated, Scrapfly will automatically wait for the download to complete.

### [Common Download Scenarios](https://scrapfly.io/docs/scrape-api/javascript-rendering#downloads_common_scenarios)

Browser downloads are commonly used to capture:

*   **PDF Reports** - Generated reports, invoices, receipts, or documents
*   **Spreadsheet Exports** - CSV, Excel, or other data exports
*   **Download Buttons** - Files triggered by clicking download buttons
*   **Dynamic Content** - Files generated on-demand by web applications
*   **Authenticated Documents** - Files that require login and session management

### [Usage Example](https://scrapfly.io/docs/scrape-api/javascript-rendering#downloads_usage)

To capture browser downloads, combine Javascript Rendering with [Javascript Scenarios](https://scrapfly.io/docs/scrape-api/javascript-scenario) to trigger the download action. Here's an example using our test page [https://web-scraping.dev/file-download](https://web-scraping.dev/file-download):

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "retry=false" \
--data-urlencode "tags=player,project:default" \
--data-urlencode "timeout=75000" \
--data-urlencode "asp=true" \
--data-urlencode "render_js=true" \
--data-urlencode "screenshots[test]=fullpage" \
--data-urlencode "js_scenario=W3siY2xpY2siOnsic2VsZWN0b3IiOiIjZG93bmxvYWQtYnRuIn19LHsid2FpdCI6MjUwMH0seyJjbGljayI6eyJzZWxlY3RvciI6IiNkb3dubG9hZC1idG4ifX0seyJ3YWl0IjoyNTAwfSx7ImNsaWNrIjp7InNlbGVjdG9yIjoiI2Rvd25sb2FkLWJ0biJ9fSx7IndhaXQiOjI1MDB9XQ" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/file-download"
```

`https://api.scrapfly.io/scrape?retry=false&tags=player%2Cproject%3Adefault&timeout=75000&asp=true&render_js=true&screenshots%5Btest%5D=fullpage&js_scenario=W3siY2xpY2siOnsic2VsZWN0b3IiOiIjZG93bmxvYWQtYnRuIn19LHsid2FpdCI6MjUwMH0seyJjbGljayI6eyJzZWxlY3RvciI6IiNkb3dubG9hZC1idG4ifX0seyJ3YWl0IjoyNTAwfSx7ImNsaWNrIjp7InNlbGVjdG9yIjoiI2Rvd25sb2FkLWJ0biJ9fSx7IndhaXQiOjI1MDB9XQ&key=&url=https%3A%2F%2Fweb-scraping.dev%2Ffile-download`

In this example, the Javascript Scenario performs these actions:

*   Clicks the download button (`#download-btn`)
*   Waits 2.5 seconds for the download to complete
*   Repeats this action three times to capture multiple downloads

#### Try It in API Player

You can test this feature directly in the [API Player](https://scrapfly.io/dashboard/playground/web-scraper). The test page [https://web-scraping.dev/file-download](https://web-scraping.dev/file-download) is specifically designed to demonstrate browser downloads functionality.

The Javascript Scenario configuration for this example is:

```
[
  {"click": {"selector":"#download-btn"}},
  {"wait": 2500},
  {"click": {"selector":"#download-btn"}},
  {"wait": 2500},
  {"click": {"selector":"#download-btn"}},
  {"wait": 2500}
]
```

This scenario clicks the download button three times with 2.5-second waits between each click. Each click triggers the download of `download-sample.pdf`, and the browser automatically handles duplicate filenames by numbering them as `download-sample.pdf`, `download-sample (1).pdf`, and `download-sample (2).pdf`.

### [Attachments Structure](https://scrapfly.io/docs/scrape-api/javascript-rendering#downloads_response)

Downloaded files appear in the API response under `result.browser_data.attachments` as an array. Each attachment contains detailed metadata:

```
{
    ...
    "result": {
        ...
        "browser_data": {
            "attachments": [
                {
                    "content": "https://api.scrapfly.io/scrape/attachment/01K9AAJG2HVNHR96M791G871MK/520d90b4-8f2e-497c-887e-44915ba3a874",
                    "content_type": "application/pdf",
                    "filename": "download-sample.pdf",
                    "id": "520d90b4-8f2e-497c-887e-44915ba3a874",
                    "size": 10360,
                    "state": "completed",
                    "suggested_filename": "download-sample.pdf",
                    "url": "https://web-scraping.dev/api/download-file"
                },
                {
                    "content": "https://api.scrapfly.io/scrape/attachment/01K9AAJG2HVNHR96M791G871MK/f7d76f5b-27d7-4db5-9ea8-e1859e6a0aa4",
                    "content_type": "application/pdf",
                    "filename": "download-sample (1).pdf",
                    "id": "f7d76f5b-27d7-4db5-9ea8-e1859e6a0aa4",
                    "size": 10360,
                    "state": "completed",
                    "suggested_filename": "download-sample.pdf",
                    "url": "https://web-scraping.dev/api/download-file"
                },
                {
                    "content": "https://api.scrapfly.io/scrape/attachment/01K9AAJG2HVNHR96M791G871MK/dd250002-23ac-494f-ac73-6f586927e181",
                    "content_type": "application/pdf",
                    "filename": "download-sample (2).pdf",
                    "id": "dd250002-23ac-494f-ac73-6f586927e181",
                    "size": 10360,
                    "state": "completed",
                    "suggested_filename": "download-sample.pdf",
                    "url": "https://web-scraping.dev/api/download-file"
                }
            ],
            ...
        }
        ...
    }
    ...
}
```

### [Downloading Files Programmatically](https://scrapfly.io/docs/scrape-api/javascript-rendering#downloads_retrieve)

Captured files are available in the API response at the JSON path `result.browser_data.attachments`. Each attachment in this array contains a `content` field with the unauthenticated download URL (You need to append your API key via `key` query parameter).

To download a file, take the URL from `result.browser_data.attachments[0].content` and append your API key as the `key` query parameter. Here's a raw curl example:

`curl -X GET "https://api.scrapfly.io/scrape/attachment/{{ log uuid }}/{{ attachment uuid }}?key=YOUR_API_KEY" -o attachment.pdf`

This downloads the file and saves it as `attachment.pdf` in your current directory.

> Attachments are priced following the binary format grid per 100kb, the first 100kb is free based on proxy network type. Refer to [Binary Format Pricing](https://scrapfly.io/docs/scrape-api/billing)for more details.

[Resource Tracking](https://scrapfly.io/docs/scrape-api/javascript-rendering#resource_tracking)
-----------------------------------------------------------------------------------------------

Scrapfly tracks all background requests performed by the scraped websites (XHR). The captured data includes all necessary request details like the URL, headers, method, cookies and the request body. This data is available under `result.browser_data`.

Scrapfly also tracks browser's `Local Storage` and `Session Storage` content which is available under `local_storage_data` and `session_storage_data` keys. See this example response:

```
...
"result": {
    ...,
    "browser_data": {
        "xhr_call": [
            {
                "url": "https://aan.amazon.fr/cem",
                "headers": {
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
                    "content-type": "application/json",
                    "accept": "*/*",
                    "referer": "https://images-eu.ssl-images-amazon.com/images/G/08/ape/sf/whitelisted/desktop/sf-1.50.628cb61._V408130105_.html"
                },
                "method": "POST",
                "body": "{\"render_id\":\"4a7152f0-cb58-4de8-b152-f0cb58cde8a2\",\"event_type\":\"impression\",\"dimensions\":{\"subtype\":\"impression\",\"value\":1,\"template_name\":\"Dynamic eCommerce - universal\"}}"
            },
            {
                "url": "https://www.amazon.fr/gp/customer-reviews/aj/private/reviewsGallery/get-image-gallery-assets",
                "headers": {
                    "rtt": "0",
                    "accept": "text/html,*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "downlink": "10",
                    "ect": "4g",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded",
                    "referer": "https://www.amazon.fr/gp/product/B008AVQXDO?pf_rd_r=APG7NKFQ8DTBPK2TEN8R&pf_rd_p=70373c30-7461-4a24-bb1f-f3fde4f2df3a",
                    "cookie": "session-id=261-7851197-2783504; i18n-prefs=EUR; ubid-acbfr=262-5387700-5547500; session-id-time=2082754801l; x-wl-uid=145H5Y5j+m7oe7NpElaItmpA5YWGFqUy34ZvPnc+Yd8m+UIZC49+YTzyieSn/K4Kfq162NF1AbZo=; session-token=aLl1Sgktrzq+wYbYCVAKoXJA+3aIAhtP36mNtxkpZORbiSqd3ur/uaU6W1aHycEtUy4LpAJrcV2YmGqNHYb4trXCj3Wt4Vxc5W/aCaww5HctUNsijeRB2Dxp/ca1gtYdEEpTJGBprLlnrFg85RsOkfiWb9nysakwy54GjF9aOjksmN0ip3XCgDbO9uIZ7/X8lgM7pTDy7tTVBJtRvK79S/k9PbfDxEjXULIpNE8iYBdTvm95Xevgmgr1nouA1frzwUFYYzhCg1k=; csm-hit=tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no"
                },
                "method": "POST",
                "body": null
            },
            {
                "url": "https://www.amazon.fr/gp/customer-reviews/aj/private/reviewsGallery/get-application-resources-for-reviews-gallery",
                "headers": {
                    "rtt": "0",
                    "accept": "*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "downlink": "10",
                    "ect": "4g",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded",
                    "referer": "https://www.amazon.fr/gp/product/B008AVQXDO?pf_rd_r=APG7NKFQ8DTBPK2TEN8R&pf_rd_p=70373c30-7461-4a24-bb1f-f3fde4f2df3a",
                    "cookie": "session-id=261-7851197-2783504; i18n-prefs=EUR; ubid-acbfr=262-5387700-5547500; session-id-time=2082754801l; x-wl-uid=145H5Y5j+m7oe7NpElaItmpA5YWGFqUy34ZvPnc+Yd8m+UIZC49+YTzyieSn/K4Kfq162NF1AbZo=; session-token=aLl1Sgktrzq+wYbYCVAKoXJA+3aIAhtP36mNtxkpZORbiSqd3ur/uaU6W1aHycEtUy4LpAJrcV2YmGqNHYb4trXCj3Wt4Vxc5W/aCaww5HctUNsijeRB2Dxp/ca1gtYdEEpTJGBprLlnrFg85RsOkfiWb9nysakwy54GjF9aOjksmN0ip3XCgDbO9uIZ7/X8lgM7pTDy7tTVBJtRvK79S/k9PbfDxEjXULIpNE8iYBdTvm95Xevgmgr1nouA1frzwUFYYzhCg1k=; csm-hit=tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no"
                },
                "method": "POST",
                "body": "noCache=1596420693002"
            },
            {
                "url": "https://www.amazon.fr/gp/cerberus/gv",
                "headers": {
                    "rtt": "0",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "cache-control": "no-cache",
                    "x-requested-with": "XMLHttpRequest",
                    "downlink": "10",
                    "ect": "4g",
                    "referer": "https://www.amazon.fr/gp/product/B008AVQXDO?pf_rd_r=APG7NKFQ8DTBPK2TEN8R&pf_rd_p=70373c30-7461-4a24-bb1f-f3fde4f2df3a",
                    "cookie": "session-id=261-7851197-2783504; i18n-prefs=EUR; ubid-acbfr=262-5387700-5547500; session-id-time=2082754801l; x-wl-uid=145H5Y5j+m7oe7NpElaItmpA5YWGFqUy34ZvPnc+Yd8m+UIZC49+YTzyieSn/K4Kfq162NF1AbZo=; session-token=aLl1Sgktrzq+wYbYCVAKoXJA+3aIAhtP36mNtxkpZORbiSqd3ur/uaU6W1aHycEtUy4LpAJrcV2YmGqNHYb4trXCj3Wt4Vxc5W/aCaww5HctUNsijeRB2Dxp/ca1gtYdEEpTJGBprLlnrFg85RsOkfiWb9nysakwy54GjF9aOjksmN0ip3XCgDbO9uIZ7/X8lgM7pTDy7tTVBJtRvK79S/k9PbfDxEjXULIpNE8iYBdTvm95Xevgmgr1nouA1frzwUFYYzhCg1k=; csm-hit=tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no"
                },
                "method": "POST",
                "body": "payload=%7B%22producerId%22%3A%22detail-page%22%2C%22asin%22%3A%22B008AVQXDO%22%2C%22asin_price%22%3A%229.49%22%2C%22asin_shipping_price%22%3A%220%22%2C%22asin_currency_code%22%3A%22EUR%22%2C%22device_type%22%3A%22WEB%22%2C%22display_code%22%3A%22Asin+is+not+eligible+because+it+has+a+retail+offer%22%2C%22substitute_count%22%3A%22-1%22%7D"
            }
        ],
        "local_storage_data": {
            "csm-hit": "tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no",
            "csm:adb": "adblk_no",
            "csm-bf": "[\"5B0K136YR4QK89MQ8RG0\"]",
            "a-font-class": "a-ember"
        },
        "session_storage_data": {
            "csm-hit": "tb:s-5B0K136YR4QK89MQ8RG0|1596420691120&t:1596420692684&adb:adblk_no",
            "csm:adb": "adblk_no",
            "csm-bf": "[\"5B0K136YR4QK89MQ8RG0\"]",
            "a-font-class": "a-ember"
        },
        "websockets": [],
        "javascript_evaluation_result": null
    },
    ...
}
...
```

[Limitations](https://scrapfly.io/docs/scrape-api/javascript-rendering#limitations)
-----------------------------------------------------------------------------------

Javascript rendering feature is only available with `GET` method. You can't use a browser to send `POST, PATCH, PUT, HEAD` requests.

Following XHR / Fetched resources are not tracked by scrapfly browsers:

*   Fonts: `.woff`, `.woff2`, `.otf`, `.ttf`
*   Media: `.webm`, `.oga`, `.aac`, `.m4a`, `.mp3`, `.wav`, `.mp4`
*   Image: `.svg`, `.png`, `.gif`, `.jpg`, `.jpeg`, `.ico`
*   Style: `.css`
*   Other: `.pbf`

> It's not possible to directly download the media/image content with a scrapfly browser as it will load the image url as a html document by wrapping image data as `img`tag. To directly download images disable the browser rendering and the image data will be returned as a base64-encoded binary data.

All related errors are listed below. You can see the full description and examples of errors response on [Errors section](https://scrapfly.io/docs/scrape-api/errors#proxy)

*   422 - [ERR::SCRAPE::DRIVER_CRASHED](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_CRASHED)
*   422 - [ERR::SCRAPE::DRIVER_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::DRIVER_TIMEOUT)
*   422 - [ERR::SCRAPE::JAVASCRIPT_EXECUTION](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::JAVASCRIPT_EXECUTION)
*   422 - [ERR::SCRAPE::NO_BROWSER_AVAILABLE](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::NO_BROWSER_AVAILABLE)

[Pricing](https://scrapfly.io/docs/scrape-api/javascript-rendering#pricing)
---------------------------------------------------------------------------

Using JavaScript rendering will cost **5 Scrape API Credits**. Keep in mind JavaScript Rendering is slow and uses a lot of resources so for maximum performance, you should avoid it when it's not required.

> API Response contains header `X-Scrapfly-Api-Cost`indicate you the billed amount.
