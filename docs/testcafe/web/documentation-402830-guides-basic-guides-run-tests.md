# Source: https://testcafe.io/documentation/402830/guides/basic-guides/run-tests

Title: Run Tests | Basic Guides | Guides

URL Source: https://testcafe.io/documentation/402830/guides/basic-guides/run-tests

Markdown Content:
[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#article-summary)Article Summary[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#article-summary)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are two ways to launch TestCafe tests.

1.   The simplest option is to use the `testcafe`[shell command](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface):

```
testcafe chrome test.js
```
2.   The [Test Runner API](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#test-runner-api) allows you to launch and configure TestCafe tasks with JavaScript code.

To launch TestCafe, specify the [target browser](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-target-browsers) and [test files](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-test-files).

To configure your test run, use the [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file), or specify [CLI options and flags](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#options-and-flags).

[Live mode](https://testcafe.io/documentation/403842/guides/intermediate-guides/live-mode) allows you to reload tests as you write them. [Quarantine mode](https://testcafe.io/documentation/403841/guides/intermediate-guides/quarantine-mode) retries failed tests to eliminate false negatives.

You can [run tests concurrently](https://testcafe.io/documentation/403626/guides/intermediate-guides/run-tests-concurrently) to speed up your test run.

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#table-of-contents)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Command Line Interface Overview](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface)
*   [Test Runner API Overview](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#test-runner-api)
*   [Select Target Browsers](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-target-browsers)
*   [Run tests in multiple browsers](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#run-tests-in-multiple-browsers)
*   [Select Test Files](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-test-files)
*   [Options and flags](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#options-and-flags)
*   [Alternative test modes](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#alternative-test-modes)
*   [Use a Proxy](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#use-a-proxy)
*   [View Test Results](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#view-test-results)
*   [Further Reading](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#further-reading)

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface)Command Line Interface[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The command line interface of TestCafe is simple and straightforward. For most users, it’s the preferred way to launch TestCafe tests.

```
testcafe <browsers> <test files> <options>
```

![Image 1: Test Launch](https://testcafe.io/images/test-launch.gif)

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#test-runner-api)Test Runner API[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#test-runner-api)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The **Test Runner API** is a Node.js API that can launch, configure and terminate TestCafe tests. It works with JavaScript and TypeScript.

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#advantages)Advantages[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#advantages)

The Test Runner has the following advantages over the [CLI](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface):

*   You can introduce additional logic to gain fine control over the execution of your test suite.
*   You can repeat the same test in a number of different run configurations without restarting it by hand.
*   You can integrate TestCafe with your favorite Node.js tools, such as `gulp`, `create-react-app`, or Angular Builders.
*   You can commit the test launch script to version control, with all the maintenance benefits that it entails.

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#quick-guide)Quick Guide[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#quick-guide)

1.   Use the `testcafe.createRunner` method to create a `Runner` instance.
2.   Add [configuration methods](https://testcafe.io/documentation/402641/reference/testcafe-api/runner).
    *   Use the `runner.src` to specify the test file path or directory.
    *   Use the `runner.browsers` method to specify the browser(s) you would like to run tests in.

3.   Call the `runner.run` method to run tests.
4.   If necessary, stop the test run with the `runner.stop` method.

The following example runs two test files in `chrome` and `safari`:

```
const createTestCafe = require('testcafe');
const testcafe = await createTestCafe('localhost', 1337, 1338);

try {
    const runner = testcafe.createRunner();

    const failed = await runner
        .src(["tests/fixture1.js", "tests/func/fixture3.js"])
        .browsers(["chrome", "edge"])
        .run();

    console.log('Tests failed: ' + failed);
}
finally {
    await testcafe.close();
}
```

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-target-browsers)Select Target Browsers[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-target-browsers)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe supports a [wide array of modern browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#browser-support). Additionally, you can run tests on [Mobile devices and mobile device emulators](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation). Read the advanced [Browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers) guide for more information about custom browsers, headless browsers, and more.

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli)CLI[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli)

Specify the [browser alias](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers) as the first command line argument.

```
testcafe chrome my-fixture.js
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner)Runner[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner)

Use the [runner.browsers](https://testcafe.io/documentation/402661/reference/testcafe-api/runner/browsers) method to select the target browser:

```
await runner
    .browsers('chrome')
    .src('./tests/')
    .run();
```

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#run-tests-in-multiple-browsers)Run tests in multiple browsers[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#run-tests-in-multiple-browsers)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TestCafe uses [Native Automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) to run tests in local Chromium-based browsers. Native automation increases test speed and stability. To run tests in multiple Chromium-based browsers, separate browser aliases with a comma:

```
# CLI
testcafe chrome,edge my-fixture.js
```

```
/* TestCafe Test Runner */
await runner
    .browsers(['chrome', 'edge'])
    .src('./tests/')
    .run();
```

If your browser string includes non-Chromium-based browsers, TestCafe **disables** Native Automation:

```
testcafe chrome,firefox my-fixture.js # Runs without native automation.
```

If you want to run tests in non-Chromium-based browsers **and** take advantage of Native Automation, [create two separate test runs](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode):

```
testcafe chrome,edge my-fixture.js # Chromium-based browsers
testcafe firefox,safari my-fixture.js --disable-native-automation # Other browsers
```

Use the `all` alias to launch the test in all your local browsers:

```
testcafe all my-fixture.js
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file)Configuration file[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file)

Warning

Command line options and Test Runner options have precedence over configuration file settings. When TestCafe overrides a configuration file setting, it outputs a description of the conflict to the console.

Use the [browsers](https://testcafe.io/documentation/402638/reference/configuration-file#browsers) configuration file option to select the target browser in your configuration file:

```
{
    "browsers": "chrome"
}
```

Pass an array of browser aliases to select multiple browsers:

```
{
    "browsers": ["ie", "firefox"]
}
```

If you specify target browsers in a configuration file, you can omit the [corresponding CLI option](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-target-browsers).

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-test-files)Select Test Files[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-test-files)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

Use [filters](https://testcafe.io/documentation/403436/guides/intermediate-guides/metadata-and-filtering) to only launch tests that meet certain criteria.

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli-1)CLI[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli-1)

Include the path to the test file or directory as the second command line argument:

```
testcafe chrome my-fixture.js
```

You can specify multiple test files and directories:

```
testcafe safari my-fixture.js ./studio/tests
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner-1)Runner[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner-1)

Use the [runner.src](https://testcafe.io/documentation/402653/reference/testcafe-api/runner/src) method to specify test files and test file directories:

```
await runner
    .src('my-fixture.js')
    .browsers('chrome')
    .run();
```

If you want to specify multiple test files and directories, store them in an array:

```
await runner
    .browsers('safari')
    .src(['my-fixture.js', './studio/tests'])
    .run();
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file-1)Configuration File[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file-1)

Warning

Command line options and Test Runner options have precedence over configuration file settings. When TestCafe overrides a configuration file setting, it outputs a description of the conflict to the console.

Use the [src](https://testcafe.io/documentation/402638/reference/configuration-file#test-files) configuration file option to specify test files and test file directories in your configuration file:

```
{
    "src": "/home/user/tests/fixture.js"
}
```

If you want to specify multiple test files and directories, store them in an array:

```
{
    "src": ["/home/user/auth-tests/fixture.testcafe", "/home/user/mobile-tests/"]
}
```

If you specify test files in a configuration file, you can omit the [corresponding CLI option](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#select-test-files).

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#options-and-flags)Options and flags[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#options-and-flags)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

There are several ways to configure your test run. Both [CLI](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#command-line-interface) users and [Runner](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#test-runner-api) users can save their settings to a [configuration file](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file-2).

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli-2)CLI[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#cli-2)

CLI users can specify [command line options](https://testcafe.io/documentation/402639/reference/command-line-interface). The example below executes tests from the `my-tests` folder at the `0.1` speed.

```
testcafe chrome my-tests --speed 0.1
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner-2)Runner[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#runner-2)

Test Runner users can pass [Test Runner Options](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) to the `runner.run` method. The example below executes tests from the `my-tests` folder at the `0.1` speed:

```
const createTestCafe = require('testcafe');
const testcafe = await createTestCafe('localhost', 1337, 1338);

try {
    const runner = testcafe.createRunner();

    const failed = await runner
        .src(["my-tests"])
        .browsers(["chrome", "edge"])
        .run({
        speed: 0.1
    });

    console.log('Tests failed: ' + failed);
}
finally {
    await testcafe.close();
}
```

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file-2)Configuration File[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#configuration-file-2)

Warning

Command line options and Test Runner options have precedence over configuration file settings. When TestCafe overrides a configuration file setting, it outputs a description of the conflict to the console.

Use the configuration file to store test settings:

```
{
    "browsers": ["chrome", "safari"],
    "src": "/home/user/tests/fixture.js",
    "speed": 0.1
}
```

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#alternative-test-modes)Alternative test modes[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#alternative-test-modes)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#live-mode)Live Mode[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#live-mode)

> Main article: [Live Mode](https://testcafe.io/documentation/403842/guides/intermediate-guides/live-mode)

When you run TestCafe in Live Mode, TestCafe restarts your test suite every time you change the test code.

![Image 2: Live mode in action](https://testcafe.io/images/testcafe-live.gif)

When the test is over, TestCafe keeps the page open so you can inspect it.

To start TestCafe in live mode, use the [-L (--live)](https://testcafe.io/documentation/402639/reference/command-line-interface#-l---live) CLI flag or the [testcafe.createLiveModeRunner](https://testcafe.io/documentation/402645/reference/testcafe-api/testcafe/createlivemoderunner) Test Runner API function.

### [](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#quarantine-mode)Quarantine Mode[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#quarantine-mode)

> Main article: [Quarantine Mode](https://testcafe.io/documentation/403841/guides/intermediate-guides/quarantine-mode)

Enable quarantine mode to _eliminate false negatives_ and _detect unstable tests_. When a test fails, TestCafe **quarantines** it, and **repeats** it until the test yields conclusive results.

To start TestCafe in quarantine mode, use the [-q (--quarantine-mode)](https://testcafe.io/documentation/402639/reference/command-line-interface#-q-attemptlimitvalue-successthresholdvalue2---quarantine-mode-attemptlimitvalue-successthresholdvalue2) CLI flag, or the `quarantineMode`[Test Runner API](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) option.

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#use-a-proxy)Use a Proxy[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#use-a-proxy)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important

When TestCafe uses [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode), it cannot route HTTP requests through a **proxy**. Use the built-in capabilities of your operating system to configure a proxy connection.

If your network uses a proxy to access the test page, you need to specify the proxy URL. Use the [--proxy](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-host) command line argument or the [runner.useProxy](https://testcafe.io/documentation/402649/reference/testcafe-api/runner/useproxy) API method:

```
testcafe chrome ./my-tests/ --proxy proxy.mycompany.com
```

```
await runner
    .browsers('chrome')
    .src('./my-tests/')
    .useProxy('proxy.mycompany.com')
    .run();
```

You can also specify URLs that should bypass the proxy. Pass the list of URLs in the [--proxy-bypass](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-bypass-rules) command line argument or a [runner.useProxy](https://testcafe.io/documentation/402649/reference/testcafe-api/runner/useproxy) parameter:

```
testcafe chrome ./my-tests/ --proxy proxy.corp.mycompany.com --proxy-bypass localhost:8080
```

```
await runner
    .browsers('chrome')
    .src('./my-tests/')
    .useProxy('proxy.corp.mycompany.com', 'localhost:8080')
    .run();
```

You can also specify the proxy URL in the [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#proxy).

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#view-test-results)View Test Results[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#view-test-results)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When the test run is over, TestCafe displays the test report in the command shell. The [reporter](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters) determines the format of the output. TestCafe includes five built-in reporters.

The following screenshot shows the result of a successful test, as reported by [spec](https://github.com/DevExpress/testcafe-reporter-spec), the default reporter.

![Image 3: Test Report](https://testcafe.io/images/report.png)

If a test fails, TestCafe outputs the error and highlights the failed action:

![Image 4: Test failure](https://testcafe.io/images/report-failure.png)

Feel free to create a [custom reporter plugin](https://testcafe.io/documentation/402810/guides/extend-testcafe/reporter-plugin), or use one of the [community reporters](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters).

[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#further-reading)Further Reading[](https://testcafe.io/documentation/402830/guides/basic-guides/run-tests#further-reading)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   Learn how to [run tests concurrently](https://testcafe.io/documentation/403626/guides/intermediate-guides/run-tests-concurrently).
*   Learn how to use [live mode](https://testcafe.io/documentation/403842/guides/intermediate-guides/live-mode) to reload tests as you write them.
*   Learn how to [quarantine tests](https://testcafe.io/documentation/403841/guides/intermediate-guides/quarantine-mode) to eliminate false negatives.
*   Learn how to [execute shell commands on startup](https://testcafe.io/documentation/403849/guides/advanced-guides/execute-shell-commands-on-startup) to deploy your app before the test run.
