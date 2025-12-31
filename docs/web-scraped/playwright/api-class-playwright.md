# Source: https://playwright.dev/docs/api/class-playwright

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Playwright Library]

On this page

<div>

# Playwright Library

</div>

Playwright module provides a method to launch a browser instance. The following is a typical example of using Playwright to drive automation:

``` 
const  = require('playwright');

(async () => )();
```

------------------------------------------------------------------------

## Properties[​](#properties "Direct link to Properties") 

### chromium[​](#playwright-chromium "Direct link to chromium") 

Added before v1.9 playwright.chromium

This object can be used to launch or connect to Chromium, returning instances of [Browser](/docs/api/class-browser "Browser").

**Usage**

``` 
playwright.chromium
```

**Type**

-   [BrowserType](/docs/api/class-browsertype "BrowserType")

------------------------------------------------------------------------

### devices[​](#playwright-devices "Direct link to devices") 

Added before v1.9 playwright.devices

Returns a dictionary of devices to be used with [browser.newContext()](/docs/api/class-browser#browser-new-context) or [browser.newPage()](/docs/api/class-browser#browser-new-page).

``` 
const  = require('playwright');
const iPhone = devices['iPhone 6'];

(async () => );
  const page = await context.newPage();
  await page.goto('http://example.com');
  // other actions...
  await browser.close();
})();
```

**Usage**

``` 
playwright.devices
```

**Type**

-   [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")

------------------------------------------------------------------------

### errors[​](#playwright-errors "Direct link to errors") 

Added before v1.9 playwright.errors

Playwright methods might throw errors if they are unable to fulfill a request. For example, [locator.waitFor()](/docs/api/class-locator#locator-wait-for) might fail if the selector doesn\'t match any nodes during the given timeframe.

For certain types of errors Playwright uses specific error classes. These classes are available via [`playwright.errors`](#playwright-errors).

An example of handling a timeout error:

``` 
try  catch (e) 
}
```

**Usage**

``` 
playwright.errors
```

**Type**

-   [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")
    -   `TimeoutError` [function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function "Function")

        A class of [TimeoutError](/docs/api/class-timeouterror "TimeoutError").

------------------------------------------------------------------------

### firefox[​](#playwright-firefox "Direct link to firefox") 

Added before v1.9 playwright.firefox

This object can be used to launch or connect to Firefox, returning instances of [Browser](/docs/api/class-browser "Browser").

**Usage**

``` 
playwright.firefox
```

**Type**

-   [BrowserType](/docs/api/class-browsertype "BrowserType")

------------------------------------------------------------------------

### request[​](#playwright-request "Direct link to request") 

Added in: v1.16 playwright.request

Exposes API that can be used for the Web API testing.

**Usage**

``` 
playwright.request
```

**Type**

-   [APIRequest](/docs/api/class-apirequest "APIRequest")

------------------------------------------------------------------------

### selectors[​](#playwright-selectors "Direct link to selectors") 

Added before v1.9 playwright.selectors

Selectors can be used to install custom selector engines. See [extensibility](/docs/extensibility) for more information.

**Usage**

``` 
playwright.selectors
```

**Type**

-   [Selectors](/docs/api/class-selectors "Selectors")

------------------------------------------------------------------------

### webkit[​](#playwright-webkit "Direct link to webkit") 

Added before v1.9 playwright.webkit

This object can be used to launch or connect to WebKit, returning instances of [Browser](/docs/api/class-browser "Browser").

**Usage**

``` 
playwright.webkit
```

**Type**

-   [BrowserType](/docs/api/class-browsertype "BrowserType")