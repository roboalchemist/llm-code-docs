# Source: https://www.electronjs.org/docs/latest/api/web-utils

On this page

# webUtils

> A utility layer to interact with Web API objects (Files, Blobs, etc.)

Process: [Renderer](/docs/latest/glossary#renderer-process)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

If you want to call this API from a renderer process with context isolation enabled, place the API call in your preload script and [expose](/docs/latest/tutorial/context-isolation#after-context-isolation-enabled) it using the [`contextBridge`](/docs/latest/api/context-bridge) API.

## Methods[â€‹](#methods "Direct link to Methods") 

The `webUtils` module has the following methods:

### `webUtils.getPathForFile(file)`[â€‹](#webutilsgetpathforfilefile "Direct link to webutilsgetpathforfilefile") 

- `file` File - A web [File](https://developer.mozilla.org/en-US/docs/Web/API/File) object.

Returns `string` - The file system path that this `File` object points to. In the case where the object passed in is not a `File` object an exception is thrown. In the case where the File object passed in was constructed in JS and is not backed by a file on disk an empty string is returned.

This method superseded the previous augmentation to the `File` object with the `path` property. An example is included below.

``` 
// Before (renderer)
const oldPath = document.querySelector('input[type=file]').files[0].path
```

``` 
// After

// Renderer:

const file = document.querySelector('input[type=file]').files[0]
electronApi.doSomethingWithFile(file)

// Preload script:

const  = require('electron')

contextBridge.exposeInMainWorld('electronApi', 
})
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/web-utils.md)