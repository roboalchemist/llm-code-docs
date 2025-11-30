# Source: https://www.electronjs.org/docs/latest/api/session

On this page

# session

> Manage browser sessions, cookies, cache, proxy settings, etc.

Process: [Main](/docs/latest/glossary#main-process)

The `session` module can be used to create new `Session` objects.

You can also access the `session` of existing pages by using the `session` property of [`WebContents`](/docs/latest/api/web-contents), or from the `session` module.

``` 
const  = require('electron')

const win = new BrowserWindow()
win.loadURL('https://github.com')

const ses = win.webContents.session
console.log(ses.getUserAgent())
```

## Methods[â€‹](#methods "Direct link to Methods") 

The `session` module has the following methods:

### `session.fromPartition(partition[, options])`[â€‹](#sessionfrompartitionpartition-options "Direct link to sessionfrompartitionpartition-options") 

- `partition` string
- `options` Object (optional)
  - `cache` boolean - Whether to enable cache. Default is `true` unless the [`--disable-http-cache` switch](/docs/latest/api/command-line-switches#--disable-http-cache) is used.

Returns `Session` - A session instance from `partition` string. When there is an existing `Session` with the same `partition`, it will be returned; otherwise a new `Session` instance will be created with `options`.

If `partition` starts with `persist:`, the page will use a persistent session available to all pages in the app with the same `partition`. if there is no `persist:` prefix, the page will use an in-memory session. If the `partition` is empty then default session of the app will be returned.

To create a `Session` with `options`, you have to ensure the `Session` with the `partition` has never been used before. There is no way to change the `options` of an existing `Session` object.

### `session.fromPath(path[, options])`[â€‹](#sessionfrompathpath-options "Direct link to sessionfrompathpath-options") 

- `path` string
- `options` Object (optional)
  - `cache` boolean - Whether to enable cache. Default is `true` unless the [`--disable-http-cache` switch](/docs/latest/api/command-line-switches#--disable-http-cache) is used.

Returns `Session` - A session instance from the absolute path as specified by the `path` string. When there is an existing `Session` with the same absolute path, it will be returned; otherwise a new `Session` instance will be created with `options`. The call will throw an error if the path is not an absolute path. Additionally, an error will be thrown if an empty string is provided.

To create a `Session` with `options`, you have to ensure the `Session` with the `path` has never been used before. There is no way to change the `options` of an existing `Session` object.

## Properties[â€‹](#properties "Direct link to Properties") 

The `session` module has the following properties:

### `session.defaultSession`[â€‹](#sessiondefaultsession "Direct link to sessiondefaultsession") 

A `Session` object, the default session object of the app.

## Class: Session[â€‹](#class-session "Direct link to Class: Session") 

> Get and set properties of a session.

Process: [Main](/docs/latest/glossary#main-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

You can create a `Session` object in the `session` module:

``` 
const  = require('electron')

const ses = session.fromPartition('persist:name')
console.log(ses.getUserAgent())
```

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

The following events are available on instances of `Session`:

#### Event: \'will-download\'[â€‹](#event-will-download "Direct link to Event: 'will-download'") 

Returns:

- `event` Event
- `item` [DownloadItem](/docs/latest/api/download-item)
- `webContents` [WebContents](/docs/latest/api/web-contents)

Emitted when Electron is about to download `item` in `webContents`.

Calling `event.preventDefault()` will cancel the download and `item` will not be available from next tick of the process.

``` 
const  = require('electron')

session.defaultSession.on('will-download', (event, item, webContents) => )
})
```

#### Event: \'extension-loaded\'[â€‹](#event-extension-loaded "Direct link to Event: 'extension-loaded'") 

Returns:

- `event` Event
- `extension` [Extension](/docs/latest/api/structures/extension)

Emitted after an extension is loaded. This occurs whenever an extension is added to the \"enabled\" set of extensions. This includes:

- Extensions being loaded from `Session.loadExtension`.
- Extensions being reloaded:
  - from a crash.
  - if the extension requested it ([`chrome.runtime.reload()`](https://developer.chrome.com/extensions/runtime#method-reload)).

#### Event: \'extension-unloaded\'[â€‹](#event-extension-unloaded "Direct link to Event: 'extension-unloaded'") 

Returns:

- `event` Event
- `extension` [Extension](/docs/latest/api/structures/extension)

Emitted after an extension is unloaded. This occurs when `Session.removeExtension` is called.

#### Event: \'extension-ready\'[â€‹](#event-extension-ready "Direct link to Event: 'extension-ready'") 

Returns:

- `event` Event
- `extension` [Extension](/docs/latest/api/structures/extension)

Emitted after an extension is loaded and all necessary browser state is initialized to support the start of the extension\'s background page.

#### Event: \'file-system-access-restricted\'[â€‹](#event-file-system-access-restricted "Direct link to Event: 'file-system-access-restricted'") 

Returns:

- `event` Event
- `details` Object
  - `origin` string - The origin that initiated access to the blocked path.
  - `isDirectory` boolean - Whether or not the path is a directory.
  - `path` string - The blocked path attempting to be accessed.
- `callback` Function
  - `action` string - The action to take as a result of the restricted path access attempt.
    - `allow` - This will allow `path` to be accessed despite restricted status.
    - `deny` - This will block the access request and trigger an [`AbortError`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController/abort).
    - `tryAgain` - This will open a new file picker and allow the user to choose another path.

``` 
const  = require('electron')

async function createWindow ()  = details
    const  = await dialog.showMessageBox( to open restricted path $?`,
      title: 'File System Access Restricted',
      buttons: ['Choose a different folder', 'Allow', 'Cancel'],
      cancelId: 2
    })

    if (response === 0)  else if (response === 1)  else 
  })

  mainWindow.webContents.executeJavaScript(`
    window.showDirectoryPicker().catch(e => )`, true
  )
}

app.whenReady().then(() => )
})

app.on('window-all-closed', function () )
```

#### Event: \'preconnect\'[â€‹](#event-preconnect "Direct link to Event: 'preconnect'") 

Returns:

- `event` Event
- `preconnectUrl` string - The URL being requested for preconnection by the renderer.
- `allowCredentials` boolean - True if the renderer is requesting that the connection include credentials (see the [spec](https://w3c.github.io/resource-hints/#preconnect) for more details.)

Emitted when a render process requests preconnection to a URL, generally due to a [resource hint](https://w3c.github.io/resource-hints/).

#### Event: \'spellcheck-dictionary-initialized\'[â€‹](#event-spellcheck-dictionary-initialized "Direct link to Event: 'spellcheck-dictionary-initialized'") 

Returns:

- `event` Event
- `languageCode` string - The language code of the dictionary file

Emitted when a hunspell dictionary file has been successfully initialized. This occurs after the file has been downloaded.

#### Event: \'spellcheck-dictionary-download-begin\'[â€‹](#event-spellcheck-dictionary-download-begin "Direct link to Event: 'spellcheck-dictionary-download-begin'") 

Returns:

- `event` Event
- `languageCode` string - The language code of the dictionary file

Emitted when a hunspell dictionary file starts downloading

#### Event: \'spellcheck-dictionary-download-success\'[â€‹](#event-spellcheck-dictionary-download-success "Direct link to Event: 'spellcheck-dictionary-download-success'") 

Returns:

- `event` Event
- `languageCode` string - The language code of the dictionary file

Emitted when a hunspell dictionary file has been successfully downloaded

#### Event: \'spellcheck-dictionary-download-failure\'[â€‹](#event-spellcheck-dictionary-download-failure "Direct link to Event: 'spellcheck-dictionary-download-failure'") 

Returns:

- `event` Event
- `languageCode` string - The language code of the dictionary file

Emitted when a hunspell dictionary file download fails. For details on the failure you should collect a netlog and inspect the download request.

#### Event: \'select-hid-device\'[â€‹](#event-select-hid-device "Direct link to Event: 'select-hid-device'") 

Returns:

- `event` Event
- `details` Object
  - `deviceList` [HIDDevice\[\]](/docs/latest/api/structures/hid-device)
  - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this event. May be `null` if accessed after the frame has either navigated or been destroyed.
- `callback` Function
  - `deviceId` string \| null (optional)

Emitted when a HID device needs to be selected when a call to `navigator.hid.requestDevice` is made. `callback` should be called with `deviceId` to be selected; passing no arguments to `callback` will cancel the request. Additionally, permissioning on `navigator.hid` can be further managed by using [`ses.setPermissionCheckHandler(handler)`](#sessetpermissioncheckhandlerhandler) and [`ses.setDevicePermissionHandler(handler)`](#sessetdevicepermissionhandlerhandler).

``` 
const  = require('electron')

