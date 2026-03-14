# Source: https://testcafe.io/documentation/402639/reference/command-line-interface

Title: Command Line Interface | API

URL Source: https://testcafe.io/documentation/402639/reference/command-line-interface

Published Time: Mon, 09 Mar 2026 04:07:34 GMT

Markdown Content:
Use the command line interface to launch and configure TestCafe.

The following shell command launches the `test.js` test in Chrome and MS Edge:

```
testcafe chrome,edge test.js
```

Add flags to specify test run settings:

```
testcafe chrome,edge test.js --live
```

Note

Create a [TestCafe configuration file](https://testcafe.io/documentation/402638/reference/configuration-file) to conveniently store and reuse TestCafe settings. You can commit the configuration file to version control.

Important

CLI options and [TestCafe Runner options](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run) have precedence over [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file) settings. When TestCafe overrides a configuration file setting, it outputs a description of the conflict to the console.

[](https://testcafe.io/documentation/402639/reference/command-line-interface#table-of-contents)Table of Contents[](https://testcafe.io/documentation/402639/reference/command-line-interface#table-of-contents)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   [Browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#browsers)
    *   [Local browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers)
    *   [Local browsers with a custom path](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers-with-a-custom-path)
    *   [Cloud browsers, custom browsers, remote browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers)
    *   [Headless mode, emulation mode, user profiles](https://testcafe.io/documentation/402639/reference/command-line-interface#headless-mode-emulation-mode-user-profiles)
    *   [Browser options](https://testcafe.io/documentation/402639/reference/command-line-interface#browser-options)

*   [Test files](https://testcafe.io/documentation/402639/reference/command-line-interface#test-files)
*   [Other options](https://testcafe.io/documentation/402639/reference/command-line-interface#other-options)
    *   [Help and information](https://testcafe.io/documentation/402639/reference/command-line-interface#help-and-information)
    *   [Configuration file settings](https://testcafe.io/documentation/402639/reference/command-line-interface#configuration-file-settings)
    *   [Advanced browser settings](https://testcafe.io/documentation/402639/reference/command-line-interface#advanced-browser-settings)
    *   [Filter tests and fixtures by name, grep pattern, or metadata](https://testcafe.io/documentation/402639/reference/command-line-interface#filter-tests-and-fixtures-by-name-grep-pattern-or-metadata)
    *   [Reporters](https://testcafe.io/documentation/402639/reference/command-line-interface#reporters)
    *   [Base URL](https://testcafe.io/documentation/402639/reference/command-line-interface#base-url)
    *   [Screenshots and videos](https://testcafe.io/documentation/402639/reference/command-line-interface#screenshots-and-videos)
    *   [Debugging settings](https://testcafe.io/documentation/402639/reference/command-line-interface#debugging-settings)
    *   [Timeouts](https://testcafe.io/documentation/402639/reference/command-line-interface#timeouts)
    *   [Automation settings](https://testcafe.io/documentation/402639/reference/command-line-interface#automation-settings)
    *   [JavaScript settings](https://testcafe.io/documentation/402639/reference/command-line-interface#javascript-settings)
    *   [TypeScript settings](https://testcafe.io/documentation/402639/reference/command-line-interface#typescript-settings)
    *   [Client scripts](https://testcafe.io/documentation/402639/reference/command-line-interface#client-scripts)
    *   [Initialization settings](https://testcafe.io/documentation/402639/reference/command-line-interface#initialization-settings)
    *   [CLI output settings](https://testcafe.io/documentation/402639/reference/command-line-interface#cli-output-settings)

[](https://testcafe.io/documentation/402639/reference/command-line-interface#browsers)Browsers[](https://testcafe.io/documentation/402639/reference/command-line-interface#browsers)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Main article: [Browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers)

Important

When you launch TestCafe v3.0.0 and up, the framework engages [Native Automation mode](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) to automate Chromium-based browsers with the native CDP protocol.

If your browser selection includes other browsers, TestCafe **disables** native autiomation.

If you want to run tests in non-Chromium-based browsers **and** take advantage of Native Automation, [create two separate test runs](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode):

```
testcafe chrome,edge test.js; 
testcafe firefox,safari test.js --disable-native-automation
```

Pass a list of browsers to the `testcafe` command:

```
testcafe chrome,edge test.js
```

If you use a [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#browsers) to specify browsers for the test run, you can omit this option:

```
testcafe test.js
```

*   [Local browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers)
*   [Local browsers with a custom path](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers-with-a-custom-path)
*   [Cloud browsers, custom browsers, remote browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers)
*   [Headless mode, emulation mode, user profiles](https://testcafe.io/documentation/402639/reference/command-line-interface#headless-mode-emulation-mode-user-profiles)
*   [Browser options](https://testcafe.io/documentation/402639/reference/command-line-interface#browser-options)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers)Local browsers[](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers)

TestCafe detects compatible local browsers on startup. Use the `-b` (`--list-browsers`) option to view the list of available local browsers:

```
testcafe --list-browsers
```

To launch a local browser, pass the browser’s alias to the `testcafe` command:

```
testcafe chrome test.js
```

To launch multiple local browsers, separate their aliases with a comma:

```
testcafe chrome,edge test.js
```

To launch tests in every detected browser, specify the `all` alias:

```
testcafe all test.js
```

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers-with-a-custom-path)Local browsers with a custom path[](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers-with-a-custom-path)

Specify the path to a custom browser executable with the `path:` prefix.

If you use a _*NIX shell_ or _Microsoft PowerShell_, enclose the entire string, including the `path` prefix, in single quotes:

```
testcafe 'path:/Users/TestCafe/Apps/firefox-beta.app' test.js
```

If you use _cmd.exe_, enclose the entire string, including the `path` prefix, in double quotes:

```
testcafe "path:d:\firefoxportable\firefoxportable.exe" test.js
```

If the path includes spaces, enclose it in backticks:

```
testcafe 'path:`/Users/TestCafe/Apps/Firefox Beta.app`' test.js
```

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers)Cloud browsers, custom browsers, remote browsers[](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers)

Note

Disable [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) to launch tests in mobile browsers, cloud browsers, and remote browsers.

To launch a browser that requires a [browser provider plugin](https://testcafe.io/documentation/402812/guides/extend-testcafe/browser-provider-plugin), prefix the browser alias with the name of the plugin:

```
testcafe "saucelabs:Chrome@52.0:Windows 8.1" test.js
```

TestCafe can run tests in [remote browsers](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation#remote-and-mobile-devices). Use the `remote` browser alias to generate remote test URLs. Specify the number of remote browser instances after the colon. If you use [concurrency](https://testcafe.io/documentation/402639/reference/command-line-interface#-c-n---concurrency-n), multiply the number of unique remote browsers by the concurrency factor.

```
testcafe remote:3 test.js
```

When you specify the `remote` browser alilas, TestCafe outputs a list of test URLs — one for each remote browser instance. If you use the [--qr-code](https://testcafe.io/documentation/402639/reference/command-line-interface#--qr-code) option, TestCafe displays these URLs as QR codes.

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#headless-mode-emulation-mode-user-profiles)Headless mode, emulation mode, user profiles[](https://testcafe.io/documentation/402639/reference/command-line-interface#headless-mode-emulation-mode-user-profiles)

To launch a browser in [headless](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers#test-in-headless-mode) mode, [emulate a mobile device](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation#simulate-devices-with-chromium), or enable [user profiles](https://testcafe.io/documentation/403584/guides/intermediate-guides/mobile-devices-cloud-browsers-and-emulation#user-profile), append the corresponding keyword to the browser alias:

```
testcafe 'firefox:headless','chrome:emulation:device=iphone X' test.js
```

Note

If you [specify a custom path](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers-with-a-custom-path) to the browser executable, you cannot take advantage of this capability.

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#browser-options)Browser options[](https://testcafe.io/documentation/402639/reference/command-line-interface#browser-options)

You can specify CLI arguments for every browser that you launch. Use single quotes in a _*NIX shell_ or _Microsoft PowerShell_:

```
testcafe 'chrome --start-fullscreen' test.js
```

Use double quotes in _cmd.exe_:

```
testcafe "chrome --start-fullscreen" test.js
```

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#other-interfaces)Other interfaces[](https://testcafe.io/documentation/402639/reference/command-line-interface#other-interfaces)

_Configuration file parameter_: [browsers](https://testcafe.io/documentation/402638/reference/configuration-file#browsers)

_API_: [runner.browsers](https://testcafe.io/documentation/402661/reference/testcafe-api/runner/browsers), [BrowserConnection](https://testcafe.io/documentation/402643/reference/testcafe-api/browserconnection)

[](https://testcafe.io/documentation/402639/reference/command-line-interface#test-files)Test files[](https://testcafe.io/documentation/402639/reference/command-line-interface#test-files)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The TestCafe framework supports the following test file formats:

*   JavaScript
*   TypeScript
*   CoffeeScript
*   [TestCafe Studio](https://www.devexpress.com/products/testcafestudio/) tests (`.testcafe` files)

You can [filter](https://testcafe.io/documentation/402639/reference/command-line-interface#filter-tests-and-fixtures-by-name-grep-pattern-or-metadata) tests and fixtures by name, grep pattern, or metadata.

Pass a path to the `testcafe` command to specify a single test file or folder:

```
testcafe chrome /Users/TestCafe/tests
```

Separate multiple paths with a space:

```
testcafe chrome my-test.js /Users/TestCafe/tests/
```

Alternatively, specify a set of files with a [glob pattern](https://github.com/isaacs/node-glob#glob-primer):

```
testcafe chrome 'tests/*page*'
```

Enclose glob patterns in single quotes to prevent automatic [glob pattern expansion](https://medium.com/@jakubsynowiec/you-should-always-quote-your-globs-in-npm-scripts-621887a2a784).

If you use a [configuration file](https://testcafe.io/documentation/402638/reference/configuration-file#browsers) to specify test files, you can omit this option:

```
testcafe chrome
```

_Configuration file parameter_: [src](https://testcafe.io/documentation/402638/reference/configuration-file#test-files)

_API_: [runner.src](https://testcafe.io/documentation/402653/reference/testcafe-api/runner/src)

[](https://testcafe.io/documentation/402639/reference/command-line-interface#other-options)Other options[](https://testcafe.io/documentation/402639/reference/command-line-interface#other-options)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Note

Create a [TestCafe configuration file](https://testcafe.io/documentation/402638/reference/configuration-file) to conveniently store and reuse TestCafe settings. You can commit the configuration file to version control.

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#help-and-information)Help and information[](https://testcafe.io/documentation/402639/reference/command-line-interface#help-and-information)

*   [-h (--help)](https://testcafe.io/documentation/402639/reference/command-line-interface#-h---help)
*   [-v (--version)](https://testcafe.io/documentation/402639/reference/command-line-interface#-v---version)
*   [-b (--list-browsers)](https://testcafe.io/documentation/402639/reference/command-line-interface#-b---list-browsers)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-h---help)-h, --help[](https://testcafe.io/documentation/402639/reference/command-line-interface#-h---help)

Displays the help screen.

```
testcafe --help
```

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-v---version)-v, --version[](https://testcafe.io/documentation/402639/reference/command-line-interface#-v---version)

Displays the TestCafe version.

```
testcafe --version
```

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-b---list-browsers)-b, --list-browsers[](https://testcafe.io/documentation/402639/reference/command-line-interface#-b---list-browsers)

Displays the list of [compatible local browsers](https://testcafe.io/documentation/402828/guides/intermediate-guides/browsers).

```
testcafe --list-browsers
```

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#configuration-file-settings)Configuration file settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#configuration-file-settings)

> Main article: [Configuration File](https://testcafe.io/documentation/402638/reference/configuration-file)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--config-file-path)--config-file <path>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--config-file-path)

To use a [TestCafe configuration file](https://testcafe.io/documentation/402638/reference/configuration-file) with a custom name or location, pass its path to the `--config-file` option.

```
testcafe --config-file /Users/foobar/dotfiles/.testcaferc.json
```

_API_: [configFile](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#advanced-browser-settings)Advanced browser settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#advanced-browser-settings)

*   [—concurrency](https://testcafe.io/documentation/402639/reference/command-line-interface#-c-n---concurrency-n)
*   [--qr-code](https://testcafe.io/documentation/402639/reference/command-line-interface#--qr-code)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-c-n---concurrency-n)-c <n>, --concurrency <n>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-c-n---concurrency-n)

Set the `concurrency` parameter to run multiple instances of the same browser simultaneously. Read the [Concurrent Test Execution](https://testcafe.io/documentation/403626/guides/intermediate-guides/run-tests-concurrently) guide for more information.

Note

Concurrent test execution is not suitable for tests that can only run in a certain order. To override this setting for a particular fixture, use the [disableConcurrency](https://testcafe.io/documentation/404618/reference/test-api/fixture/disableconcurrency) fixture method.

```
testcafe -c 3 chrome test.js
```

_Configuration file parameter_: [concurrency](https://testcafe.io/documentation/402638/reference/configuration-file#concurrency)

_API_: [runner.concurrency](https://testcafe.io/documentation/402658/reference/testcafe-api/runner/concurrency)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--qr-code)--qr-code[](https://testcafe.io/documentation/402639/reference/command-line-interface#--qr-code)

TestCafe can run tests in remote browsers. If you enable the `--qr-code` option, TestCafe outputs QR codes with remote connection URLs to the command line.

```
testcafe remote my-tests --qr-code
```

![Image 1: QR code in the CLI](https://testcafe.io/images/qr.png)

_Configuration file parameter_: [qrCode](https://testcafe.io/documentation/402638/reference/configuration-file#qrcode)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#filter-tests-and-fixtures-by-name-grep-pattern-or-metadata)Filter tests and fixtures by name, grep pattern, or metadata[](https://testcafe.io/documentation/402639/reference/command-line-interface#filter-tests-and-fixtures-by-name-grep-pattern-or-metadata)

> Main article: [Metadata and Filtering](https://testcafe.io/documentation/403436/guides/intermediate-guides/metadata-and-filtering)

*   [-t (--test)](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-name---test-name)
*   [-f (--fixture)](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-name---fixture-name)
*   [-T (--test-grep)](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-pattern---test-grep-pattern)
*   [-F (--fixture-grep)](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-pattern---fixture-grep-pattern)
*   [--test-meta](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-meta-keyvaluekey2value2)
*   [--fixture-meta](https://testcafe.io/documentation/402639/reference/command-line-interface#--fixture-meta-keyvaluekey2value2)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-name---test-name)-t <name>, --test <name>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-name---test-name)

Use the `-t (--test)` option to run a test with the specified name.

```
testcafe chrome test.js -t "Click a label"
```

_Configuration file parameter_: [filter.test](https://testcafe.io/documentation/402638/reference/configuration-file#filter-tests-by-name)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-name---fixture-name)-f <name>, --fixture <name>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-name---fixture-name)

Use the `-f (--fixture)` option to run a fixture with the specified name.

```
testcafe chrome my-tests -f "Sample fixture"
```

_Configuration file parameter_: [filter.fixture](https://testcafe.io/documentation/402638/reference/configuration-file#filter-fixtures-by-name)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-pattern---test-grep-pattern)-T <pattern>, --test-grep <pattern>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-t-pattern---test-grep-pattern)

Use the `-T (--test-grep)` option to filter tests by grep pattern.

The following command launches tests with names that match the `Click.*` grep pattern (`Click a label`, `Click a button`, etc.):

```
testcafe chrome my-tests -T "Click.*"
```

_Configuration file parameter_: [filter.testGrep](https://testcafe.io/documentation/402638/reference/configuration-file#filter-tests-by-grep-pattern)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-pattern---fixture-grep-pattern)-F <pattern>, --fixture-grep <pattern>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-f-pattern---fixture-grep-pattern)

Use the `-F (--fixture-grep)` option to filter fixtures by grep pattern.

The following command launches fixtures with names that match the `Page.*` grep pattern (`Page 1`, `Page 2`, etc.):

```
testcafe chrome my-tests -F "Page.*"
```

_Configuration file parameter_: [filter.fixtureGrep](https://testcafe.io/documentation/402638/reference/configuration-file#filter-fixtures-by-grep-pattern)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-meta-keyvaluekey2value2)--test-meta <key=value[,key2=value2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-meta-keyvaluekey2value2)

Use the `--test-meta` option to filter tests by [metadata](https://testcafe.io/documentation/403436/guides/intermediate-guides/metadata-and-filtering).

The example below instructs TestCafe to run tests that meet the following requirements:

*   The value of the `device` metadata property is `mobile`.
*   The value of the `env` metadata property is `production`.

```
testcafe chrome my-tests --test-meta device=mobile,env=production
```

_Configuration file parameter_: [filter.testMeta](https://testcafe.io/documentation/402638/reference/configuration-file#filter-tests-by-metadata)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--fixture-meta-keyvaluekey2value2)--fixture-meta <key=value[,key2=value2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--fixture-meta-keyvaluekey2value2)

Use the `--fixture-meta` option to filter fxitures by [metadata](https://testcafe.io/documentation/403436/guides/intermediate-guides/metadata-and-filtering).

The example below instructs TestCafe to run tests that meet the following requirements:

*   The value of the `device` metadata property is `mobile`.
*   The value of the `env` metadata property is `production`.

```
testcafe chrome my-tests --fixture-meta device=mobile,env=production
```

_Configuration file parameter_: [filter.fixtureMeta](https://testcafe.io/documentation/402638/reference/configuration-file#filter-fixtures-by-metadata)

_API_: [runner.filter](https://testcafe.io/documentation/402657/reference/testcafe-api/runner/filter)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#reporters)Reporters[](https://testcafe.io/documentation/402639/reference/command-line-interface#reporters)

> Main article: [Reporters](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-r-nameoutput---reporter-nameoutput)-r <name[:output],[…]>, --reporter <name[:output],[…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-r-nameoutput---reporter-nameoutput)

Use the `-r (--reporter)` option to select a [test reporter](https://testcafe.io/documentation/402825/guides/intermediate-guides/reporters).

The following command generates a test report in the `xunit` format:

```
testcafe chrome test.js -r xunit
```

Reporters output data to `stdout`. To save report data to a file, specify the filename after the colon:

```
testcafe all tests/sample-fixture.js -r json:report.json
```

You can use multiple test reporters simultaneously. However, only one reporter at a time can output data to `stdout`. Define a filename for each subsequent reporter:

```
testcafe all tests/sample-fixture.js -r spec,xunit:report.xml
```

_Configuration file parameter_: [reporter](https://testcafe.io/documentation/402638/reference/configuration-file#reporters)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#base-url)Base URL[](https://testcafe.io/documentation/402639/reference/command-line-interface#base-url)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--base-url)--base-url[](https://testcafe.io/documentation/402639/reference/command-line-interface#--base-url)

The `--base-url` option defines the starting URL of every fixture and test in your test suite. Additionally, the option enables you to use _relative_[Role URLs](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication).

To [override this setting](https://testcafe.io/documentation/402831/guides/basic-guides/test-structure#relative-test-url), use the [fixture.page](https://testcafe.io/documentation/402778/reference/test-api/fixture/page) and [test.page](https://testcafe.io/documentation/402732/reference/test-api/test/page) methods.

```
testcafe all tests/sample-fixture.js --base-url https://devexpress.github.io/testcafe
```

_Configuration file parameter_: [baseUrl](https://testcafe.io/documentation/402638/reference/configuration-file#base-url).

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#screenshots-and-videos)Screenshots and videos[](https://testcafe.io/documentation/402639/reference/command-line-interface#screenshots-and-videos)

> Main article: [Screenshots and videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos)

*   [-s (--screenshots)](https://testcafe.io/documentation/402639/reference/command-line-interface#-s---screenshots-optionvalueoption2value2)
*   [--disable-screenshots](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-screenshots)
*   [--video](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-basepath)
*   [--video-options](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-options-optionvalueoption2value2)
*   [--video-encoding-options](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-encoding-options-optionvalueoption2value2)

The following options have been **deprecated** in TestCafe v1.5.0 and higher:

*   [-s (--screenshots) <path>](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s-path---screenshots-path)
*   [-S (--screenshots-on-fails)](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s---screenshots-on-fails)
*   [-p (--pattern, --screenshot-path-pattern)](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--p-pattern---screenshot-path-pattern-pattern)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-s---screenshots-optionvalueoption2value2)-s, --screenshots <option=value[,option2=value2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-s---screenshots-optionvalueoption2value2)

Use the `--screenshots` option to specify [screenshot](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#screenshots) settings.

```
testcafe all tests/sample-fixture.js -s path=artifacts/screenshots,takeOnFails=true
```

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#path)path[](https://testcafe.io/documentation/402639/reference/command-line-interface#path)

The `path` option specifies the screenshot storage folder:

```
testcafe all tests/sample-fixture.js -s path=artifacts/screenshots
```

_Configuration file parameter_: [screenshots.path](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotspath)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#takeonfails)takeOnFails[](https://testcafe.io/documentation/402639/reference/command-line-interface#takeonfails)

Enable the `takeOnFails` option to take screenshots on test failure:

```
testcafe all tests/sample-fixture.js -s takeOnFails=true
```

_Configuration file parameter_: [screenshots.takeOnFails](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotstakeonfails)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#pathpattern)pathPattern[](https://testcafe.io/documentation/402639/reference/command-line-interface#pathpattern)

Set the `pathPattern` option to define a [custom naming pattern](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#path-pattern-placeholders) for screenshot files. Enclose the pattern in quotes:

```
testcafe all tests/sample-fixture.js -s pathPattern='${DATE} ${TIME}/test ${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png' # *NIX shells (single quotes)
testcafe all tests/sample-fixture.js -s pathPattern="${DATE} ${TIME}/test ${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png" # cmd.exe (double quotes)
```

_Configuration file parameter_: [screenshots.pathPattern](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotspathpattern)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#pathpatternonfails)pathPatternOnFails[](https://testcafe.io/documentation/402639/reference/command-line-interface#pathpatternonfails)

Set the `pathPatternOnFails` option to define a custom naming pattern for screenshots taken on test failure.

If you set both the `pathPattern` option and the `pathPatternOnFails` option, the latter takes precedence in the event of test failure.

```
testcafe all tests/sample-fixture.js -s pathPatternOnFails=${DATE}_${TIME}/failedTests/test-${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png
```

_Configuration file parameter_: [screenshots.pathPatternOnFails](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotspathpatternonfails)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#fullpage)fullPage[](https://testcafe.io/documentation/402639/reference/command-line-interface#fullpage)

Enable the `fullPage` option to capture screenshots of the entire page.

```
testcafe all tests/sample-fixture.js -s fullPage=true
```

_Configuration file parameter_: [screenshots.fullPage](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotsfullpage)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#thumbnails)thumbnails[](https://testcafe.io/documentation/402639/reference/command-line-interface#thumbnails)

Enable the `thumbnails` option to generate thumbnail copies of every screenshot.

```
testcafe all tests/sample-fixture.js -s thumbnails=false
```

_Configuration file parameter_: [screenshots.thumbnails](https://testcafe.io/documentation/402638/reference/configuration-file#screenshotsthumbnails)

_API_: [runner.screenshots](https://testcafe.io/documentation/402654/reference/testcafe-api/runner/screenshots)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-screenshots)--disable-screenshots[](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-screenshots)

If you enable the `disableScreenshots` option, TestCafe ignores the [t.screenshot() action](https://testcafe.io/documentation/402675/reference/test-api/testcontroller/takescreenshot) and the [takeOnFails](https://testcafe.io/documentation/402639/reference/command-line-interface#takeonfails) option.

```
testcafe all tests/sample-fixture.js --disable-screenshots
```

_Configuration file parameter_: [disableScreenshots](https://testcafe.io/documentation/402638/reference/configuration-file#disablescreenshots)

_API_: [runner.run({ disableScreenshots })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-basepath)--video <basePath>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-basepath)

Use the `--video` option to record videos of test runs and store them in the specified directory.

```
testcafe chrome test.js --video reports/screen-captures
```

See [Record Videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#record-videos) for details.

_Configuration file parameter_: [videoPath](https://testcafe.io/documentation/402638/reference/configuration-file#videopath)

_API_: [runner.video](https://testcafe.io/documentation/402648/reference/testcafe-api/runner/video)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-options-optionvalueoption2value2)--video-options <option=value[,option2=value2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-options-optionvalueoption2value2)

Note

The `--video-options` parameter has no effect unless you enable video recording with the [--video](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-basepath) option.

Specifies video recording options. See the [Record Videos](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#basic-video-options) guide for the full list of available options.

```
testcafe chrome test.js --video videos --video-options singleFile=true,failedOnly=true
```

Enclose parameter values in quotes if they contain spaces:

```
testcafe chrome test.js --video videos --video-options pathPattern='${DATE} ${TIME}/test ${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png' # *NIX shells (single quotes)
testcafe chrome test.js --video videos --video-options pathPattern="${DATE} ${TIME}/test ${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png" # cmd.exe (double quotes)
```

_Configuration file parameter_: [videoOptions](https://testcafe.io/documentation/402638/reference/configuration-file#videooptions)

_API_: [runner.video](https://testcafe.io/documentation/402648/reference/testcafe-api/runner/video)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-encoding-options-optionvalueoption2value2)--video-encoding-options <option=value[,option2=value2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-encoding-options-optionvalueoption2value2)

Note

The `--video-encoding-options` parameter has no effect unless you enable video recording with the [--video](https://testcafe.io/documentation/402639/reference/command-line-interface#--video-basepath) option.

Specifies video encoding options. Refer to [the FFmpeg documentation](https://ffmpeg.org/ffmpeg.html#Options) for the full list of available options.

```
testcafe chrome test.js --video videos --video-encoding-options r=20,aspect=4:3
```

_Configuration file parameter_: [videoEncodingOptions](https://testcafe.io/documentation/402638/reference/configuration-file#videoencodingoptions)

_API_: [runner.video](https://testcafe.io/documentation/402648/reference/testcafe-api/runner/video)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s-path---screenshots-path)Deprecated: -s <path>, --screenshots <path>[](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s-path---screenshots-path)

**Deprecated in favor of [-s (--screenshots)](https://testcafe.io/documentation/402639/reference/command-line-interface#-s---screenshots-optionvalueoption2value2).**

TestCafe v1.4.X and lower _does not_ enable screenshots out of the box. The `-s` option allows you to enable screenshots and specify the path to the screenshot storage location.

```
testcafe all tests/sample-fixture.js -s screenshots
```

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s---screenshots-on-fails)Deprecated: -S, --screenshots-on-fails[](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--s---screenshots-on-fails)

**Deprecated in favor of the [takeOnFails](https://testcafe.io/documentation/402639/reference/command-line-interface#takeonfails) option.**

If you use TestCafe v1.4.X or lower, enable the `-S` option to take screenshots on test failure:

```
testcafe chrome test.js -S
```

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--p-pattern---screenshot-path-pattern-pattern)Deprecated: -p <pattern>, --screenshot-path-pattern <pattern>[](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated--p-pattern---screenshot-path-pattern-pattern)

**Deprecated in favor of the [pathPattern](https://testcafe.io/documentation/402639/reference/command-line-interface#pathpattern) option.**

If you use TestCafe v1.4.X or lower, use the `-screenshot-path-pattern` parameter to define a [custom naming pattern](https://testcafe.io/documentation/402840/guides/intermediate-guides/screenshots-and-videos#path-pattern-placeholders) for your screenshots:

```
testcafe all tests/sample-fixture.js -s screenshots -p '${DATE}_${TIME}/test-${TEST_INDEX}/${USERAGENT}/${FILE_INDEX}.png'
```

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#debugging-settings)Debugging settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#debugging-settings)

> Main article: [Debug Tests](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests)

*   [-q (--quarantine-mode)](https://testcafe.io/documentation/402639/reference/command-line-interface#-q-attemptlimitvalue-successthresholdvalue2---quarantine-mode-attemptlimitvalue-successthresholdvalue2)
*   [-d (--debug-mode)](https://testcafe.io/documentation/402639/reference/command-line-interface#-d---debug-mode)
*   [--debug-on-fail](https://testcafe.io/documentation/402639/reference/command-line-interface#--debug-on-fail)
*   [--inspect-brk](https://testcafe.io/documentation/402639/reference/command-line-interface#--inspect-brk)
*   [--sf (--stop-on-first-fail)](https://testcafe.io/documentation/402639/reference/command-line-interface#--sf---stop-on-first-fail)
*   [-e (--skip-js-errors)](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3)
*   [-u (--skip-uncaught-errors)](https://testcafe.io/documentation/402639/reference/command-line-interface#-u---skip-uncaught-errors)
*   [--dev](https://testcafe.io/documentation/402639/reference/command-line-interface#--dev)
*   [--retry-test-pages](https://testcafe.io/documentation/402639/reference/command-line-interface#--retry-test-pages)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-q-attemptlimitvalue-successthresholdvalue2---quarantine-mode-attemptlimitvalue-successthresholdvalue2)-q [attemptLimit=value, successThreshold=value2] --quarantine-mode [attemptLimit=value, successThreshold=value2][](https://testcafe.io/documentation/402639/reference/command-line-interface#-q-attemptlimitvalue-successthresholdvalue2---quarantine-mode-attemptlimitvalue-successthresholdvalue2)

> Main article: [Quarantine Mode](https://testcafe.io/documentation/403841/guides/intermediate-guides/quarantine-mode)

Enable quarantine mode to _eliminate false negatives_ and _detect unstable tests_. TestCafe **[quarantines](https://testcafe.io/documentation/403841/guides/intermediate-guides/quarantine-mode)** tests that fail and **repeats** them until they yield conclusive results.

The option accepts the following parameters:

*   successThreshold - The number of successful attempts necessary to confirm a test’s success. The option value should be greater than `0`. The default value is `3`.
*   attemptLimit - The maximum number of test execution attempts. The value of this option should exceed the value of the `successThreshold` option. The default value is `5`.

```
testcafe all tests/sample-fixture.js -q
testcafe all tests/sample-fixture.js -q attemptLimit=5
testcafe all tests/sample-fixture.js -q successThreshold=1
testcafe all tests/sample-fixture.js -q attemptLimit=5,successThreshold=1
```

_Configuration file parameter_: [quarantineMode](https://testcafe.io/documentation/402638/reference/configuration-file#quarantinemode)

_API_: [runner.run({ quarantineMode })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-d---debug-mode)-d, --debug-mode[](https://testcafe.io/documentation/402639/reference/command-line-interface#-d---debug-mode)

Enables [debug mode](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode):

```
testcafe chrome test.js --debug-mode
```

_Configuration file parameter_: [debugMode](https://testcafe.io/documentation/402638/reference/configuration-file#debugmode)

_API_: [runner.run({ debugMode })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--debug-on-fail)--debug-on-fail[](https://testcafe.io/documentation/402639/reference/command-line-interface#--debug-on-fail)

Enable the `--debug-on-fail` flag to enter [debug mode](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#debug-mode) on test failure.

```
testcafe chrome tests/sample-fixture.js --debug-on-fail
```

_Configuration file parameter_: [debugOnFail](https://testcafe.io/documentation/402638/reference/configuration-file#debugonfail)

_API_: [runner.run({ debugOnFail })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--inspect-brk)--inspect-brk[](https://testcafe.io/documentation/402639/reference/command-line-interface#--inspect-brk)

> Main article: [Debug Tests in Chrome Developer Tools](https://testcafe.io/documentation/402801/recipes/debugging/chrome-dev-tools)

Enable the `--inspect-brk` flag to launch a Node.js debugger:

```
testcafe --inspect-brk chrome ./tests
```

![Image 2: Node.js debugger link](https://testcafe.io/images/node-debugger.png)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--sf---stop-on-first-fail)--sf, --stop-on-first-fail[](https://testcafe.io/documentation/402639/reference/command-line-interface#--sf---stop-on-first-fail)

Stops the entire test run if one test fails.

```
testcafe chrome my-tests --sf
```

_Configuration file parameter_: [stopOnFirstFail](https://testcafe.io/documentation/402638/reference/configuration-file#stoponfirstfail)

_API_: [runner.run({ stopOnFirstFail })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3)-e [message=value, stack=value2, pageUrl=value3], --skip-js-errors [message=value, stack=value2, pageUrl=value3][](https://testcafe.io/documentation/402639/reference/command-line-interface#-e-messagevalue-stackvalue2-pageurlvalue3---skip-js-errors-messagevalue-stackvalue2-pageurlvalue3)

> Main article: [Skip JavaScript Errors](https://testcafe.io/documentation/404038/recipes/debugging/skip-javascript-errors)

TestCafe tests fail when a page yields a JavaScript error. Use the `-e`(`--skip-js-errors`) option to **ignore** JavaScript errors during the test run.

Important

Errors are signs of malfunction. Do not ignore errors that you can fix. 

 If a page outputs unwarranted error messages, modify your application to prevent this behavior. 

 Use the `skipJsErrors` option to silence errors that you cannot act upon.

If you use the `-e` flag without options, TestCafe ignores all JavaScript errors:

```
testcafe chrome test.js -e
```

Specify options to filter errors by string or regular expression.

Warning

Enclose regular expressions in forward slashes to avoid strict matches for special characters.

If you specify the `message` option, TestCafe ignores JavaScript errors with messages that match the string:

```
testcafe chrome test.js -e message='/.*User ID.*/ig'
```

If you specify the `pageUrl` option, TestCafe ignores JavaScript errors on pages with a URL that matches the string:

```
testcafe chrome test.js -e pageUrl='/.*.*html/'
```

If you specify the `stack` option, TestCafe ignores JavaScript errors with a call stack that matches the string:

```
testcafe chrome test.js -e stack='/.*jquery.*/g'
```

Specify several arguments to skip errors that fit **multiple criteria at once** — for example, errors with a specific message **and** a specific call stack.

```
testcafe chrome test.js -e stack='/.*jquery.*/', message='/.*User ID.*/ig'
```

_Configuration file parameter_: [skipJsErrors](https://testcafe.io/documentation/402638/reference/configuration-file#skipjserrors)

_API_: [runner.run({ skipJsErrors })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#skipjserrors)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-u---skip-uncaught-errors)-u, --skip-uncaught-errors[](https://testcafe.io/documentation/402639/reference/command-line-interface#-u---skip-uncaught-errors)

Enable the `-u`(`--skip-uncaught-errors`) flag to ignore uncaught errors and unhandled promise rejections during test execution.

```
testcafe chrome tests/sample-fixture.js -u
```

_Configuration file parameter_: [skipUncaughtErrors](https://testcafe.io/documentation/402638/reference/configuration-file#skipuncaughterrors)

_API_: [runner.run({ skipUncaughtErrors })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--dev)--dev[](https://testcafe.io/documentation/402639/reference/command-line-interface#--dev)

Enable the `--dev` flag to generate TestCafe crash reports.

Note

TestCafe does not relaunch unresponsive browsers when you enable Development Mode.

```
testcafe chrome my-tests --dev
```

_Configuration file parameter_: [developmentMode](https://testcafe.io/documentation/402638/reference/configuration-file#developmentmode)

_API_: [createTestCafe(developmentMode: true)](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--retry-test-pages)--retry-test-pages[](https://testcafe.io/documentation/402639/reference/command-line-interface#--retry-test-pages)

If you enable the `--retry-test-pages` flag, TestCafe performs up to 10 attempts to resolve unsuccessful network requests.

```
testcafe firefox my-tests --retry-test-pages
```

This capability requires a secure network connection thanks to its use of [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API). To run TestCafe over a secure connection, [set up HTTPS](https://testcafe.io/documentation/402839/guides/advanced-guides/test-https-features-and-http2-websites#test-https-websites) or use the **--hostname localhost** CLI option.

_Configuration file parameter_: [retryTestPages](https://testcafe.io/documentation/402638/reference/configuration-file#retrytestpages)

_API_: [createTestCafe](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#timeouts)timeouts[](https://testcafe.io/documentation/402639/reference/command-line-interface#timeouts)

> Main article: [Adjust timeouts](https://testcafe.io/documentation/402835/guides/basic-guides/debug-tests#adjust-timeouts)

*   [--selector-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--selector-timeout-ms)
*   [--assertion-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms)
*   [--page-load-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-load-timeout-ms)
*   [--ajax-request-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--ajax-request-timeout-ms)
*   [--page-request-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-request-timeout-ms)
*   [--browser-init-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--browser-init-timeout-ms)
*   [--test-execution-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-execution-timeout-ms)
*   [--run-execution-timeout](https://testcafe.io/documentation/402639/reference/command-line-interface#--run-execution-timeout-ms)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--selector-timeout-ms)--selector-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--selector-timeout-ms)

Specify the `--selector-timeout` parameter to adjust the [Selector timeout](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors#timeout) (default: **10000 ms**).

If TestCafe fails to resolve an element [selector](https://testcafe.io/documentation/402829/guides/basic-guides/element-selectors) query within the **Selector timeout** period, the test fails.

```
testcafe chrome my-tests --selector-timeout 500000
```

_Configuration file parameter_: [selectorTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#selectortimeout)

_API_: [runner.run({ selectorTimeout })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms)--assertion-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--assertion-timeout-ms)

Specify the `--assertion-timeout` option to adjust the [Assertion timeout](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) (default: **3000 ms**).

TestCafe executes [compatible assertions](https://testcafe.io/documentation/402837/guides/basic-guides/assertions#smart-assertion-query-mechanism) multiple times within the **Assertion timeout** period, repeating measurements and calculations with each attempt. If an assertion does not succeed, the test fails.

```
testcafe chrome my-tests --assertion-timeout 10000
```

_Configuration file parameter_: [assertionTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#assertiontimeout)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-load-timeout-ms)--page-load-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-load-timeout-ms)

Specify the `--page-load-timeout` option to adjust the **Page Load timeout** (default: **3000 ms**).

The **Page Load timeout** defines the maximum amount of time between the `DOMContentLoaded` event and the `window.load` event. TestCafe applies the timeout when the user delays test execution until the `window.loadEventRaised` event.

```
testcafe chrome my-tests --page-load-timeout 1000
```

_Configuration file parameter_: [pageLoadTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#pageloadtimeout)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--ajax-request-timeout-ms)--ajax-request-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--ajax-request-timeout-ms)

Specify the `--ajax-request-timeout` option to adjust the **AJAX Request timeout** (default: **120000 ms**).

If TestCafe does not resolve an XHR/AJAX request within the **AJAX Request timeout** period, the test fails.

```
testcafe chrome my-tests --ajax-request-timeout 40000
```

_Configuration file parameter_: [ajaxRequestTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#ajaxrequesttimeout)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-request-timeout-ms)--page-request-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--page-request-timeout-ms)

Specify the `--page-request-timeout` option to adjust the **Page Request timeout** (default: **25000 ms**).

If the server does not fulfill a page request within the **Page Request timeout** period, the test fails.

Note

If you want to retry unsuccessful test page requests, enable the [--retry-test-pages](https://testcafe.io/documentation/402639/reference/command-line-interface#--retry-test-pages) flag.

```
testcafe chrome my-tests --page-request-timeout 8000
```

_Configuration file parameter_: [pageRequestTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#pagerequesttimeout)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--browser-init-timeout-ms)--browser-init-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--browser-init-timeout-ms)

Specify the `browserInitTimeout` parameter to adjust the **Browser Initialization timeout**.

If one or more browsers fail to connect to TestCafe within the **Browser Initialization timeout** period, the test run fails.

```
testcafe chrome my-tests --browser-init-timeout 180000
```

**Default values**:

*   `120000` for [local browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#local-browsers)
*   `360000` for [remote browsers](https://testcafe.io/documentation/402639/reference/command-line-interface#cloud-browsers-custom-browsers-remote-browsers)

_Configuration file parameter_: [browserInitTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#browserinittimeout)

_API_: [runner.run({ browserInitTimeout })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-execution-timeout-ms)--test-execution-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--test-execution-timeout-ms)

Specify the `testExecutionTimeout` parameter to set a **Test Execution timeout**.

When the total execution time of a test exceeds the **Test Execution timeout** period, TestCafe terminates the test, even if the browser is responsive.

```
testcafe chrome my-tests --test-execution-timeout 180000
```

_Configuration file parameter_: [testExecutionTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#testexecutiontimeout)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--run-execution-timeout-ms)--run-execution-timeout <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--run-execution-timeout-ms)

Specify the `runExecutionTimeout` parameter to set a **Run Execution timeout**.

When the total execution time of a run exceeds the **Run Execution timeout** period, TestCafe terminates the test run, even if the browsers are responsive.

```
testcafe chrome my-tests --run-execution-timeout 180000
```

_Configuration file parameter_: [runExecutionTimeout](https://testcafe.io/documentation/402638/reference/configuration-file#runexecutiontimeout)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#automation-settings)Automation settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#automation-settings)

*   [-L (--live)](https://testcafe.io/documentation/402639/reference/command-line-interface#-l---live)
*   [--speed](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor)
*   [--disable-native-automation](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-native-automation)
*   [--ports](https://testcafe.io/documentation/402639/reference/command-line-interface#--ports-port1port2)
*   [--hostname](https://testcafe.io/documentation/402639/reference/command-line-interface#--hostname-name)
*   [--proxy](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-host)
*   [--proxy-bypass](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-bypass-rules)
*   [--ssl](https://testcafe.io/documentation/402639/reference/command-line-interface#--ssl-options)
*   [--cache](https://testcafe.io/documentation/402639/reference/command-line-interface#--cache)
*   [--disable-page-caching](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-page-caching)
*   [--disable-http2](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-http2)
*   [--disable-multiple-windows](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-multiple-windows)
*   [--experimental-multiple-windows](https://testcafe.io/documentation/402639/reference/command-line-interface#--experimental-multiple-windows)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-l---live)-L, --live[](https://testcafe.io/documentation/402639/reference/command-line-interface#-l---live)

Enable the `--live` option to run TestCafe in [Live Mode](https://testcafe.io/documentation/403842/guides/intermediate-guides/live-mode):

```
testcafe chrome test.js --live
```

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor)--speed <factor>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--speed-factor)

Specifies test execution speed.

Use the `speed` parameter to limit test execution speed. The parameter accepts values between `1` (the fastest speed, default value) and `0.01` (the slowest speed).

```
testcafe chrome my-tests --speed 0.1
```

**Default value**: `1`

_Configuration file parameter_: [speed](https://testcafe.io/documentation/402638/reference/configuration-file#speed)

_API_: [runner.run({ speed })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

_Test Controller_: [t.click({speed})](https://testcafe.io/documentation/402674/reference/test-api/testcontroller/typetext#options) (overrides the global setting)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-native-automation)--disable-native-automation[](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-native-automation)

When you launch TestCafe v3.0.0 and up, the framework engages [Native Automation mode](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) to automate Chromium-based browsers with the native CDP protocol. **Disable Native Automation** to automate browsers with the TestCafe proxy.

Specify the `--disable-native-automation` flag to disable Native Automation:

```
testcafe firefox,safari test.js --disable-native-automation
```

If you want to run tests in Chrome **and** other browsers, launch two instances of TestCafe — one with Native Automation, and one without:

```
testcafe chrome,edge test.js; 
testcafe firefox,safari test.js --disable-native-automation
```

_Configuration file parameter_: [disableNativeAutomation](https://testcafe.io/documentation/402638/reference/configuration-file#disablenativeautomation)

_API_: [runner.run({ disableNativeAutomation: true; })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run#disablenativeautomation)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--ports-port1port2)--ports <port1,port2>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--ports-port1port2)

TestCafe automatically selects two open network ports to automate browsers and access cross-domain resources.

Specify the `--ports` option to manually select two ports in the [0 — 65535] range.

```
testcafe chrome my-tests --ports 12345,54321
```

_Configuration file parameter_: [port1, port2](https://testcafe.io/documentation/402638/reference/configuration-file#port1-port2)

_API_: [createTestCafe](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--hostname-name)--hostname <name>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--hostname-name)

Specify the `--hostname` option to select the hostname of your machine for remote browser connections. If you do not specify this property, TestCafe detects your hostname and IP address.

```
testcafe chrome my-tests --hostname host.mycorp.com
```

_Configuration file parameter_: [hostname](https://testcafe.io/documentation/402638/reference/configuration-file#hostname)

_API_: [createTestCafe](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-host)--proxy <host>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-host)

Specify the `--proxy` option to access remote resources through a proxy.

```
testcafe chrome my-tests/**/*.js --proxy proxy.corp.mycompany.com
```

```
testcafe chrome my-tests/**/*.js --proxy 172.0.10.10:8080
```

The value may include authentication credentials:

```
testcafe chrome my-tests/**/*.js --proxy username:password@proxy.mycorp.com
```

_Configuration file parameter_: [proxy](https://testcafe.io/documentation/402638/reference/configuration-file#proxy)

_API_: [runner.useProxy](https://testcafe.io/documentation/402649/reference/testcafe-api/runner/useproxy)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-bypass-rules)--proxy-bypass <rules>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--proxy-bypass-rules)

Use the `--proxy-bypass` option to bypass the proxy when you load select resources.

The **wildcard symbol (*)** indicates variable URL parts. You can omit wildcards at the beginning and the end of the URL: `*.mycorp.com` and `.mycorp.com` are identical.

```
testcafe chrome my-tests/**/*.js --proxy proxy.corp.mycompany.com --proxy-bypass *.mycompany.com
```

```
testcafe chrome my-tests/**/*.js --proxy proxy.corp.mycompany.com --proxy-bypass localhost:8080
```

_Configuration file parameter_: [proxyBypass](https://testcafe.io/documentation/402638/reference/configuration-file#proxybypass)

_API_: [runner.useProxy](https://testcafe.io/documentation/402649/reference/testcafe-api/runner/useproxy)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--ssl-options)--ssl <options>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--ssl-options)

To run the TestCafe proxy over HTTPS, pass [HTTPS initialization options](https://nodejs.org/api/https.html#httpscreateserveroptions-requestlistener) to the `--ssl` flag.

Separate individual options with a colon.

```
testcafe --ssl pfx=path/to/file.pfx;rejectUnauthorized=true;...
```

See the [HTTPS and HTTP/2 Guide](https://testcafe.io/documentation/402839/guides/advanced-guides/test-https-features-and-http2-websites) for more information.

_Configuration file parameter_: [ssl](https://testcafe.io/documentation/402638/reference/configuration-file#ssl)

_API_: [createTestCafe](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--cache)--cache[](https://testcafe.io/documentation/402639/reference/command-line-interface#--cache)

Specify the `--cache` option to cache assets (such as stylesheets and scripts) when you load a web page for the first time.

When TestCafe accesses the page a second time, it pulls assets from its cache instead of requesting them from the server.

```
testcafe chrome my-tests --cache
```

TestCafe emulates the browser’s native caching behavior. For example, when TestCafe runs tests in _Google Chrome_, it only caches resources that _Chrome_ itself would cache.

TestCafe caches scripts, stylesheets, fonts, and other assets up to **5 MB** in size. TestCafe does not cache HTML because that could break [user roles](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication#user-roles).

If the application relies on heavy remote assets, enable server-side caching to decrease test run time.

_Configuration file parameter_: [cache](https://testcafe.io/documentation/402638/reference/configuration-file#cache)

_API_: [createTestCafe](https://testcafe.io/documentation/402662/reference/testcafe-api/global/createtestcafe)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-page-caching)--disable-page-caching[](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-page-caching)

Enable the `--disable-page-caching` flag to prohibit the browser from caching page content.

```
testcafe chrome my-tests --disable-page-caching
```

Users may inadvertently access cached pages that contain outdated automation scripts, for example, when they [activate a Role](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication#user-roles). Specify the `disablePageCaching` parameter to prevent the browser from caching automation scripts.

For more information, see [Troubleshooting: Test Actions Fail After Authentication](https://testcafe.io/documentation/402845/guides/intermediate-guides/authentication#test-actions-fail-after-authentication).

You can disable page caching for an individual [fixture](https://testcafe.io/documentation/402782/reference/test-api/fixture/disablepagecaching) or [test](https://testcafe.io/documentation/402736/reference/test-api/test/disablepagecaching).

_Configuration file parameter_: [disablePageCaching](https://testcafe.io/documentation/402638/reference/configuration-file#disablepagecaching)

_API_: [runner.run({ disablePageCaching })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-http2)--disable-http2[](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-http2)

Enable the `--disable-http2` flag to prohibit [HTTP/2](https://http2.github.io/) network requests.

```
testcafe firefox my-tests --disable-http2
```

_Configuration file parameter_: [disableHttp2](https://testcafe.io/documentation/402638/reference/configuration-file#disablehttp2)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-multiple-windows)--disable-multiple-windows[](https://testcafe.io/documentation/402639/reference/command-line-interface#--disable-multiple-windows)

If multi-window tests cause crashes, disable support for [multi-window testing](https://testcafe.io/documentation/402841/guides/intermediate-guides/multiple-browser-windows) with the `--disable-multiple-windows` flag.

```
testcafe firefox my-tests --disable-multiple-windows
```

_Configuration file parameter_: [disableMultipleWindows](https://testcafe.io/documentation/402638/reference/configuration-file#disablemultiplewindows)

_API_: [runner.run({ disableMultipleWindows })](https://testcafe.io/documentation/402655/reference/testcafe-api/runner/run)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--experimental-multiple-windows)--experimental-multiple-windows[](https://testcafe.io/documentation/402639/reference/command-line-interface#--experimental-multiple-windows)

Important

This option is **experimental**. Do not use it in production or for business-critical tasks.

The `--experimental-multiple-windows` option allows TestCafe to use [native automation](https://testcafe.io/documentation/404237/guides/intermediate-guides/native-automation-mode) when it runs multi-window tests.

```
testcafe chrome my-tests --experimental-multiple-windows
```

The `--experimental-multiple-windows` mode does not support tests that include the following:

*   Pop-up windows that launch file downloads.
*   Browser window resizing.
*   Screenshots.
*   Video recording.

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#javascript-settings)JavaScript settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#javascript-settings)

> Main article: [ESM Module Support](https://testcafe.io/documentation/404258/guides/advanced-guides/esm-module-support)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--esm)--esm[](https://testcafe.io/documentation/402639/reference/command-line-interface#--esm)

Enable the `-esm` CLI flag to import ESM modules. Note: Tests with ECMAScript module syntax are subject to [additional requirements](https://testcafe.io/documentation/402639/reference/command-line-interface#additional-requirements).

```
testcafe chrome tests --esm
```

##### [](https://testcafe.io/documentation/402639/reference/command-line-interface#additional-requirements)Additional Requirements[](https://testcafe.io/documentation/402639/reference/command-line-interface#additional-requirements)

To run tests with ECMAScript `import` statements, make sure that your project meets one of the following requirements:

1.   The value of the `type` key in your project’s [package.json file](https://nodejs.org/api/packages.html#packagejson-and-file-extensions) is `module`.
2.   The test files in your project use the `.mjs` extension.

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#typescript-settings)TypeScript settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#typescript-settings)

> Main article: [TypeScript and CoffeeScript](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript)

*   [--compiler-options](https://testcafe.io/documentation/402639/reference/command-line-interface#--compiler-options-options)
*   [--ts-config-path](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated---ts-config-path-path)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--compiler-options-options)--compiler-options <options>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--compiler-options-options)

Use the `--compiler-options` option to specify [TypeScript compilation settings](https://testcafe.io/documentation/402824/guides/intermediate-guides/typescript-and-coffeescript#customize-compiler-options). Refer to the official [TypeScript documentation](https://www.typescriptlang.org/docs/handbook/compiler-options.html) for the full list of available settings.

```
testcafe chrome my-tests --compiler-options typescript.options.lib=lib.es5.d.ts,lib.webworker.d.ts;typescript.typesRoot='this value contains spaces'
```

Specify the `typescript.configPath` compiler option to import compiler settings from a dedicated TypeScript configuration file:

```
testcafe chrome my-tests --compiler-options typescript.configPath='config file path'
```

TestCafe ships with a `typescript@3` compiler. Specify the `typescript.customCompilerModulePath` option to compile your tests with a different compiler.

```
testcafe chrome test.ts --compiler-options typescript.customCompilerModulePath=../typescript@4
```

Note

TestCafe resolves relative paths against the framework’s installation folder.

_Configuration file parameter_: [compilerOptions](https://testcafe.io/documentation/402638/reference/configuration-file#compileroptions)_API_: [runner.compilerOptions](https://testcafe.io/documentation/402659/reference/testcafe-api/runner/compileroptions)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated---ts-config-path-path)Deprecated: --ts-config-path <path>[](https://testcafe.io/documentation/402639/reference/command-line-interface#deprecated---ts-config-path-path)

The `tsConfigPath` parameter has been deprecated in favor of the [--compiler-options](https://testcafe.io/documentation/402639/reference/command-line-interface#--compiler-options-options) parameter.

_Configuration file parameter_: [tsConfigPath](https://testcafe.io/documentation/402638/reference/configuration-file#tsconfigpath-deprecated)

_API_: [runner.tsConfigPath](https://testcafe.io/documentation/402650/reference/testcafe-api/runner/tsconfigpath)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#client-scripts)Client scripts[](https://testcafe.io/documentation/402639/reference/command-line-interface#client-scripts)

> Main article: [Inject Client Scripts](https://testcafe.io/documentation/402843/guides/advanced-guides/inject-client-scripts)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--cs-pathpath2---client-scripts-pathpath2)--cs <path[,path2,…]>, --client-scripts <path[,path2,…]>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--cs-pathpath2---client-scripts-pathpath2)

Specify the `--client-scripts` option to inject custom JavaScript files into the browser. Separate file paths with a comma.

```
testcafe chrome my-tests --client-scripts mockDate.js,assets/react-helpers.js
```

Pass the [path to a JavaScript file](https://testcafe.io/documentation/402843/guides/advanced-guides/inject-client-scripts#inject-a-javascript-file) to inject its content.

Note

TestCafe resolves relative paths against the current working directory.

_Configuration file parameter_: [clientScripts](https://testcafe.io/documentation/402638/reference/configuration-file#client-scripts)

_API_: [runner.clientScripts](https://testcafe.io/documentation/402660/reference/testcafe-api/runner/clientscripts)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#initialization-settings)Initialization settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#initialization-settings)

> Main article: [Execute Shell Commands on Startup](https://testcafe.io/documentation/403849/guides/advanced-guides/execute-shell-commands-on-startup)

*   [-a (-app)](https://testcafe.io/documentation/402639/reference/command-line-interface#-a-command---app-command)
*   [--app-init-delay](https://testcafe.io/documentation/402639/reference/command-line-interface#--app-init-delay-ms)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#-a-command---app-command)-a <command>, --app <command>[](https://testcafe.io/documentation/402639/reference/command-line-interface#-a-command---app-command)

Use the `--app` option to execute a shell command on startup. TestCafe terminates this process when the test run is complete.

```
testcafe chrome my-tests --app "node server.js"
```

TestCafe awaits the resolution of the command for **1000 milliseconds**. Set the [--app-init-delay](https://testcafe.io/documentation/402639/reference/command-line-interface#--app-init-delay-ms) option to change this value.

Note

TestCafe adds the `node_modules/.bin` folder to the `PATH` environment variable. Do not use prefixes if you want to launch local dependency binaries.

_Configuration file parameter_: [appCommand](https://testcafe.io/documentation/402638/reference/configuration-file#appcommand)

_API_: [runner.startApp](https://testcafe.io/documentation/402652/reference/testcafe-api/runner/startapp)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--app-init-delay-ms)--app-init-delay <ms>[](https://testcafe.io/documentation/402639/reference/command-line-interface#--app-init-delay-ms)

Specifies the time (in milliseconds) between the execution of the [--app](https://testcafe.io/documentation/402639/reference/command-line-interface#-a-command---app-command) shell command and the launch of the first test.

```
testcafe chrome my-tests --app "node server.js" --app-init-delay 4000
```

**Default value**: `1000`

_Configuration file parameter_: [appInitDelay](https://testcafe.io/documentation/402638/reference/configuration-file#appinitdelay)

_API_: [runner.startApp](https://testcafe.io/documentation/402652/reference/testcafe-api/runner/startapp)

### [](https://testcafe.io/documentation/402639/reference/command-line-interface#cli-output-settings)CLI output settings[](https://testcafe.io/documentation/402639/reference/command-line-interface#cli-output-settings)

*   [--no-color](https://testcafe.io/documentation/402639/reference/command-line-interface#--no-color)
*   [--color](https://testcafe.io/documentation/402639/reference/command-line-interface#--color)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--no-color)--no-color[](https://testcafe.io/documentation/402639/reference/command-line-interface#--no-color)

TestCafe uses multiple colors to format its CLI output. To disable this behavior, use the `--no-color` option.

```
testcafe chrome my-tests --no-color
```

_Configuration file parameter_: [noColor](https://testcafe.io/documentation/402638/reference/configuration-file#nocolor)

#### [](https://testcafe.io/documentation/402639/reference/command-line-interface#--color)--color[](https://testcafe.io/documentation/402639/reference/command-line-interface#--color)

If you [disabled](https://testcafe.io/documentation/402638/reference/configuration-file#nocolor) command line colors in the Configuration File, you can override this setting with the `--color` command line option.

```
testcafe chrome my-tests --color
```
