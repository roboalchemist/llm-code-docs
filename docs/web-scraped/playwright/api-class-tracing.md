# Source: https://playwright.dev/docs/api/class-tracing

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Tracing]

On this page

<div>

# Tracing

</div>

API for collecting and saving Playwright traces. Playwright traces can be opened in [Trace Viewer](/docs/trace-viewer) after Playwright script runs.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

You probably want to [enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead of using `context.tracing`.

The `context.tracing` API captures browser operations and network activity, but it doesn\'t record test assertions (like `expect` calls). We recommend [enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace), which includes those assertions and provides a more complete trace for debugging test failures.

Start recording a trace before performing actions. At the end, stop tracing and save it to a file.

``` 
const browser = await chromium.launch();
const context = await browser.newContext();
await context.tracing.start();
const page = await context.newPage();
await page.goto('https://playwright.dev');
expect(page.url()).toBe('https://playwright.dev');
await context.tracing.stop();
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### group[​](#tracing-group "Direct link to group") 

Added in: v1.49 tracing.group

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

Use `test.step` instead when available.

Creates a new group within the trace, assigning any subsequent API calls to this group, until [tracing.groupEnd()](/docs/api/class-tracing#tracing-group-end) is called. Groups can be nested and will be visible in the trace viewer.

**Usage**

``` 
// use test.step instead
await test.step('Log in', async () => );
```

**Arguments**

-   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")[][\#](#tracing-group-option-name)

    Group name shown in the trace viewer.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `location` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*[][\#](#tracing-group-option-location)

        -   `file` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string")

        -   `line` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*

        -   `column` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*

        Specifies a custom location for the group to be shown in the trace viewer. Defaults to the location of the [tracing.group()](/docs/api/class-tracing#tracing-group) call.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-group-return)

------------------------------------------------------------------------

### groupEnd[​](#tracing-group-end "Direct link to groupEnd") 

Added in: v1.49 tracing.groupEnd

Closes the last group created by [tracing.group()](/docs/api/class-tracing#tracing-group).

**Usage**

``` 
await tracing.groupEnd();
```

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-group-end-return)

------------------------------------------------------------------------

### start[​](#tracing-start "Direct link to start") 

Added in: v1.12 tracing.start

Start tracing.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

You probably want to [enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead of using `Tracing.start`.

The `context.tracing` API captures browser operations and network activity, but it doesn\'t record test assertions (like `expect` calls). We recommend [enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace), which includes those assertions and provides a more complete trace for debugging test failures.

**Usage**

``` 
await context.tracing.start();
const page = await context.newPage();
await page.goto('https://playwright.dev');
expect(page.url()).toBe('https://playwright.dev');
await context.tracing.stop();
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#tracing-start-option-name)

        If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the [tracesDir](/docs/api/class-browsertype#browser-type-launch-option-traces-dir) directory specified in [browserType.launch()](/docs/api/class-browsertype#browser-type-launch). To specify the final trace zip file name, you need to pass `path` option to [tracing.stop()](/docs/api/class-tracing#tracing-stop) instead.

    -   `screenshots` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*[][\#](#tracing-start-option-screenshots)

        Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview.

    -   `snapshots` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)*[][\#](#tracing-start-option-snapshots)

        If this option is true tracing will

        -   capture DOM snapshot on every action
        -   record network activity

    -   `sources` [boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Boolean_type "Boolean") *(optional)* Added in: v1.17[][\#](#tracing-start-option-sources)

        Whether to include source files for trace actions.

    -   `title` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)* Added in: v1.17[][\#](#tracing-start-option-title)

        Trace name to be shown in the Trace Viewer.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-start-return)

------------------------------------------------------------------------

### startChunk[​](#tracing-start-chunk "Direct link to startChunk") 

Added in: v1.15 tracing.startChunk

Start a new trace chunk. If you\'d like to record multiple traces on the same [BrowserContext](/docs/api/class-browsercontext "BrowserContext"), use [tracing.start()](/docs/api/class-tracing#tracing-start) once, and then create multiple trace chunks with [tracing.startChunk()](/docs/api/class-tracing#tracing-start-chunk) and [tracing.stopChunk()](/docs/api/class-tracing#tracing-stop-chunk).

**Usage**

``` 
await context.tracing.start();
const page = await context.newPage();
await page.goto('https://playwright.dev');

await context.tracing.startChunk();
await page.getByText('Get Started').click();
// Everything between startChunk and stopChunk will be recorded in the trace.
await context.tracing.stopChunk();

await context.tracing.startChunk();
await page.goto('http://example.com');
// Save a second trace file with different actions.
await context.tracing.stopChunk();
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `name` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)* Added in: v1.32[][\#](#tracing-start-chunk-option-name)

        If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the [tracesDir](/docs/api/class-browsertype#browser-type-launch-option-traces-dir) directory specified in [browserType.launch()](/docs/api/class-browsertype#browser-type-launch). To specify the final trace zip file name, you need to pass `path` option to [tracing.stopChunk()](/docs/api/class-tracing#tracing-stop-chunk) instead.

    -   `title` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)* Added in: v1.17[][\#](#tracing-start-chunk-option-title)

        Trace name to be shown in the Trace Viewer.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-start-chunk-return)

------------------------------------------------------------------------

### stop[​](#tracing-stop "Direct link to stop") 

Added in: v1.12 tracing.stop

Stop tracing.

**Usage**

``` 
await tracing.stop();
await tracing.stop(options);
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#tracing-stop-option-path)

        Export trace into the file with the given path.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-stop-return)

------------------------------------------------------------------------

### stopChunk[​](#tracing-stop-chunk "Direct link to stopChunk") 

Added in: v1.15 tracing.stopChunk

Stop the trace chunk. See [tracing.startChunk()](/docs/api/class-tracing#tracing-start-chunk) for more details about multiple trace chunks.

**Usage**

``` 
await tracing.stopChunk();
await tracing.stopChunk(options);
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `path` [string](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#String_type "string") *(optional)*[][\#](#tracing-stop-chunk-option-path)

        Export trace collected since the last [tracing.startChunk()](/docs/api/class-tracing#tracing-start-chunk) call into the file with the given path.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#tracing-stop-chunk-return)