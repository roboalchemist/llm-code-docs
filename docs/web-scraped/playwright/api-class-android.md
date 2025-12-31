# Source: https://playwright.dev/docs/api/class-android

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Experimental]
-   [Android]

On this page

<div>

# Android

</div>

Playwright has **experimental** support for Android automation. This includes Chrome for Android and Android WebView.

*Requirements*

-   Android device or AVD Emulator.
-   [ADB daemon](https://developer.android.com/studio/command-line/adb) running and authenticated with your device. Typically running `adb devices` is all you need to do.
-   [`Chrome 87`](https://play.google.com/store/apps/details?id=com.android.chrome) or newer installed on the device
-   \"Enable command line on non-rooted devices\" enabled in `chrome://flags`.

*Known limitations*

-   Raw USB operation is not yet supported, so you need ADB.
-   Device needs to be awake to produce screenshots. Enabling \"Stay awake\" developer mode will help.
-   We didn\'t run all the tests against the device, so not everything works.

*How to run*

An example of the Android automation script would be:

``` 
const  = require('playwright');

(async () => `);
  console.log(`Serial: $`);
  // Take screenshot of the whole device.
  await device.screenshot();

  );

    // Fill the input box.
    await device.fill(, 'github.com/microsoft/playwright');
    await device.press(, 'Enter');

    // Work with WebView's page as usual.
    const page = await webview.page();
    await page.waitForNavigation();
    console.log(await page.title());
  }

  );

    await context.close();
  }

  // Close the device.
  await device.close();
})();
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### connect[​](#android-connect "Direct link to connect") 

Added in: v1.28 android.connect

This methods attaches Playwright to an existing Android device. Use [android.launchServer()](/docs/api/class-android#android-launch-server) to launch a new Android server instance.

**Usage**

``` 
await android.connect(wsEndpoint);
await android.connect(wsEndpoint, options);
```

**Arguments**

-   `wsEndpoint` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#android-connect-option-ws-endpoint)

    A browser websocket endpoint to connect to.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `headers` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object")\<[string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string"), [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")\> *(optional)*[][\#](#android-connect-option-headers)

        Additional HTTP headers to be sent with web socket connect request. Optional.

    -   `slowMo` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#android-connect-option-slow-mo)

        Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. Defaults to `0`.

    -   `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#android-connect-option-timeout)

        Maximum time in milliseconds to wait for the connection to be established. Defaults to `30000` (30 seconds). Pass `0` to disable timeout.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[AndroidDevice](/docs/api/class-androiddevice "AndroidDevice")\>[][\#](#android-connect-return)

------------------------------------------------------------------------

### devices[​](#android-devices "Direct link to devices") 

Added in: v1.9 android.devices

Returns the list of detected Android devices.

**Usage**

``` 
await android.devices();
await android.devices(options);
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `host` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)* Added in: v1.22[][\#](#android-devices-option-host)

        Optional host to establish ADB server connection. Default to `127.0.0.1`.

    -   `omitDriverInstall` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)* Added in: v1.21[][\#](#android-devices-option-omit-driver-install)

        Prevents automatic playwright driver installation on attach. Assumes that the drivers have been installed already.

    -   `port` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)* Added in: v1.20[][\#](#android-devices-option-port)

        Optional port to establish ADB server connection. Default to `5037`.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array "Array")\<[AndroidDevice](/docs/api/class-androiddevice "AndroidDevice")\>\>[][\#](#android-devices-return)

------------------------------------------------------------------------

### launchServer[​](#android-launch-server "Direct link to launchServer") 

Added in: v1.28 android.launchServer

Launches Playwright Android server that clients can connect to. See the following example:

**Usage**

Server Side:

``` 
const  = require('playwright');

(async () => );
  const wsEndpoint = browserServer.wsEndpoint();
  console.log(wsEndpoint);
})();
```

Client Side:

``` 
const  = require('playwright');

(async () => );

  await context.close();
})();
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `adbHost` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#android-launch-server-option-adb-host)

        Optional host to establish ADB server connection. Default to `127.0.0.1`.

    -   `adbPort` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#android-launch-server-option-adb-port)

        Optional port to establish ADB server connection. Default to `5037`.

    -   `deviceSerialNumber` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#android-launch-server-option-device-serial-number)

        Optional device serial number to launch the browser on. If not specified, it will throw if multiple devices are connected.

    -   `host` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)* Added in: v1.45[][\#](#android-launch-server-option-host)

        Host to use for the web socket. It is optional and if it is omitted, the server will accept connections on the unspecified IPv6 address (::) when IPv6 is available, or the unspecified IPv4 address (0.0.0.0) otherwise. Consider hardening it with picking a specific interface.

    -   `omitDriverInstall` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*[][\#](#android-launch-server-option-omit-driver-install)

        Prevents automatic playwright driver installation on attach. Assumes that the drivers have been installed already.

    -   `port` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#android-launch-server-option-port)

        Port to use for the web socket. Defaults to 0 that picks any available port.

    -   `wsPath` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#android-launch-server-option-ws-path)

        Path at which to serve the Android Server. For security, this defaults to an unguessable string.

        ::: 
        ::: admonitionHeading_Gvgb
        [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning
        :::

        ::: admonitionContent_BuS1
        Any process or web page (including those running in Playwright) with knowledge of the `wsPath` can take control of the OS user. For this reason, you should use an unguessable token when using this option.
        :::
        :::

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[BrowserServer](/docs/api/class-browserserver "BrowserServer")\>[][\#](#android-launch-server-return)

------------------------------------------------------------------------

### setDefaultTimeout[​](#android-set-default-timeout "Direct link to setDefaultTimeout") 

Added in: v1.9 android.setDefaultTimeout

This setting will change the default maximum time for all the methods accepting [timeout](/docs/api/class-android#android-set-default-timeout-option-timeout) option.

**Usage**

``` 
android.setDefaultTimeout(timeout);
```

**Arguments**

-   `timeout` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#android-set-default-timeout-option-timeout)

    Maximum time in milliseconds