# Source: https://playwright.dev/docs/api/class-video

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Video]

On this page

<div>

# Video

</div>

When browser context is created with the `recordVideo` option, each page has a video object associated with it.

``` 
console.log(await page.video().path());
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### delete[​](#video-delete "Direct link to delete") 

Added in: v1.11 video.delete

Deletes the video file. Will wait for the video to finish if necessary.

**Usage**

``` 
await video.delete();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#video-delete-return)

------------------------------------------------------------------------

### path[​](#video-path "Direct link to path") 

Added before v1.9 video.path

Returns the file system path this video will be recorded to. The video is guaranteed to be written to the filesystem upon closing the browser context. This method throws when connected remotely.

**Usage**

``` 
await video.path();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\>[][\#](#video-path-return)

------------------------------------------------------------------------

### saveAs[​](#video-save-as "Direct link to saveAs") 

Added in: v1.11 video.saveAs

Saves the video to a user-specified path. It is safe to call this method while the video is still in progress, or after the page has closed. This method waits until the page is closed and the video is fully saved.

**Usage**

``` 
await video.saveAs(path);
```

**Arguments**

-   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#video-save-as-option-path)

    Path where the video should be saved.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#video-save-as-return)