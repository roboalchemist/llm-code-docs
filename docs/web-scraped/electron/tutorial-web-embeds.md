# Source: https://www.electronjs.org/docs/latest/tutorial/web-embeds

On this page

# Web Embeds

## Overview[â€‹](#overview "Direct link to Overview") 

If you want to embed (third-party) web content in an Electron `BrowserWindow`, there are three options available to you: `<iframe>` tags, `<webview>` tags, and `WebContentsView`. Each one offers slightly different functionality and is useful in different situations. To help you choose between these, this guide explains the differences and capabilities of each option.

### Iframes[â€‹](#iframes "Direct link to Iframes") 

Iframes in Electron behave like iframes in regular browsers. An `<iframe>` element in your page can show external web pages, provided that their [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) allows it. To limit the number of capabilities of a site in an `<iframe>` tag, it is recommended to use the [`sandbox` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-sandbox) and only allow the capabilities you want to support.

### WebViews[â€‹](#webviews "Direct link to WebViews") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

[We do not recommend you to use WebViews](/docs/latest/api/webview-tag#warning), as this tag undergoes dramatic architectural changes that may affect stability of your application. Consider switching to alternatives, like `iframe` and Electron\'s [`WebContentsView`](/docs/latest/api/web-contents-view), or an architecture that avoids embedded content by design.

[WebViews](/docs/latest/api/webview-tag) are based on Chromium\'s WebViews and are not explicitly supported by Electron. We do not guarantee that the WebView API will remain available in future versions of Electron. To use `<webview>` tags, you will need to set `webviewTag` to `true` in the `webPreferences` of your `BrowserWindow`.

WebView is a custom element (`<webview>`) that will only work inside Electron. They are implemented as an \"out-of-process iframe\". This means that all communication with the `<webview>` is done asynchronously using IPC. The `<webview>` element has many custom methods and events, similar to `webContents`, that provide you with greater control over the content.

Compared to an `<iframe>`, `<webview>` tends to be slightly slower but offers much greater control in loading and communicating with the third-party content and handling various events.

### WebContentsView[â€‹](#webcontentsview "Direct link to WebContentsView") 

[`WebContentsView`](/docs/latest/api/web-contents-view)s are not a part of the DOMâ€"instead, they are created, controlled, positioned, and sized by your Main process. Using `WebContentsView`, you can combine and layer many pages together in the same [`BaseWindow`](/docs/latest/api/base-window).

`WebContentsView`s offer the greatest control over their contents, since they implement the `webContents` similarly to how `BrowserWindow` does it. However, as `WebContentsView`s are not elements inside the DOM, positioning them accurately with respect to DOM content requires coordination between the Main and Renderer processes.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/tutorial/web-embeds.md)