let win = null

app.whenReady().then(() => 
    return false
  })

  // Optionally, retrieve previously persisted devices from a persistent store
  const grantedDevices = fetchGrantedDevices()

  win.webContents.session.setDevicePermissionHandler((details) => 

      // Search through the list of devices that have previously been granted permission
      return grantedDevices.some((grantedDevice) => )
    }
    return false
  })

  win.webContents.session.on('select-hid-device', (event, details, callback) => )
    callback(selectedDevice?.deviceId)
  })
})
```

#### Event: \'hid-device-added\'[â€‹](#event-hid-device-added "Direct link to Event: 'hid-device-added'") 

Returns:

- `event` Event
- `details` Object
  - `device` [HIDDevice](/docs/latest/api/structures/hid-device)
  - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this event. May be `null` if accessed after the frame has either navigated or been destroyed.

Emitted after `navigator.hid.requestDevice` has been called and `select-hid-device` has fired if a new device becomes available before the callback from `select-hid-device` is called. This event is intended for use when using a UI to ask users to pick a device so that the UI can be updated with the newly added device.

#### Event: \'hid-device-removed\'[â€‹](#event-hid-device-removed "Direct link to Event: 'hid-device-removed'") 

Returns:

- `event` Event
- `details` Object
  - `device` [HIDDevice](/docs/latest/api/structures/hid-device)
  - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this event. May be `null` if accessed after the frame has either navigated or been destroyed.

Emitted after `navigator.hid.requestDevice` has been called and `select-hid-device` has fired if a device has been removed before the callback from `select-hid-device` is called. This event is intended for use when using a UI to ask users to pick a device so that the UI can be updated to remove the specified device.

#### Event: \'hid-device-revoked\'[â€‹](#event-hid-device-revoked "Direct link to Event: 'hid-device-revoked'") 

Returns:

- `event` Event
- `details` Object
  - `device` [HIDDevice](/docs/latest/api/structures/hid-device)
  - `origin` string (optional) - The origin that the device has been revoked from.

Emitted after `HIDDevice.forget()` has been called. This event can be used to help maintain persistent storage of permissions when `setDevicePermissionHandler` is used.

#### Event: \'select-serial-port\'[â€‹](#event-select-serial-port "Direct link to Event: 'select-serial-port'") 

Returns:

- `event` Event
- `portList` [SerialPort\[\]](/docs/latest/api/structures/serial-port)
- `webContents` [WebContents](/docs/latest/api/web-contents)
- `callback` Function
  - `portId` string

Emitted when a serial port needs to be selected when a call to `navigator.serial.requestPort` is made. `callback` should be called with `portId` to be selected, passing an empty string to `callback` will cancel the request. Additionally, permissioning on `navigator.serial` can be managed by using [ses.setPermissionCheckHandler(handler)](#sessetpermissioncheckhandlerhandler) with the `serial` permission.

``` 
const  = require('electron')

let win = null

app.whenReady().then(() => )

  win.webContents.session.setPermissionCheckHandler((webContents, permission, requestingOrigin, details) => 
    return false
  })

  // Optionally, retrieve previously persisted devices from a persistent store
  const grantedDevices = fetchGrantedDevices()

  win.webContents.session.setDevicePermissionHandler((details) => 

      // Search through the list of devices that have previously been granted permission
      return grantedDevices.some((grantedDevice) => )
    }
    return false
  })

  win.webContents.session.on('select-serial-port', (event, portList, webContents, callback) => )
    if (!selectedPort)  else 
  })
})
```

#### Event: \'serial-port-added\'[â€‹](#event-serial-port-added "Direct link to Event: 'serial-port-added'") 

Returns:

- `event` Event
- `port` [SerialPort](/docs/latest/api/structures/serial-port)
- `webContents` [WebContents](/docs/latest/api/web-contents)

Emitted after `navigator.serial.requestPort` has been called and `select-serial-port` has fired if a new serial port becomes available before the callback from `select-serial-port` is called. This event is intended for use when using a UI to ask users to pick a port so that the UI can be updated with the newly added port.

#### Event: \'serial-port-removed\'[â€‹](#event-serial-port-removed "Direct link to Event: 'serial-port-removed'") 

Returns:

- `event` Event
- `port` [SerialPort](/docs/latest/api/structures/serial-port)
- `webContents` [WebContents](/docs/latest/api/web-contents)

Emitted after `navigator.serial.requestPort` has been called and `select-serial-port` has fired if a serial port has been removed before the callback from `select-serial-port` is called. This event is intended for use when using a UI to ask users to pick a port so that the UI can be updated to remove the specified port.

#### Event: \'serial-port-revoked\'[â€‹](#event-serial-port-revoked "Direct link to Event: 'serial-port-revoked'") 

Returns:

- `event` Event
- `details` Object
  - `port` [SerialPort](/docs/latest/api/structures/serial-port)
  - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this event. May be `null` if accessed after the frame has either navigated or been destroyed.
  - `origin` string - The origin that the device has been revoked from.

Emitted after `SerialPort.forget()` has been called. This event can be used to help maintain persistent storage of permissions when `setDevicePermissionHandler` is used.

``` 
// Browser Process
const  = require('electron')

