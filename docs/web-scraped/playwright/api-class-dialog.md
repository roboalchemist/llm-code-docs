# Source: https://playwright.dev/docs/api/class-dialog

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Dialog]

On this page

<div>

# Dialog

</div>

[Dialog](/docs/api/class-dialog "Dialog") objects are dispatched by page via the [page.on(\'dialog\')](/docs/api/class-page#page-event-dialog) event.

An example of using `Dialog` class:

``` 
const  = require('playwright');  // Or 'firefox' or 'webkit'.

(async () => );
  await page.evaluate(() => alert('1'));
  await browser.close();
})();
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Dialogs are dismissed automatically, unless there is a [page.on(\'dialog\')](/docs/api/class-page#page-event-dialog) listener. When listener is present, it **must** either [dialog.accept()](/docs/api/class-dialog#dialog-accept) or [dialog.dismiss()](/docs/api/class-dialog#dialog-dismiss) the dialog - otherwise the page will [freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop#never_blocking) waiting for the dialog, and actions like click will never finish.

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### accept[​](#dialog-accept "Direct link to accept") 

Added before v1.9 dialog.accept

Returns when the dialog has been accepted.

**Usage**

``` 
await dialog.accept();
await dialog.accept(promptText);
```

**Arguments**

-   `promptText` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#dialog-accept-option-prompt-text)

    A text to enter in prompt. Does not cause any effects if the dialog\'s `type` is not prompt. Optional.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#dialog-accept-return)

------------------------------------------------------------------------

### defaultValue[​](#dialog-default-value "Direct link to defaultValue") 

Added before v1.9 dialog.defaultValue

If dialog is prompt, returns default prompt value. Otherwise, returns empty string.

**Usage**

``` 
dialog.defaultValue();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#dialog-default-value-return)

------------------------------------------------------------------------

### dismiss[​](#dialog-dismiss "Direct link to dismiss") 

Added before v1.9 dialog.dismiss

Returns when the dialog has been dismissed.

**Usage**

``` 
await dialog.dismiss();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#dialog-dismiss-return)

------------------------------------------------------------------------

### message[​](#dialog-message "Direct link to message") 

Added before v1.9 dialog.message

A message displayed in the dialog.

**Usage**

``` 
dialog.message();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#dialog-message-return)

------------------------------------------------------------------------

### page[​](#dialog-page "Direct link to page") 

Added in: v1.34 dialog.page

The page that initiated this dialog, if available.

**Usage**

``` 
dialog.page();
```

**Returns**

-   [null](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null "null") \| [Page](/docs/api/class-page "Page")[][\#](#dialog-page-return)

------------------------------------------------------------------------

### type[​](#dialog-type "Direct link to type") 

Added before v1.9 dialog.type

Returns dialog\'s type, can be one of `alert`, `beforeunload`, `confirm` or `prompt`.

**Usage**

``` 
dialog.type();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#dialog-type-return)