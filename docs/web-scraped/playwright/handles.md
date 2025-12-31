# Source: https://playwright.dev/docs/handles

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Handles]

On this page

<div>

# Handles

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright can create handles to the page DOM elements or any other objects inside the page. These handles live in the Playwright process, whereas the actual objects live in the browser. There are two types of handles:

-   [JSHandle](/docs/api/class-jshandle "JSHandle") to reference any JavaScript objects in the page
-   [ElementHandle](/docs/api/class-elementhandle "ElementHandle") to reference DOM elements in the page, it has extra methods that allow performing actions on the elements and asserting their properties.

Since any DOM element in the page is also a JavaScript object, any [ElementHandle](/docs/api/class-elementhandle "ElementHandle") is a [JSHandle](/docs/api/class-jshandle "JSHandle") as well.

Handles are used to perform operations on those actual objects in the page. You can evaluate on a handle, get handle properties, pass handle as an evaluation parameter, serialize page object into JSON etc. See the [JSHandle](/docs/api/class-jshandle "JSHandle") class API for these and methods.

### API reference[​](#api-reference "Direct link to API reference") 

-   [JSHandle](/docs/api/class-jshandle "JSHandle")
-   [ElementHandle](/docs/api/class-elementhandle "ElementHandle")

Here is the easiest way to obtain a [JSHandle](/docs/api/class-jshandle "JSHandle").

``` 
const jsHandle = await page.evaluateHandle('window');
//  Use jsHandle for evaluations.
```

## Element Handles[​](#element-handles "Direct link to Element Handles") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Discouraged

The use of [ElementHandle](/docs/api/class-elementhandle "ElementHandle") is discouraged, use [Locator](/docs/api/class-locator "Locator") objects and web-first assertions instead.

When [ElementHandle](/docs/api/class-elementhandle "ElementHandle") is required, it is recommended to fetch it with the [page.waitForSelector()](/docs/api/class-page#page-wait-for-selector) or [frame.waitForSelector()](/docs/api/class-frame#frame-wait-for-selector) methods. These APIs wait for the element to be attached and visible.

``` 
// Get the element handle
const elementHandle = page.waitForSelector('#box');

// Assert bounding box for the element
const boundingBox = await elementHandle.boundingBox();
expect(boundingBox.width).toBe(100);

// Assert attribute for the element
const classNames = await elementHandle.getAttribute('class');
expect(classNames.includes('highlighted')).toBeTruthy();
```

## Handles as parameters[​](#handles-as-parameters "Direct link to Handles as parameters") 

Handles can be passed into the [page.evaluate()](/docs/api/class-page#page-evaluate) and similar methods. The following snippet creates a new array in the page, initializes it with data and returns a handle to this array into Playwright. It then uses the handle in subsequent evaluations:

``` 
// Create new array in page.
const myArrayHandle = await page.evaluateHandle(() => );

// Get the length of the array.
const length = await page.evaluate(a => a.length, myArrayHandle);

// Add one more element to the array using the handle
await page.evaluate(arg => arg.myArray.push(arg.newElement), );

// Release the object when it's no longer needed.
await myArrayHandle.dispose();
```

## Handle Lifecycle[​](#handle-lifecycle "Direct link to Handle Lifecycle") 

Handles can be acquired using the page methods such as [page.evaluateHandle()](/docs/api/class-page#page-evaluate-handle), [page.\$()](/docs/api/class-page#page-query-selector) or [page.\$\$()](/docs/api/class-page#page-query-selector-all) or their frame counterparts [frame.evaluateHandle()](/docs/api/class-frame#frame-evaluate-handle), [frame.\$()](/docs/api/class-frame#frame-query-selector) or [frame.\$\$()](/docs/api/class-frame#frame-query-selector-all). Once created, handles will retain object from [garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) unless page navigates or the handle is manually disposed via the [jsHandle.dispose()](/docs/api/class-jshandle#js-handle-dispose) method.

### API reference[​](#api-reference-1 "Direct link to API reference") 

-   [JSHandle](/docs/api/class-jshandle "JSHandle")
-   [ElementHandle](/docs/api/class-elementhandle "ElementHandle")
-   [elementHandle.boundingBox()](/docs/api/class-elementhandle#element-handle-bounding-box)
-   [elementHandle.getAttribute()](/docs/api/class-elementhandle#element-handle-get-attribute)
-   [elementHandle.innerText()](/docs/api/class-elementhandle#element-handle-inner-text)
-   [elementHandle.innerHTML()](/docs/api/class-elementhandle#element-handle-inner-html)
-   [elementHandle.textContent()](/docs/api/class-elementhandle#element-handle-text-content)
-   [jsHandle.evaluate()](/docs/api/class-jshandle#js-handle-evaluate)
-   [page.evaluateHandle()](/docs/api/class-page#page-evaluate-handle)
-   [page.\$()](/docs/api/class-page#page-query-selector)
-   [page.\$\$()](/docs/api/class-page#page-query-selector-all)

## Locator vs ElementHandle[​](#locator-vs-elementhandle "Direct link to Locator vs ElementHandle") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]caution

We only recommend using [ElementHandle](/docs/api/class-elementhandle "ElementHandle") in the rare cases when you need to perform extensive DOM traversal on a static page. For all user actions and assertions use locator instead.

The difference between the [Locator](/docs/api/class-locator "Locator") and [ElementHandle](/docs/api/class-elementhandle "ElementHandle") is that the latter points to a particular element, while Locator captures the logic of how to retrieve that element.

In the example below, handle points to a particular DOM element on page. If that element changes text or is used by React to render an entirely different component, handle is still pointing to that very stale DOM element. This can lead to unexpected behaviors.

``` 
const handle = await page.$('text=Submit');
// ...
await handle.hover();
await handle.click();
```

With the locator, every time the locator is used, up-to-date DOM element is located in the page using the selector. So in the snippet below, underlying DOM element is going to be located twice.

``` 
const locator = page.getByText('Submit');
// ...
await locator.hover();
await locator.click();
```