app.whenReady().then(() => )

  win.webContents.session.on('serial-port-revoked', (event, details) => `)
  })
})
```

``` 
// Renderer Process

const portConnect = async () => )

  // ...later, revoke access to the serial port.
  await port.forget()
}
```

#### Event: \'select-usb-device\'[â€‹](#event-select-usb-device "Direct link to Event: 'select-usb-device'") 

Returns:

- `event` Event
- `details` Object
  - `deviceList` [USBDevice\[\]](/docs/latest/api/structures/usb-device)
  - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this event. May be `null` if accessed after the frame has either navigated or been destroyed.
- `callback` Function
  - `deviceId` string (optional)

Emitted when a USB device needs to be selected when a call to `navigator.usb.requestDevice` is made. `callback` should be called with `deviceId` to be selected; passing no arguments to `callback` will cancel the request. Additionally, permissioning on `navigator.usb` can be further managed by using [`ses.setPermissionCheckHandler(handler)`](#sessetpermissioncheckhandlerhandler) and [`ses.setDevicePermissionHandler(handler)`](#sessetdevicepermissionhandlerhandler).

``` 
const  = require('electron')

let win = null

app.whenReady().then(() => 
    return false
  })

  // Optionally, retrieve previously persisted devices from a persistent store (fetchGrantedDevices needs to be implemented by developer to fetch persisted permissions)
  const grantedDevices = fetchGrantedDevices()

  win.webContents.session.setDevicePermissionHandler((details) => 

      // Search through the list of devices that have previously been granted permission
      return grantedDevices.some((grantedDevice) => )
    }
    return false
  })

  win.webContents.session.on('select-usb-device', (event, details, callback) => )
    if (selectedDevice) 
    callback(selectedDevice?.deviceId)
  })
})
```

#### Event: \'usb-device-added\'[â€‹](#event-usb-device-added "Direct link to Event: 'usb-device-added'") 

Returns:

- `event` Event
- `device` [USBDevice](/docs/latest/api/structures/usb-device)
- `webContents` [WebContents](/docs/latest/api/web-contents)

Emitted after `navigator.usb.requestDevice` has been called and `select-usb-device` has fired if a new device becomes available before the callback from `select-usb-device` is called. This event is intended for use when using a UI to ask users to pick a device so that the UI can be updated with the newly added device.

#### Event: \'usb-device-removed\'[â€‹](#event-usb-device-removed "Direct link to Event: 'usb-device-removed'") 

Returns:

- `event` Event
- `device` [USBDevice](/docs/latest/api/structures/usb-device)
- `webContents` [WebContents](/docs/latest/api/web-contents)

Emitted after `navigator.usb.requestDevice` has been called and `select-usb-device` has fired if a device has been removed before the callback from `select-usb-device` is called. This event is intended for use when using a UI to ask users to pick a device so that the UI can be updated to remove the specified device.

#### Event: \'usb-device-revoked\'[â€‹](#event-usb-device-revoked "Direct link to Event: 'usb-device-revoked'") 

Returns:

- `event` Event
- `details` Object
  - `device` [USBDevice](/docs/latest/api/structures/usb-device)
  - `origin` string (optional) - The origin that the device has been revoked from.

Emitted after `USBDevice.forget()` has been called. This event can be used to help maintain persistent storage of permissions when `setDevicePermissionHandler` is used.

### Instance Methods[â€‹](#instance-methods "Direct link to Instance Methods") 

The following methods are available on instances of `Session`:

#### `ses.getCacheSize()`[â€‹](#sesgetcachesize "Direct link to sesgetcachesize") 

Returns `Promise<Integer>` - the session\'s current cache size, in bytes.

#### `ses.clearCache()`[â€‹](#sesclearcache "Direct link to sesclearcache") 

Returns `Promise<void>` - resolves when the cache clear operation is complete.

Clears the sessionâ€™s HTTP cache.

#### `ses.clearStorageData([options])`[â€‹](#sesclearstoragedataoptions "Direct link to sesclearstoragedataoptions") 

- `options` Object (optional)
  - `origin` string (optional) - Should follow `window.location.origin`â€™s representation `scheme://host:port`.
  - `storages` string\[\] (optional) - The types of storages to clear, can be `cookies`, `filesystem`, `indexdb`, `localstorage`, `shadercache`, `websql`, `serviceworkers`, `cachestorage`. If not specified, clear all storage types.
  - `quotas` string\[\] (optional) - The types of quotas to clear, can be `temporary`. If not specified, clear all quotas.

Returns `Promise<void>` - resolves when the storage data has been cleared.

#### `ses.flushStorageData()`[â€‹](#sesflushstoragedata "Direct link to sesflushstoragedata") 

Writes any unwritten DOMStorage data to disk.

#### `ses.setProxy(config)`[â€‹](#sessetproxyconfig "Direct link to sessetproxyconfig") 

- `config` [ProxyConfig](/docs/latest/api/structures/proxy-config)

Returns `Promise<void>` - Resolves when the proxy setting process is complete.

Sets the proxy settings.

You may need `ses.closeAllConnections` to close currently in flight connections to prevent pooled sockets using previous proxy from being reused by future requests.

#### `ses.resolveHost(host, [options])`[â€‹](#sesresolvehosthost-options "Direct link to sesresolvehosthost-options") 

- `host` string - Hostname to resolve.
- `options` Object (optional)
  - `queryType` string (optional) - Requested DNS query type. If unspecified, resolver will pick A or AAAA (or both) based on IPv4/IPv6 settings:
    - `A` - Fetch only A records
    - `AAAA` - Fetch only AAAA records.
  - `source` string (optional) - The source to use for resolved addresses. Default allows the resolver to pick an appropriate source. Only affects use of big external sources (e.g. calling the system for resolution or using DNS). Even if a source is specified, results can still come from cache, resolving \"localhost\" or IP literals, etc. One of the following values:
    - `any` (default) - Resolver will pick an appropriate source. Results could come from DNS, MulticastDNS, HOSTS file, etc
    - `system` - Results will only be retrieved from the system or OS, e.g. via the `getaddrinfo()` system call
    - `dns` - Results will only come from DNS queries
    - `mdns` - Results will only come from Multicast DNS queries
    - `localOnly` - No external sources will be used. Results will only come from fast local sources that are available no matter the source setting, e.g. cache, hosts file, IP literal resolution, etc.
  - `cacheUsage` string (optional) - Indicates what DNS cache entries, if any, can be used to provide a response. One of the following values:
    - `allowed` (default) - Results may come from the host cache if non-stale
    - `staleAllowed` - Results may come from the host cache even if stale (by expiration or network changes)
    - `disallowed` - Results will not come from the host cache.
  - `secureDnsPolicy` string (optional) - Controls the resolver\'s Secure DNS behavior for this request. One of the following values:
    - `allow` (default)
    - `disable`

Returns [Promise\<ResolvedHost\>](/docs/latest/api/structures/resolved-host) - Resolves with the resolved IP addresses for the `host`.

#### `ses.resolveProxy(url)`[â€‹](#sesresolveproxyurl "Direct link to sesresolveproxyurl") 

- `url` URL

Returns `Promise<string>` - Resolves with the proxy information for `url`.

#### `ses.forceReloadProxyConfig()`[â€‹](#sesforcereloadproxyconfig "Direct link to sesforcereloadproxyconfig") 

Returns `Promise<void>` - Resolves when the all internal states of proxy service is reset and the latest proxy configuration is reapplied if it\'s already available. The pac script will be fetched from `pacScript` again if the proxy mode is `pac_script`.

#### `ses.setDownloadPath(path)`[â€‹](#sessetdownloadpathpath "Direct link to sessetdownloadpathpath") 

- `path` string - The download location.

Sets download saving directory. By default, the download directory will be the `Downloads` under the respective app folder.

#### `ses.enableNetworkEmulation(options)`[â€‹](#sesenablenetworkemulationoptions "Direct link to sesenablenetworkemulationoptions") 

- `options` Object
  - `offline` boolean (optional) - Whether to emulate network outage. Defaults to false.
  - `latency` Double (optional) - RTT in ms. Defaults to 0 which will disable latency throttling.
  - `downloadThroughput` Double (optional) - Download rate in Bps. Defaults to 0 which will disable download throttling.
  - `uploadThroughput` Double (optional) - Upload rate in Bps. Defaults to 0 which will disable upload throttling.

Emulates network with the given configuration for the `session`.

``` 
const win = new BrowserWindow()

// To emulate a GPRS connection with 50kbps throughput and 500 ms latency.
win.webContents.session.enableNetworkEmulation()

// To emulate a network outage.
win.webContents.session.enableNetworkEmulation()
```

#### `ses.preconnect(options)`[â€‹](#sespreconnectoptions "Direct link to sespreconnectoptions") 

- `options` Object
  - `url` string - URL for preconnect. Only the origin is relevant for opening the socket.
  - `numSockets` number (optional) - number of sockets to preconnect. Must be between 1 and 6. Defaults to 1.

Preconnects the given number of sockets to an origin.

#### `ses.closeAllConnections()`[â€‹](#sescloseallconnections "Direct link to sescloseallconnections") 

Returns `Promise<void>` - Resolves when all connections are closed.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

It will terminate / fail all requests currently in flight.

#### `ses.fetch(input[, init])`[â€‹](#sesfetchinput-init "Direct link to sesfetchinput-init") 

- `input` string \| [GlobalRequest](https://nodejs.org/api/globals.html#request)
- `init` [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/fetch#options) &  (optional)

Returns `Promise<GlobalResponse>` - see [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response).

Sends a request, similarly to how `fetch()` works in the renderer, using Chrome\'s network stack. This differs from Node\'s `fetch()`, which uses Node.js\'s HTTP stack.

Example:

``` 
async function example () 
}
```

See also [`net.fetch()`](/docs/latest/api/net#netfetchinput-init), a convenience method which issues requests from the [default session](#sessiondefaultsession).

See the MDN documentation for [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/fetch) for more details.

Limitations:

- `net.fetch()` does not support the `data:` or `blob:` schemes.
- The value of the `integrity` option is ignored.
- The `.type` and `.url` values of the returned `Response` object are incorrect.

By default, requests made with `net.fetch` can be made to [custom protocols](/docs/latest/api/protocol) as well as `file:`, and will trigger [webRequest](/docs/latest/api/web-request) handlers if present. When the non-standard `bypassCustomProtocolHandlers` option is set in RequestInit, custom protocol handlers will not be called for this request. This allows forwarding an intercepted request to the built-in handler. [webRequest](/docs/latest/api/web-request) handlers will still be triggered when bypassing custom protocols.

``` 
protocol.handle('https', (req) =>  else )
  }
})
```

#### `ses.disableNetworkEmulation()`[â€‹](#sesdisablenetworkemulation "Direct link to sesdisablenetworkemulation") 

Disables any network emulation already active for the `session`. Resets to the original network configuration.

#### `ses.setCertificateVerifyProc(proc)`[â€‹](#sessetcertificateverifyprocproc "Direct link to sessetcertificateverifyprocproc") 

- `proc` Function \| null
  - `request` Object
    - `hostname` string
    - `certificate` [Certificate](/docs/latest/api/structures/certificate)
    - `validatedCertificate` [Certificate](/docs/latest/api/structures/certificate)
    - `isIssuedByKnownRoot` boolean - `true` if Chromium recognises the root CA as a standard root. If it isn\'t then it\'s probably the case that this certificate was generated by a MITM proxy whose root has been installed locally (for example, by a corporate proxy). This should not be trusted if the `verificationResult` is not `OK`.
    - `verificationResult` string - `OK` if the certificate is trusted, otherwise an error like `CERT_REVOKED`.
    - `errorCode` Integer - Error code.
  - `callback` Function
    - `verificationResult` Integer - Value can be one of certificate error codes from [here](https://source.chromium.org/chromium/chromium/src/+/main:net/base/net_error_list.h). Apart from the certificate error codes, the following special codes can be used.
      - `0` - Indicates success and disables Certificate Transparency verification.
      - `-2` - Indicates failure.
      - `-3` - Uses the verification result from chromium.

Sets the certificate verify proc for `session`, the `proc` will be called with `proc(request, callback)` whenever a server certificate verification is requested. Calling `callback(0)` accepts the certificate, calling `callback(-2)` rejects it.

Calling `setCertificateVerifyProc(null)` will revert back to default certificate verify proc.

``` 
const  = require('electron')

const win = new BrowserWindow()

win.webContents.session.setCertificateVerifyProc((request, callback) =>  = request
  if (hostname === 'github.com')  else 
})
```

> **NOTE:** The result of this procedure is cached by the network service.

#### `ses.setPermissionRequestHandler(handler)`[â€‹](#sessetpermissionrequesthandlerhandler "Direct link to sessetpermissionrequesthandlerhandler") 

- `handler` Function \| null
  - `webContents` [WebContents](/docs/latest/api/web-contents) - WebContents requesting the permission. Please note that if the request comes from a subframe you should use `requestingUrl` to check the request origin.
  - `permission` string - The type of requested permission.
    - `clipboard-read` - Request access to read from the clipboard.
    - `clipboard-sanitized-write` - Request access to write to the clipboard.
    - `display-capture` - Request access to capture the screen via the [Screen Capture API](https://developer.mozilla.org/en-US/docs/Web/API/Screen_Capture_API).
    - `fullscreen` - Request control of the app\'s fullscreen state via the [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API).
    - `geolocation` - Request access to the user\'s location via the [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
    - `idle-detection` - Request access to the user\'s idle state via the [IdleDetector API](https://developer.mozilla.org/en-US/docs/Web/API/IdleDetector).
    - `media` - Request access to media devices such as camera, microphone and speakers.
    - `mediaKeySystem` - Request access to DRM protected content.
    - `midi` - Request MIDI access in the [Web MIDI API](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API).
    - `midiSysex` - Request the use of system exclusive messages in the [Web MIDI API](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API).
    - `notifications` - Request notification creation and the ability to display them in the user\'s system tray using the [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/notification)
    - `pointerLock` - Request to directly interpret mouse movements as an input method via the [Pointer Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API). These requests always appear to originate from the main frame.
    - `keyboardLock` - Request capture of keypresses for any or all of the keys on the physical keyboard via the [Keyboard Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Keyboard/lock). These requests always appear to originate from the main frame.
    - `openExternal` - Request to open links in external applications.
    - `speaker-selection` - Request to enumerate and select audio output devices via the [speaker-selection permissions policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy/speaker-selection).
    - `storage-access` - Allows content loaded in a third-party context to request access to third-party cookies using the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API).
    - `top-level-storage-access` - Allow top-level sites to request third-party cookie access on behalf of embedded content originating from another site in the same related website set using the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API).
    - `window-management` - Request access to enumerate screens using the [`getScreenDetails`](https://developer.chrome.com/en/articles/multi-screen-window-placement/) API.
    - `unknown` - An unrecognized permission request.
    - `fileSystem` - Request access to read, write, and file management capabilities using the [File System API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API).
  - `callback` Function
    - `permissionGranted` boolean - Allow or deny the permission.
  - `details` [PermissionRequest](/docs/latest/api/structures/permission-request) \| [FilesystemPermissionRequest](/docs/latest/api/structures/filesystem-permission-request) \| [MediaAccessPermissionRequest](/docs/latest/api/structures/media-access-permission-request) \| [OpenExternalPermissionRequest](/docs/latest/api/structures/open-external-permission-request) - Additional information about the permission being requested.

Sets the handler which can be used to respond to permission requests for the `session`. Calling `callback(true)` will allow the permission and `callback(false)` will reject it. To clear the handler, call `setPermissionRequestHandler(null)`. Please note that you must also implement `setPermissionCheckHandler` to get complete permission handling. Most web APIs do a permission check and then make a permission request if the check is denied.

``` 
const  = require('electron')

session.fromPartition('some-partition').setPermissionRequestHandler((webContents, permission, callback) => 

  callback(true)
})
```

#### `ses.setPermissionCheckHandler(handler)`[â€‹](#sessetpermissioncheckhandlerhandler "Direct link to sessetpermissioncheckhandlerhandler") 

- `handler` Function\<boolean\> \| null
  - `webContents` ([WebContents](/docs/latest/api/web-contents) \| null) - WebContents checking the permission. Please note that if the request comes from a subframe you should use `requestingUrl` to check the request origin. All cross origin sub frames making permission checks will pass a `null` webContents to this handler, while certain other permission checks such as `notifications` checks will always pass `null`. You should use `embeddingOrigin` and `requestingOrigin` to determine what origin the owning frame and the requesting frame are on respectively.
  - `permission` string - Type of permission check.
    - `clipboard-read` - Request access to read from the clipboard.
    - `clipboard-sanitized-write` - Request access to write to the clipboard.
    - `geolocation` - Access the user\'s geolocation data via the [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API)
    - `fullscreen` - Control of the app\'s fullscreen state via the [Fullscreen API](https://developer.mozilla.org/en-US/docs/Web/API/Fullscreen_API).
    - `hid` - Access the HID protocol to manipulate HID devices via the [WebHID API](https://developer.mozilla.org/en-US/docs/Web/API/WebHID_API).
    - `idle-detection` - Access the user\'s idle state via the [IdleDetector API](https://developer.mozilla.org/en-US/docs/Web/API/IdleDetector).
    - `media` - Access to media devices such as camera, microphone and speakers.
    - `mediaKeySystem` - Access to DRM protected content.
    - `midi` - Enable MIDI access in the [Web MIDI API](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API).
    - `midiSysex` - Use system exclusive messages in the [Web MIDI API](https://developer.mozilla.org/en-US/docs/Web/API/Web_MIDI_API).
    - `notifications` - Configure and display desktop notifications to the user with the [Notifications API](https://developer.mozilla.org/en-US/docs/Web/API/notification).
    - `openExternal` - Open links in external applications.
    - `pointerLock` - Directly interpret mouse movements as an input method via the [Pointer Lock API](https://developer.mozilla.org/en-US/docs/Web/API/Pointer_Lock_API). These requests always appear to originate from the main frame.
    - `serial` - Read from and write to serial devices with the [Web Serial API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Serial_API).
    - `storage-access` - Allows content loaded in a third-party context to request access to third-party cookies using the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API).
    - `top-level-storage-access` - Allow top-level sites to request third-party cookie access on behalf of embedded content originating from another site in the same related website set using the [Storage Access API](https://developer.mozilla.org/en-US/docs/Web/API/Storage_Access_API).
    - `usb` - Expose non-standard Universal Serial Bus (USB) compatible devices services to the web with the [WebUSB API](https://developer.mozilla.org/en-US/docs/Web/API/WebUSB_API).
    - `deprecated-sync-clipboard-read` *Deprecated* - Request access to run `document.execCommand("paste")`
    - `fileSystem` - Access to read, write, and file management capabilities using the [File System API](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API).
  - `requestingOrigin` string - The origin URL of the permission check
  - `details` Object - Some properties are only available on certain permission types.
    - `embeddingOrigin` string (optional) - The origin of the frame embedding the frame that made the permission check. Only set for cross-origin sub frames making permission checks.
    - `securityOrigin` string (optional) - The security origin of the `media` check.
    - `mediaType` string (optional) - The type of media access being requested, can be `video`, `audio` or `unknown`.
    - `requestingUrl` string (optional) - The last URL the requesting frame loaded. This is not provided for cross-origin sub frames making permission checks.
    - `isMainFrame` boolean - Whether the frame making the request is the main frame.
    - `filePath` string (optional) - The path of a `fileSystem` request.
    - `isDirectory` boolean (optional) - Whether a `fileSystem` request is a directory.
    - `fileAccessType` string (optional) - The access type of a `fileSystem` request. Can be `writable` or `readable`.

Sets the handler which can be used to respond to permission checks for the `session`. Returning `true` will allow the permission and `false` will reject it. Please note that you must also implement `setPermissionRequestHandler` to get complete permission handling. Most web APIs do a permission check and then make a permission request if the check is denied. To clear the handler, call `setPermissionCheckHandler(null)`.

``` 
const  = require('electron')

const url = require('node:url')

session.fromPartition('some-partition').setPermissionCheckHandler((webContents, permission, requestingOrigin) => 

  return false // denied
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

`isMainFrame` will always be `false` for a `fileSystem` request as a result of Chromium limitations.

#### `ses.setDisplayMediaRequestHandler(handler[, opts])`[â€‹](#sessetdisplaymediarequesthandlerhandler-opts "Direct link to sessetdisplaymediarequesthandlerhandler-opts") 

- `handler` Function \| null
  - `request` Object
    - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - Frame that is requesting access to media. May be `null` if accessed after the frame has either navigated or been destroyed.
    - `securityOrigin` String - Origin of the page making the request.
    - `videoRequested` Boolean - true if the web content requested a video stream.
    - `audioRequested` Boolean - true if the web content requested an audio stream.
    - `userGesture` Boolean - Whether a user gesture was active when this request was triggered.
  - `callback` Function
    - `streams` Object
      - `video` Object \| [WebFrameMain](/docs/latest/api/web-frame-main) (optional)
        - `id` String - The id of the stream being granted. This will usually come from a [DesktopCapturerSource](/docs/latest/api/structures/desktop-capturer-source) object.
        - `name` String - The name of the stream being granted. This will usually come from a [DesktopCapturerSource](/docs/latest/api/structures/desktop-capturer-source) object.
      - `audio` String \| [WebFrameMain](/docs/latest/api/web-frame-main) (optional) - If a string is specified, can be `loopback` or `loopbackWithMute`. Specifying a loopback device will capture system audio, and is currently only supported on Windows. If a WebFrameMain is specified, will capture audio from that frame.
      - `enableLocalEcho` Boolean (optional) - If `audio` is a [WebFrameMain](/docs/latest/api/web-frame-main) and this is set to `true`, then local playback of audio will not be muted (e.g. using `MediaRecorder` to record `WebFrameMain` with this flag set to `true` will allow audio to pass through to the speakers while recording). Default is `false`.
- `opts` Object (optional) *macOS* *Experimental*
  - `useSystemPicker` Boolean - true if the available native system picker should be used. Default is `false`. *macOS* *Experimental*

This handler will be called when web content requests access to display media via the `navigator.mediaDevices.getDisplayMedia` API. Use the [desktopCapturer](/docs/latest/api/desktop-capturer) API to choose which stream(s) to grant access to.

`useSystemPicker` allows an application to use the system picker instead of providing a specific video source from `getSources`. This option is experimental, and currently available for MacOS 15+ only. If the system picker is available and `useSystemPicker` is set to `true`, the handler will not be invoked.

``` 
const  = require('electron')

session.defaultSession.setDisplayMediaRequestHandler((request, callback) => ).then((sources) => )
  })
  // Use the system picker if available.
  // Note: this is currently experimental. If the system picker
  // is available, it will be used and the media request handler
  // will not be invoked.
}, )
```

Passing a [WebFrameMain](/docs/latest/api/web-frame-main) object as a video or audio stream will capture the video or audio stream from that frame.

``` 
const  = require('electron')

session.defaultSession.setDisplayMediaRequestHandler((request, callback) => )
})
```

Passing `null` instead of a function resets the handler to its default state.

#### `ses.setDevicePermissionHandler(handler)`[â€‹](#sessetdevicepermissionhandlerhandler "Direct link to sessetdevicepermissionhandlerhandler") 

- `handler` Function\<boolean\> \| null
  - `details` Object
    - `deviceType` string - The type of device that permission is being requested on, can be `hid`, `serial`, or `usb`.
    - `origin` string - The origin URL of the device permission check.
    - `device` [HIDDevice](/docs/latest/api/structures/hid-device) \| [SerialPort](/docs/latest/api/structures/serial-port) \| [USBDevice](/docs/latest/api/structures/usb-device) - the device that permission is being requested for.

Sets the handler which can be used to respond to device permission checks for the `session`. Returning `true` will allow the device to be permitted and `false` will reject it. To clear the handler, call `setDevicePermissionHandler(null)`. This handler can be used to provide default permissioning to devices without first calling for permission to devices (eg via `navigator.hid.requestDevice`). If this handler is not defined, the default device permissions as granted through device selection (eg via `navigator.hid.requestDevice`) will be used. Additionally, the default behavior of Electron is to store granted device permission in memory. If longer term storage is needed, a developer can store granted device permissions (eg when handling the `select-hid-device` event) and then read from that storage with `setDevicePermissionHandler`.

``` 
const  = require('electron')

let win = null

app.whenReady().then(() =>  else if (permission === 'serial')  else if (permission === 'usb') 
    return false
  })

  // Optionally, retrieve previously persisted devices from a persistent store
  const grantedDevices = fetchGrantedDevices()

  win.webContents.session.setDevicePermissionHandler((details) => 

      // Search through the list of devices that have previously been granted permission
      return grantedDevices.some((grantedDevice) => )
    } else if (details.deviceType === 'serial') 
    }
    return false
  })

  win.webContents.session.on('select-hid-device', (event, details, callback) => )
    callback(selectedDevice?.deviceId)
  })
})
```

#### `ses.setUSBProtectedClassesHandler(handler)`[â€‹](#sessetusbprotectedclasseshandlerhandler "Direct link to sessetusbprotectedclasseshandlerhandler") 

- `handler` Function\<string\[\]\> \| null
  - `details` Object
    - `protectedClasses` string\[\] - The current list of protected USB classes. Possible class values include:
      - `audio`
      - `audio-video`
      - `hid`
      - `mass-storage`
      - `smart-card`
      - `video`
      - `wireless`

Sets the handler which can be used to override which [USB classes are protected](https://wicg.github.io/webusb/#usbinterface-interface). The return value for the handler is a string array of USB classes which should be considered protected (eg not available in the renderer). Valid values for the array are:

- `audio`
- `audio-video`
- `hid`
- `mass-storage`
- `smart-card`
- `video`
- `wireless`

Returning an empty string array from the handler will allow all USB classes; returning the passed in array will maintain the default list of protected USB classes (this is also the default behavior if a handler is not defined). To clear the handler, call `setUSBProtectedClassesHandler(null)`.

``` 
const  = require('electron')

