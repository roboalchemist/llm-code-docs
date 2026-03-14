# Source: https://testcafe.io/documentation/402832/guides/basic-guides/client-functions

Title: Client Functions | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402832/guides/basic-guides/client-functions

Markdown Content:
Important

Do not use client functions to permanently alter website behavior. Use [client scripts](https://testcafe.io/documentation/402843/guides/advanced-guides/inject-client-scripts) to inject libraries and helper functions into the page.

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#article-summary)Article Summary[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#article-summary)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Create a **client function** to [run custom client-side code](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#common-use-cases) and obtain page data. Client functions can return any serializable value from the browser, such as the current URL.

Use the [ClientFunction](https://testcafe.io/documentation/402789/reference/test-api/clientfunction/constructor) constructor to create a client function. Client functions can be [asynchronous](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#include-asynchronous-code) and accept [parameters](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-parameters).

```
import { ClientFunction } from 'testcafe';
const getWindowLocation = ClientFunction(() => window.location);
```

You can execute client functions within [the test body](https://testcafe.io/documentation/403366/reference/test-api/test), [test hooks](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks), and [Role definitions](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication). Manually import the [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) object to use client functions elsewhere.

Call the client function with the `await` keyword to execute it.

```
test('My Test', async t => {
    const location = await getWindowLocation();
});
```

Alternatively, use the [t.eval](https://testcafe.io/documentation/402703/reference/test-api/testcontroller/eval) action:

```
await t.eval(() => window.location);
```

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#table-of-contents)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Common Use Cases](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#common-use-cases)
    *   [Practices to Avoid](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#practices-to-avoid)

*   [Create a Client Function](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#create-a-client-function)
    *   [Include Asynchronous Code](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#include-asynchronous-code)
    *   [Specify Parameters](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-parameters)
    *   [Specify Options and Dependencies](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-options-and-dependencies)

*   [Execute Client Functions](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-client-functions)
    *   [The t.eval test action](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#the-teval-test-action)
    *   [Trigger Client Functions in Node.js Callbacks](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#trigger-client-functions-in-nodejs-callbacks)

*   [Limitations](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#limitations)
*   [Examples](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#examples)
    *   [Retrieve Page URL](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#retrieve-page-url)
    *   [Execute complex DOM queries](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-complex-dom-queries)
    *   [Determine text direction](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#determine-text-direction)
    *   [Select page text](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#select-page-text)
    *   [Access clipboard](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#access-clipboard)
    *   [Observe page events](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#observe-page-events)
    *   [Obtain the value of an option element](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#obtain-the-value-of-an-option-element)

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#common-use-cases)Common Use Cases[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#common-use-cases)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Client functions have two primary purposes.

*   If you cannot extract page data with a [Selector query](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors), use a ClientFunction to perform client-side calculations.
*   If a combination of [standard test methods](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) cannot perform the page action you want, use a ClientFunction to interact with the page.

See the [Examples](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#examples) section to view code examples for common Client Function use cases.

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#practices-to-avoid)Practices to Avoid[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#practices-to-avoid)

*   Do not use client functions to perform common page actions. Use [test actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions) instead.

*   Client functions increase the complexity of your test suite. Before you create a new Client Function, check if you can perform the same action with [custom DOM events](https://testcafe.io/documentation/403091/reference/test-api/testcontroller/dispatchevent).

*   Do not use client functions to permanently alter website behavior. Use [client scripts](https://testcafe.io/documentation/402843/guides/advanced-guides/inject-client-scripts) to inject libraries and helper functions into the page.

*   Client functions cannot return DOM nodes. Use [Selector queries](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) to inspect the DOM.

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#create-a-client-function)Create a Client Function[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#create-a-client-function)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the [ClientFunction](https://testcafe.io/documentation/402789/reference/test-api/clientfunction/constructor) constructor to create a client function.

```
import { ClientFunction } from 'testcafe';
const getWindowLocation = ClientFunction(() => window.location);
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#include-asynchronous-code)Include Asynchronous Code[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#include-asynchronous-code)

To run asynchronous client-side code, create a client function that returns a Promise. When you execute an asynchronous client function, TestCafe waits for the Promise to resolve.

```
import { ClientFunction } from 'testcafe';

const performAsyncOperation = ClientFunction(() => {
    return new Promise(resolve => {
        window.setTimeout(resolve, 500); // asynchronous code
    });
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-parameters)Specify Parameters[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-parameters)

Client functions can accept parameters:

```
import { ClientFunction } from 'testcafe';

const getLocationPart = ClientFunction(locationPart => {
    return window.location[locationPart];
});

fixture ('My fixture').page('http://www.example.com/');

test('Parameterized Client Functions', async t => {
    const hostName = await getLocationPart('host');
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-options-and-dependencies)Specify Options and Dependencies[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-options-and-dependencies)

Use the `dependencies` option to pass Selector queries, helper functions, and server-side data to the client function.

```
const getUri = ClientFunction(() => {
        return getDocumentURI();
    }, dependencies: { /* dependencies go here */ } });
```

Use the [CommonJs](https://nodejs.org/api/modules.html#requireid)`require` syntax to access helper functions in your test file.

**utils.js**

```
export function getDocumentURI() {
    return document.documentURI;
}
```

**test.js**

```
import { ClientFunction } from 'testcafe';

const getDocumentURI = require('./utils.js').getDocumentURI;

fixture('My fixture')
    .page('http://devexpress.github.io/testcafe/example/');

test('My test', async t => {
    const getUri = ClientFunction(() => {
        return getDocumentURI();
    }, { dependencies: { getDocumentURI } });

    const uri = await getUri();

    await t.expect(uri).eql('https://devexpress.github.io/testcafe/example/');
});
```

#### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#override-client-function-options-and-dependencies)Override Client Function Options and Dependencies[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#override-client-function-options-and-dependencies)

Use the [with](https://testcafe.io/documentation/402788/reference/test-api/clientfunction/with) method to override client function options and dependencies:

```
const cfWithDependency = cfWithoutDependency.with({
    dependencies: { foo: 'bar' }
});
```

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-client-functions)Execute Client Functions[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-client-functions)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can execute client functions in any part of the test that can contain test actions — be it [test body](https://testcafe.io/documentation/403366/reference/test-api/test), [test hooks](https://testcafe.io/documentation/403435/guides/intermediate-guides/hooks), or helper files.

Call the client function with the `await` keyword to execute it.

```
import { ClientFunction } from 'testcafe';

const getWindowLocation = ClientFunction(() => window.location);

fixture('My fixture')
    .page `http://www.example.com/`;

test('My Test', async t => {
    const location = await getWindowLocation();
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#the-teval-test-action)The t.eval test action[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#the-teval-test-action)

Use the [t.eval](https://testcafe.io/documentation/402703/reference/test-api/testcontroller/eval) action to execute client-side functions that you did not define beforehand.

```
test('My Test', async t => {
    const docURI = await t.eval(() => document.documentURI);
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#trigger-client-functions-in-nodejs-callbacks)Trigger Client Functions in Node.js callbacks[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#trigger-client-functions-in-nodejs-callbacks)

Client functions require access to the [TestController](https://testcafe.io/documentation/402665/reference/test-api/testcontroller) object. Client functions inside the test implicitly obtain this access. Follow the steps below to execute a client function inside a Node.js callback:

1.   Bind the function to the test controller with the [boundTestRun](https://testcafe.io/documentation/402789/reference/test-api/clientfunction/constructor) option.
2.   To make sure that TestCafe doesn’t end the test before the callback function triggers, suspend the test with a Promise and wait for its resolution.

Important

The `boundTestRun` option has to share a single test controller instance with the test itself. It doesn’t work with [imported test controllers](https://testcafe.io/documentation/402665/reference/test-api/testcontroller#implicit-test-controller-use).

```
import fs from 'fs';
import { ClientFunction } from 'testcafe';

fixture ('My fixture')
    .page('http://www.example.com/');

const getDataFromClient = ClientFunction(() => getSomeData());

test('Check client data', async t => {
    const boundGetDataFromClient = getDataFromClient.with({ boundTestRun: t });

    const equal = await new Promise(resolve => {
        fs.readFile('/home/user/tests/reference/clientData.json', (err, data) => {
            boundGetDataFromClient().then(clientData => {
                resolve(JSON.stringify(clientData) === data);
            });
        });
    });

    await t.expect(equal).ok();
});
```

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#limitations)Limitations[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#limitations)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Client functions are subject to the following limitations:

*   Client functions do not support generators and the `async/await` syntax.
*   Client functions cannot access outer scope variables. Use [parameters](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-parameters) or [dependencies](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#specify-options-and-dependencies) to pass data to client functions.
*   Client functions do not support iterable destructuring operators ([`spread`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), [`rest`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters), etc.) for non-array objects (`NodeList`, `HTMLCollection`, etc.).
*   Client functions do not support the property shorthand syntax for the `dependencies` option and other imported values.
*   Client functions do not support the [`Array.from()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) and the [`Array.of()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/of) methods.
*   Client functions cannot contain keyed collections ([`Map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map), [`Set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set), [`WeakMap`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap), [`WeakSet`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)).

[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#examples)Examples[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#examples)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Retrieve Page URL](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#retrieve-page-url)
*   [Execute complex DOM queries](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-complex-dom-queries)
*   [Determine text direction](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#determine-text-direction)
*   [Select page text](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#select-page-text)
*   [Access clipboard](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#access-clipboard)
*   [Observe page events](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#observe-page-events)
*   [Obtain the value of an option element](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#obtain-the-value-of-an-option-element)

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#retrieve-page-url)Retrieve Page URL[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#retrieve-page-url)

Page actions may redirect the user to an unexpected URL. Create a client function to retrieve the current URL.

Use an [assertion](https://testcafe.io/documentation/402837/guides/basic-guides/assertions) to compare the value of the [window.location.href](https://developer.mozilla.org/en-US/docs/Web/API/Location/href) property to your expectations:

```
import { ClientFunction } from 'testcafe';

fixture ('My Fixture')
    .page ('http://devexpress.github.io/testcafe/example');

// Returns the URL of the current web page
const getPageUrl = ClientFunction(() => window.location.href);

test('Check the page URL', async t => {
    await t
        .typeText('#developer-name', 'John Smith')
        .click('#submit-button') // Redirects to the 'Thank you' page
        .expect(getPageUrl()).contains('thank-you'); // Checks if the current page URL contains the 'thank-you' string
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-complex-dom-queries)Execute complex DOM queries[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#execute-complex-dom-queries)

Important

To traverse the DOM, use [Selector queries](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) instead of native `querySelector` and `querySelectorAll` methods. You can pass Selector queries as client function [dependencies](https://testcafe.io/documentation/402789/reference/test-api/clientfunction/constructor#optionsdependencies). Chain [selector methods](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#selector-methods) for simpler query syntax.

Client functions can perform complex client-side calculations.

For example, the [https://js.devexpress.com/](https://js.devexpress.com/) page contains a table. The example below extracts data from **only two** of the table’s columns and pushes it to an array:

```
import { ClientFunction } from 'testcafe';

fixture('Get sale amount')
    .page('https://js.devexpress.com/');

    const getSalesAmount = ClientFunction(() => {
        const grid      = document.querySelector('.dx-datagrid-rowsview');
        const rowCount  = grid.querySelectorAll('.dx-data-row').length;
        const sales     = grid.querySelectorAll('td:nth-child(3)');
        const customers = grid.querySelectorAll('td:nth-child(7)');

        const array = [];

        for (let i = 0; i < rowCount; i++) {
            const salesPerCustomer = {
                sales: sales[i].textContent,
                customer: customers[i].textContent
            }

            array.push(salesPerCustomer);
        }

        return array;
    });

const expectedData = [
            { sales: '$6,370', customer: 'Renewable Supplies' },
            { sales: '$4,530', customer: 'Apollo Inc' },
            { sales: '$1,110', customer: 'Johnson & Assoc' },
            { sales: '$6,600', customer: 'Global Services' },
            { sales: '$2,830', customer: 'Health Plus Inc' },
            { sales: '$6,770', customer: 'Gemini Stores' },
            { sales: '$1,460', customer: 'Discovery Systems' }
        ];

test('My test', async t => {
    await t
        .expect(getSalesAmount()).eql(expectedData);
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#determine-text-direction)Determine text direction[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#determine-text-direction)

The `getDocumentDirection` client function determines the predominant text direction of the page:

```
import { ClientFunction } from 'testcafe';

const getDocumentDirection = ClientFunction(() => {
  return getComputedStyle(document.documentElement).direction;
})

fixture('Client Functions')
  .page('https://devexpress.github.io/testcafe/example');

test('Determine test direction', async t => {

  await t
    .expect(getDocumentDirection()).eql('ltr');
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#select-page-text)Select page text[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#select-page-text)

The [selectText](https://testcafe.io/documentation/402687/reference/test-api/testcontroller/selecttext) test action can select text from user-editable elements, such as `input`, `textarea`, and `contenteditable`. To select regular page text, create a client function that uses the [JavaScript Selection API](https://developer.mozilla.org/en-US/docs/Web/API/Selection).

```
import { Selector, ClientFunction } from 'testcafe';

fixture('selection')
    .page('http://example.com');

const selectElement = (selector) => ClientFunction(() => {
    const selection = document.getSelection();
    const range = document.createRange();

    range.selectNode(selector());
    selection.addRange(range);
}, { dependencies: { selector } });

test('selection', async t => {
    await selectElement(Selector('h1'))();

    await t.debug();
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#access-clipboard)Access clipboard[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#access-clipboard)

Clipboard manipulation requires a high level of system access. The majority of browsers [do not support](https://caniuse.com/clipboard) the HTML5 [Clipboard API](https://developer.mozilla.org/en-US/docs/Web/API/Clipboard_API). Due to these factors, TestCafe doesn’t offer any clipboard management tools out of the box.

You can work around this limitation with a client function. Create event listeners that intercept “copy” and “paste” keyboard shortcuts:

```
import { Selector, ClientFunction } from 'testcafe';
fixture ('Example')
    .page('http://devexpress.github.io/testcafe/example/');

test('Clipboard test', async t => {
    const text = 'Value for copy-paste';

    const emulateClipboard = ClientFunction(() => {
        let buffer = '';

        document.addEventListener('keypress', event => {
            if (event.ctrlKey) {
                if (event.key === 'c')
                    buffer = document.getSelection().toString();

                if (event.key === 'v')
                    document.activeElement.value = buffer;
            }
        });
    });

    await emulateClipboard();
    await t
        .typeText('#developer-name', text)
        .selectText('#developer-name')
        .pressKey('ctrl+c')
        .click('#tried-test-cafe')
        .click('#comments')
        .pressKey('ctrl+v')
        .expect(Selector('#comments').value).eql(text)
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#observe-page-events)Observe page events[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#observe-page-events)

TestCafe can [fire custom DOM events](https://testcafe.io/documentation/403091/reference/test-api/testcontroller/dispatchevent), but doesn’t have the capability to observe page events as they happen.

To work around this limitation, create three client functions:

*   A Client Function that modifies the `window` object to capture page events.
*   A Client Function that retrieves the event log.
*   A Client Function that shuts down event capture.

You can then use these functions in your test whenever you retrieve event data.

```
import { ClientFunction } from 'testcafe';

fixture('Sample App')
    .page('https://cf51n.csb.app/');

// Create a function that intercepts window events
const spyOn = ClientFunction(() => {

    window.myFunctionSpyData = []; // Array for event data
    window.orirginalFunction = window.myObject.myFunction; // Preserve the original state of the window object

    // Modify the window object to collect event data
    window.myObject.myFunction = function () {
        window.myFunctionSpyData.push(...arguments); // Adds event to the array
        window.orirginalFunction(...arguments);
    };
});

// Create a function to retrieve event data
const getSpyData = ClientFunction(() => {
    return window.myFunctionSpyData;
});

// Create a function to reset the window object
const spyOff = ClientFunction(() => {
    window.myObject.myFunction = window.orirginalFunction; // Restore the original window object
    delete window.spyData;
});

test('Observe page events', async t => {
    await spyOn();

    await t.click('#btn');

    const data = await getSpyData();

    await spyOff();

    await t
        .expect(data.length).eql(2)
        .expect(data[0]).eql('1')
        .expect(data[1]).eql('2');
});
```

### [](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#obtain-the-value-of-an-option-element)Obtain the value of an “option” element[](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions#obtain-the-value-of-an-option-element)

If the `value` property of an option element differs from the element’s text content, a regluar Selector query cannot extract it. Create a Selector function that retrieves this value instead:

```
import { Selector, ClientFunction } from 'testcafe';

fixture('Fixture 1')
    .page('https://kys0l.csb.app/');

test('Test 1', async t => {
    const selector = Selector('select');

    const getValue = ClientFunction((index) => {
        const select = selector();

        return select.options[index].value;
    }, { dependencies: { selector } });

    await t
        .expect(getValue(0)).eql('1234')
        .expect(getValue(1)).eql('5432')
        .expect(getValue(2)).eql('9999');
});
```
