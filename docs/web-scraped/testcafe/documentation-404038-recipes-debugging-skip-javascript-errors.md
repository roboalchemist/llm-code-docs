# Source: https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors

Title: Skip JavaScript Errors | Debugging | Recipes

URL Source: https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors

Markdown Content:
TestCafe tests fail when a page yields a JavaScript error. If you enable the `skipJsErrors` option, TestCafe deliberately **ignores** JavaScript errors and lets tests proceed.

Important

Errors are signs of malfunction. Do not ignore errors that you can fix. 

 If a page outputs unwarranted error messages, modify your application to prevent this behavior. 

 Use the `skipJsErrors` option to silence errors that you cannot act upon.

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#overview)Overview[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#overview)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#methods)Methods[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#methods)

*   Use the [CLI flag](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3), the [configuration file property](https://testcafe.io/documentation/402638/reference/configuration-file#skipjserrors), or the [Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#skipjserrors) to ignore JavaScript errors throughout your entire test suite.

*   Use the [fixture.skipJsErrors](https://testcafe.io/documentation/404025/reference/test-api/fixture/skipjserrors) method to ignore JavaScript errors for individual fixtures. 

*   Use the [test.skipJsErrors](https://testcafe.io/documentation/404026/reference/test-api/test/skipjserrors) method to ignore JavaScript errors in individual tests.

*   Use the [t.skipJsErrors](https://testcafe.io/documentation/404027/reference/test-api/testcontroller/skipjserrors) action to ignore JavaScript errors at specific points in the test.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#options)Options[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#options)

You can skip all JavaScript errors that occur, or only skip errors that meet specific criteria.

*   [Skip all errors](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-all-errors)
*   [Skip errors by message](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-message)
*   [Skip errors by URL](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-url)
*   [Skip errors by stack](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-stack)
*   [Skip errors by multiple criteria](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-multiple-criteria)
*   [Use custom logic to skip errors](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#use-custom-logic-to-skip-errors)
*   [Disable skipJsErrors](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#disable-skipjserrors)

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#conflict-resolution)Conflict resolution[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#conflict-resolution)

*   The [CLI flag](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3) and the [Test Runner API option](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#skipjserrors) override the [configuration file property](https://testcafe.io/documentation/402638/reference/configuration-file#skipjserrors).
*   The [fixture.skipJsErrors](https://testcafe.io/documentation/404025/reference/test-api/fixture/skipjserrors) method overrides global `skipJsErrors` settings.
*   The [test.skipJsErrors](https://testcafe.io/documentation/404026/reference/test-api/test/skipjserrors) method overrides the fixture-wide `skipJsErrors` setting. 
*   The [t.skipJsErrors](https://testcafe.io/documentation/404027/reference/test-api/testcontroller/skipjserrors) action overrides the test-wide `skipJsErrors` setting.

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-all-errors)Skip all errors[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-all-errors)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you do not specify additional options, TestCafe ignores all JavaScript errors.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples)

*   **CLI**
```
testcafe chrome test.js -e
```
*   **Configuration file**
```
{
    "skipJsErrors": true
}
```
*   **Test Runner API**
```
const runner = await runner.run({skipJsErrors: true});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors();
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors();
```
*   **Test action**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t
        .skipJsErrors() // Ignore all JavaScript errors from this point
        .click('#button')
        .skipJsErrors(false) // Until this point
});
```

Specify options to filter errors by string or regular expression.

Warning

Enclose regular expressions in forward slashes to avoid strict matches for special characters.

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-message)Skip errors by message[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-message)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you specify the `message` option, TestCafe ignores JavaScript errors with specific messages. The `message` option accepts strings or **regular expressions**.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-1)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-1)

*   **CLI**
```
testcafe chrome test.js -e message='/.*User ID.*/ig'
```
*   **Configuration file**
```
{
    "skipJsErrors": {
        "message": /.*User ID.*/ig
    }
}
```
*   **Test Runner API**
```
const runner = await runner.run({
        skipJsErrors: { message: /.*User ID.*/ }
});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors({
        message: /.*User.*/ig
    });
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors({
        message: /.*User.*/ig
    });
```
*   **Test action**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t
        .skipJsErrors({message: /.*User.*/ig})
        .click('#button');
});
```

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-url)Skip errors by URL[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-url)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you specify the `pageUrl` option, TestCafe ignores JavaScript errors on specific pages. The `pageUrl` option accepts strings or **regular expressions**.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-2)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-2)

*   **CLI**
```
testcafe chrome test.js -e pageUrl='/.*.*html/'
```
*   **Configuration file**
```
{
    "skipJsErrors": {
        "pageUrl": /.*.*html/
    }
}
```
*   **Test Runner API**
```
const runner = await runner.run({
    skipJsErrors: {pageUrl: /.*.*html/}
});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors({
        pageUrl: /.*.*html/ // Ignores all pages with the html extension
    });
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors({
        pageUrl: /.*.*html/ // Ignores all pages with the html extension
    });
```
*   **Test action**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t
        .skipJsErrors({pageUrl: /.*.html/}) // Only ignore errors that occur on pages with the html extension
        .click('#button');
});
```

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-stack)Skip errors by stack[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-stack)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you specify the `stack` option, TestCafe ignores JavaScript errors with specific call stacks. The `stack` option accepts strings or regular expressions.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-3)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-3)

*   **CLI**
```
testcafe chrome test.js -e stack='/.*jquery.*/g'
```
*   **Configuration file**
```
{
    "skipJsErrors": {
        "stack": /.*jquery.*/ig
    }
}
```
*   **Test Runner API**
```
const runner = await runner.run({
    skipJsErrors: { stack: /.*jquery.*/ }
});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors({
        stack: /.*jquery.*/ig
    });
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors({
        stack: /.*jquery.*/ig;
    });
```
*   **Test action**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t
        .skipJsErrors({stack: /.*jquery.*/}) 
        .click('#button');
});
```

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-multiple-criteria)Skip errors by multiple criteria[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#skip-errors-by-multiple-criteria)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Specify several arguments to skip errors that fit **multiple criteria at once** — for example, errors with a specific message **and** a specific call stack.

Note

Specify a [callback function](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#use-custom-logic-to-skip-errors) to set complex rules — for example, to skip errors that match only _one_ criterion of multiple.

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-4)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-4)

