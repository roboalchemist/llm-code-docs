# Source: https://playwright.dev/docs/api/class-androidwebview

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Experimental]
-   [AndroidWebView]

On this page

<div>

# AndroidWebView

</div>

[AndroidWebView](/docs/api/class-androidwebview "AndroidWebView") represents a WebView open on the [AndroidDevice](/docs/api/class-androiddevice "AndroidDevice"). WebView is usually obtained using [androidDevice.webView()](/docs/api/class-androiddevice#android-device-web-view).

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### page[​](#android-web-view-page "Direct link to page") 

Added in: v1.9 androidWebView.page

Connects to the WebView and returns a regular Playwright [Page](/docs/api/class-page "Page") to interact with.

**Usage**

``` 
await androidWebView.page();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[Page](/docs/api/class-page "Page")\>[][\#](#android-web-view-page-return)

------------------------------------------------------------------------

### pid[​](#android-web-view-pid "Direct link to pid") 

Added in: v1.9 androidWebView.pid

WebView process PID.

**Usage**

``` 
androidWebView.pid();
```

**Returns**

-   [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#android-web-view-pid-return)

------------------------------------------------------------------------

### pkg[​](#android-web-view-pkg "Direct link to pkg") 

Added in: v1.9 androidWebView.pkg

WebView package identifier.

**Usage**

``` 
androidWebView.pkg();
```

**Returns**

-   [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#android-web-view-pkg-return)

------------------------------------------------------------------------

## Events[​](#events "Direct link to Events") 

### on(\'close\')[​](#android-web-view-event-close "Direct link to on('close')") 

Added in: v1.9 androidWebView.on(\'close\')

Emitted when the WebView is closed.

**Usage**

``` 
androidWebView.on('close', data => );
```