let win = null

app.whenReady().then(() => )
  })
})
```

#### `ses.setBluetoothPairingHandler(handler)` *Windows* *Linux*[â€‹](#sessetbluetoothpairinghandlerhandler-windows-linux "Direct link to sessetbluetoothpairinghandlerhandler-windows-linux") 

- `handler` Function \| null
  - `details` Object
    - `deviceId` string
    - `pairingKind` string - The type of pairing prompt being requested. One of the following values:
      - `confirm` This prompt is requesting confirmation that the Bluetooth device should be paired.
      - `confirmPin` This prompt is requesting confirmation that the provided PIN matches the pin displayed on the device.
      - `providePin` This prompt is requesting that a pin be provided for the device.
    - `frame` [WebFrameMain](/docs/latest/api/web-frame-main) \| null - The frame initiating this handler. May be `null` if accessed after the frame has either navigated or been destroyed.
    - `pin` string (optional) - The pin value to verify if `pairingKind` is `confirmPin`.
  - `callback` Function
    - `response` Object
      - `confirmed` boolean - `false` should be passed in if the dialog is canceled. If the `pairingKind` is `confirm` or `confirmPin`, this value should indicate if the pairing is confirmed. If the `pairingKind` is `providePin` the value should be `true` when a value is provided.
      - `pin` string \| null (optional) - When the `pairingKind` is `providePin` this value should be the required pin for the Bluetooth device.

Sets a handler to respond to Bluetooth pairing requests. This handler allows developers to handle devices that require additional validation before pairing. When a handler is not defined, any pairing on Linux or Windows that requires additional validation will be automatically cancelled. macOS does not require a handler because macOS handles the pairing automatically. To clear the handler, call `setBluetoothPairingHandler(null)`.

``` 
const  = require('electron')

