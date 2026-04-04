# Source: https://playwright.dev/python/docs/api/class-browser

Title: Browser | Playwright Python

URL Source: https://playwright.dev/python/docs/api/class-browser

Published Time: Thu, 26 Mar 2026 01:00:24 GMT

Markdown Content:
A Browser is created via [browser_type.launch()](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch). An example of using a [Browser](https://playwright.dev/python/docs/api/class-browser "Browser") to create a [Page](https://playwright.dev/python/docs/api/class-page "Page"):

*   Sync
*   Async

`from playwright.sync_api import sync_playwright, Playwrightdef run(playwright: Playwright):    firefox = playwright.firefox    browser = firefox.launch()    page = browser.new_page()    page.goto("https://example.com")    browser.close()with sync_playwright() as playwright:    run(playwright)`

* * *

## Methods[​](https://playwright.dev/python/docs/api/class-browser#methods "Direct link to Methods")

### close[​](https://playwright.dev/python/docs/api/class-browser#browser-close "Direct link to close")

Added before v1.9

browser.close
In case this browser is obtained using [browser_type.launch()](https://playwright.dev/python/docs/api/class-browsertype#browser-type-launch), closes the browser and all of its pages (if any were opened).

In case this browser is connected to, clears all created contexts belonging to this browser and disconnects from the browser server.

The [Browser](https://playwright.dev/python/docs/api/class-browser "Browser") object itself is considered to be disposed and cannot be used anymore.

**Usage**

`browser.close()browser.close(**kwargs)`

**Arguments**

*   `reason`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_ Added in: v1.40[#](https://playwright.dev/python/docs/api/class-browser#browser-close-option-reason)

The reason to be reported to the operations interrupted by the browser closure.

**Returns**

*   [NoneType](https://docs.python.org/3/library/constants.html#None "None")[#](https://playwright.dev/python/docs/api/class-browser#browser-close-return)

* * *

### new_browser_cdp_session[​](https://playwright.dev/python/docs/api/class-browser#browser-new-browser-cdp-session "Direct link to new_browser_cdp_session")

Added in: v1.11

browser.new_browser_cdp_session

note

CDP Sessions are only supported on Chromium-based browsers.

Returns the newly created browser session.

**Usage**

`browser.new_browser_cdp_session()`

**Returns**

*   [CDPSession](https://playwright.dev/python/docs/api/class-cdpsession "CDPSession")[#](https://playwright.dev/python/docs/api/class-browser#browser-new-browser-cdp-session-return)

* * *

### new_context[​](https://playwright.dev/python/docs/api/class-browser#browser-new-context "Direct link to new_context")

Added before v1.9

browser.new_context
Creates a new browser context. It won't share cookies/cache with other browser contexts.

note

If directly using this method to create [BrowserContext](https://playwright.dev/python/docs/api/class-browsercontext "BrowserContext")s, it is best practice to explicitly close the returned context via [browser_context.close()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-close) when your code is done with the [BrowserContext](https://playwright.dev/python/docs/api/class-browsercontext "BrowserContext"), and before calling [browser.close()](https://playwright.dev/python/docs/api/class-browser#browser-close). This will ensure the `context` is closed gracefully and any artifacts—like HARs and videos—are fully flushed and saved.

**Usage**

*   Sync
*   Async

`browser = playwright.firefox.launch() # or "chromium" or "webkit".# create a new incognito browser context.context = browser.new_context()# create a new page in a pristine context.page = context.new_page()page.goto("https://example.com")# gracefully close up everythingcontext.close()browser.close()`

**Arguments**

*   `accept_downloads`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-accept-downloads)

Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted.

*   `base_url`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-base-url)

When using [page.goto()](https://playwright.dev/python/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/python/docs/api/class-page#page-route), [page.wait_for_url()](https://playwright.dev/python/docs/api/class-page#page-wait-for-url), [page.expect_request()](https://playwright.dev/python/docs/api/class-page#page-wait-for-request), or [page.expect_response()](https://playwright.dev/python/docs/api/class-page#page-wait-for-response) it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples:

    *   baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html`
    *   baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html`
    *   baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html`

*   `bypass_csp`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-bypass-csp)

Toggles bypassing page's Content-Security-Policy. Defaults to `false`.

*   `client_certificates`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")] _(optional)_ Added in: 1.46[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-client-certificates)

    *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Exact origin that the certificate is valid for. Origin includes `https` protocol, a hostname and optionally a port.

    *   `certPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the file with the certificate in PEM format.

    *   `cert`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the certificate in PEM format.

    *   `keyPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the file with the private key in PEM format.

    *   `key`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the private key in PEM format.

    *   `pfxPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the PFX or PKCS12 encoded private key and certificate chain.

    *   `pfx`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the PFX or PKCS12 encoded private key and certificate chain.

    *   `passphrase`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Passphrase for the private key (PEM or PFX).

TLS Client Authentication allows the server to request a client certificate and verify it.

**Details**

An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.

Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.

note

When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`.

*   `color_scheme` "light" | "dark" | "no-preference" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-color-scheme)

Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`.

*   `contrast` "no-preference" | "more" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-contrast)

Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`.

*   `device_scale_factor`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-device-scale-factor)

Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about [emulating devices with device scale factor](https://playwright.dev/python/docs/emulation#devices).

*   `extra_http_headers`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-extra-http-headers)

An object containing additional HTTP headers to be sent with every request. Defaults to none.

*   `forced_colors` "active" | "none" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-forced-colors)

Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`.

*   `geolocation`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-geolocation)

    *   `latitude`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Latitude between -90 and 90.

    *   `longitude`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Longitude between -180 and 180.

    *   `accuracy`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")_(optional)_

Non-negative accuracy value. Defaults to `0`.

*   `has_touch`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-has-touch)

Specifies if viewport supports touch events. Defaults to false. Learn more about [mobile emulation](https://playwright.dev/python/docs/emulation#devices).

*   `http_credentials`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-http-credentials)

    *   `username`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

    *   `password`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

    *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Restrain sending http credentials on specific origin (scheme://host:port).

    *   `send` "unauthorized" | "always" _(optional)_

This option only applies to the requests sent from corresponding [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext "APIRequestContext") and does not affect requests sent from the browser. `'always'` - `Authorization` header with basic authentication credentials will be sent with the each API request. `'unauthorized` - the credentials are only sent when 401 (Unauthorized) response with `WWW-Authenticate` header is received. Defaults to `'unauthorized'`.

Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.

*   `ignore_https_errors`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-ignore-https-errors)

Whether to ignore HTTPS errors when sending network requests. Defaults to `false`.

*   `is_mobile`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-is-mobile)

Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false` and is not supported in Firefox. Learn more about [mobile emulation](https://playwright.dev/python/docs/emulation#ismobile).

*   `java_script_enabled`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-java-script-enabled)

Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about [disabling JavaScript](https://playwright.dev/python/docs/emulation#javascript-enabled).

*   `locale`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-locale)

Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our [emulation guide](https://playwright.dev/python/docs/emulation#locale--timezone).

*   `no_viewport`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-no-viewport)

Does not enforce fixed viewport, allows resizing window in the headed mode.

*   `offline`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-offline)

Whether to emulate network being offline. Defaults to `false`. Learn more about [network emulation](https://playwright.dev/python/docs/emulation#offline).

*   `permissions`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-permissions)

A list of permissions to grant to all pages in this context. See [browser_context.grant_permissions()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-grant-permissions) for more details. Defaults to none.

*   `proxy`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-proxy)

    *   `server`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Proxy to be used for all requests. HTTP and SOCKS proxies are supported, for example `http://myproxy.com:3128` or `socks5://myproxy.com:3128`. Short form `myproxy.com:3128` is considered an HTTP proxy.

    *   `bypass`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional comma-separated domains to bypass proxy, for example `".com, chromium.org, .domain.com"`.

    *   `username`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional username to use if HTTP proxy requires authentication.

    *   `password`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional password to use if HTTP proxy requires authentication.

Network proxy settings to use with this context. Defaults to none.

*   `record_har_content` "omit" | "embed" | "attach" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-har-content)

Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification.

*   `record_har_mode` "full" | "minimal" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-har-mode)

