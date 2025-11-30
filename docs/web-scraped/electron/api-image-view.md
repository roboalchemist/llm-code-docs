# Source: https://www.electronjs.org/docs/latest/api/image-view

On this page

# ImageView

> A View that displays an image.

Process: [Main](/docs/latest/glossary#main-process)

This module cannot be used until the `ready` event of the `app` module is emitted.

Useful for showing splash screens that will be swapped for `WebContentsView`s when the content finishes loading.

Note that `ImageView` is experimental and may be changed or removed in the future.

``` 
const  = require('electron')

const path = require('node:path')

const win = new BaseWindow()

// Create a "splash screen" image to display while the WebContentsView loads
const splashView = new ImageView()
const splashImage = nativeImage.createFromPath(path.join(__dirname, 'loading.png'))
splashView.setImage(splashImage)
win.setContentView(splashView)

const webContentsView = new WebContentsView()
webContentsView.webContents.once('did-finish-load', () => )
webContentsView.webContents.loadURL('https://electronjs.org')
```

## Class: ImageView extends `View`[â€‹](#class-imageview-extends-view "Direct link to class-imageview-extends-view") 

> A View that displays an image.

Process: [Main](/docs/latest/glossary#main-process)

`ImageView` inherits from [`View`](/docs/latest/api/view).

`ImageView` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]warning

Electron\'s built-in classes cannot be subclassed in user code. For more information, see [the FAQ](/docs/latest/faq#class-inheritance-does-not-work-with-electron-built-in-modules).

### `new ImageView()` *Experimental*[â€‹](#new-imageview-experimental "Direct link to new-imageview-experimental") 

Creates an ImageView.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

The following methods are available on instances of the `ImageView` class, in addition to those inherited from [View](/docs/latest/api/view):

#### `image.setImage(image)` *Experimental*[â€‹](#imagesetimageimage-experimental "Direct link to imagesetimageimage-experimental") 

- `image` NativeImage

Sets the image for this `ImageView`. Note that only image formats supported by `NativeImage` can be used with an `ImageView`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/image-view.md)