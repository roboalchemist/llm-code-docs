# Source: https://www.electronjs.org/docs/latest/api/clipboard

On this page

# clipboard

> Perform copy and paste operations on the system clipboard.

Process: [Main](/docs/latest/glossary#main-process), [Renderer](/docs/latest/glossary#renderer-process) (non-sandboxed only)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

If you want to call this API from a renderer process with context isolation enabled, place the API call in your preload script and [expose](/docs/latest/tutorial/context-isolation#after-context-isolation-enabled) it using the [`contextBridge`](/docs/latest/api/context-bridge) API.

On Linux, there is also a `selection` clipboard. To manipulate it you need to pass `selection` to each method:

``` 
const  = require('electron')

clipboard.writeText('Example string', 'selection')
console.log(clipboard.readText('selection'))
```

## Methods[â€‹](#methods "Direct link to Methods") 

The `clipboard` module has the following methods:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Experimental APIs are marked as such and could be removed in future.

### `clipboard.readText([type])`[â€‹](#clipboardreadtexttype "Direct link to clipboardreadtexttype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns `string` - The content in the clipboard as plain text.

``` 
const  = require('electron')

clipboard.writeText('hello i am a bit of text!')

const text = clipboard.readText()
console.log(text)
// hello i am a bit of text!'
```

### `clipboard.writeText(text[, type])`[â€‹](#clipboardwritetexttext-type "Direct link to clipboardwritetexttext-type") 

- `text` string
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes the `text` into the clipboard as plain text.

``` 
const  = require('electron')

const text = 'hello i am a bit of text!'
clipboard.writeText(text)
```

### `clipboard.readHTML([type])`[â€‹](#clipboardreadhtmltype "Direct link to clipboardreadhtmltype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns `string` - The content in the clipboard as markup.

``` 
const  = require('electron')

clipboard.writeHTML('<b>Hi</b>')
const html = clipboard.readHTML()

console.log(html)
// <meta charset='utf-8'><b>Hi</b>
```

### `clipboard.writeHTML(markup[, type])`[â€‹](#clipboardwritehtmlmarkup-type "Direct link to clipboardwritehtmlmarkup-type") 

- `markup` string
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes `markup` to the clipboard.

``` 
const  = require('electron')

clipboard.writeHTML('<b>Hi</b>')
```

### `clipboard.readImage([type])`[â€‹](#clipboardreadimagetype "Direct link to clipboardreadimagetype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns [`NativeImage`](/docs/latest/api/native-image) - The image content in the clipboard.

### `clipboard.writeImage(image[, type])`[â€‹](#clipboardwriteimageimage-type "Direct link to clipboardwriteimageimage-type") 

- `image` [NativeImage](/docs/latest/api/native-image)
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes `image` to the clipboard.

### `clipboard.readRTF([type])`[â€‹](#clipboardreadrtftype "Direct link to clipboardreadrtftype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns `string` - The content in the clipboard as RTF.

``` 
const  = require('electron')

clipboard.writeRTF('\\f0\\pard\nThis is some  text.\\par\n}')

const rtf = clipboard.readRTF()
console.log(rtf)
// \\f0\\pard\nThis is some  text.\\par\n}
```

### `clipboard.writeRTF(text[, type])`[â€‹](#clipboardwritertftext-type "Direct link to clipboardwritertftext-type") 

- `text` string
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes the `text` into the clipboard in RTF.

``` 
const  = require('electron')

const rtf = '\\f0\\pard\nThis is some  text.\\par\n}'
clipboard.writeRTF(rtf)
```

### `clipboard.readBookmark()` *macOS* *Windows*[â€‹](#clipboardreadbookmark-macos-windows "Direct link to clipboardreadbookmark-macos-windows") 

Returns `Object`:

- `title` string
- `url` string

Returns an Object containing `title` and `url` keys representing the bookmark in the clipboard. The `title` and `url` values will be empty strings when the bookmark is unavailable. The `title` value will always be empty on Windows.

### `clipboard.writeBookmark(title, url[, type])` *macOS* *Windows*[â€‹](#clipboardwritebookmarktitle-url-type-macos-windows "Direct link to clipboardwritebookmarktitle-url-type-macos-windows") 

- `title` string - Unused on Windows
- `url` string
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes the `title` (macOS only) and `url` into the clipboard as a bookmark.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Most apps on Windows don\'t support pasting bookmarks into them so you can use `clipboard.write` to write both a bookmark and fallback text to the clipboard.

``` 
const  = require('electron')

clipboard.writeBookmark('Electron Homepage', 'https://electronjs.org')
```

### `clipboard.readFindText()` *macOS*[â€‹](#clipboardreadfindtext-macos "Direct link to clipboardreadfindtext-macos") 

Returns `string` - The text on the find pasteboard, which is the pasteboard that holds information about the current state of the active applicationâ€™s find panel.

This method uses synchronous IPC when called from the renderer process. The cached value is reread from the find pasteboard whenever the application is activated.

### `clipboard.writeFindText(text)` *macOS*[â€‹](#clipboardwritefindtexttext-macos "Direct link to clipboardwritefindtexttext-macos") 

- `text` string

Writes the `text` into the find pasteboard (the pasteboard that holds information about the current state of the active applicationâ€™s find panel) as plain text. This method uses synchronous IPC when called from the renderer process.

### `clipboard.clear([type])`[â€‹](#clipboardcleartype "Direct link to clipboardcleartype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Clears the clipboard content.

### `clipboard.availableFormats([type])`[â€‹](#clipboardavailableformatstype "Direct link to clipboardavailableformatstype") 

- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns `string[]` - An array of supported formats for the clipboard `type`.

``` 
const  = require('electron')

const formats = clipboard.availableFormats()
console.log(formats)
// [ 'text/plain', 'text/html' ]
```

### `clipboard.has(format[, type])` *Experimental*[â€‹](#clipboardhasformat-type-experimental "Direct link to clipboardhasformat-type-experimental") 

- `format` string
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Returns `boolean` - Whether the clipboard supports the specified `format`.

``` 
const  = require('electron')

const hasFormat = clipboard.has('public/utf8-plain-text')
console.log(hasFormat)
// 'true' or 'false'
```

### `clipboard.read(format)` *Experimental*[â€‹](#clipboardreadformat-experimental "Direct link to clipboardreadformat-experimental") 

- `format` string

Returns `string` - Reads `format` type from the clipboard.

`format` should contain valid ASCII characters and have `/` separator. `a/c`, `a/bc` are valid formats while `/abc`, `abc/`, `a/`, `/a`, `a` are not valid.

### `clipboard.readBuffer(format)` *Experimental*[â€‹](#clipboardreadbufferformat-experimental "Direct link to clipboardreadbufferformat-experimental") 

- `format` string

Returns `Buffer` - Reads `format` type from the clipboard.

``` 
const  = require('electron')

const buffer = Buffer.from('this is binary', 'utf8')
clipboard.writeBuffer('public/utf8-plain-text', buffer)

const ret = clipboard.readBuffer('public/utf8-plain-text')

console.log(buffer.equals(ret))
// true
```

### `clipboard.writeBuffer(format, buffer[, type])` *Experimental*[â€‹](#clipboardwritebufferformat-buffer-type-experimental "Direct link to clipboardwritebufferformat-buffer-type-experimental") 

- `format` string
- `buffer` Buffer
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes the `buffer` into the clipboard as `format`.

``` 
const  = require('electron')

const buffer = Buffer.from('writeBuffer', 'utf8')
clipboard.writeBuffer('public/utf8-plain-text', buffer)
```

### `clipboard.write(data[, type])`[â€‹](#clipboardwritedata-type "Direct link to clipboardwritedata-type") 

- `data` Object
  - `text` string (optional)
  - `html` string (optional)
  - `image` [NativeImage](/docs/latest/api/native-image) (optional)
  - `rtf` string (optional)
  - `bookmark` string (optional) - The title of the URL at `text`.
- `type` string (optional) - Can be `selection` or `clipboard`; default is \'clipboard\'. `selection` is only available on Linux.

Writes `data` to the clipboard.

``` 
const  = require('electron')

clipboard.write(',
  bookmark: 'a title'
})

console.log(clipboard.readText())
// 'test'

console.log(clipboard.readHTML())
// <meta charset='utf-8'><b>Hi</b>

console.log(clipboard.readRTF())
// ''

console.log(clipboard.readBookmark())
// 
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/clipboard.md)