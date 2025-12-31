# Source: https://playwright.dev/docs/api/class-download

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Download]

On this page

<div>

# Download

</div>

[Download](/docs/api/class-download "Download") objects are dispatched by page via the [page.on(\'download\')](/docs/api/class-page#page-event-download) event.

All the downloaded files belonging to the browser context are deleted when the browser context is closed.

Download event is emitted once the download starts. Download path becomes available once download completes.

``` 
// Start waiting for download before clicking. Note no await.
const downloadPromise = page.waitForEvent('download');
await page.getByText('Download file').click();
const download = await downloadPromise;

// Wait for the download process to complete and save the downloaded file somewhere.
await download.saveAs('/path/to/save/at/' + download.suggestedFilename());
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### cancel[​](#download-cancel "Direct link to cancel") 

Added in: v1.13 download.cancel

Cancels a download. Will not fail if the download is already finished or canceled. Upon successful cancellations, `download.failure()` would resolve to `'canceled'`.

**Usage**

``` 
await download.cancel();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#download-cancel-return)

------------------------------------------------------------------------

### createReadStream[​](#download-create-read-stream "Direct link to createReadStream") 

Added before v1.9 download.createReadStream

Returns a readable stream for a successful download, or throws for a failed/canceled download.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

If you don\'t need a readable stream, it\'s usually simpler to read the file from disk after the download completed. See [download.path()](/docs/api/class-download#download-path).

**Usage**

``` 
await download.createReadStream();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[Readable](https://nodejs.org/api/stream.html#stream_class_stream_readable "Readable")\>[][\#](#download-create-read-stream-return)

------------------------------------------------------------------------

### delete[​](#download-delete "Direct link to delete") 

Added before v1.9 download.delete

Deletes the downloaded file. Will wait for the download to finish if necessary.

**Usage**

``` 
await download.delete();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#download-delete-return)

------------------------------------------------------------------------

### failure[​](#download-failure "Direct link to failure") 

Added before v1.9 download.failure

Returns download error if any. Will wait for the download to finish if necessary.

**Usage**

``` 
await download.failure();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") \| [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\>[][\#](#download-failure-return)

------------------------------------------------------------------------

### page[​](#download-page "Direct link to page") 

Added in: v1.12 download.page

Get the page that the download belongs to.

**Usage**

``` 
download.page();
```

**Returns**

-   [Page](/docs/api/class-page "Page")[][\#](#download-page-return)

------------------------------------------------------------------------

### path[​](#download-path "Direct link to path") 

Added before v1.9 download.path

Returns path to the downloaded file for a successful download, or throws for a failed/canceled download. The method will wait for the download to finish if necessary. The method throws when connected remotely.

Note that the download\'s file name is a random GUID, use [download.suggestedFilename()](/docs/api/class-download#download-suggested-filename) to get suggested file name.

**Usage**

``` 
await download.path();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\>[][\#](#download-path-return)

------------------------------------------------------------------------

### saveAs[​](#download-save-as "Direct link to saveAs") 

Added before v1.9 download.saveAs

Copy the download to a user-specified path. It is safe to call this method while the download is still in progress. Will wait for the download to finish if necessary.

**Usage**

``` 
await download.saveAs('/path/to/save/at/' + download.suggestedFilename());
```

**Arguments**

-   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#download-save-as-option-path)

    Path where the download should be copied.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#download-save-as-return)

------------------------------------------------------------------------

### suggestedFilename[​](#download-suggested-filename "Direct link to suggestedFilename") 

Added before v1.9 download.suggestedFilename

Returns suggested filename for this download. It is typically computed by the browser from the [`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) response header or the `download` attribute. See the spec on [whatwg](https://html.spec.whatwg.org/#downloading-resources). Different browsers can use different logic for computing it.

**Usage**

``` 
download.suggestedFilename();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#download-suggested-filename-return)

------------------------------------------------------------------------

### url[​](#download-url "Direct link to url") 

Added before v1.9 download.url

Returns downloaded url.

**Usage**

``` 
download.url();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#download-url-return)