# Source: https://www.electronjs.org/docs/latest/api/share-menu

On this page

# ShareMenu

The `ShareMenu` class creates [Share Menu](https://developer.apple.com/design/human-interface-guidelines/macos/extensions/share-extensions/) on macOS, which can be used to share information from the current context to apps, social media accounts, and other services.

For including the share menu as a submenu of other menus, please use the `shareMenu` role of [`MenuItem`](/docs/latest/api/menu-item).

## Class: ShareMenu[â€‹](#class-sharemenu "Direct link to Class: ShareMenu") 

> Create share menu on macOS.

Process: [Main](/docs/latest/glossary#main-process)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### `new ShareMenu(sharingItem)`[â€‹](#new-sharemenusharingitem "Direct link to new-sharemenusharingitem") 

- `sharingItem` SharingItem - The item to share.

Creates a new share menu.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

The `shareMenu` object has the following instance methods:

#### `shareMenu.popup([options])`[â€‹](#sharemenupopupoptions "Direct link to sharemenupopupoptions") 

- `options` PopupOptions (optional)
  - `browserWindow` [BrowserWindow](/docs/latest/api/browser-window) (optional) - Default is the focused window.
  - `x` number (optional) - Default is the current mouse cursor position. Must be declared if `y` is declared.
  - `y` number (optional) - Default is the current mouse cursor position. Must be declared if `x` is declared.
  - `positioningItem` number (optional) *macOS* - The index of the menu item to be positioned under the mouse cursor at the specified coordinates. Default is -1.
  - `callback` Function (optional) - Called when menu is closed.

Pops up this menu as a context menu in the [`BrowserWindow`](/docs/latest/api/browser-window).

#### `shareMenu.closePopup([browserWindow])`[â€‹](#sharemenuclosepopupbrowserwindow "Direct link to sharemenuclosepopupbrowserwindow") 

- `browserWindow` [BrowserWindow](/docs/latest/api/browser-window) (optional) - Default is the focused window.

Closes the context menu in the `browserWindow`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/share-menu.md)