const path = require('node:path')

function createWindow () 
  })

  mainWindow.webContents.session.setBluetoothPairingHandler((details, callback) => )

  // Listen for an IPC message from the renderer to get the response for the Bluetooth pairing.
  mainWindow.webContents.ipc.on('bluetooth-pairing-response', (event, response) => )
}

app.whenReady().then(() => )
```

#### `ses.clearHostResolverCache()`[â€‹](#sesclearhostresolvercache "Direct link to sesclearhostresolvercache") 

Returns `Promise<void>` - Resolves when the operation is complete.

Clears the host resolver cache.

#### `ses.allowNTLMCredentialsForDomains(domains)`[â€‹](#sesallowntlmcredentialsfordomainsdomains "Direct link to sesallowntlmcredentialsfordomainsdomains") 

- `domains` string - A comma-separated list of servers for which integrated authentication is enabled.

Dynamically sets whether to always send credentials for HTTP NTLM or Negotiate authentication.

``` 
const  = require('electron')
// consider any url ending with `example.com`, `foobar.com`, `baz`
// for integrated authentication.
session.defaultSession.allowNTLMCredentialsForDomains('*example.com, *foobar.com, *baz')

// consider all urls for integrated authentication.
session.defaultSession.allowNTLMCredentialsForDomains('*')
```

#### `ses.setUserAgent(userAgent[, acceptLanguages])`[â€‹](#sessetuseragentuseragent-acceptlanguages "Direct link to sessetuseragentuseragent-acceptlanguages") 

- `userAgent` string
- `acceptLanguages` string (optional)

Overrides the `userAgent` and `acceptLanguages` for this session.

The `acceptLanguages` must a comma separated ordered list of language codes, for example `"en-US,fr,de,ko,zh-CN,ja"`.

This doesn\'t affect existing `WebContents`, and each `WebContents` can use `webContents.setUserAgent` to override the session-wide user agent.

#### `ses.isPersistent()`[â€‹](#sesispersistent "Direct link to sesispersistent") 

Returns `boolean` - Whether or not this session is a persistent one. The default `webContents` session of a `BrowserWindow` is persistent. When creating a session from a partition, session prefixed with `persist:` will be persistent, while others will be temporary.

#### `ses.getUserAgent()`[â€‹](#sesgetuseragent "Direct link to sesgetuseragent") 

Returns `string` - The user agent for this session.

#### `ses.setSSLConfig(config)`[â€‹](#sessetsslconfigconfig "Direct link to sessetsslconfigconfig") 

- `config` Object
  - `minVersion` string (optional) - Can be `tls1`, `tls1.1`, `tls1.2` or `tls1.3`. The minimum SSL version to allow when connecting to remote servers. Defaults to `tls1`.
  - `maxVersion` string (optional) - Can be `tls1.2` or `tls1.3`. The maximum SSL version to allow when connecting to remote servers. Defaults to `tls1.3`.
  - `disabledCipherSuites` Integer\[\] (optional) - List of cipher suites which should be explicitly prevented from being used in addition to those disabled by the net built-in policy. Supported literal forms: 0xAABB, where AA is `cipher_suite[0]` and BB is `cipher_suite[1]`, as defined in RFC 2246, Section 7.4.1.2. Unrecognized but parsable cipher suites in this form will not return an error. Ex: To disable TLS_RSA_WITH_RC4_128_MD5, specify 0x0004, while to disable TLS_ECDH_ECDSA_WITH_RC4_128_SHA, specify 0xC002. Note that TLSv1.3 ciphers cannot be disabled using this mechanism.

Sets the SSL configuration for the session. All subsequent network requests will use the new configuration. Existing network connections (such as WebSocket connections) will not be terminated, but old sockets in the pool will not be reused for new connections.

#### `ses.getBlobData(identifier)`[â€‹](#sesgetblobdataidentifier "Direct link to sesgetblobdataidentifier") 

- `identifier` string - Valid UUID.

Returns `Promise<Buffer>` - resolves with blob data.

#### `ses.downloadURL(url[, options])`[â€‹](#sesdownloadurlurl-options "Direct link to sesdownloadurlurl-options") 

- `url` string
- `options` Object (optional)
  - `headers` Record\<string, string\> (optional) - HTTP request headers.

Initiates a download of the resource at `url`. The API will generate a [DownloadItem](/docs/latest/api/download-item) that can be accessed with the [will-download](#event-will-download) event.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This does not perform any security checks that relate to a page\'s origin, unlike [`webContents.downloadURL`](/docs/latest/api/web-contents#contentsdownloadurlurl-options).

#### `ses.createInterruptedDownload(options)`[â€‹](#sescreateinterrupteddownloadoptions "Direct link to sescreateinterrupteddownloadoptions") 

- `options` Object
  - `path` string - Absolute path of the download.
  - `urlChain` string\[\] - Complete URL chain for the download.
  - `mimeType` string (optional)
  - `offset` Integer - Start range for the download.
  - `length` Integer - Total length of the download.
  - `lastModified` string (optional) - Last-Modified header value.
  - `eTag` string (optional) - ETag header value.
  - `startTime` Double (optional) - Time when download was started in number of seconds since UNIX epoch.

Allows resuming `cancelled` or `interrupted` downloads from previous `Session`. The API will generate a [DownloadItem](/docs/latest/api/download-item) that can be accessed with the [will-download](#event-will-download) event. The [DownloadItem](/docs/latest/api/download-item) will not have any `WebContents` associated with it and the initial state will be `interrupted`. The download will start only when the `resume` API is called on the [DownloadItem](/docs/latest/api/download-item).

#### `ses.clearAuthCache()`[â€‹](#sesclearauthcache "Direct link to sesclearauthcache") 

Returns `Promise<void>` - resolves when the sessionâ€™s HTTP authentication cache has been cleared.

#### `ses.setPreloads(preloads)` *Deprecated*[â€‹](#sessetpreloadspreloads-deprecated "Direct link to sessetpreloadspreloads-deprecated") 

- `preloads` string\[\] - An array of absolute path to preload scripts

Adds scripts that will be executed on ALL web contents that are associated with this session just before normal `preload` scripts run.

**Deprecated:** Use the new `ses.registerPreloadScript` API.

#### `ses.getPreloads()` *Deprecated*[â€‹](#sesgetpreloads-deprecated "Direct link to sesgetpreloads-deprecated") 

Returns `string[]` an array of paths to preload scripts that have been registered.

**Deprecated:** Use the new `ses.getPreloadScripts` API. This will only return preload script paths for `frame` context types.

#### `ses.registerPreloadScript(script)`[â€‹](#sesregisterpreloadscriptscript "Direct link to sesregisterpreloadscriptscript") 

- `script` [PreloadScriptRegistration](/docs/latest/api/structures/preload-script-registration) - Preload script

Registers preload script that will be executed in its associated context type in this session. For `frame` contexts, this will run prior to any preload defined in the web preferences of a WebContents.

Returns `string` - The ID of the registered preload script.

#### `ses.unregisterPreloadScript(id)`[â€‹](#sesunregisterpreloadscriptid "Direct link to sesunregisterpreloadscriptid") 

- `id` string - Preload script ID

Unregisters script.

#### `ses.getPreloadScripts()`[â€‹](#sesgetpreloadscripts "Direct link to sesgetpreloadscripts") 

Returns [PreloadScript\[\]](/docs/latest/api/structures/preload-script): An array of paths to preload scripts that have been registered.

#### `ses.setCodeCachePath(path)`[â€‹](#sessetcodecachepathpath "Direct link to sessetcodecachepathpath") 

- `path` String - Absolute path to store the v8 generated JS code cache from the renderer.

Sets the directory to store the generated JS [code cache](https://v8.dev/blog/code-caching-for-devs) for this session. The directory is not required to be created by the user before this call, the runtime will create if it does not exist otherwise will use the existing directory. If directory cannot be created, then code cache will not be used and all operations related to code cache will fail silently inside the runtime. By default, the directory will be `Code Cache` under the respective user data folder.

Note that by default code cache is only enabled for http(s) URLs, to enable code cache for custom protocols, `codeCache: true` and `standard: true` must be specified when registering the protocol.

#### `ses.clearCodeCaches(options)`[â€‹](#sesclearcodecachesoptions "Direct link to sesclearcodecachesoptions") 

- `options` Object
  - `urls` String\[\] (optional) - An array of url corresponding to the resource whose generated code cache needs to be removed. If the list is empty then all entries in the cache directory will be removed.

Returns `Promise<void>` - resolves when the code cache clear operation is complete.

#### `ses.getSharedDictionaryUsageInfo()`[â€‹](#sesgetshareddictionaryusageinfo "Direct link to sesgetshareddictionaryusageinfo") 

Returns `Promise<SharedDictionaryUsageInfo[]>` - an array of shared dictionary information entries in Chromium\'s networking service\'s storage.

Shared dictionaries are used to power advanced compression of data sent over the wire, specifically with Brotli and ZStandard. You don\'t need to call any of the shared dictionary APIs in Electron to make use of this advanced web feature, but if you do, they allow deeper control and inspection of the shared dictionaries used during decompression.

To get detailed information about a specific shared dictionary entry, call `getSharedDictionaryInfo(options)`.

#### `ses.getSharedDictionaryInfo(options)`[â€‹](#sesgetshareddictionaryinfooptions "Direct link to sesgetshareddictionaryinfooptions") 

- `options` Object
  - `frameOrigin` string - The origin of the frame where the request originates. Itâ€™s specific to the individual frame making the request and is defined by its scheme, host, and port. In practice, will look like a URL.
  - `topFrameSite` string - The site of the top-level browsing context (the main frame or tab that contains the request). Itâ€™s less granular than `frameOrigin` and focuses on the broader \"site\" scope. In practice, will look like a URL.

Returns `Promise<SharedDictionaryInfo[]>` - an array of shared dictionary information entries in Chromium\'s networking service\'s storage.

To get information about all present shared dictionaries, call `getSharedDictionaryUsageInfo()`.

#### `ses.clearSharedDictionaryCache()`[â€‹](#sesclearshareddictionarycache "Direct link to sesclearshareddictionarycache") 

Returns `Promise<void>` - resolves when the dictionary cache has been cleared, both in memory and on disk.

#### `ses.clearSharedDictionaryCacheForIsolationKey(options)`[â€‹](#sesclearshareddictionarycacheforisolationkeyoptions "Direct link to sesclearshareddictionarycacheforisolationkeyoptions") 

- `options` Object
  - `frameOrigin` string - The origin of the frame where the request originates. Itâ€™s specific to the individual frame making the request and is defined by its scheme, host, and port. In practice, will look like a URL.
  - `topFrameSite` string - The site of the top-level browsing context (the main frame or tab that contains the request). Itâ€™s less granular than `frameOrigin` and focuses on the broader \"site\" scope. In practice, will look like a URL.

Returns `Promise<void>` - resolves when the dictionary cache has been cleared for the specified isolation key, both in memory and on disk.

#### `ses.setSpellCheckerEnabled(enable)`[â€‹](#sessetspellcheckerenabledenable "Direct link to sessetspellcheckerenabledenable") 

- `enable` boolean

Sets whether to enable the builtin spell checker.

#### `ses.isSpellCheckerEnabled()`[â€‹](#sesisspellcheckerenabled "Direct link to sesisspellcheckerenabled") 

Returns `boolean` - Whether the builtin spell checker is enabled.

#### `ses.setSpellCheckerLanguages(languages)`[â€‹](#sessetspellcheckerlanguageslanguages "Direct link to sessetspellcheckerlanguageslanguages") 

- `languages` string\[\] - An array of language codes to enable the spellchecker for.

The built in spellchecker does not automatically detect what language a user is typing in. In order for the spell checker to correctly check their words you must call this API with an array of language codes. You can get the list of supported language codes with the `ses.availableSpellCheckerLanguages` property.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, the OS spellchecker is used and will detect your language automatically. This API is a no-op on macOS.

#### `ses.getSpellCheckerLanguages()`[â€‹](#sesgetspellcheckerlanguages "Direct link to sesgetspellcheckerlanguages") 

Returns `string[]` - An array of language codes the spellchecker is enabled for. If this list is empty the spellchecker will fallback to using `en-US`. By default on launch if this setting is an empty list Electron will try to populate this setting with the current OS locale. This setting is persisted across restarts.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, the OS spellchecker is used and has its own list of languages. On macOS, this API will return whichever languages have been configured by the OS.

#### `ses.setSpellCheckerDictionaryDownloadURL(url)`[â€‹](#sessetspellcheckerdictionarydownloadurlurl "Direct link to sessetspellcheckerdictionarydownloadurlurl") 

- `url` string - A base URL for Electron to download hunspell dictionaries from.

By default Electron will download hunspell dictionaries from the Chromium CDN. If you want to override this behavior you can use this API to point the dictionary downloader at your own hosted version of the hunspell dictionaries. We publish a `hunspell_dictionaries.zip` file with each release which contains the files you need to host here.

The file server must be **case insensitive**. If you cannot do this, you must upload each file twice: once with the case it has in the ZIP file and once with the filename as all lowercase.

If the files present in `hunspell_dictionaries.zip` are available at `https://example.com/dictionaries/language-code.bdic` then you should call this api with `ses.setSpellCheckerDictionaryDownloadURL('https://example.com/dictionaries/')`. Please note the trailing slash. The URL to the dictionaries is formed as `$$`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS, the OS spellchecker is used and therefore we do not download any dictionary files. This API is a no-op on macOS.