When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`.

*   `record_har_omit_content`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-har-omit-content)

Optional setting to control whether to omit request content from the HAR. Defaults to `false`.

*   `record_har_path`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-har-path)

Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call [browser_context.close()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-close) for the HAR to be saved.

*   `record_har_url_filter`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str") | [Pattern](https://docs.python.org/3/library/re.html "Pattern")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-har-url-filter)

*   `record_video_dir`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-video-dir)

Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call [browser_context.close()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-close) for videos to be saved.

*   `record_video_size`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-record-video-size)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

Video frame width.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

Video frame height.

Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size.

*   `reduced_motion` "reduce" | "no-preference" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-reduced-motion)

Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`.

*   `screen`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-screen)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page width in pixels.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page height in pixels.

Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the [viewport](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-viewport) is set.

*   `service_workers` "allow" | "block" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-service-workers)

Whether to allow sites to register Service workers. Defaults to `'allow'`.

    *   `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered.
    *   `'block'`: Playwright will block all registration of Service Workers.

*   `storage_state`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-storage-state)

    *   `cookies`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

        *   `name`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `value`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `domain`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Domain and path are required. For the cookie to apply to all subdomains as well, prefix domain with a dot, like this: ".example.com"

        *   `path`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Domain and path are required

        *   `expires`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Unix time in seconds.

        *   `httpOnly`[bool](https://docs.python.org/3/library/stdtypes.html "bool")

        *   `secure`[bool](https://docs.python.org/3/library/stdtypes.html "bool")

        *   `sameSite` "Strict" | "Lax" | "None"

sameSite flag

Cookies to set for context

    *   `origins`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

        *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `localStorage`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

            *   `name`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

            *   `value`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

localStorage to set for context

Learn more about [storage state and auth](https://playwright.dev/python/docs/auth).

Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via [browser_context.storage_state()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-storage-state).

*   `strict_selectors`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-strict-selectors)

If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See [Locator](https://playwright.dev/python/docs/api/class-locator "Locator") to learn more about the strict mode.

*   `timezone_id`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-timezone-id)

Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone.

*   `user_agent`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-user-agent)

Specific user agent to use in this context.

*   `viewport`[NoneType](https://docs.python.org/3/library/constants.html#None "None") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-option-viewport)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page width in pixels.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page height in pixels.

Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about [viewport emulation](https://playwright.dev/python/docs/emulation#viewport).

**Returns**

*   [BrowserContext](https://playwright.dev/python/docs/api/class-browsercontext "BrowserContext")[#](https://playwright.dev/python/docs/api/class-browser#browser-new-context-return)

* * *

### new_page[​](https://playwright.dev/python/docs/api/class-browser#browser-new-page "Direct link to new_page")

Added before v1.9

browser.new_page
Creates a new page in a new browser context. Closing this page will close the context as well.

This is a convenience API that should only be used for the single-page scenarios and short snippets. Production code and testing frameworks should explicitly create [browser.new_context()](https://playwright.dev/python/docs/api/class-browser#browser-new-context) followed by the [browser_context.new_page()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-new-page) to control their exact life times.

**Usage**

`browser.new_page()browser.new_page(**kwargs)`

**Arguments**

*   `accept_downloads`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-accept-downloads)

Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted.

*   `base_url`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-base-url)

When using [page.goto()](https://playwright.dev/python/docs/api/class-page#page-goto), [page.route()](https://playwright.dev/python/docs/api/class-page#page-route), [page.wait_for_url()](https://playwright.dev/python/docs/api/class-page#page-wait-for-url), [page.expect_request()](https://playwright.dev/python/docs/api/class-page#page-wait-for-request), or [page.expect_response()](https://playwright.dev/python/docs/api/class-page#page-wait-for-response) it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples:

    *   baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html`
    *   baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html`
    *   baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html`

