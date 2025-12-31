# Source: https://playwright.dev/docs/api/class-mouse

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [API reference]
-   [Classes]
-   [Mouse]

On this page

<div>

# Mouse

</div>

The Mouse class operates in main-frame CSS pixels relative to the top-left corner of the viewport.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

If you want to debug where the mouse moved, you can use the [Trace viewer](/docs/trace-viewer-intro) or [Playwright Inspector](/docs/running-tests). A red dot showing the location of the mouse will be shown for every mouse action.

Every `page` object has its own Mouse, accessible with [page.mouse](/docs/api/class-page#page-mouse).

``` 
// Using ‘page.mouse’ to trace a 100x100 square.
await page.mouse.move(0, 0);
await page.mouse.down();
await page.mouse.move(0, 100);
await page.mouse.move(100, 100);
await page.mouse.move(100, 0);
await page.mouse.move(0, 0);
await page.mouse.up();
```

------------------------------------------------------------------------

## Methods[​](#methods "Direct link to Methods") 

### click[​](#mouse-click "Direct link to click") 

Added before v1.9 mouse.click

Shortcut for [mouse.move()](/docs/api/class-mouse#mouse-move), [mouse.down()](/docs/api/class-mouse#mouse-down), [mouse.up()](/docs/api/class-mouse#mouse-up).

**Usage**

``` 
await mouse.click(x, y);
await mouse.click(x, y, options);
```

**Arguments**

-   `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-click-option-x)

    X coordinate relative to the main frame\'s viewport in CSS pixels.

-   `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-click-option-y)

    Y coordinate relative to the main frame\'s viewport in CSS pixels.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `button` \"left\" \| \"right\" \| \"middle\" *(optional)*[][\#](#mouse-click-option-button)

        Defaults to `left`.

    -   `clickCount` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-click-option-click-count)

        defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").

    -   `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-click-option-delay)

        Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-click-return)

------------------------------------------------------------------------

### dblclick[​](#mouse-dblclick "Direct link to dblclick") 

Added before v1.9 mouse.dblclick

Shortcut for [mouse.move()](/docs/api/class-mouse#mouse-move), [mouse.down()](/docs/api/class-mouse#mouse-down), [mouse.up()](/docs/api/class-mouse#mouse-up), [mouse.down()](/docs/api/class-mouse#mouse-down) and [mouse.up()](/docs/api/class-mouse#mouse-up).

**Usage**

``` 
await mouse.dblclick(x, y);
await mouse.dblclick(x, y, options);
```

**Arguments**

-   `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-dblclick-option-x)

    X coordinate relative to the main frame\'s viewport in CSS pixels.

-   `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-dblclick-option-y)

    Y coordinate relative to the main frame\'s viewport in CSS pixels.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `button` \"left\" \| \"right\" \| \"middle\" *(optional)*[][\#](#mouse-dblclick-option-button)

        Defaults to `left`.

    -   `delay` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-dblclick-option-delay)

        Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-dblclick-return)

------------------------------------------------------------------------

### down[​](#mouse-down "Direct link to down") 

Added before v1.9 mouse.down

Dispatches a `mousedown` event.

**Usage**

``` 
await mouse.down();
await mouse.down(options);
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `button` \"left\" \| \"right\" \| \"middle\" *(optional)*[][\#](#mouse-down-option-button)

        Defaults to `left`.

    -   `clickCount` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-down-option-click-count)

        defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-down-return)

------------------------------------------------------------------------

### move[​](#mouse-move "Direct link to move") 

Added before v1.9 mouse.move

Dispatches a `mousemove` event.

**Usage**

``` 
await mouse.move(x, y);
await mouse.move(x, y, options);
```

**Arguments**

-   `x` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-move-option-x)

    X coordinate relative to the main frame\'s viewport in CSS pixels.

-   `y` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-move-option-y)

    Y coordinate relative to the main frame\'s viewport in CSS pixels.

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*

    -   `steps` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-move-option-steps)

        Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright\'s current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-move-return)

------------------------------------------------------------------------

### up[​](#mouse-up "Direct link to up") 

Added before v1.9 mouse.up

Dispatches a `mouseup` event.

**Usage**

``` 
await mouse.up();
await mouse.up(options);
```

**Arguments**

-   `options` [Object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object "Object") *(optional)*
    -   `button` \"left\" \| \"right\" \| \"middle\" *(optional)*[][\#](#mouse-up-option-button)

        Defaults to `left`.

    -   `clickCount` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number") *(optional)*[][\#](#mouse-up-option-click-count)

        defaults to 1. See [UIEvent.detail](https://developer.mozilla.org/en-US/docs/Web/API/UIEvent/detail "UIEvent.detail").

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-up-return)

------------------------------------------------------------------------

### wheel[​](#mouse-wheel "Direct link to wheel") 

Added in: v1.15 mouse.wheel

Dispatches a `wheel` event. This method is usually used to manually scroll the page. See [scrolling](/docs/input#scrolling) for alternative ways to scroll.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

Wheel events may cause scrolling if they are not handled, and this method does not wait for the scrolling to finish before returning.

**Usage**

``` 
await mouse.wheel(deltaX, deltaY);
```

**Arguments**

-   `deltaX` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-wheel-option-delta-x)

    Pixels to scroll horizontally.

-   `deltaY` [number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#Number_type "Number")[][\#](#mouse-wheel-option-delta-y)

    Pixels to scroll vertically.

**Returns**

-   [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise "Promise")\<[void](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined "void")\>[][\#](#mouse-wheel-return)