#### `ses.listWordsInSpellCheckerDictionary()`[â€‹](#seslistwordsinspellcheckerdictionary "Direct link to seslistwordsinspellcheckerdictionary") 

Returns `Promise<string[]>` - An array of all words in app\'s custom dictionary. Resolves when the full dictionary is loaded from disk.

#### `ses.addWordToSpellCheckerDictionary(word)`[â€‹](#sesaddwordtospellcheckerdictionaryword "Direct link to sesaddwordtospellcheckerdictionaryword") 

- `word` string - The word you want to add to the dictionary

Returns `boolean` - Whether the word was successfully written to the custom dictionary. This API will not work on non-persistent (in-memory) sessions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS and Windows, this word will be written to the OS custom dictionary as well.

#### `ses.removeWordFromSpellCheckerDictionary(word)`[â€‹](#sesremovewordfromspellcheckerdictionaryword "Direct link to sesremovewordfromspellcheckerdictionaryword") 

- `word` string - The word you want to remove from the dictionary

Returns `boolean` - Whether the word was successfully removed from the custom dictionary. This API will not work on non-persistent (in-memory) sessions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

On macOS and Windows, this word will be removed from the OS custom dictionary as well.

#### `ses.loadExtension(path[, options])` *Deprecated*[â€‹](#sesloadextensionpath-options-deprecated "Direct link to sesloadextensionpath-options-deprecated") 