*   `bypass_csp`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-bypass-csp)

Toggles bypassing page's Content-Security-Policy. Defaults to `false`.

*   `client_certificates`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")] _(optional)_ Added in: 1.46[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-client-certificates)

    *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Exact origin that the certificate is valid for. Origin includes `https` protocol, a hostname and optionally a port.

    *   `certPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the file with the certificate in PEM format.

    *   `cert`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the certificate in PEM format.

    *   `keyPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the file with the private key in PEM format.

    *   `key`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the private key in PEM format.

    *   `pfxPath`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_

Path to the PFX or PKCS12 encoded private key and certificate chain.

    *   `pfx`[bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")_(optional)_

Direct value of the PFX or PKCS12 encoded private key and certificate chain.

    *   `passphrase`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Passphrase for the private key (PEM or PFX).

TLS Client Authentication allows the server to request a client certificate and verify it.

**Details**

An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.

Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.

note

When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`.

*   `color_scheme` "light" | "dark" | "no-preference" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-color-scheme)

Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`.

*   `contrast` "no-preference" | "more" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-contrast)

Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`.

*   `device_scale_factor`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-device-scale-factor)

Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about [emulating devices with device scale factor](https://playwright.dev/python/docs/emulation#devices).

*   `extra_http_headers`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-extra-http-headers)

An object containing additional HTTP headers to be sent with every request. Defaults to none.

*   `forced_colors` "active" | "none" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-forced-colors)

Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`.

