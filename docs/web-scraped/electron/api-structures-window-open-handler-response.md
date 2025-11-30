# Source: https://www.electronjs.org/docs/latest/api/structures/window-open-handler-response

# WindowOpenHandlerResponse Object

- `action` string - Can be `allow` or `deny`. Controls whether new window should be created.
- `overrideBrowserWindowOptions` BrowserWindowConstructorOptions (optional) - Allows customization of the created window.
- `outlivesOpener` boolean (optional) - By default, child windows are closed when their opener is closed. This can be changed by specifying `outlivesOpener: true`, in which case the opened window will not be closed when its opener is closed.
- `createWindow` (options: BrowserWindowConstructorOptions) =\> WebContents (optional) - If specified, will be called instead of `new BrowserWindow` to create the new child window and event [`did-create-window`](/docs/latest/api/web-contents#event-did-create-window) will not be emitted. Constructed child window should use passed `options` object. This can be used for example to have the new window open as a BrowserView instead of in a separate window.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/window-open-handler-response.md)