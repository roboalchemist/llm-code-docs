# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/BrowserHelper.md

# [BrowserHelper](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper)

Static helper class that does browser or platform detection and provides other helper functions.

## Properties

Properties are getters/setters or publicly accessible variables on this class

[isPhone](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isPhone)
Yields `true` if the platform running is a phone (screen width or height <= 414 CSS pixels)

[supportsOverflowClip](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-supportsOverflowClip-static)
Yields `true` if the current browser supports CSS style `overflow:clip`.

[supportsSticky](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-supportsSticky-static)
Yields `true` if the current browser supports CSS style `position:sticky`.

[isTouchDevice](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isTouchDevice-static)
Determines if the user is using a touch device.

[isMac](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isMac-static)
Checks if platform is Mac.

[isWindows](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isWindows-static)
Checks if platform is Windows.

[isLinux](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isLinux-static)
Checks if platform is Linux.

[isAndroid](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isAndroid-static)
Checks if platform is Android.

[isWebkit](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isWebkit-static)
Checks if browser is Webkit.

[isChrome](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isChrome-static)
Checks if browser is Chrome or Chromium based browser. Returns truthy value for Edge Chromium.

[chromeVersion](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-chromeVersion-static)
Returns the major Chrome version or 0 for other browsers.

[isFirefox](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isFirefox-static)
Checks if browser is Firefox.

[firefoxVersion](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-firefoxVersion-static)
Returns the major Firefox version or 0 for other browsers.

[isSafari](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isSafari-static)
Checks if browser is Safari.

[isMobileSafari](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isMobileSafari-static)
Checks if browser is mobile Safari

[isMobile](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isMobile-static)
Checks if the active device is a mobile device

[ctrlKey](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-ctrlKey-static)
Returns the event property name for the `ctrlKey`. The `ctrlKey` key is `'ctrlKey'` on all platforms except Mac, where `ctrlKey` is `'metaKey'`.

See also [metaKey](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper#property-metaKey-static).

[metaKey](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-metaKey-static)
Returns the event property name for the `metaKey`. The `metaKey` is `'metaKey'` on all platforms except Mac, where `metaKey` is `'ctrlKey'`.

See also [ctrlKey](https://bryntum.com/docs/gantt/api/#Core/helper/BrowserHelper#property-ctrlKey-static).

[isCSP](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#property-isCSP-static)
Returns truthy value if page contains Content Security Policy meta tag or globalThis.bryntum.CSP is truthy value

## Functions

Functions are methods available for calling on the class

[getVersion](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#function-getVersion-static)
Returns matched version for userAgent.

[searchParam](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#function-searchParam-static)
Returns parameter value from search string by parameter name.

[getCookie](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#function-getCookie-static)
Returns cookie by name.

[download](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#function-download-static)
Triggers a download of a file with the specified name / URL.

[downloadBlob](https://bryntum.com/docs/gantt/api/Core/helper/BrowserHelper#function-downloadBlob-static)
Triggers a download of a Blob with the specified name.