*   `geolocation`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-geolocation)

    *   `latitude`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Latitude between -90 and 90.

    *   `longitude`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Longitude between -180 and 180.

    *   `accuracy`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")_(optional)_

Non-negative accuracy value. Defaults to `0`.

*   `has_touch`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-has-touch)

Specifies if viewport supports touch events. Defaults to false. Learn more about [mobile emulation](https://playwright.dev/python/docs/emulation#devices).

*   `http_credentials`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-http-credentials)

    *   `username`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

    *   `password`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

    *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Restrain sending http credentials on specific origin (scheme://host:port).

    *   `send` "unauthorized" | "always" _(optional)_

This option only applies to the requests sent from corresponding [APIRequestContext](https://playwright.dev/python/docs/api/class-apirequestcontext "APIRequestContext") and does not affect requests sent from the browser. `'always'` - `Authorization` header with basic authentication credentials will be sent with the each API request. `'unauthorized` - the credentials are only sent when 401 (Unauthorized) response with `WWW-Authenticate` header is received. Defaults to `'unauthorized'`.

Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.

*   `ignore_https_errors`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-ignore-https-errors)

Whether to ignore HTTPS errors when sending network requests. Defaults to `false`.

*   `is_mobile`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-is-mobile)

Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false` and is not supported in Firefox. Learn more about [mobile emulation](https://playwright.dev/python/docs/emulation#ismobile).

*   `java_script_enabled`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-java-script-enabled)

Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about [disabling JavaScript](https://playwright.dev/python/docs/emulation#javascript-enabled).

*   `locale`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-locale)

Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our [emulation guide](https://playwright.dev/python/docs/emulation#locale--timezone).

*   `no_viewport`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-no-viewport)

Does not enforce fixed viewport, allows resizing window in the headed mode.

*   `offline`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-offline)

Whether to emulate network being offline. Defaults to `false`. Learn more about [network emulation](https://playwright.dev/python/docs/emulation#offline).

*   `permissions`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-permissions)

A list of permissions to grant to all pages in this context. See [browser_context.grant_permissions()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-grant-permissions) for more details. Defaults to none.

*   `proxy`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-proxy)

    *   `server`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Proxy to be used for all requests. HTTP and SOCKS proxies are supported, for example `http://myproxy.com:3128` or `socks5://myproxy.com:3128`. Short form `myproxy.com:3128` is considered an HTTP proxy.

    *   `bypass`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional comma-separated domains to bypass proxy, for example `".com, chromium.org, .domain.com"`.

    *   `username`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional username to use if HTTP proxy requires authentication.

    *   `password`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_

