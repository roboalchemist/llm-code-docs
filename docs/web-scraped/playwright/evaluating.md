# Source: https://playwright.dev/docs/evaluating

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Guides]
-   [Evaluating JavaScript]

On this page

<div>

# Evaluating JavaScript

</div>

## Introduction[​](#introduction "Direct link to Introduction") 

Playwright scripts run in your Playwright environment. Your page scripts run in the browser page environment. Those environments don\'t intersect, they are running in different virtual machines in different processes and even potentially on different computers.

The [page.evaluate()](/docs/api/class-page#page-evaluate) API can run a JavaScript function in the context of the web page and bring results back to the Playwright environment. Browser globals like `window` and `document` can be used in `evaluate`.

``` 
const href = await page.evaluate(() => document.location.href);
```

If the result is a Promise or if the function is asynchronous evaluate will automatically wait until it\'s resolved:

``` 
const status = await page.evaluate(async () => );
```

## Different environments[​](#different-environments "Direct link to Different environments") 

Evaluated scripts run in the browser environment, while your test runs in a testing environments. This means you cannot use variables from your test in the page and vice versa. Instead, you should pass them explicitly as an argument.

The following snippet is **WRONG** because it uses the variable directly:

``` 
const data = 'some data';
const result = await page.evaluate(() => );
```

The following snippet is **CORRECT** because it passes the value explicitly as an argument:

``` 
const data = 'some data';
// Pass |data| as a parameter.
const result = await page.evaluate(data => , data);
```

## Evaluation Argument[​](#evaluation-argument "Direct link to Evaluation Argument") 

Playwright evaluation methods like [page.evaluate()](/docs/api/class-page#page-evaluate) take a single optional argument. This argument can be a mix of [Serializable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify#Description "Serializable") values and [JSHandle](/docs/api/class-jshandle "JSHandle") instances. Handles are automatically converted to the value they represent.

``` 
// A primitive value.
await page.evaluate(num => num, 42);

// An array.
await page.evaluate(array => array.length, [1, 2, 3]);

// An object.
await page.evaluate(object => object.foo, );

// A single handle.
const button = await page.evaluateHandle('window.button');
await page.evaluate(button => button.textContent, button);

// Alternative notation using JSHandle.evaluate.
await button.evaluate((button, from) => button.textContent.substring(from), 5);

// Object with multiple handles.
const button1 = await page.evaluateHandle('window.button1');
const button2 = await page.evaluateHandle('window.button2');
await page.evaluate(
    o => o.button1.textContent + o.button2.textContent,
    );

// Object destructuring works. Note that property names must match
// between the destructured object and the argument.
// Also note the required parenthesis.
await page.evaluate(
    () => button1.textContent + button2.textContent,
    );

// Array works as well. Arbitrary names can be used for destructuring.
// Note the required parenthesis.
await page.evaluate(
    ([b1, b2]) => b1.textContent + b2.textContent,
    [button1, button2]);

// Any mix of serializables and handles works.
await page.evaluate(
    x => x.button1.textContent + x.list[0].textContent + String(x.foo),
    );
```

## Init scripts[​](#init-scripts "Direct link to Init scripts") 

Sometimes it is convenient to evaluate something in the page before it starts loading. For example, you might want to setup some mocks or test data.

In this case, use [page.addInitScript()](/docs/api/class-page#page-add-init-script) or [browserContext.addInitScript()](/docs/api/class-browsercontext#browser-context-add-init-script). In the example below, we will replace `Math.random()` with a constant value.

First, create a `preload.js` file that contains the mock.

``` 
// preload.js
Math.random = () => 42;
```

Next, add init script to the page.

``` 
import  from '@playwright/test';
import path from 'path';

test.beforeEach(async () => );
});
```

###### 

Alternatively, you can pass a function instead of creating a preload script file. This is more convenient for short or one-off scripts. You can also pass an argument this way.

``` 
import  from '@playwright/test';

// Add script for every test in the beforeEach hook.
test.beforeEach(async () => , value);
});
```