*   **CLI**
```
testcafe chrome test.js -e stack='/.*jquery.*/', message='/.*User ID.*/ig'
```
*   **Configuration file**
```
{
    "skipJsErrors": {
        "stack": "/.*jquery.*/",
        "message": "/.*User ID.*/ig"
    }
}
```
*   **Test Runner API**
```
const runner = await runner.run({
    skipJsErrors: {
    stack: /.*jquery.*/,
    message: /.*User ID.*/
    }
});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors({
        stack: /.*jquery.*/,
        message: /.*User ID.*/ig
    });
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors({
        message: /.*User ID.*/ig,
        stack: /.*jquery.*/;
    });
```
*   **Test action**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t
        .skipJsErrors({pageUrl: 'http://example.com', stack: /.*jquery.*/})
        .click('#button');
});
```

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#use-custom-logic-to-skip-errors)Use custom logic to skip errors[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#use-custom-logic-to-skip-errors)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Create a **callback function** with custom logic and pass it to the `skipJsErrors` method.

The callback function can access the error’s message, call stack, and URL. TestCafe executes the function **client-side**.

Make sure that the function returns a Boolean value — **true** if you want to skip the error; **false** otherwise.

The following example skips errors with **either** the specified message **or** the specified stack:

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-5)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-5)

*   **CLI** The command line interface _does not support_ this capability.
*   **Configuration file**

Use a [JavaScript configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#javascript) to define a callback function with custom logic:

```
const callbackFunction = {
    fn:           ({ message }) => message.includes('User') || stack.includes('jquery');
};

module.exports = {
    skipJsErrors: callbackFunction,
};
```
*   **Test Runner API**

```
runner.run({

    skipJsErrors: ({ message, stack, pageUrl }) => message.includes('User') || stack.includes('jquery');

});
```
*   **Fixture method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors(
        ({ message, stack, pageUrl }) => {
            return message === 'Invalid User ID' || stack.includes('jquery')
        }
    );
```
*   **Test method**
```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.click('#button');
}).skipJsErrors(
        ({ message, stack, pageUrl }) => {
            return message ==='Invalid User ID' || stack.includes('jquery')
        }
    );
```
*   **Test action**
```
t.skipJsErrors(({ message, stack, pageUrl }) => {
    return message === 'Invalid User ID' || stack.includes('jquery')
})
```

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#pass-additional-data-to-the-callback-function)Pass additional data to the callback function[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#pass-additional-data-to-the-callback-function)

The function accepts three arguments out of the box: `message`, `stack`, and `pageUrl`. To pass additional data to the function, create an object with dependency data. Then, pass an object with both the function and your dependencies to the `skipJsErrors` method.

```
skipJsErrors(
    {
        fn: ({ message, stack, pageUrl }) => {
        // This code can reference 'key1' and 'key2'
        },
        dependencies: {key1: value, key2: value2}
    }
);
```

[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#disable-skipjserrors)Disable skipJsErrors[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#disable-skipjserrors)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Pass `false` to the [fixture.skipJsErrors](https://testcafe.io/documentation/404025/reference/test-api/fixture/skipjserrors) method, the [test.skipJsErrors](https://testcafe.io/documentation/404026/reference/test-api/test/skipjserrors) method, or the [t.skipJsErrors](https://testcafe.io/documentation/404027/reference/test-api/testcontroller/skipjserrors) action to disable a `skipJsError` setting that is greater in scope:

### [](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-6)Examples[](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors#examples-6)

*   Fixture method

```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors(false); // overrides any global setting
```
*   Test method

```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`
    .skipJsErrors()

test('Click a button', async t => {
        await t.click('#button');
    }).skipJsErrors(false); // overrides the fixture-wide setting
```
*   Test action

```
fixture `Authentication tests`
    .page `https://devexpress.github.io/testcafe/`

test('Click a button', async t => {
    await t.skipJsErrors(false) // overrides the test-wide setting
}).skipJsErrors(true);
```
