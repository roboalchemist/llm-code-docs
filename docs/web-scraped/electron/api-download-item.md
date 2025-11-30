# Source: https://www.electronjs.org/docs/latest/api/download-item

On this page

# Class: DownloadItem

## Class: DownloadItem[â€‹](#class-downloaditem "Direct link to Class: DownloadItem") 

> Control file downloads from remote sources.

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

`DownloadItem` is an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter) that represents a download item in Electron. It is used in `will-download` event of `Session` class, and allows users to control the download item.

``` 
// In the main process.
const  = require('electron')

const win = new BrowserWindow()
win.webContents.session.on('will-download', (event, item, webContents) =>  else if (state === 'progressing')  else `)
      }
    }
  })
  item.once('done', (event, state) =>  else `)
    }
  })
})
```

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

#### Event: \'updated\'[â€‹](#event-updated "Direct link to Event: 'updated'") 

Returns:

- `event` Event
- `state` string - Can be `progressing` or `interrupted`.

Emitted when the download has been updated and is not done.

The `state` can be one of following:

- `progressing` - The download is in-progress.
- `interrupted` - The download has interrupted and can be resumed.

#### Event: \'done\'[â€‹](#event-done "Direct link to Event: 'done'") 

Returns:

- `event` Event
- `state` string - Can be `completed`, `cancelled` or `interrupted`.

Emitted when the download is in a terminal state. This includes a completed download, a cancelled download (via `downloadItem.cancel()`), and interrupted download that can\'t be resumed.

The `state` can be one of following:

- `completed` - The download completed successfully.
- `cancelled` - The download has been cancelled.
- `interrupted` - The download has interrupted and can not resume.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

The `downloadItem` object has the following methods:

#### `downloadItem.setSavePath(path)`[â€‹](#downloaditemsetsavepathpath "Direct link to downloaditemsetsavepathpath") 

- `path` string - Set the save file path of the download item.

The API is only available in session\'s `will-download` callback function. If `path` doesn\'t exist, Electron will try to make the directory recursively. If user doesn\'t set the save path via the API, Electron will use the original routine to determine the save path; this usually prompts a save dialog.

#### `downloadItem.getSavePath()`[â€‹](#downloaditemgetsavepath "Direct link to downloaditemgetsavepath") 

Returns `string` - The save path of the download item. This will be either the path set via `downloadItem.setSavePath(path)` or the path selected from the shown save dialog.

#### `downloadItem.setSaveDialogOptions(options)`[â€‹](#downloaditemsetsavedialogoptionsoptions "Direct link to downloaditemsetsavedialogoptionsoptions") 

- `options` SaveDialogOptions - Set the save file dialog options. This object has the same properties as the `options` parameter of [`dialog.showSaveDialog()`](/docs/latest/api/dialog).

This API allows the user to set custom options for the save dialog that opens for the download item by default. The API is only available in session\'s `will-download` callback function.

#### `downloadItem.getSaveDialogOptions()`[â€‹](#downloaditemgetsavedialogoptions "Direct link to downloaditemgetsavedialogoptions") 

Returns `SaveDialogOptions` - Returns the object previously set by `downloadItem.setSaveDialogOptions(options)`.

#### `downloadItem.pause()`[â€‹](#downloaditempause "Direct link to downloaditempause") 

Pauses the download.

#### `downloadItem.isPaused()`[â€‹](#downloaditemispaused "Direct link to downloaditemispaused") 

Returns `boolean` - Whether the download is paused.

#### `downloadItem.resume()`[â€‹](#downloaditemresume "Direct link to downloaditemresume") 

Resumes the download that has been paused.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

To enable resumable downloads the server you are downloading from must support range requests and provide both `Last-Modified` and `ETag` header values. Otherwise `resume()` will dismiss previously received bytes and restart the download from the beginning.

#### `downloadItem.canResume()`[â€‹](#downloaditemcanresume "Direct link to downloaditemcanresume") 

Returns `boolean` - Whether the download can resume.

#### `downloadItem.cancel()`[â€‹](#downloaditemcancel "Direct link to downloaditemcancel") 

Cancels the download operation.

#### `downloadItem.getURL()`[â€‹](#downloaditemgeturl "Direct link to downloaditemgeturl") 

Returns `string` - The origin URL where the item is downloaded from.

#### `downloadItem.getMimeType()`[â€‹](#downloaditemgetmimetype "Direct link to downloaditemgetmimetype") 

Returns `string` - The files mime type.

#### `downloadItem.hasUserGesture()`[â€‹](#downloaditemhasusergesture "Direct link to downloaditemhasusergesture") 

Returns `boolean` - Whether the download has user gesture.

#### `downloadItem.getFilename()`[â€‹](#downloaditemgetfilename "Direct link to downloaditemgetfilename") 

Returns `string` - The file name of the download item.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The file name is not always the same as the actual one saved in local disk. If user changes the file name in a prompted download saving dialog, the actual name of saved file will be different.

#### `downloadItem.getCurrentBytesPerSecond()`[â€‹](#downloaditemgetcurrentbytespersecond "Direct link to downloaditemgetcurrentbytespersecond") 

Returns `Integer` - The current download speed in bytes per second.

#### `downloadItem.getTotalBytes()`[â€‹](#downloaditemgettotalbytes "Direct link to downloaditemgettotalbytes") 

Returns `Integer` - The total size in bytes of the download item.

If the size is unknown, it returns 0.

#### `downloadItem.getReceivedBytes()`[â€‹](#downloaditemgetreceivedbytes "Direct link to downloaditemgetreceivedbytes") 

Returns `Integer` - The received bytes of the download item.

#### `downloadItem.getPercentComplete()`[â€‹](#downloaditemgetpercentcomplete "Direct link to downloaditemgetpercentcomplete") 

Returns `Integer` - The download completion in percent.

#### `downloadItem.getContentDisposition()`[â€‹](#downloaditemgetcontentdisposition "Direct link to downloaditemgetcontentdisposition") 

Returns `string` - The Content-Disposition field from the response header.

#### `downloadItem.getState()`[â€‹](#downloaditemgetstate "Direct link to downloaditemgetstate") 

Returns `string` - The current state. Can be `progressing`, `completed`, `cancelled` or `interrupted`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

The following methods are useful specifically to resume a `cancelled` item when session is restarted.

#### `downloadItem.getURLChain()`[â€‹](#downloaditemgeturlchain "Direct link to downloaditemgeturlchain") 

Returns `string[]` - The complete URL chain of the item including any redirects.

#### `downloadItem.getLastModifiedTime()`[â€‹](#downloaditemgetlastmodifiedtime "Direct link to downloaditemgetlastmodifiedtime") 

Returns `string` - Last-Modified header value.

#### `downloadItem.getETag()`[â€‹](#downloaditemgetetag "Direct link to downloaditemgetetag") 

Returns `string` - ETag header value.

#### `downloadItem.getStartTime()`[â€‹](#downloaditemgetstarttime "Direct link to downloaditemgetstarttime") 

Returns `Double` - Number of seconds since the UNIX epoch when the download was started.

#### `downloadItem.getEndTime()`[â€‹](#downloaditemgetendtime "Direct link to downloaditemgetendtime") 

Returns `Double` - Number of seconds since the UNIX epoch when the download ended.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

#### `downloadItem.savePath`[â€‹](#downloaditemsavepath "Direct link to downloaditemsavepath") 

A `string` property that determines the save file path of the download item.

The property is only available in session\'s `will-download` callback function. If user doesn\'t set the save path via the property, Electron will use the original routine to determine the save path; this usually prompts a save dialog.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/download-item.md)