Optional password to use if HTTP proxy requires authentication.

Network proxy settings to use with this context. Defaults to none.

*   `record_har_content` "omit" | "embed" | "attach" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-har-content)

Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification.

*   `record_har_mode` "full" | "minimal" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-har-mode)

When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`.

*   `record_har_omit_content`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-har-omit-content)

Optional setting to control whether to omit request content from the HAR. Defaults to `false`.

*   `record_har_path`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-har-path)

Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call [browser_context.close()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-close) for the HAR to be saved.

*   `record_har_url_filter`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str") | [Pattern](https://docs.python.org/3/library/re.html "Pattern")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-har-url-filter)

*   `record_video_dir`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-video-dir)

Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call [browser_context.close()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-close) for videos to be saved.

*   `record_video_size`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-record-video-size)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

Video frame width.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

Video frame height.

Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size.

*   `reduced_motion` "reduce" | "no-preference" | "null" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-reduced-motion)

Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See [page.emulate_media()](https://playwright.dev/python/docs/api/class-page#page-emulate-media) for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`.

*   `screen`[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-screen)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page width in pixels.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page height in pixels.

Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the [viewport](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-viewport) is set.

*   `service_workers` "allow" | "block" _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-service-workers)

Whether to allow sites to register Service workers. Defaults to `'allow'`.

    *   `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered.
    *   `'block'`: Playwright will block all registration of Service Workers.

*   `storage_state`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-storage-state)

    *   `cookies`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

        *   `name`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `value`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `domain`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Domain and path are required. For the cookie to apply to all subdomains as well, prefix domain with a dot, like this: ".example.com"

        *   `path`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

Domain and path are required

        *   `expires`[float](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "float")

Unix time in seconds.

        *   `httpOnly`[bool](https://docs.python.org/3/library/stdtypes.html "bool")

        *   `secure`[bool](https://docs.python.org/3/library/stdtypes.html "bool")

        *   `sameSite` "Strict" | "Lax" | "None"

sameSite flag

Cookies to set for context

    *   `origins`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

        *   `origin`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

        *   `localStorage`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")]

            *   `name`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

            *   `value`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")

localStorage to set for context

Learn more about [storage state and auth](https://playwright.dev/python/docs/auth).

Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via [browser_context.storage_state()](https://playwright.dev/python/docs/api/class-browsercontext#browser-context-storage-state).

*   `strict_selectors`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-strict-selectors)

If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See [Locator](https://playwright.dev/python/docs/api/class-locator "Locator") to learn more about the strict mode.

*   `timezone_id`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-timezone-id)

Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone.

*   `user_agent`[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-user-agent)

Specific user agent to use in this context.

*   `viewport`[NoneType](https://docs.python.org/3/library/constants.html#None "None") | [Dict](https://docs.python.org/3/library/typing.html#typing.Dict "Dict")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-option-viewport)

    *   `width`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page width in pixels.

    *   `height`[int](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "int")

page height in pixels.

Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about [viewport emulation](https://playwright.dev/python/docs/emulation#viewport).

**Returns**

*   [Page](https://playwright.dev/python/docs/api/class-page "Page")[#](https://playwright.dev/python/docs/api/class-browser#browser-new-page-return)

* * *

### start_tracing[​](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing "Direct link to start_tracing")

Added in: v1.11

browser.start_tracing
You can use [browser.start_tracing()](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing) and [browser.stop_tracing()](https://playwright.dev/python/docs/api/class-browser#browser-stop-tracing) to create a trace file that can be opened in Chrome DevTools performance panel.

**Usage**

*   Sync
*   Async

`browser.start_tracing(page, path="trace.json")page.goto("https://www.google.com")browser.stop_tracing()`

**Arguments**

*   `page`[Page](https://playwright.dev/python/docs/api/class-page "Page")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing-option-page)

Optional, if specified, tracing includes screenshots of the given page.

*   `categories`[List](https://docs.python.org/3/library/typing.html#typing.List "List")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing-option-categories)

specify custom categories to use instead of default.

*   `path`[Union](https://docs.python.org/3/library/typing.html#typing.Union "Union")[[str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str"), [pathlib.Path](https://realpython.com/python-pathlib/ "pathlib.Path")] _(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing-option-path)

A path to write the trace file to.

*   `screenshots`[bool](https://docs.python.org/3/library/stdtypes.html "bool")_(optional)_[#](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing-option-screenshots)

captures screenshots in the trace.

**Returns**

*   [NoneType](https://docs.python.org/3/library/constants.html#None "None")[#](https://playwright.dev/python/docs/api/class-browser#browser-start-tracing-return)

* * *

### stop_tracing[​](https://playwright.dev/python/docs/api/class-browser#browser-stop-tracing "Direct link to stop_tracing")

Added in: v1.11

browser.stop_tracing
Returns the buffer with trace data.

**Usage**

`browser.stop_tracing()`

**Returns**

*   [bytes](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")[#](https://playwright.dev/python/docs/api/class-browser#browser-stop-tracing-return)

* * *

## Properties[​](https://playwright.dev/python/docs/api/class-browser#properties "Direct link to Properties")

### browser_type[​](https://playwright.dev/python/docs/api/class-browser#browser-browser-type "Direct link to browser_type")

Added in: v1.23

browser.browser_type
Get the browser type (chromium, firefox or webkit) that the browser belongs to.

**Usage**

`browser.browser_type`

**Returns**

*   [BrowserType](https://playwright.dev/python/docs/api/class-browsertype "BrowserType")[#](https://playwright.dev/python/docs/api/class-browser#browser-browser-type-return)

* * *

### contexts[​](https://playwright.dev/python/docs/api/class-browser#browser-contexts "Direct link to contexts")

Added before v1.9

browser.contexts
Returns an array of all open browser contexts. In a newly created browser, this will return zero browser contexts.

**Usage**

*   Sync
*   Async

`browser = pw.webkit.launch()print(len(browser.contexts)) # prints `0`context = browser.new_context()print(len(browser.contexts)) # prints `1``

