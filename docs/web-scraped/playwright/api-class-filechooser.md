# Source: https://playwright.dev/docs/api/class-filechooser

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [FileChooser]

On this page

<div>

# FileChooser

</div>

[FileChooser](/docs/api/class-filechooser "FileChooser") objects are dispatched by the page in the [page.on(\'filechooser\')](/docs/api/class-page#page-event-file-chooser) event.

``` 
// Start waiting for file chooser before clicking. Note no await.
const fileChooserPromise = page.waitForEvent('filechooser');
await page.getByText('Upload file').click();
const fileChooser = await fileChooserPromise;
await fileChooser.setFiles(path.join(__dirname, 'myfile.pdf'));
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### element[​](#file-chooser-element "Direct link to element") 

Added before v1.9 fileChooser.element

Returns input element associated with this file chooser.

**Usage**

``` 
fileChooser.element();
```

**Returns**

-   [ElementHandle](/docs/api/class-elementhandle "ElementHandle")[][\#](#file-chooser-element-return)

------------------------------------------------------------------------

### isMultiple[​](#file-chooser-is-multiple "Direct link to isMultiple") 

Added before v1.9 fileChooser.isMultiple

Returns whether this file chooser accepts multiple files.

**Usage**

``` 
fileChooser.isMultiple();
```

**Returns**

-   [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean")[][\#](#file-chooser-is-multiple-return)

------------------------------------------------------------------------

### page[​](#file-chooser-page "Direct link to page") 

Added before v1.9 fileChooser.page

Returns page this file chooser belongs to.

**Usage**

``` 
fileChooser.page();
```

**Returns**

-   [Page](/docs/api/class-page "Page")[][\#](#file-chooser-page-return)

------------------------------------------------------------------------

### setFiles[​](#file-chooser-set-files "Direct link to setFiles") 

Added before v1.9 fileChooser.setFiles

Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths, then they are resolved relative to the current working directory. For empty array, clears the selected files.

**Usage**

``` 
await fileChooser.setFiles(files);
await fileChooser.setFiles(files, options);
```

**Arguments**

-   `files` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") \| [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\> \| [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") \| [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")\>[][\#](#file-chooser-set-files-option-files)
    -   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        File name

    -   `mimeType` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        File type

    -   `buffer` [Buffer](https://nodejs.org/api/buffer.html#buffer_class_buffer "Buffer")

        File content
-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `noWaitAfter` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*[][\#](#file-chooser-set-files-option-no-wait-after)

        ::: 
        ::: admonitionHeading_Gvgb
        [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Deprecated
        :::

        ::: admonitionContent_BuS1
        This option has no effect.
        :::
        :::

        This option has no effect.

    -   `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#file-chooser-set-files-option-timeout)

        Maximum time in milliseconds. Defaults to `0` - no timeout. The default value can be changed via `actionTimeout` option in the config, or by using the [browserContext.setDefaultTimeout()](/docs/api/class-browsercontext#browser-context-set-default-timeout) or [page.setDefaultTimeout()](/docs/api/class-page#page-set-default-timeout) methods.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#file-chooser-set-files-return)