# Source: https://www.electronjs.org/docs/latest/api/web-contents-view

On this page

# WebContentsView

> A View that displays a WebContents.

Process: [Main](/docs/latest/glossary#main-process)

This module cannot be used until the `ready` event of the `app` module is emitted.

``` 
const  = require('electron')

const win = new BaseWindow()

const view1 = new WebContentsView()
win.contentView.addChildView(view1)
view1.webContents.loadURL('https://electronjs.org')
view1.setBounds()

const view2 = new WebContentsView()
win.contentView.addChildView(view2)
view2.webContents.loadURL('https://github.com/electron/electron')
view2.setBounds()
```

## Class: WebContentsView extends `View`[â€‹](#class-webcontentsview-extends-view "Direct link to class-webcontentsview-extends-view") 

> A View that displays a WebContents.

Process: [Main](/docs/latest/glossary#main-process)

`WebContentsView` inherits from [`View`](/docs/latest/api/view).

`WebContentsView` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### `new WebContentsView([options])`[â€‹](#new-webcontentsviewoptions "Direct link to new-webcontentsviewoptions") 

- `options` Object (optional)
  - `webPreferences` [WebPreferences](/docs/latest/api/structures/web-preferences) (optional) - Settings of web page\'s features.
  - `webContents` [WebContents](/docs/latest/api/web-contents) (optional) - If present, the given WebContents will be adopted by the WebContentsView. A WebContents may only be presented in one WebContentsView at a time.

Creates a WebContentsView.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

Objects created with `new WebContentsView` have the following properties, in addition to those inherited from [View](/docs/latest/api/view):

#### `view.webContents` *Readonly*[â€‹](#viewwebcontents-readonly "Direct link to viewwebcontents-readonly") 

A `WebContents` property containing a reference to the displayed `WebContents`. Use this to interact with the `WebContents`, for instance to load a URL.

``` 
const  = require('electron')

const view = new WebContentsView()
view.webContents.loadURL('https://electronjs.org/')
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/web-contents-view.md)