- `path` string - Path to a directory containing an unpacked Chrome extension
- `options` Object (optional)
  - `allowFileAccess` boolean - Whether to allow the extension to read local files over `file://` protocol and inject content scripts into `file://` pages. This is required e.g. for loading devtools extensions on `file://` URLs. Defaults to false.

Returns `Promise<Extension>` - resolves when the extension is loaded.

This method will raise an exception if the extension could not be loaded. If there are warnings when installing the extension (e.g. if the extension requests an API that Electron does not support) then they will be logged to the console.

Note that Electron does not support the full range of Chrome extensions APIs. See [Supported Extensions APIs](/docs/latest/api/extensions#supported-extensions-apis) for more details on what is supported.

Note that in previous versions of Electron, extensions that were loaded would be remembered for future runs of the application. This is no longer the case: `loadExtension` must be called on every boot of your app if you want the extension to be loaded.

``` 
const  = require('electron')

const path = require('node:path')

app.whenReady().then(async () => 
  )
  // Note that in order to use the React DevTools extension, you'll need to
  // download and unzip a copy of the extension.
})
```

This API does not support loading packed (.crx) extensions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API cannot be called before the `ready` event of the `app` module is emitted.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Loading extensions into in-memory (non-persistent) sessions is not supported and will throw an error.

**Deprecated:** Use the new `ses.extensions.loadExtension` API.

#### `ses.removeExtension(extensionId)` *Deprecated*[â€‹](#sesremoveextensionextensionid-deprecated "Direct link to sesremoveextensionextensionid-deprecated") 

- `extensionId` string - ID of extension to remove

Unloads an extension.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API cannot be called before the `ready` event of the `app` module is emitted.

**Deprecated:** Use the new `ses.extensions.removeExtension` API.

#### `ses.getExtension(extensionId)` *Deprecated*[â€‹](#sesgetextensionextensionid-deprecated "Direct link to sesgetextensionextensionid-deprecated") 

- `extensionId` string - ID of extension to query

Returns `Extension | null` - The loaded extension with the given ID.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API cannot be called before the `ready` event of the `app` module is emitted.

**Deprecated:** Use the new `ses.extensions.getExtension` API.

#### `ses.getAllExtensions()` *Deprecated*[â€‹](#sesgetallextensions-deprecated "Direct link to sesgetallextensions-deprecated") 

Returns `Extension[]` - A list of all loaded extensions.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This API cannot be called before the `ready` event of the `app` module is emitted.

**Deprecated:** Use the new `ses.extensions.getAllExtensions` API.

#### `ses.getStoragePath()`[â€‹](#sesgetstoragepath "Direct link to sesgetstoragepath") 

Returns `string | null` - The absolute file system path where data for this session is persisted on disk. For in memory sessions this returns `null`.

#### `ses.clearData([options])`[â€‹](#sescleardataoptions "Direct link to sescleardataoptions") 

- `options` Object (optional)
  - `dataTypes` String\[\] (optional) - The types of data to clear. By default, this will clear all types of data. This can potentially include data types not explicitly listed here. (See Chromium\'s [`BrowsingDataRemover`](https://source.chromium.org/chromium/chromium/src/+/main:content/public/browser/browsing_data_remover.h) for the full list.)
    - `backgroundFetch` - Background Fetch
    - `cache` - Cache (includes `cachestorage` and `shadercache`)
    - `cookies` - Cookies
    - `downloads` - Downloads
    - `fileSystems` - File Systems
    - `indexedDB` - IndexedDB
    - `localStorage` - Local Storage
    - `serviceWorkers` - Service Workers
    - `webSQL` - WebSQL
  - `origins` String\[\] (optional) - Clear data for only these origins. Cannot be used with `excludeOrigins`.
  - `excludeOrigins` String\[\] (optional) - Clear data for all origins except these ones. Cannot be used with `origins`.
  - `avoidClosingConnections` boolean (optional) - Skips deleting cookies that would close current network connections. (Default: `false`)
  - `originMatchingMode` String (optional) - The behavior for matching data to origins.
    - `third-parties-included` (default) - Storage is matched on origin in first-party contexts and top-level-site in third-party contexts.
    - `origin-in-all-contexts` - Storage is matched on origin only in all contexts.

Returns `Promise<void>` - resolves when all data has been cleared.

Clears various different types of data.

This method clears more types of data and is more thorough than the `clearStorageData` method.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Cookies are stored at a broader scope than origins. When removing cookies and filtering by `origins` (or `excludeOrigins`), the cookies will be removed at the [registrable domain](https://url.spec.whatwg.org/#host-registrable-domain) level. For example, clearing cookies for the origin `https://really.specific.origin.example.com/` will end up clearing all cookies for `example.com`. Clearing cookies for the origin `https://my.website.example.co.uk/` will end up clearing all cookies for `example.co.uk`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

Clearing cache data will also clear the shared dictionary cache. This means that any dictionaries used for compression may be reloaded after clearing the cache. If you wish to clear the shared dictionary cache but leave other cached data intact, you may want to use the `clearSharedDictionaryCache` method.

For more information, refer to Chromium\'s [`BrowsingDataRemover` interface](https://source.chromium.org/chromium/chromium/src/+/main:content/public/browser/browsing_data_remover.h).

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

The following properties are available on instances of `Session`:

#### `ses.availableSpellCheckerLanguages` *Readonly*[â€‹](#sesavailablespellcheckerlanguages-readonly "Direct link to sesavailablespellcheckerlanguages-readonly") 

A `string[]` array which consists of all the known available spell checker languages. Providing a language code to the `setSpellCheckerLanguages` API that isn\'t in this array will result in an error.

#### `ses.spellCheckerEnabled`[â€‹](#sesspellcheckerenabled "Direct link to sesspellcheckerenabled") 

A `boolean` indicating whether builtin spell checker is enabled.

#### `ses.storagePath` *Readonly*[â€‹](#sesstoragepath-readonly "Direct link to sesstoragepath-readonly") 

A `string | null` indicating the absolute file system path where data for this session is persisted on disk. For in memory sessions this returns `null`.

#### `ses.cookies` *Readonly*[â€‹](#sescookies-readonly "Direct link to sescookies-readonly") 

A [`Cookies`](/docs/latest/api/cookies) object for this session.

#### `ses.extensions` *Readonly*[â€‹](#sesextensions-readonly "Direct link to sesextensions-readonly") 

A [`Extensions`](/docs/latest/api/extensions-api) object for this session.

#### `ses.serviceWorkers` *Readonly*[â€‹](#sesserviceworkers-readonly "Direct link to sesserviceworkers-readonly") 

A [`ServiceWorkers`](/docs/latest/api/service-workers) object for this session.

#### `ses.webRequest` *Readonly*[â€‹](#seswebrequest-readonly "Direct link to seswebrequest-readonly") 

A [`WebRequest`](/docs/latest/api/web-request) object for this session.

#### `ses.protocol` *Readonly*[â€‹](#sesprotocol-readonly "Direct link to sesprotocol-readonly") 

A [`Protocol`](/docs/latest/api/protocol) object for this session.

``` 
const  = require('electron')

const path = require('node:path')

app.whenReady().then(() => )
  })) 
})
```

#### `ses.netLog` *Readonly*[â€‹](#sesnetlog-readonly "Direct link to sesnetlog-readonly") 

A [`NetLog`](/docs/latest/api/net-log) object for this session.

``` 
const  = require('electron')

app.whenReady().then(async () => )
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/session.md)