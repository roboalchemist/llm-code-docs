# Source: https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests

Title: Debug Tests | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests

Markdown Content:
Some tests fail even when your website works as intended. This guide describes tools and strategies that you can use to fix failing TestCafe tests.

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#table-of-contents)Table of contents[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#table-of-contents)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Common reasons for test failure](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#common-reasons-for-test-failure)
    *   [Element Selector issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#element-selector-issues)
    *   [Network issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#network-issues)
    *   [Browser issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-issues)
    *   [Application errors](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#application-errors)

*   [Debug mode](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode)
*   [Visual Selector debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger)
*   [Quarantine mode](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#quarantine-mode)
*   [Node.js debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#nodejs-debugger)
*   [Adjust timeouts](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-timeouts)
*   [Adjust test speed](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-test-speed)
*   [Take screenshots on test failure](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#take-screenshots-on-test-failure)
*   [Skip JavaScript errors](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#skip-javascript-errors)

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#common-reasons-for-test-failure)Common reasons for test failure[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#common-reasons-for-test-failure)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most tests fail for one of the following reasons:

1.   [Element Selector issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#element-selector-issues)
2.   [Network issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#network-issues)
3.   [Browser issues](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-issues)
4.   [Application errors](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#application-errors)

If you don’t understand what causes a test to fail, try one of the following strategies:

*   Enter debug mode and [inspect the page](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode).
*   Take [screenshots and videos](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#take-screenshots-on-test-failure) of the test to capture the moment of failure.
*   Decrease [test execution speed](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-test-speed) to pinpoint the cause of failure.

If a test yields inconclusive results, determine the reason for its irregular behavior. If you can’t resolve the issue, [quarantine the test](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#quarantine-mode) to rule out false negatives.

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#element-selector-issues)Element Selector issues[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#element-selector-issues)

Actions and assertions use [Element Selector queries](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) to interact with the DOM. Imprecise and poorly written Element Selector queries may cause actions and assertions to fail or yield unexpected results.

*   Make sure that your Selectors adhere to [the recommended guidelines](https://testcafe.io/documentation/402836/guides/best-practices/best-practices#selector-strategy).
*   Use the [Visual Selector debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger) to troubleshoot Element Selector queries.
*   If your Selector query is correct, but TestCafe cannot find the page element in time, adjust the [Element Selector timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#selector-timeout). 
*   If an assertion fails before your application updates page content, adjust the [Assertion timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#assertion-timeout).

See also: [My tests fail because TestCafe cannot locate a page element. Why does this happen?](https://testcafe.io/documentation/403937/faq/working-with-testcafe#my-tests-fail-because-testcafe-cannot-locate-a-page-element-why-does-this-happen)

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#network-issues)Network issues[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#network-issues)

TestCafe tests fail when the browser fails to load a web page.

*   If your server is slow to respond, increase the [Page request timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-request-timeout) or the [AJAX request timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#ajax-request-timeout).
*   Enable the [Retry Test Pages](https://testcafe.io/documentation/402638/reference/configuration-file#retrytestpages) option to retry unsuccessful page requests.
*   If TestCafe routes your request through a low bandwidth [proxy](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#use-a-proxy), turn the proxy off, or [bypass](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-bypass-rules) the proxy when you access a particular resource.
*   TestCafe uses [two network ports](https://testcafe.io/documentation/402639/reference/command-line-interface#--ports-port1port2) in the [0 - 65535] range to automate browsers. TestCafe cannot run if your firewall blocks network activity on these ports.

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-issues)Browser issues[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-issues)

TestCafe tests fail when browsers disconnect or malfunction.

*   If you run multiple browsers concurrently, you may exhaust your system resources. Poor browser performance can negatively impact test performance. Decrease [the concurrency factor](https://testcafe.io/documentation/403626/guides/intermediate-guides/run-tests-concurrently) or run your browsers in [headless mode](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-in-headless-mode).
*   TestCafe fails when a browser does not initialize within the [browser initialization timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-initialization-timeout). Increase the timeout to account for slow browser performance.
*   TestCafe may experience performance issues if you minimize the browser window, or run the test in a background tab. The operating system detects that the browser runs in the background, and does not allocate the necessary amount of system resources to the test run.
*   TestCafe automatically restarts browsers that appear unresponsive. If TestCafe restarts your browser by mistake, enable [development mode](https://testcafe.io/documentation/402638/reference/configuration-file#developmentmode) to prevent this behavior.

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#application-errors)Application errors[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#application-errors)

*   If your application yields a JavaScript error, TestCafe fails the test. If you cannot fix the JavaScript error in question, enable the [skipJsErrors](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#skip-javascript-errors) option to let tests proceed.
*   If your application is slow to load, adjust the [page request timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-request-timeout).

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode)Debug mode[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![Image 1: Debug mode footer](https://testcafe.io/images/debug-mode.png)

If you launch TestCafe in [debug mode](https://testcafe.io/documentation/402639/reference/command-line-interface#-d---debug-mode), TestCafe pauses the test before the first action. You can then advance the test step by step, inspect the page, and use the [Visual Selector debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger).

TestCafe displays information about breakpoints in the test log:

![Image 2: Logging Debugger Breakpoints](https://testcafe.io/images/debugging/log-debugger.png)

Enable the `debugMode` setting to enter debug mode:

*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#-d---debug-mode)
```
testcafe chrome test.js --debug-mode
```
*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#debugmode)
```
{
    "debugMode": true
}
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ debugMode: true});
```

To enter debug mode on test failure, enable the `debugOnFail` option:

*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--debug-on-fail)
```
testcafe chrome tests/sample-fixture.js --debug-on-fail
```
*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#debugonfail)
```
{
    "debugOnFail": true
}
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ debugOnFail: true});
```

Use the [t.debug](https://testcafe.io/documentation/402707/reference/test-api/testcontroller/debug) action to manually add a breakpoint. If you include a Selector query as the argument, TestCafe automatically passes the query to the [Visual Selector Debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger).

```
fixture `Debugger example`
    .page `http://devexpress.github.io/testcafe/example/`;

test('Debugger', async t => {
    await t
        .debug()
        .setNativeDialogHandler(() => true)
        .click('#populate')
        .click('#submit-button');
});
```

Important

When you enter [debug mode](https://testcafe.io/documentation/402707/reference/test-api/testcontroller/debug) with [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) enabled, the web page **does not** freeze. The application reacts to clicks, hovers, and other interactions.

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger)Visual Selector debugger[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the [Visual Selector debugger](https://testcafe.io/documentation/404288/guides/intermediate-guides/visual-selector-debugger) to interactively debug and generate Selector queries.

*   Enter a Selector query to see page elements that match it.
*   Click a page element to generate a Selector query.
*   Click the “Hide Picker” button to disable the debugger and hide the Selector input field.

![Image 3: Enter a Selector query](https://testcafe.io/images/inspector/enter-query.gif)

If you pass a Selector query to the [t.debug()](https://testcafe.io/documentation/402707/reference/test-api/testcontroller/debug) method, TestCafe automatically inserts the query into the input field of the Visual Selector Debugger, and highlights page elements that match the query.

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#quarantine-mode)Quarantine mode[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#quarantine-mode)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enable quarantine mode to eliminate false negatives and detect unstable tests. When a test fails, TestCafe quarantines it, and repeats it until the test yields conclusive results.

Enable quarantine mode with the `-q (--quarantine-mode)` command line flag, the `quarantineMode` configuration file setting, or the `quarantineMode`[Test Runner](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) option:

*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#-q-attemptlimitvalue-successthresholdvalue2---quarantine-mode-attemptlimitvalue-successthresholdvalue2)
```
testcafe chrome ./tests/ -q
```
*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#quarantinemode)
```
{
    "quarantineMode": true
}
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ quarantineMode: true });
```

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#nodejs-debugger)Node.js debugger[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#nodejs-debugger)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can debug server-side code in Chrome Developer Tools and popular IDEs.

Important

Use the [Visual Selector debugger](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#visual-selector-debugger) to debug Element Selector queries.

Specify the [--inspect-brk](https://testcafe.io/documentation/402639/reference/command-line-interface#--inspect-brk) CLI flag to launch a Node.js debugger and use the [Google Chrome Developer Tools panel](https://testcafe.io/documentation/402801/recipes/debugging/chrome-dev-tools):

```
testcafe --inspect-brk chrome ./tests
```

![Image 4: Node.js debugger link](https://testcafe.io/images/node-debugger.png)

For more information on debugging Node.js code in your text editor, read the following tutorials:

*   [Visual Studio Code](https://testcafe.io/documentation/402800/recipes/debugging/visual-studio-code)
*   [WebStorm](https://testcafe.io/documentation/402799/recipes/debugging/webstorm)

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-timeouts)Adjust timeouts[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-timeouts)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

High timeout values may increase the total runtime of your test suite.

*   [Selector timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#selector-timeout)
*   [Assertion timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#assertion-timeout)
*   [Page load timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-load-timeout)
*   [Page request timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-request-timeout)
*   [AJAX request timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#ajax-request-timeout)
*   [Browser initialization timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-initialization-timeout)
*   [Test execution timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#test-execution-timeout)
*   [Run execution timeout](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#run-execution-timeout)

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#selector-timeout)Selector timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#selector-timeout)

If the action target is slow to appear, investigate the root cause of the issue. If you cannot improve the performance of your network or application, increase the **Selector timeout**.

If TestCafe fails to resolve an [element selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) query within the Selector timeout period, the test fails.

Default value: **10000 ms**

Specify the [timeout](https://testcafe.io/documentation/402756/reference/test-api/selector/constructor#optionstimeout) option to change the Selector timeout for an individual Selector query:

```
const footerSelector = Selector('#footer', { timeout: 20000 });
```

Use one of the following options to change the Selector timeout for the entire test run:

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#selectortimeout)
```
{
    "selectorTimeout": 3000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--selector-timeout-ms)
```
testcafe chrome my-tests --selector-timeout 500000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ selectorTimeout: 50000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#assertion-timeout)Assertion timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#assertion-timeout)

If an assertion fails because your application is slow to update its content, investigate the root cause of the issue. If you cannot improve the performance of your application, increase the **Assertion timeout**.

TestCafe executes [compatible assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) multiple times within the **Assertion timeout** period, repeating measurements and calculations with each attempt. If an assertion does not succeed, the test fails.

Default value: **3000 ms**

Specify the [timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#assertion-timeout) option to change the timeout for an individual assertion:

```
await t.expect(Selector('h1').innerText).eql('Hello World!', { timeout: 20000 });
```

Use one of the following options to change the assertion timeout for the entire test run:

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#assertiontimeout)
```
{
    "assertionTimeout": 1000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms)
```
testcafe chrome my-tests --assertion-timeout 10000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ assertionTimeout: 50000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-load-timeout)Page Load timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-load-timeout)

The **Page Load timeout** defines the maximum amount of time between the `DOMContentLoaded` event and the `window.load` event. TestCafe applies the timeout when the user delays test execution until the `window.loadEventRaised` event.

Default value: **3000 ms**

Use the [test.timeouts](https://testcafe.io/documentation/403062/reference/test-api/test/timeouts) method to change the page load timeout for an individual test:

```
test('My test', async () => {
    /* test code goes here */
}).timeouts({ pageLoadTimeout:    5000 });
```

Use one of the following options to change the page load timeout for the entire test run:

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#pageloadtimeout)
```
{
    "pageLoadTimeout": 5000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-load-timeout-ms)
```
testcafe chrome my-tests --page-load-timeout 5000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ assertionTimeout: 50000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#ajax-request-timeout)AJAX request timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#ajax-request-timeout)

If your application is slow to respond to AJAX requests, investigate the root cause of the issue. If you cannot improve the performance of your application, increase the **AJAX request timeout**.

If TestCafe does not resolve an XHR/Fetch request within the AJAX request timeout period, the test fails.

Default value: **120000 ms**

Use the [test.timeouts](https://testcafe.io/documentation/403062/reference/test-api/test/timeouts) method to change the AJAX request timeout for an individual test:

```
test('My test', async () => {
    /* test code goes here */
}).timeouts({ ajaxRequestTimeout:    5000 });
```

Use one of the following options to change the AJAX request timeout for the entire test run:

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#ajaxrequesttimeout)
```
{
    "ajaxRequestTimeout": 40000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--ajax-request-timeout-ms)
```
testcafe chrome my-tests --ajax-request-timeout 40000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ ajaxRequestTimeout: 50000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-request-timeout)Page request timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#page-request-timeout)

If your application is slow to respond to HTTP requests, investigate the root cause of the issue. If you cannot improve the performance of your application, increase the **Page request timeout**.

If the server does not fulfill a page request within the Page request timeout period, the test fails.

Default value: **25000 ms**

Use the [test.timeouts](https://testcafe.io/documentation/403062/reference/test-api/test/timeouts) method to change the page request timeout for an individual test:

```
test('My test', async () => {
    /* test code goes here */
}).timeouts({ pageRequestTimeout:    5000 });
```

Use one of the following options to change the page request timeout for the entire test run:

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#pagerequesttimeout)
```
{
    "pageRequestTimeout": 8000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-request-timeout-ms)
```
testcafe chrome my-tests --page-request-timeout 8000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ pageRequestTimeout: 8000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-initialization-timeout)Browser initialization timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#browser-initialization-timeout)

If your browser is slow to launch, investigate the root cause of the issue. If you cannot improve the performance of your testing environment, increase the **Browser initialization timeout**.

If one or more browsers fail to connect to TestCafe within the Browser initialization timeout period, the test run fails.

![Image 5: Browser init error](https://testcafe.io/images/browser-disconnection.png)

**Default value**: `120000` for [local browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers), `360000` for [remote browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers).

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#browserinittimeout)
```
{
    "browserInitTimeout": 180000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--browser-init-timeout-ms)
```
testcafe chrome my-tests --browser-init-timeout 180000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ browserInitTimeout: 8000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#test-execution-timeout)Test Execution timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#test-execution-timeout)

When the total execution time of a test exceeds the **Test Execution timeout**, TestCafe terminates the test, even if the browser is responsive.

Default value: **none (timeout disabled)**

Note

Continuous Integration systems offer built-in task runtime management capabilities. Use the Test Execution timeout when other options are not available.

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#testexecutiontimeout)
```
{
    "testExecutionTimeout": 180000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-execution-timeout-ms)
```
testcafe chrome my-tests --test-execution-timeout 180000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ testExecutionTimeout: 8000 });
```

### [](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#run-execution-timeout)Run Execution timeout[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#run-execution-timeout)

When the total execution time of a run exceeds the **Run Execution timeout**, TestCafe terminates the test run, even if the browsers are responsive.

Default value: **none (timeout disabled)**

Note

Continuous Integration systems offer built-in task runtime management capabilities. Use the Run Execution timeout when other options are not available.

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#runexecutiontimeout)
```
{
    "runExecutionTimeout": 180000
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--run-execution-timeout-ms)
```
testcafe chrome my-tests --run-execution-timeout 180000
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ runExecutionTimeout: 8000 });
```

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-test-speed)Adjust test speed[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-test-speed)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use the `speed` parameter to limit test execution speed. The parameter accepts values between `1` (the fastest speed, **default value**) and `0.01` (the slowest speed).

If you limit test execution speed, it is easier to notice differences in test behavior.

*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor)
```
testcafe chrome ./my-tests --speed 0.1
```
*   [Configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#speed)
```
{
    "speed": 0.1
}
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)
```
await runner.run({ speed: 0.1 });
```

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#take-screenshots-on-test-failure)Take screenshots on test failure[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#take-screenshots-on-test-failure)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Enable the `takeOnFails` option to take screenshots on test failure. Use the screenshots to determine the cause of the failure.

Additionally, you can record [test videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos) to review video footage of your tests.

Important

Video recording incurs a heavy system resource overhead. If you record too many videos simultaneously, test performance may suffer.

*   [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotstakeonfails)
```
{
    "screenshots": {
        "takeOnFails": true
    }
}
```
*   [Command Line Interface](https://testcafe.io/documentation/402639/reference/command-line-interface#takeonfails)
```
testcafe all tests/sample-fixture.js -s takeOnFails=true
```
*   [TestCafe Test Runner API](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)
```
runner.screenshots({
    takeOnFails: true
});
```

[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#skip-javascript-errors)Skip JavaScript errors[](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#skip-javascript-errors)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Main article: [Skip JavaScript Errors](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors)

TestCafe tests fail when a page yields a JavaScript error. Usually, errors are signs of malfunction that warrant action. However, in some cases third-party modules yield errors that the user cannot fix.

If you enable the `skipJsErrors` option, TestCafe deliberately **ignores** JavaScript errors and lets tests proceed.

*   Use the [CLI flag](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3), the [configuration file property](https://testcafe.io/documentation/402638/reference/configuration-file#skipjserrors), or the [Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#skipjserrors) to ignore JavaScript errors throughout your entire test suite.

*   Use the [fixture.skipJsErrors](https://testcafe.io/documentation/404025/reference/test-api/fixture/skipjserrors) method to ignore JavaScript errors for individual fixtures. 

*   Use the [test.skipJsErrors](https://testcafe.io/documentation/404026/reference/test-api/test/skipjserrors) method to ignore JavaScript errors in individual tests.

*   Use the [t.skipJsErrors](https://testcafe.io/documentation/404027/reference/test-api/testcontroller/skipjserrors) action to ignore JavaScript errors at specific points in the test.

For each of the methods above, you can define the following options:

*   The `pageUrl` option filters errors by page URL.
*   The `message` option filters errors by message.
*   The `stack` option filters errors by call stack.