**Returns**

*   [List](https://docs.python.org/3/library/typing.html#typing.List "List")[[BrowserContext](https://playwright.dev/python/docs/api/class-browsercontext "BrowserContext")][#](https://playwright.dev/python/docs/api/class-browser#browser-contexts-return)

* * *

### is_connected[​](https://playwright.dev/python/docs/api/class-browser#browser-is-connected "Direct link to is_connected")

Added before v1.9

browser.is_connected
Indicates that the browser is connected.

**Usage**

`browser.is_connected()`

**Returns**

*   [bool](https://docs.python.org/3/library/stdtypes.html "bool")[#](https://playwright.dev/python/docs/api/class-browser#browser-is-connected-return)

* * *

### version[​](https://playwright.dev/python/docs/api/class-browser#browser-version "Direct link to version")

Added before v1.9

browser.version
Returns the browser version.

**Usage**

`browser.version`

**Returns**

*   [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str "str")[#](https://playwright.dev/python/docs/api/class-browser#browser-version-return)

* * *

## Events[​](https://playwright.dev/python/docs/api/class-browser#events "Direct link to Events")

### on("disconnected")[​](https://playwright.dev/python/docs/api/class-browser#browser-event-disconnected "Direct link to on(\"disconnected\")")

Added before v1.9

browser.on("disconnected")
Emitted when Browser gets disconnected from the browser application. This might happen because of one of the following:

*   Browser application is closed or crashed.
*   The [browser.close()](https://playwright.dev/python/docs/api/class-browser#browser-close) method was called.

**Usage**

`browser.on("disconnected", handler)`

**Event data**

*   [Browser](https://playwright.dev/python/docs/api/class-browser "Browser")
