# Source: https://www.electronjs.org/docs/latest/api/process

On this page

# process

> Extensions to process object.

Process: [Main](/docs/latest/glossary#main-process), [Renderer](/docs/latest/glossary#renderer-process)

Electron\'s `process` object is extended from the [Node.js `process` object](https://nodejs.org/api/process.html). It adds the following events, properties, and methods:

## Sandbox[â€‹](#sandbox "Direct link to Sandbox") 

In sandboxed renderers the `process` object contains only a subset of the APIs:

- `crash()`
- `hang()`
- `getCreationTime()`
- `getHeapStatistics()`
- `getBlinkMemoryInfo()`
- `getProcessMemoryInfo()`
- `getSystemMemoryInfo()`
- `getSystemVersion()`
- `getCPUUsage()`
- `uptime()`
- `argv`
- `execPath`
- `env`
- `pid`
- `arch`
- `platform`
- `sandboxed`
- `contextIsolated`
- `type`
- `version`
- `versions`
- `mas`
- `windowsStore`
- `contextId`

## Events[â€‹](#events "Direct link to Events") 

### Event: \'loaded\'[â€‹](#event-loaded "Direct link to Event: 'loaded'") 

Emitted when Electron has loaded its internal initialization script and is beginning to load the web page or the main script.

## Properties[â€‹](#properties "Direct link to Properties") 

### `process.defaultApp` *Readonly*[â€‹](#processdefaultapp-readonly "Direct link to processdefaultapp-readonly") 

A `boolean`. When the app is started by being passed as parameter to the default Electron executable, this property is `true` in the main process, otherwise it is `undefined`. For example when running the app with `electron .`, it is `true`, even if the app is packaged ([`isPackaged`](/docs/latest/api/app#appispackaged-readonly)) is `true`. This can be useful to determine how many arguments will need to be sliced off from `process.argv`.

### `process.isMainFrame` *Readonly*[â€‹](#processismainframe-readonly "Direct link to processismainframe-readonly") 

A `boolean`, `true` when the current renderer context is the \"main\" renderer frame. If you want the ID of the current frame you should use `webFrame.routingId`.

### `process.mas` *Readonly*[â€‹](#processmas-readonly "Direct link to processmas-readonly") 

A `boolean`. For Mac App Store build, this property is `true`, for other builds it is `undefined`.

### `process.noAsar`[â€‹](#processnoasar "Direct link to processnoasar") 

A `boolean` that controls ASAR support inside your application. Setting this to `true` will disable the support for `asar` archives in Node\'s built-in modules.

### `process.noDeprecation`[â€‹](#processnodeprecation "Direct link to processnodeprecation") 

A `boolean` that controls whether or not deprecation warnings are printed to `stderr`. Setting this to `true` will silence deprecation warnings. This property is used instead of the `--no-deprecation` command line flag.

### `process.resourcesPath` *Readonly*[â€‹](#processresourcespath-readonly "Direct link to processresourcespath-readonly") 

A `string` representing the path to the resources directory.

### `process.sandboxed` *Readonly*[â€‹](#processsandboxed-readonly "Direct link to processsandboxed-readonly") 

A `boolean`. When the renderer process is sandboxed, this property is `true`, otherwise it is `undefined`.

### `process.contextIsolated` *Readonly*[â€‹](#processcontextisolated-readonly "Direct link to processcontextisolated-readonly") 

A `boolean` that indicates whether the current renderer context has `contextIsolation` enabled. It is `undefined` in the main process.

### `process.throwDeprecation`[â€‹](#processthrowdeprecation "Direct link to processthrowdeprecation") 

A `boolean` that controls whether or not deprecation warnings will be thrown as exceptions. Setting this to `true` will throw errors for deprecations. This property is used instead of the `--throw-deprecation` command line flag.

### `process.traceDeprecation`[â€‹](#processtracedeprecation "Direct link to processtracedeprecation") 

A `boolean` that controls whether or not deprecations printed to `stderr` include their stack trace. Setting this to `true` will print stack traces for deprecations. This property is instead of the `--trace-deprecation` command line flag.

### `process.traceProcessWarnings`[â€‹](#processtraceprocesswarnings "Direct link to processtraceprocesswarnings") 

A `boolean` that controls whether or not process warnings printed to `stderr` include their stack trace. Setting this to `true` will print stack traces for process warnings (including deprecations). This property is instead of the `--trace-warnings` command line flag.

### `process.type` *Readonly*[â€‹](#processtype-readonly "Direct link to processtype-readonly") 

A `string` representing the current process\'s type, can be:

- `browser` - The main process
- `renderer` - A renderer process
- `service-worker` - In a service worker
- `worker` - In a web worker
- `utility` - In a node process launched as a service

### `process.versions.chrome` *Readonly*[â€‹](#processversionschrome-readonly "Direct link to processversionschrome-readonly") 

A `string` representing Chrome\'s version string.

### `process.versions.electron` *Readonly*[â€‹](#processversionselectron-readonly "Direct link to processversionselectron-readonly") 

A `string` representing Electron\'s version string.

### `process.windowsStore` *Readonly*[â€‹](#processwindowsstore-readonly "Direct link to processwindowsstore-readonly") 

A `boolean`. If the app is running as a Windows Store app (appx), this property is `true`, for otherwise it is `undefined`.

### `process.contextId` *Readonly*[â€‹](#processcontextid-readonly "Direct link to processcontextid-readonly") 

A `string` (optional) representing a globally unique ID of the current JavaScript context. Each frame has its own JavaScript context. When contextIsolation is enabled, the isolated world also has a separate JavaScript context. This property is only available in the renderer process.

### `process.parentPort`[â€‹](#processparentport "Direct link to processparentport") 

A [`Electron.ParentPort`](/docs/latest/api/parent-port) property if this is a [`UtilityProcess`](/docs/latest/api/utility-process) (or `null` otherwise) allowing communication with the parent process.

## Methods[â€‹](#methods "Direct link to Methods") 

The `process` object has the following methods:

### `process.crash()`[â€‹](#processcrash "Direct link to processcrash") 

Causes the main thread of the current process crash.

### `process.getCreationTime()`[â€‹](#processgetcreationtime "Direct link to processgetcreationtime") 

Returns `number | null` - The number of milliseconds since epoch, or `null` if the information is unavailable

Indicates the creation time of the application. The time is represented as number of milliseconds since epoch. It returns null if it is unable to get the process creation time.

### `process.getCPUUsage()`[â€‹](#processgetcpuusage "Direct link to processgetcpuusage") 

Returns [CPUUsage](/docs/latest/api/structures/cpu-usage)

### `process.getHeapStatistics()`[â€‹](#processgetheapstatistics "Direct link to processgetheapstatistics") 

Returns `Object`:

- `totalHeapSize` Integer
- `totalHeapSizeExecutable` Integer
- `totalPhysicalSize` Integer
- `totalAvailableSize` Integer
- `usedHeapSize` Integer
- `heapSizeLimit` Integer
- `mallocedMemory` Integer
- `peakMallocedMemory` Integer
- `doesZapGarbage` boolean

Returns an object with V8 heap statistics. Note that all statistics are reported in Kilobytes.

### `process.getBlinkMemoryInfo()`[â€‹](#processgetblinkmemoryinfo "Direct link to processgetblinkmemoryinfo") 

Returns `Object`:

- `allocated` Integer - Size of all allocated objects in Kilobytes.
- `total` Integer - Total allocated space in Kilobytes.

Returns an object with Blink memory information. It can be useful for debugging rendering / DOM related memory issues. Note that all values are reported in Kilobytes.

### `process.getProcessMemoryInfo()`[â€‹](#processgetprocessmemoryinfo "Direct link to processgetprocessmemoryinfo") 

Returns `Promise<ProcessMemoryInfo>` - Resolves with a [ProcessMemoryInfo](/docs/latest/api/structures/process-memory-info)

Returns an object giving memory usage statistics about the current process. Note that all statistics are reported in Kilobytes. This api should be called after app ready.

Chromium does not provide `residentSet` value for macOS. This is because macOS performs in-memory compression of pages that haven\'t been recently used. As a result the resident set size value is not what one would expect. `private` memory is more representative of the actual pre-compression memory usage of the process on macOS.

### `process.getSystemMemoryInfo()`[â€‹](#processgetsystemmemoryinfo "Direct link to processgetsystemmemoryinfo") 

Returns `Object`:

- `total` Integer - The total amount of physical memory in Kilobytes available to the system.
- `free` Integer - The total amount of memory not being used by applications or disk cache.
- `fileBacked` Integer *macOS* - The amount of memory that currently has been paged out to storage. Includes memory for file caches, network buffers, and other system services.
- `purgeable` Integer *macOS* - The amount of memory that is marked as \"purgeable\". The system can reclaim it if memory pressure increases.
- `swapTotal` Integer *Windows* *Linux* - The total amount of swap memory in Kilobytes available to the system.
- `swapFree` Integer *Windows* *Linux* - The free amount of swap memory in Kilobytes available to the system.

Returns an object giving memory usage statistics about the entire system. Note that all statistics are reported in Kilobytes.

### `process.getSystemVersion()`[â€‹](#processgetsystemversion "Direct link to processgetsystemversion") 

Returns `string` - The version of the host operating system.

Example:

``` 
const version = process.getSystemVersion()
console.log(version)
// On macOS -> '10.13.6'
// On Windows -> '10.0.17763'
// On Linux -> '4.15.0-45-generic'
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

It returns the actual operating system version instead of kernel version on macOS unlike `os.release()`.

### `process.takeHeapSnapshot(filePath)`[â€‹](#processtakeheapsnapshotfilepath "Direct link to processtakeheapsnapshotfilepath") 

- `filePath` string - Path to the output file.

Returns `boolean` - Indicates whether the snapshot has been created successfully.

Takes a V8 heap snapshot and saves it to `filePath`.

### `process.hang()`[â€‹](#processhang "Direct link to processhang") 

Causes the main thread of the current process hang.

### `process.setFdLimit(maxDescriptors)` *macOS* *Linux*[â€‹](#processsetfdlimitmaxdescriptors-macos-linux "Direct link to processsetfdlimitmaxdescriptors-macos-linux") 

- `maxDescriptors` Integer

Sets the file descriptor soft limit to `maxDescriptors` or the OS hard limit, whichever is lower for the current process.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/process.md)