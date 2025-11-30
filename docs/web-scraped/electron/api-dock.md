# Source: https://www.electronjs.org/docs/latest/api/dock

On this page

# Class: Dock

## Class: Dock[â€‹](#class-dock "Direct link to Class: Dock") 

> Control your app in the macOS dock

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

See also: [A detailed guide about how to implement Dock menus](/docs/latest/tutorial/macos-dock).

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

#### `dock.bounce([type])` *macOS*[â€‹](#dockbouncetype-macos "Direct link to dockbouncetype-macos") 

- `type` string (optional) - Can be `critical` or `informational`. The default is `informational`

Returns `Integer` - an ID representing the request.

When `critical` is passed, the dock icon will bounce until either the application becomes active or the request is canceled.

When `informational` is passed, the dock icon will bounce for one second. However, the request remains active until either the application becomes active or the request is canceled.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This method can only be used while the app is not focused; when the app is focused it will return -1.

#### `dock.cancelBounce(id)` *macOS*[â€‹](#dockcancelbounceid-macos "Direct link to dockcancelbounceid-macos") 

- `id` Integer

Cancel the bounce of `id`.

#### `dock.downloadFinished(filePath)` *macOS*[â€‹](#dockdownloadfinishedfilepath-macos "Direct link to dockdownloadfinishedfilepath-macos") 

- `filePath` string

Bounces the Downloads stack if the filePath is inside the Downloads folder.

#### `dock.setBadge(text)` *macOS*[â€‹](#docksetbadgetext-macos "Direct link to docksetbadgetext-macos") 

- `text` string

Sets the string to be displayed in the dockâ€™s badging area.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

You need to ensure that your application has the permission to display notifications for this method to work.

#### `dock.getBadge()` *macOS*[â€‹](#dockgetbadge-macos "Direct link to dockgetbadge-macos") 

Returns `string` - The badge string of the dock.

#### `dock.hide()` *macOS*[â€‹](#dockhide-macos "Direct link to dockhide-macos") 

Hides the dock icon.

#### `dock.show()` *macOS*[â€‹](#dockshow-macos "Direct link to dockshow-macos") 

Returns `Promise<void>` - Resolves when the dock icon is shown.

#### `dock.isVisible()` *macOS*[â€‹](#dockisvisible-macos "Direct link to dockisvisible-macos") 

Returns `boolean` - Whether the dock icon is visible.

#### `dock.setMenu(menu)` *macOS*[â€‹](#docksetmenumenu-macos "Direct link to docksetmenumenu-macos") 

- `menu` [Menu](/docs/latest/api/menu)

Sets the application\'s [dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus).

#### `dock.getMenu()` *macOS*[â€‹](#dockgetmenu-macos "Direct link to dockgetmenu-macos") 

Returns `Menu | null` - The application\'s [dock menu](https://developer.apple.com/design/human-interface-guidelines/dock-menus).

#### `dock.setIcon(image)` *macOS*[â€‹](#dockseticonimage-macos "Direct link to dockseticonimage-macos") 

- `image` ([NativeImage](/docs/latest/api/native-image) \| string)

Sets the `image` associated with this dock icon.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/dock.md)