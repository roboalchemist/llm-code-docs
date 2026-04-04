# Source: https://testcafe.io/documentation/

Title: Getting Started | Overview | Guides

URL Source: https://testcafe.io/documentation/

Markdown Content:
[](https://testcafe.io/documentation/#in-this-article)In this article[](https://testcafe.io/documentation/#in-this-article)
---------------------------------------------------------------------------------------------------------------------------

This article describes the basics of TestCafe for readers with zero prior TestCafe experience. It requires basic familiarity with JavaScript, the web, and the command line.

*   [What is TestCafe?](https://testcafe.io/documentation/#what-is-testcafe)
*   [Install TestCafe](https://testcafe.io/documentation/#install-testcafe)
*   [Create a new test](https://testcafe.io/documentation/#create-a-new-test)
*   [Add test actions](https://testcafe.io/documentation/#add-test-actions)
*   [Add a success condition](https://testcafe.io/documentation/#add-a-success-condition)
    *   [Create an assertion](https://testcafe.io/documentation/#1-create-an-assertion)
    *   [Examine the page](https://testcafe.io/documentation/#2-specify-the-actual-header-value)
    *   [Define your expectations](https://testcafe.io/documentation/#3-specify-the-expected-header-value)

*   [Run the test](https://testcafe.io/documentation/#run-the-test)
*   [View test results](https://testcafe.io/documentation/#view-test-results)
*   [What’s next?](https://testcafe.io/documentation/#whats-next)

[](https://testcafe.io/documentation/#what-is-testcafe)What Is TestCafe?[](https://testcafe.io/documentation/#what-is-testcafe)
-------------------------------------------------------------------------------------------------------------------------------

TestCafe is an end-to-end testing framework for web applications. TestCafe runs on [Node.js](https://nodejs.org/en). TestCafe supports all three major operating systems — Linux, Windows, and macOS.

You can use TestCafe to simulate common user scenarios in major desktop browsers, cloud browsers, and on mobile devices. If your website malfunctions, TestCafe reports can help you diagnose the issue.

[](https://testcafe.io/documentation/#install-testcafe)Install TestCafe[](https://testcafe.io/documentation/#install-testcafe)
------------------------------------------------------------------------------------------------------------------------------

> Main article: [Install TestCafe](https://testcafe.io/documentation/402834/guides/basic-guides/install-testcafe)

![Image 1: Install TestCafe](https://testcafe.io/images/install-testcafe.gif)

### [](https://testcafe.io/documentation/#prerequisites)Prerequisites[](https://testcafe.io/documentation/#prerequisites)

TestCafe requires a recent version of the [Node.js](https://nodejs.org/en) platform. Run the following command to confirm that your setup includes Node.js:

```
node --version
```

The best way to install the TestCafe framework is to use [npm](https://www.npmjs.com/) — the most popular Node.js package manager. The NPM repository hosts ready-to-use builds of the framework. Confirm that your setup contains an [up-to-date version](https://www.npmjs.com/package/npm) of the package manager:

```
npm --version
```

### [](https://testcafe.io/documentation/#installation)Installation[](https://testcafe.io/documentation/#installation)

Run the following command to install the `testcafe` package from npm:

```
npm install -g testcafe
```

[](https://testcafe.io/documentation/#create-a-new-test)Create a new test[](https://testcafe.io/documentation/#create-a-new-test)
---------------------------------------------------------------------------------------------------------------------------------

> Main article: [Test Structure](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure)

Let’s create a simple test for the [TestCafe demo page](https://devexpress.github.io/testcafe/example/).

![Image 2: New test file](https://testcafe.io/images/new-test-file.gif)

1.   TestCafe tests are Node.js scripts. Create a new [TypeScript](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript) or JavaScript file, and open the file in the text editor.

2.   TestCafe test files consist of _fixtures_ and _tests_. A fixture is a groups of tests that share the same starting URL. Invoke the `fixture` keyword to create a new fixture.

```
fixture('Getting Started')
```
3.   Use the [page](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#declare-a-fixture) method to set the starting URL of the fixture.

```
fixture('Getting Started')
    .page('https://devexpress.github.io/testcafe/example');
```
4.   Finally, declare a new test with the `test` method.

```
fixture('Getting Started')
    .page('https://devexpress.github.io/testcafe/example');

test('My first test', async t => {
    // Test code goes here
});
```

[](https://testcafe.io/documentation/#add-test-actions)Add test actions[](https://testcafe.io/documentation/#add-test-actions)
------------------------------------------------------------------------------------------------------------------------------

> Main article: [Test Actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions)

Let’s add two simple actions to the “My first test” test function.

![Image 3: Test actions](https://testcafe.io/images/getting-started.gif)

### [](https://testcafe.io/documentation/#action-1-type-text)Action 1: Type text[](https://testcafe.io/documentation/#action-1-type-text)

The first action — [t.typeText](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext) — populates the `#developer-name` input field with a dummy name:

```
await t.typeText('#developer-name', 'John Smith');
```

The first argument is a [CSS Selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) that identifies the target element (`#developer-name`). The second argument contains the input value (`John Smith`).

### [](https://testcafe.io/documentation/#action-2-click-the-button)Action 2: Click the button[](https://testcafe.io/documentation/#action-2-click-the-button)

The second action — [t.click](https://testcafe.io/documentation/402710/reference/test-api/testcontroller/click) — clicks the “Submit” button:

```
await t.click('#submit-button');
```

This action requires a single argument — a [CSS Keyword](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) that identifies the target element.

### [](https://testcafe.io/documentation/#chain-multiple-actions)Chain multiple actions[](https://testcafe.io/documentation/#chain-multiple-actions)

Let’s [chain](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions#action-chaining) these actions together. Action chains make your code easier to read.

```
fixture('Getting Started')
    .page('https://devexpress.github.io/testcafe/example');

test('My first test', async t => {
    await t
        .typeText('#developer-name', 'John Smith')
        .click('#submit-button');
});
```

[](https://testcafe.io/documentation/#add-a-success-condition)Add a success condition[](https://testcafe.io/documentation/#add-a-success-condition)
---------------------------------------------------------------------------------------------------------------------------------------------------

Tests without an explicit **success condition** are inconclusive.

If one of the following errors occurs, the test automatically fails:

1.   TestCafe **cannot reach** the test page URL.
2.   TestCafe **cannot perform a test action** — for example, if the target element does not exist.
3.   Your website **throws a [JavaScript error](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors)**.

But you still don’t know if test actions have had the desired effect. That’s why you should add **assertions** (custom success conditions) to your test.

When you [submit the form](https://testcafe.io/documentation/#action-2-click-the-button), the application should open a page that greets the user by name. Let’s use an **assertion** to compare the actual value of the greeting to our expectations.

### [](https://testcafe.io/documentation/#1-create-an-assertion)1. Create an assertion[](https://testcafe.io/documentation/#1-create-an-assertion)

> Main article: [Assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions)

Assertions are functions that **compare** page data to your expectations. Assertions allow you to create custom success conditions — if an assertion fails, the test fails, too. Add the following **assertion** to your test:

```
await t.expect(x).eql(y);
```

This assertion compares the value of `x` to the value of `y`, and succeeds if they are equal.

> Main article: [Element Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors)

Replace the `x` with the header’s **actual** value. Use a [Selector query](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) to extract this data from the page.

1.   Import the `Selector` class in the beginning of the test file:

```
import { Selector } from 'testcafe';
```
2.   Place a Selector query into the left-hand side of the assertion:

```
await t.expect(Selector('#article-header').innerText).eql(y);
```

The `#article-header` CSS Selector identifies the Selector target. The `innerText` method retrieves the element’s `innerText` property.

If the application is slow to respond, and the Selector query fails at first, TestCafe employs the [Smart Assertion Query Mechanism](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) to ensure test stability.

Note

You can use Selector queries to extract page data at any point in the test, not just inside Assertions. Read the [Element Selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) guide for more information.

Replace `y` with the header’s **expected** value:

```
await t.expect(Selector('#article-header').innerText).eql('Thank you, John Smith!');
```

### [](https://testcafe.io/documentation/#4-add-the-assertion-to-the-action-chain)4. Add the assertion to the action chain[](https://testcafe.io/documentation/#4-add-the-assertion-to-the-action-chain)

```
import { Selector } from 'testcafe';

fixture('Getting Started')
    .page('https://devexpress.github.io/testcafe/example');

test('My first test', async t => {
    await t
        .typeText('#developer-name', 'John Smith')
        .click('#submit-button')
        .expect(Selector('#article-header').innerText).eql('Thank you, John Smith!');
});
```

Now that you have a working success condition, the test is complete.

[](https://testcafe.io/documentation/#run-the-test)Run the Test[](https://testcafe.io/documentation/#run-the-test)
------------------------------------------------------------------------------------------------------------------

> Main article: [Run tests](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests)

The easiest way to run TestCafe tests is to use the [command line interface](https://testcafe.io/documentation/402639/reference/command-line-interface).

![Image 4: Test Launch](https://testcafe.io/images/test-launch.gif)

Specify the [target browser](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers) and [test file path](https://testcafe.io/documentation/402639/reference/command-line-interface#test-files). TestCafe opens the selected browser and starts test execution.

```
testcafe chrome getting-started.js
```

### [](https://testcafe.io/documentation/#reload-tests-on-the-fly)Reload tests on the fly[](https://testcafe.io/documentation/#reload-tests-on-the-fly)

TestCafe can _reload_ tests as you edit them. Enable **[live mode](https://testcafe.io/documentation/403842/guides/intermediate-guides/live-mode)** to take advantage of this capability:

```
testcafe chrome getting-started.js --live
```

Important

You can interact with other applications while TestCafe runs your tests. However, do not switch away from the browser tab that runs the test or minimize the browser window. Inactive tabs and minimized browser windows may trigger a resource saving mode, which harms the test’s performance.

Do not zoom pages while testing. Tests may lose stability when you zoom the page in and out.

[](https://testcafe.io/documentation/#view-test-results)View Test Results[](https://testcafe.io/documentation/#view-test-results)
---------------------------------------------------------------------------------------------------------------------------------

> Main article: [Reporters](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters)

TestCafe outputs real-time test results to the console.

![Image 5: Test Report](https://testcafe.io/images/report.png)

If a test fails, TestCafe outputs the error and highlights the failed action:

![Image 6: Test failure](https://testcafe.io/images/report-failure.png)

[](https://testcafe.io/documentation/#whats-next)What’s Next?[](https://testcafe.io/documentation/#whats-next)
--------------------------------------------------------------------------------------------------------------

*   Add more [test actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions). For example, [navigate](https://testcafe.io/documentation/402695/reference/test-api/testcontroller/navigateto) to a different page, or [take a screenshot](https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot).
*   Use [Element Selector queries](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) to extract new information from the page.
*   Use [Client Functions](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions) to run custom client-side code and return its value.
*   Send [HTTP Requests](https://testcafe.io/documentation/403971/guides/intermediate-guides/api-testing) to your back-end server.
*   Learn how to [troubleshoot common test issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests).

The following [Basic Guides](https://testcafe.io/documentation/402634/guides) offer a deeper look at basic TestCafe capabilities:

*   [Test Structure](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure)
*   [Element Selectors](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors)
*   [Test Actions](https://testcafe.io/documentation/402833/guides/basic-guides/test-actions)
*   [Assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions)
*   [Client Functions](https://testcafe.io/documentation/402832/guides/basic-guides/client-functions)
*   [Run Tests](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests)
*   [Debug Tests](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests)
